#!/usr/bin/env python3
"""Camoufox sweep: every 8+ CCD EPYC 9005 SKU on eBay.com — title, price, condition, ship.

Route: Camoufox (Firefox engine, fingerprint spoofing) per RECOMMENDATION.md pass 30,
which decoded eBay.com where 4/4 headless-Chromium attempts were IP-walled.

Markup note: eBay renders `li.s-card` (2026-11), NOT the legacy `li.s-item`.
Fields live in `s-card__title` / `s-card__price` / `s-card__subtitle`.
First card in the page is always a "Shop on eBay" placeholder — skipped.

Usage: pwenv/bin/python ebay_cpu_sweep.py [sku ...]
Writes JSON to stdout, a human table to stderr.
"""
import html
import json
import re
import sys
from camoufox.sync_api import Camoufox

SKUS = [
    # SP5 Zen 5 (Turin)
    "9175F", "9275F", "9355P", "9355", "9375F", "9455P", "9455", "9475F",
    "9535", "9555P", "9555", "9575F", "9565", "9655P", "9655", "9755",
    # SP5 Zen 5c (Turin Dense)
    "9645", "9745", "9845", "9825", "9965",
    # SP6 Sorano (6-channel — kept for completeness, flagged downstream)
    "8325P", "8435P", "8535P", "8635P",
]

URL = "https://www.ebay.com/sch/i.html?_nkw={q}&_sacat=0&LH_BIN=1&_sop=15"
CARD = re.compile(r'<li[^>]*class="[^"]*s-card[^"]*".*?</li>', re.S)
TAG = re.compile(r'<[^>]+>')
PRICE_NUM = re.compile(r'[\d,]+\.?\d*')


def clean(s):
    return re.sub(r'\s+', ' ', TAG.sub('', html.unescape(s or ''))).strip()


def field(block, cls):
    m = re.search(r'class="[^"]*' + cls + r'[^"]*"[^>]*>(.*?)</(?:span|div|h[0-9])>', block, re.S)
    return clean(m.group(1)) if m else ""


def usd(s):
    m = PRICE_NUM.search(s.replace(',', ''))
    try:
        return float(m.group(0))
    except Exception:
        return None


def sweep(page, sku):
    page.goto(URL.format(q=f"EPYC+{sku}"), wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(3500)
    html_doc = page.content()
    rows = []
    for b in CARD.findall(html_doc):
        t = field(b, 's-card__title')
        if not t or t == "Shop on eBay":
            continue
        if sku.upper() not in t.upper():
            continue
        price = field(b, 's-card__price')
        rows.append({
            "title": t[:170],
            "price": price,
            "usd": usd(price),
            "condition": field(b, 's-card__subtitle'),
        })
    return rows


def main():
    skus = sys.argv[1:] or SKUS
    result = {}
    with Camoufox(headless=True, humanize=False) as browser:
        page = browser.new_page()
        for sku in skus:
            try:
                rows = sweep(page, sku)
                result[sku] = rows
                if rows:
                    priced = [r for r in rows if r["usd"]]
                    lo = min(priced, key=lambda r: r["usd"]) if priced else None
                    print(f"### {sku} — {len(rows)} listings"
                          + (f" | cheapest ${lo['usd']:,.0f} ({lo['condition']})" if lo else ""),
                          file=sys.stderr)
                    for r in sorted(priced, key=lambda r: r["usd"])[:4]:
                        print(f"    ${r['usd']:>9,.0f}  {r['condition']:<12} {r['title'][:80]}",
                              file=sys.stderr)
                else:
                    print(f"### {sku} — 0 listings", file=sys.stderr)
            except Exception as e:
                print(f"### {sku} — ERROR {e}", file=sys.stderr)
                result[sku] = [{"error": str(e)}]
    json.dump(result, sys.stdout, indent=1)


if __name__ == "__main__":
    main()
