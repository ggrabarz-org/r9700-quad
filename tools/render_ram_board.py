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
FX = data.get("fx", {"EUR":4.4070,"USD":3.9852,"CHF":4.7618,"GBP":5.2737,"PLN":1.0})
for _k,_v in FX.items():  # format for the footnote (comma decimals, like the rest of the board)
    FX[_k] = _v

def fmt(v):
    return f"€{v:,.0f}" if isinstance(v, (int, float)) else v

def money(v, cur):
    """format a number in its own currency, European style"""
    if v is None: return "—"
    s = f"{v:,.2f}"
    if cur in ("EUR", "PLN", "CHF", "USD", "GBP"):
        s = s.replace(",", "\u00a0").replace(".", ",").replace("\u00a0", " ")
    sym = {"EUR": "€", "PLN": "zł", "CHF": "CHF ", "USD": "$", "GBP": "£"}.get(cur, "")
    return f"{sym}{s}" if cur in ("EUR", "GBP") else f"{sym}{s}"

rows = ""
for o in data["offers"]:
    p = o.get("price") or {}
    cur = p.get("cur")
    vatp = p.get("vat")
    has = cur is not None and (p.get("gross") is not None or p.get("net") is not None)
    vats = f"{vatp*100:.0f}%" if (has and isinstance(vatp, (int, float))) else "—"
    gross = money(p.get("gross"), cur) + (f'<span class="k">*</span>' if p.get("gross_derived") else "")
    net   = money(p.get("net"), cur)   + (f'<span class="k">*</span>' if p.get("net_derived") else "")
    gl = "gross · VAT " + vats if has else "—"
    nl = "net " + (cur or "") if has else "—"
    netpln = money(p.get("net_pln"), "PLN") if p.get("net_pln") is not None else "—"
    eurgb = o.get("eur_per_gb", "—")

    def sk(v):
        return "" if v is None else f"{v:.2f}"
    best = ' <span class="tag rec">BEST</span>' if o.get("best") else ""
    orgv = str(o.get("org", ""))
    # org is informational since the 2026-11-17 directive dropped the 2Rx4-only rule; only the
    # JEDEC-SPD-6400@1.1V gate decides eligibility, so no org value is flagged bad.
    org = f' <span class="tag {"rec" if "2Rx4" in orgv else ""}">{html.escape(orgv)}</span>' if orgv else ""
    cd = o.get("condition") or ""
    ctag = ""
    if cd:
        _used = any(k in cd.lower() for k in ("pull", "used", "refurb", "open box"))
        ctag = f' <span class="tag {"bad" if _used else "rec"}">{html.escape(cd)}</span>'
    qv = o.get("qvl_mz23su0")
    qtag = ""
    if qv == "pass": qtag = ' <span class="tag rec" title="listed on the MZ23-SU0 memory QVL">QVL ✓</span>'
    elif qv == "fail": qtag = ' <span class="tag bad" title="NOT in the MZ23-SU0 memory QVL">QVL ✗</span>'
    flag = "" if o.get("state", "ok") in ("ok", "new") else f' <span class="tag {"warn" if o["state"] in ("stale","unreachable","withdrawn") else "bad"}">{html.escape(o["state"])}</span>'
    rows += f"""<tr>
      <td data-s="{sk(p.get('net_pln'))}">{html.escape(o['part'])}<br><span class="k">{html.escape(o.get('spec',''))}</span>{best}{org}{ctag}{qtag}{flag}</td>
      <td data-s="{html.escape(o['shop'])}">{html.escape(o['shop'])}<br><span class="k">{html.escape(o.get('country',''))}</span></td>
      <td class="num" data-s="{sk(p.get('gross'))}">{gross}<br><span class="k">{gl}</span></td>
      <td class="num" data-s="{sk(p.get('net'))}">{net}<br><span class="k">{nl}</span></td>
      <td class="num" data-s="{sk(p.get('net_pln'))}">{netpln}<br><span class="k">net PLN</span></td>
      <td class="num" data-s="{sk(p.get('net_pln') if False else None)}">{eurgb}</td>
      <td>{html.escape(str(o.get('stock','—')))}</td>
      <td class="num" data-s="{html.escape(str(o.get('checked','—')))}">{html.escape(str(o.get('checked','—')))}</td>
      <td><a href="{html.escape(o['url'])}">open ↗</a></td>
    </tr>"""

for o in data["offers"]:
    if o.get("best"):
        break

best_kit = next((o for o in data["offers"] if o.get("best")), data["offers"][0])
gen = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ")

# KPI 1: cheapest total-spend build from QVL-PASSING parts, priced per 12 modules.
# (2Rx4-only filter dropped 2026-11-17 by user directive — only the JEDEC-SPD-6400@1.1V gate counts now.)
_q = [o for o in data["offers"]
      if o.get("qvl_mz23su0") == "pass"
      and (o.get("price") or {}).get("net_pln") and (o.get("price") or {}).get("gb")]
if _q:
    def _pergb(o):
        p = o["price"]
        return p["net"] * (data["fx"][p["cur"]] / data["fx"]["EUR"]) / p["gb"]
    # card 1 answers "cheapest TOTAL spend for a QVL-passing 12-module build"
    o = min(_q, key=lambda x: x["price"]["net"] * (data["fx"][x["price"]["cur"]] / data["fx"]["EUR"]))
    gb12 = o["price"]["gb"] * 12
    kit_net = money(o["price"]["net"] * 12, o["price"]["cur"])
    kit_label = f'12× {o["part"].split(" (")[0]} — {o["shop"].split(" (")[0]} · {gb12} GB · €{_pergb(o):.2f}/GB'
    kit_url = o.get("url")
    kit_cap = f"Lowest total spend — QVL-passing ({gb12} GB)"
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

if _q:
    _b = min(_q, key=lambda x: _pergb(x))
    gb_best = f"€{_pergb(_b):.2f}"
    _cond = _b.get("condition", "")
    gb_label = f'{_b["part"].split(" (")[0]} · {_b["shop"].split(" (")[0]}' + (f' · {_cond}' if _cond else "")
    gb_url = _b.get("url")
else:
    gb_best, gb_label, gb_url = best_kit.get("eur_per_gb", "—"), best_kit["part"], best_kit.get("url", "")

brc = data.get("board_rule_check")
if brc:
    BOARD_NOTE = (f"<div class='ask'><b>Board rule verified on the current board</b> — {html.escape(brc['source'])}<br>"
                  f"<span class='k'>{html.escape(brc['verbatim'])}</span><br>"
                  f"<b>→ {html.escape(brc['conclusion'])}</b></div>")
else:
    BOARD_NOTE = ""

qs = data.get("qvl_buyable_shortlist")
if qs:
    BOARD_NOTE += (f"<div class='ask'><b>QVL shortlist — what can actually be bought</b> "
                   f"<span class='k'>(checked {html.escape(qs['checked'])})</span><br>"
                   f"<span class='k'>{html.escape(qs['conclusion'])}</span><br>"
                   f"<b>→ {html.escape(qs['implication'])}</b></div>")

lc = data.get("lifecycle_signal")
if lc:
    BOARD_NOTE += (f"<div class='ask' style='background:linear-gradient(180deg,#3a2a12,#101317);border-color:#8a6417'>"
                   f"<b style='color:#f5c451'>Lifecycle warning</b> — observed {html.escape(lc['observed'])}<br>"
                   f"<span class='k' style='color:#d8c49a'>{html.escape(lc['digikey'])}</span><br>"
                   f"<span class='k' style='color:#d8c49a'>Corroboration: {html.escape(lc['corroboration'])}</span><br>"
                   f"<span class='k' style='color:#d8c49a'>Scope: {html.escape(lc['scope'])}</span><br>"
                   f"<b style='color:#f5c451'>→ {html.escape(lc['consequence'])}</b></div>")

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>R9700 ×4 — RAM offer board (DDR5-6400 RDIMM, JEDEC-SPD rule)</title><style>
  :root {{ --bg:#101317; --panel:#171c22; --text:#e8edf2; --muted:#96a3b2; --line:#2b3540; --accent:#f5a524; }}
  body {{ margin:0; background:var(--bg); color:var(--text); font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif; }}
  .wrap {{ max-width:1100px; margin:0 auto; padding:36px 24px 60px; }}
  h1 {{ font-size:26px; margin:0 0 4px; letter-spacing:-.02em; }}
  .sub {{ color:var(--muted); margin:0 0 20px; }}
  .ask {{ background:linear-gradient(180deg,#12341f,#101317); border:1px solid #1f6b3d; border-radius:12px; padding:14px 18px; margin:0 0 20px; }}
  .ask b {{ color:#7ee2a8; }}
  .ask .k {{ color:#9fc7b0; }}
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
<p class="sub">Board: <b>GIGABYTE MZ23-SU0 (Rev. 3.x)</b> · CPU: EPYC 9555 · 12-channel, 12 DIMM slots (2DPC capable, up to 9 TB) · JEDEC-only BIOS → a module counts only if its <b>JEDEC SPD default is 6400 @ 1.1 V</b> (no EXPO/XMP). <b>Any rank/org (directive 2026-11-17)</b> — the rated speed on the box is irrelevant; a 7600-rated kit with a 6400 JEDEC default qualifies, a 6400-rated kit defaulting to 4800 does not. Net = VAT-less where the shop allows it. PLN→EUR @ {EURPLN}.</p>
<div class="kpi">
  <div class="card"><h2>{kit_cap}</h2><div class="big">{kit_net}</div><span class="k">{html.escape(kit_label)}{f' — <a href="{html.escape(kit_url)}">source ↗</a>' if kit_url else ''}</span></div>
  <div class="card"><h2>Cheapest per GB — QVL-passing</h2><div class="big">{gb_best}</div><span class="k"><a href="{html.escape(gb_url)}">open the offer ↗</a> · {html.escape(gb_label)}</span></div>
  <div class="card"><h2>Updated</h2><div class="big">{gen}</div><span class="k">by the 30-min scheduler · <code>docs/research/beam-eu-6400-repoke.md</code></span></div>
</div>
{LADDER}
{BOARD_NOTE}
<table id="offers">
<thead><tr>
  <th>Part / spec</th><th>Shop</th>
  <th class="num">Gross <span class="k">(own currency)</span></th>
  <th class="num">Net <span class="k">(own currency)</span></th>
  <th class="num">Net <span class="k">PLN</span></th>
  <th class="num">€/GB net</th>
  <th>Stock</th><th class="num">Checked</th><th>Link</th>
</tr></thead>
<tbody>
{rows}
</tbody></table>
<p class="sub" style="margin:10px 0 0">Click a column header to sort (again to reverse). <b>*</b> = value derived from the other side of the VAT split, not read off the page. FX: NBP table A 2026-11-13 — EUR {FX['EUR']}, USD {FX['USD']}, CHF {FX['CHF']}, GBP {FX['GBP']} PLN. Rows showing "—" have no price (status records) or a multi-SKU text cell; their prose cell remains authoritative.</p>
<footer>Rule reminder: "6400" only counts if JEDEC SPD default = 6400 @ 1.1 V (Kingston datasheet sentence verified per part; Samsung/Micron publish no SPD sentence). Source of truth: docs/research/RECOMMENDATION.md + beam-eu-6400-*.md. This page is generated from docs/research/ram-offers.json.</footer>
</div>
<script>
(function(){{
  var t=document.getElementById('offers'), tb=t.tBodies[0];
  var dir={{}};
  t.querySelectorAll('th').forEach(function(th,i){{
    th.style.cursor='pointer';
    th.title='sort by this column';
    th.addEventListener('click',function(){{
      var rows=Array.prototype.slice.call(tb.rows);
      dir[i]=!dir[i];
      var num=(th.className||'').indexOf('num')>-1;
      rows.sort(function(a,b){{
        var x=a.cells[i].getAttribute('data-s'), y=b.cells[i].getAttribute('data-s');
        var ex=(x===null||x===''), ey=(y===null||y==='');
        if(ex&&ey) return 0;
        if(ex) return 1;            // empties always last
        if(ey) return -1;
        if(num){{var nx=parseFloat(x),ny=parseFloat(y);
          if(!isNaN(nx)&&!isNaN(ny)) return dir[i]?nx-ny:ny-nx;}}
        return dir[i]? x.localeCompare(y) : y.localeCompare(x);
      }});
      rows.forEach(function(r){{tb.appendChild(r)}});
      t.querySelectorAll('th').forEach(function(h,j){{if(j!==i)h.removeAttribute('data-arrow')}});
      th.setAttribute('data-arrow', dir[i]?'▲':'▼');
      th.textContent = th.textContent.replace(/[▲▼]$/,'').trim() + (dir[i]?' ▲':' ▼');
    }});
  }});
}})();
</script>
</body></html>"""

OUT.write_text(page)
print(f"wrote {OUT} ({len(data['offers'])} offers)")
