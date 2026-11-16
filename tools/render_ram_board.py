#!/usr/bin/env python3
"""Render the RAM offer board (docs/research/beam-eu-6400-repoke.md + a pinned offers table) to ram-board.html.

Reads: docs/research/ram-offers.json (pinned current bests, updated by the scheduler runs or by hand)
Writes: ram-board.html — one-page, always-current view of every tracked offer.
"""
import json, html, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "research" / "ram-offers.json"
OUT = ROOT / "ram-board.html"

data = json.loads(SRC.read_text())
EURPLN = data.get("eurpln", 4.4070)

def fmt(v):
    return f"€{v:,.0f}" if isinstance(v, (int, float)) else v

rows = ""
for o in sorted(data["offers"], key=lambda x: (x.get("state") == "excluded", x.get("eur_per_gb", 99))):
    best = ' <span class="tag rec">BEST</span>' if o.get("best") else ""
    org = f' <span class="tag {"rec" if "2Rx4" in str(o.get("org", "")) else "bad"}">{html.escape(o["org"])}</span>' if o.get("org") else ""
    flag = "" if o.get("state", "ok") in ("ok", "new") else f' <span class="tag {"warn" if o["state"]=="stale" else "bad"}">{html.escape(o["state"])}</span>'
    rows += f"""<tr>
      <td>{html.escape(o['part'])}<br><span class="k">{html.escape(o.get('spec',''))}</span>{best}{org}{flag}</td>
      <td>{html.escape(o['shop'])}<br><span class="k">{html.escape(o.get('country',''))}</span></td>
      <td class="num">{html.escape(str(o.get('price_net','—')))}<br><span class="k">net / {html.escape(str(o.get('price_gross','—'))) if o.get('price_gross') else '—'}</span></td>
      <td class="num">{o.get('eur_per_gb','—')}</td>
      <td>{html.escape(str(o.get('stock','—')))}</td>
      <td class="num">{html.escape(str(o.get('checked','—')))}</td>
      <td><a href="{html.escape(o['url'])}">open ↗</a></td>
    </tr>"""

for o in data["offers"]:
    if o.get("best"):
        break

best_kit = next((o for o in data["offers"] if o.get("best")), data["offers"][0])
gen = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ")

# KPI card 1 is the cheapest full 2Rx4 build (user directive 2026-11-16: 2Rx4 only, so the 384 GB
# 12x32 tier is gone). Read it from the ladder so the card cannot drift from the table below.
fullrows = [r for r in (data.get("ladder") or {}).get("rows", []) if r["cap"].startswith("768 GB (12×64")]
if fullrows:
    row = min(fullrows, key=lambda r: float(r["net"].replace("€", "").replace(".", "").replace(",", ".")))
    route = row["route"].split(" @ ")
    kit_net, kit_label, kit_url = row["net"], f"12× {route[0].split('× ', 1)[-1]}" + (f" — {route[1]}" if len(route) > 1 else ""), row.get("url")
    kit_cap = "Cheapest qualified 768 GB (12×64, 2Rx4)"
else:
    kit_net, kit_label, kit_url, kit_cap = best_kit.get("twelve_kit_net", 14372), best_kit["part"], best_kit.get("url"), "Cheapest kit"

lad = data.get("ladder")
if lad and lad.get("rows"):
    def _lroute(r):
        rt = html.escape(r["route"])
        return f'<a href="{html.escape(r["url"])}">{rt}</a>' if r.get("url") else rt

    lrows = "".join(
        f"<tr><td><b>{html.escape(r['cap'])}</b><br><span class='k'>{html.escape(r['caveat'])}</span></td>"
        f"<td>{_lroute(r)}</td>"
        f"<td class='num'>{html.escape(r['net'])}</td>"
        f"<td class='num'>{html.escape(r['per_gb'])}</td></tr>"
        for r in lad["rows"])
    LADDER = (f"<h1 style='font-size:18px;margin:0 0 6px'>Capacity ladder — cheapest verified route</h1>"
              f"<p class='sub' style='margin:0 0 10px'>{html.escape(lad.get('rule',''))} · ladder updated {html.escape(lad.get('updated',''))}</p>"
              f"<table style='margin-bottom:22px'><thead><tr><th>Capacity</th><th>Route</th><th class='num'>Net total</th><th class='num'>€/GB</th></tr></thead>"
              f"<tbody>{lrows}</tbody></table>")
else:
    LADDER = ""

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>R9700 ×4 — RAM offer board (DDR5-6400 RDIMM, JEDEC-SPD rule)</title><style>
  :root {{ --bg:#101317; --panel:#171c22; --text:#e8edf2; --muted:#96a3b2; --line:#2b3540; --accent:#f5a524; }}
  body {{ margin:0; background:var(--bg); color:var(--text); font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif; }}
  .wrap {{ max-width:1100px; margin:0 auto; padding:36px 24px 60px; }}
  h1 {{ font-size:26px; margin:0 0 4px; letter-spacing:-.02em; }}
  .sub {{ color:var(--muted); margin:0 0 20px; }}
  .kpi {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-bottom:22px; }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:16px 18px; }}
  .card h2 {{ margin:0; font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:.04em; }}
  .big {{ font-size:26px; font-weight:700; margin-top:6px; letter-spacing:-.02em; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; background:var(--panel); border:1px solid var(--line); border-radius:12px; overflow:hidden; }}
  th,td {{ text-align:left; padding:10px 10px; border-bottom:1px solid var(--line); vertical-align:top; }}
  th {{ font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--muted); background:var(--panel); }}
  td.num,th.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
  tr:last-child td {{ border-bottom:0; }}
  a {{ color:#4cc9f0; text-decoration:none; }}
  .tag {{ font-size:11px; padding:2px 8px; border-radius:999px; border:1px solid var(--line); color:var(--muted); }}
  .tag.rec {{ background:var(--accent); border-color:var(--accent); color:#101317; font-weight:700; }}
  .tag.warn {{ border-color:var(--accent); color:var(--accent); }}
  .tag.bad {{ border-color:#f87171; color:#f87171; }}
  .k {{ color:var(--muted); font-size:12px; }}
  footer {{ margin-top:18px; color:var(--muted); font-size:12px; }}
  code {{ color:#4cc9f0; }}
</style></head><body><div class="wrap">
<h1>RAM offer board — DDR5-6400 RDIMM (JEDEC-SPD rule)</h1>
<p class="sub">Board: Supermicro H14SSL-NT · CPU: EPYC 9555 · 12 DIMM slots, 1DPC · JEDEC-only BIOS → a module counts only if its <b>JEDEC SPD default is 6400 @ 1.1 V</b> (no EXPO/XMP). <b>Module type: 2Rx4 only</b> (directive 2026-11-16) — 1Rx8/2Rx8 rows are struck from the ladder. Net = VAT-less where the shop allows it. PLN→EUR @ {EURPLN}.</p>
<div class="kpi">
  <div class="card"><h2>{kit_cap}</h2><div class="big">{kit_net}</div><span class="k">{html.escape(kit_label)}{f' — <a href="{html.escape(kit_url)}">source ↗</a>' if kit_url else ''}</span></div>
  <div class="card"><h2>Cheapest per GB (net)</h2><div class="big">{best_kit.get('eur_per_gb','€37.43')}</div><span class="k"><a href="{html.escape(best_kit['url'])}">open the offer ↗</a> · {html.escape(best_kit['part'].split(' (')[0])}</span></div>
  <div class="card"><h2>Updated</h2><div class="big">{gen}</div><span class="k">by the 30-min scheduler · <code>docs/research/beam-eu-6400-repoke.md</code></span></div>
</div>
{LADDER}
<table>
<thead><tr><th>Part / spec</th><th>Shop</th><th class="num">Price (net / gross)</th><th class="num">€/GB net</th><th>Stock</th><th class="num">Checked</th><th>Link</th></tr></thead>
<tbody>
{rows}
</tbody></table>
<footer>Rule reminder: "6400" only counts if JEDEC SPD default = 6400 @ 1.1 V (Kingston datasheet sentence verified per part; Samsung/Micron publish no SPD sentence). Source of truth: docs/research/RECOMMENDATION.md + beam-eu-6400-*.md. This page is generated from docs/research/ram-offers.json.</footer>
</div></body></html>"""

OUT.write_text(page)
print(f"wrote {OUT} ({len(data['offers'])} offers)")
