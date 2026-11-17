#!/usr/bin/env python3
"""Render ram-board.html from docs/research/ram-offers.json.

The ladder is the page's spine: one cheapest route per capacity, 12 modules each.
The offer list is the raw record, kept below in a closed <details>.
"""
import html
import json
import pathlib
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "research" / "ram-offers.json"
OUT = ROOT / "ram-board.html"

D = json.loads(SRC.read_text())
FX = D["fx"]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")


def esc(v):
    return html.escape(str(v))


def plain(v):
    return str(v).replace("**", "").strip()


def num(v, dec=2):
    if v is None:
        return "—"
    return f"{v:,.{dec}f}".replace(",", "\u00a0").replace(".", ",")


def money(v, cur, dec=2):
    if v is None:
        return "—"
    s = num(v, dec)
    if cur == "PLN":
        return f"{s}\u00a0zł"
    if cur == "CHF":
        return f"CHF {s}"
    return f"{'€' if cur == 'EUR' else '$' if cur == 'USD' else '£'}{s}"


def eur(v, cur):
    return v * FX[cur] / FX["EUR"]


def net_pln(p):
    if not p or p.get("net") is None or not p.get("cur"):
        return None
    return p["net"] * FX[p["cur"]]


def per_gb(p):
    if not p or p.get("net") is None or not p.get("gb") or not p.get("cur"):
        return None
    return eur(p["net"], p["cur"]) / p["gb"]


def qvl_tag(q):
    if q == "pass":
        return '<span class="tag ok">QVL ✓</span>'
    if q == "fail":
        return '<span class="tag bad">QVL ✗</span>'
    return ""


STATE = {
    "lead": ("lead", "warn"),
    "unavailable": ("unavailable", "warn"),
    "withdrawn": ("withdrawn", "warn"),
    "unreachable": ("unreachable", "warn"),
    "blocked": ("blocked", "warn"),
    "excluded": ("excluded", "bad"),
    "reject": ("rejected", "bad"),
    "qvl-fail": ("QVL fail", "bad"),
}


def state_tag(state):
    if state not in STATE:
        return ""
    label, kind = STATE[state]
    return f'<span class="tag {kind}">{label}</span>'


def condition_tag(cond):
    if not cond or not any(k in cond.lower() for k in ("pull", "used", "refurb", "open box")):
        return ""
    return f'<span class="tag bad">{esc(cond)}</span>'


def supply_tag(row):
    label = esc(row.get("sellers") or "—")
    qty = row.get("qty")
    if row["status"] == "not_buildable":
        return f'<span class="tag bad">{label}</span>'
    if qty is not None and qty < 12:
        return f'<span class="tag bad">{qty} pcs — short</span>'
    return f'<span class="tag {"ok" if qty and qty >= 12 else "warn"}">{label}</span>'


# ---------------------------------------------------------------- capacity matrix

tiers = [r for r in D["ladder"]["rows"] if r["status"] != "over_budget"]
assert sorted(r["modules"] for r in tiers) == [16, 24, 32, 48, 64], "ladder must carry 12x16..12x64"
assert all(r["module_net_eur"] > 0 for r in tiers)

tiers.sort(key=lambda r: r["module_net_eur"] / r["module_gb"])
best_tier = tiers[0]

matrix = ""
for r in tiers:
    gb = r["module_net_eur"] / r["module_gb"]
    total = r["total_net_eur"]
    tags = qvl_tag(r.get("qvl")) + supply_tag(r)
    if r.get("label"):
        tags = f'<span class="tag info">{esc(r["label"])}</span>' + tags
    alt = ""
    if r.get("alt"):
        a = r["alt"]
        a_mod = eur(a["module_net"], a["cur"])
        alt = (f'<div class="alt"><b>{esc(a["label"])}:</b> {esc(a["part"])} @ {esc(a["shop"])} — '
               f'{money(a_mod, "EUR")}/module · {money(a_mod * 12, "EUR", 0)} total · '
               f'{money(a_mod / r["module_gb"], "EUR")}/GB · {esc(a["qty"])}</div>')
    matrix += f"""<tr{' class="best"' if r is best_tier else ''}>
      <td data-v="{r['modules']}"><b>12×{r['module_gb']} GB</b><div class="k">{r['tier_gb']} GB total</div></td>
      <td data-v="{esc(r['part'])}"><b>{esc(r['part'])}</b><div class="k">{esc(r['shop'])}</div>
        <div class="tags">{tags}</div>
        <div class="note">{esc(r['note'])}</div>{alt}</td>
      <td class="num" data-v="{r['module_net_eur']:.2f}">{money(r['module_net_eur'], 'EUR')}</td>
      <td class="num" data-v="{'' if total is None else f'{total:.2f}'}">{money(total, 'EUR', 0)}</td>
      <td class="num strong" data-v="{gb:.4f}">{money(gb, 'EUR')}</td>
      <td><a href="{esc(r['url'])}">open ↗</a></td>
    </tr>"""

ref = next(r for r in D["ladder"]["rows"] if r["status"] == "over_budget")
ref_gb = ref["module_net_eur"] / ref["module_gb"]

marginal = " · ".join(
    f'{m["step"].replace("->", "→")} <b>{money(m["marginal_eur_per_gb"], "EUR")}/GB</b>'
    for m in D["budget_directive"]["marginal_costs"]
    if "1152" not in m["step"])

# ---------------------------------------------------------------- all offers

UNBUYABLE = {"excluded", "reject", "qvl-fail", "withdrawn", "unavailable", "blocked", "unreachable", "lead"}

offers = []
for i, o in enumerate(D["offers"]):
    p = o.get("price") or {}
    g = per_gb(p)
    used = any(k in (o.get("condition") or "").lower() for k in ("pull", "used", "refurb", "open box"))
    rank = (bool(o.get("excluded_reason")) or o.get("state") in UNBUYABLE,
            used,
            o.get("qty") is not None and o["qty"] < 12,
            g is None, g or 0)
    offers.append((rank, i, o, p))
offers.sort()

rows = ""
for _, _, o, p in offers:
    cur = p.get("cur")
    gb = per_gb(p)
    np_ = net_pln(p)
    part_short = plain(o["part"]).split(" — ")[0]
    tags = condition_tag(o.get("condition")) + qvl_tag(o.get("qvl_mz23su0")) + state_tag(o.get("state"))
    extra = f'<div class="note">{esc(o["excluded_reason"])}</div>' if o.get("excluded_reason") else ""
    extra += f'<div class="note">{esc(o["spd_note"])}</div>' if o.get("spd_note") else ""
    gross = money(p.get("gross"), cur) if p.get("gross") is not None else "—"
    net = money(p.get("net"), cur) if p.get("net") is not None else "—"
    gross_eur = eur(p["gross"], cur) if p.get("gross") is not None and cur else None
    net_eur = eur(p["net"], cur) if p.get("net") is not None and cur else None
    if p.get("gross_derived") or p.get("net_derived"):
        net += '<span class="k">*</span>'
    rows += f"""<tr>
      <td data-v="{esc(plain(o['part']))}" title="{esc(plain(o["part"]))}"><b>{esc(part_short)}</b>
        <div class="tags">{tags}</div>{extra}</td>
      <td data-v="{esc(o['shop'])}" title="{esc(o['shop'])}">{esc(o['shop'].split(' (')[0])}<div class="k">{esc(o.get('country', ''))}</div></td>
      <td class="num" data-v="{'' if gross_eur is None else f'{gross_eur:.2f}'}">{gross}</td>
      <td class="num" data-v="{'' if net_eur is None else f'{net_eur:.2f}'}">{net}</td>
      <td class="num" data-v="{'' if np_ is None else f'{np_:.2f}'}">{money(np_, 'PLN')}</td>
      <td class="num" data-v="{'' if gb is None else f'{gb:.4f}'}">{money(gb, 'EUR')}</td>
      <td data-v="{esc(plain(o.get('stock', '')))}" title="{esc(plain(o.get('stock', '—')))}">{esc(plain(o.get('stock', '—'))[:64])}{'…' if len(plain(o.get('stock', ''))) > 64 else ''}</td>
      <td><a href="{esc(o['url'])}">open ↗</a></td>
    </tr>"""

# ---------------------------------------------------------------- page

CSS = """
  :root { --bg:#0e1114; --panel:#151a1f; --line:#232b34; --text:#e6ebf1; --muted:#8b98a8;
          --accent:#e0a33e; --ok:#57c98a; --bad:#ef6b6b; --warn:#e0a33e; --info:#6fb3e0; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--text);
         font:15px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif; }
  .wrap { max-width:1120px; margin:0 auto; padding:34px 24px 56px; }
  .eyebrow { color:var(--muted); font-size:12px; letter-spacing:.08em; text-transform:uppercase; }
  h1 { font-size:27px; line-height:1.2; margin:4px 0 8px; letter-spacing:-.02em; }
  .rule { color:var(--muted); max-width:82ch; margin:0 0 6px; font-size:14px; }
  .rule b { color:var(--text); font-weight:600; }
  .stamp { color:var(--muted); font-size:12px; margin:0 0 24px; }
  table { width:100%; border-collapse:collapse; }
  th,td { text-align:left; padding:12px 14px; border-bottom:1px solid var(--line); vertical-align:top; }
  th { font-size:11px; text-transform:uppercase; letter-spacing:.06em; color:var(--muted);
       font-weight:600; white-space:nowrap; }
  th button { all:unset; cursor:pointer; }
  th button:hover { color:var(--text); }
  th[data-dir="asc"] button::after { content:" ↑"; color:var(--accent); }
  th[data-dir="desc"] button::after { content:" ↓"; color:var(--accent); }
  td.num,th.num { text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }
  .offers { font-size:13px; }
  .offers th, .offers td { padding:10px; }
  .offers td:first-child { min-width:200px; max-width:220px; }
  .offers td:nth-child(2) { min-width:140px; max-width:175px; }
  .offers td:nth-child(7) { max-width:180px; }
  tr:last-child td { border-bottom:0; }
  .panel { background:var(--panel); border:1px solid var(--line); border-radius:10px; overflow:hidden; }
  tr.best { background:#171d23; box-shadow:inset 3px 0 0 var(--accent); }
  .strong { font-size:16px; font-weight:700; }
  .matrix td:first-child { white-space:nowrap; }
  td:last-child a { white-space:nowrap; }
  .k { color:var(--muted); font-size:12px; }
  .note { color:var(--muted); font-size:12.5px; margin-top:5px; max-width:66ch; }
  .alt { color:#b9c4d0; font-size:12.5px; margin-top:5px; padding-left:9px; border-left:2px solid var(--line); }
  .tags { margin-top:5px; display:flex; flex-wrap:wrap; gap:4px; }
  .tag { font-size:11px; line-height:1.6; padding:0 7px; border-radius:999px; border:1px solid var(--line);
         color:var(--muted); white-space:nowrap; }
  .tag.ok { border-color:#2c6b4a; color:var(--ok); }
  .tag.bad { border-color:#7a3434; color:var(--bad); }
  .tag.warn { border-color:#6b5222; color:var(--warn); }
  .tag.info { border-color:#2d5570; color:var(--info); }
  .tag.plain { color:var(--muted); }
  a { color:#7cc4e8; text-decoration:none; }
  a:hover { text-decoration:underline; }
  .marginal { color:var(--muted); font-size:13px; margin:14px 2px 0; }
  .marginal b { color:var(--text); }
  .ref { color:var(--muted); font-size:13px; margin:6px 2px 0; }
  details { margin-top:26px; background:var(--panel); border:1px solid var(--line); border-radius:10px; }
  summary { cursor:pointer; padding:13px 16px; font-weight:600; }
  summary::marker { color:var(--muted); }
  .scroll { overflow-x:auto; border-top:1px solid var(--line); }
  footer { color:var(--muted); font-size:12px; margin-top:24px; max-width:90ch; }
  footer code { color:#9fb0c0; }
  @media (max-width:720px) {
    .wrap { padding:22px 12px 40px; }
    h1 { font-size:22px; }
    th,td { padding:9px 10px; }
  }
"""

JS = """
for (const table of document.querySelectorAll('table[data-sortable]')) {
  const tbody = table.tBodies[0];
  for (const th of table.tHead.rows[0].cells) {
    if (!('sortable' in th.dataset)) continue;
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.textContent = th.textContent.trim();
    th.textContent = '';
    th.appendChild(btn);
    btn.addEventListener('click', () => {
      const i = th.cellIndex;
      const dir = th.dataset.dir === 'asc' ? 'desc' : 'asc';
      for (const h of table.tHead.rows[0].cells) {
        delete h.dataset.dir;
        h.removeAttribute('aria-sort');
      }
      th.dataset.dir = dir;
      th.setAttribute('aria-sort', dir === 'asc' ? 'ascending' : 'descending');
      const rows = [...tbody.rows];
      rows.sort((a, b) => {
        const x = a.cells[i].dataset.v ?? '';
        const y = b.cells[i].dataset.v ?? '';
        if (x === '' || y === '') return (x === '') - (y === '');
        const nx = parseFloat(x);
        const ny = parseFloat(y);
        const c = !isNaN(nx) && !isNaN(ny) ? nx - ny : x.localeCompare(y);
        return dir === 'asc' ? c : -c;
      });
      tbody.append(...rows);
    });
  }
}
"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>R9700 ×4 — DDR5-6400 RDIMM, full 12-channel builds</title>
<style>{CSS}</style></head>
<body><div class="wrap">
<div class="eyebrow">R9700 ×4 · RAM</div>
<h1>DDR5-6400 ECC RDIMM — full 12-channel builds</h1>
<p class="rule">GIGABYTE MZ23-SU0 · 12 DIMM slots, 12 channels · JEDEC-only BIOS. A module qualifies only if its
<b>JEDEC SPD default is DDR5-6400 at 1.1 V</b> — not if it is merely rated 6400. A 7600-rated Kingston FURY
declaring JEDEC 6400 qualifies; a 6400-rated KF564R32RBE declaring JEDEC 4800 does not. RDIMM only · any rank/org ·
budget ceiling 64 GB modules · net prices, VAT removed · zł @ {num(FX['EUR'], 4)}.</p>
<p class="stamp">Prices checked {esc(D.get('updated', NOW)).replace('T', ' ')} · {len(D['offers'])} offers tracked · the matrix is 12 modules per route</p>

<div class="panel"><table class="matrix" data-sortable>
<thead><tr>
  <th data-sortable>Capacity</th>
  <th data-sortable>Cheapest build</th>
  <th class="num" data-sortable>Net / module</th>
  <th class="num" data-sortable>Net total</th>
  <th class="num" data-sortable data-dir="asc" aria-sort="ascending">€/GB</th>
  <th>Link</th>
</tr></thead>
<tbody>{matrix}</tbody>
</table></div>

<p class="marginal">Marginal cost of the next 192 GB: {marginal}. The 48 GB step is the best money in the matrix; the 64 GB step is the worst.</p>
<p class="ref">Outside the ceiling: 12×96 GB {esc(ref['part'])} @ {esc(ref['shop'])} — {money(ref['total_net_eur'], 'EUR', 0)},
{money(ref_gb, 'EUR')}/GB. Cheapest per GB overall, but a €32k build.</p>

<details>
<summary>All {len(D['offers'])} tracked offers — buyable first · latest check {esc(D.get('updated', NOW)).replace('T', ' ')}</summary>
<div class="scroll"><table class="offers" data-sortable>
<thead><tr>
  <th data-sortable>Part</th><th data-sortable>Shop</th>
  <th class="num" data-sortable>Gross</th>
  <th class="num" data-sortable>Net</th>
  <th class="num" data-sortable>Net PLN</th>
  <th class="num" data-sortable>€/GB</th>
  <th>Stock</th><th>Link</th>
</tr></thead>
<tbody>{rows}</tbody>
</table></div>
</details>

<footer>
Prices are net of VAT where the shop permits; totals are 12 modules. <b>*</b> marks a value derived from the other side of the VAT split.
FX: NBP table A 2026-11-13 — EUR {FX['EUR']}, USD {FX['USD']}, CHF {FX['CHF']}, GBP {FX['GBP']} PLN.
QVL ✗ means untested on this board, not incompatible. Enumeration: Geizhals DDR5-6400 RDIMM category sweep; every shop read is logged in <code>docs/research/beam-eu-6400-repoke.md</code>.
Lifecycle: Kingston 64MD is “obsolete” at DigiKey and the 128 GB kit is discontinued — thin stock is the norm.
</footer>
</div><script>{JS}</script></body></html>"""

OUT.write_text(page)
print(f"wrote {OUT} ({len(D['offers'])} offers, {len(tiers)} tiers)")
