# eBay.com sweep — every 8+ CCD EPYC 9005 SKU

**Route:** Camoufox (Firefox engine, fingerprint spoofing, `headless`), run
**2026-11-15**. eBay.com search per SKU, `LH_BIN=1`, sorted price+shipping
lowest. Script: `/tmp/opencode/ebay_cpu_sweep.py` (kept outside the repo — it
needs the `/tmp/opencode/pwenv` venv). Raw listings:
[`cpu-ebay-sweep.json`](cpu-ebay-sweep.json).

**Why Camoufox:** per this project's pass-30 note, eBay.com item and search pages
are IP-walled to 4/4 headless-Chromium attempts and render under Camoufox. Used
here for the same reason.

**Markup note for future sweeps:** eBay renders `li.s-card` (2026-11), **not** the
legacy `li.s-item` — a parser written for `s-item` returns zero rows while the
page is perfectly healthy. Fields are `s-card__title` / `s-card__price` /
`s-card__subtitle`; the first card on every page is a "Shop on eBay" placeholder.

Units: **USD, Buy-It-Now, before shipping/tax.** "Valid floor" = cheapest listing
that (a) names the SKU as a standalone token and (b) is not a sample, not
vendor-locked, not an OEM re-badge, not a bundle. See traps below — the raw
"cheapest" number is misleading on six SKUs.

---

## The board

| SKU | Cores | CCDs | L3 MB | Base GHz | TDP | Plat | Valid floor | New floor | Best cond. |
|---|---:|---:|---:|---:|---:|---|---:|---:|---|
| 9175F | 16 | 16 | 512 | 4.20 | 320 | SP5 | **$2,616** | $2,616 | Brand New |
| 9275F | 24 | 8 | 256 | 4.10 | 320 | SP5 | $660 ⛔ | $3,180 | Pre-Owned |
| 9355P | 32 | 8 | 256 | 3.55 | 280 | SP5 | $3,568 | $3,830 | Refurb |
| **9355** | 32 | 8 | 256 | 3.55 | 280 | SP5 | **$2,130** | $2,299 | Pre-Owned |
| 9375F | 32 | 8 | 256 | 3.80 | 320 | SP5 | $3,849 | $3,849 | Brand New |
| 9455P | 48 | 8 | 256 | 3.15 | 300 | SP5 | $3,983 | $3,983 | New (Other) |
| 9455 | 48 | 8 | 256 | 3.15 | 300 | SP5 | $3,857 | $3,857 | Brand New |
| 9475F | 48 | 8 | 256 | 3.65 | 400 | SP5 | $4,580 | $4,800 | Open Box |
| 9535 | 64 | 8 | 256 | **2.40** | 300 | SP5 | $2,999 | $4,135 | Pre-Owned |
| 9555P | 64 | 8 | 256 | 3.20 | 360 | SP5 | $5,870 | $5,870 | Brand New |
| **9555** | 64 | 8 | 256 | 3.20 | 360 | SP5 | $4,362 | $4,362 | Brand New |
| 9575F | 64 | 8 | 256 | 3.30 | 400 | SP5 | $4,945 | $4,945 | Brand New |
| 9565 | 72 | 12 | 384 | 3.15 | 400 | SP5 | $4,852 | $4,968 | Open Box |
| 9655P | 96 | 12 | 384 | 2.50 | 400 | SP5 | $5,488 | $10,445 | Open Box |
| 9655 | 96 | 12 | 384 | 2.50 | 400 | SP5 | $4,286 | $4,286 | Brand New |
| 9755 | 128 | 16 | 512 | 2.70 | 500 | SP5 | $4,499 | $4,688 | Pre-Owned |
| 9645 | 96 | 8 | 256 | 2.30 | 320 | SP5c | $4,688 | $4,688 | Brand New |
| 9745 | 128 | 8 | 256 | 2.40 | 400 | SP5c | $4,000 | $4,520 | Open Box |
| 9845 | 160 | 10 | 320 | 2.10 | 390 | SP5c | $4,950 | $5,699 | Pre-Owned |
| 9825 | 144 | 12 | 384 | 2.20 | 390 | SP5c | $5,550 | $6,888 | Refurb |
| 9965 | 192 | 12 | 384 | 2.25 | 500 | SP5c | $5,680 | $5,680 | Brand New |
| 8325P | 32 | 8 | 256 | 2.70 | 175 | SP6 | **—** | — | no listings |
| 8435P | 48 | 8 | 256 | 2.45 | 200 | SP6 | $4,329 | $4,329 | Brand New |
| 8535P | 64 | 8 | 256 | 2.00 | 210 | SP6 | $5,706 | $5,706 | Brand New |
| 8635P | 84 | 12 | 384 | 1.60 | 225 | SP6 | $5,903 | $5,903 | Brand New |

**SP6 parts are flagged, not qualified** — six-channel (≈307 GB/s), so their
8 CCDs outrun the socket; listed because they were in the SKU set.

## Traps this sweep found (why the raw "cheapest" column lies)

Six SKUs show a headline price that is **not the part being advertised**. Each
was caught by reading the titles rather than trusting the sort order:

| SKU | Raw cheapest | What it actually is |
|---|---:|---|
| 9535 | $896 | **A 9555 sample.** Every cheap "9535" carries OPN `100-000001247-12` and "1.9 GHz" — that is the **9555's** sample OPN, mislabelled as a 9535. |
| 9555 | $1,037 | The real 9555 sample bin — `1.9–3.35 GHz`, i.e. the **low-clock ES** this project already ruled out. |
| 9555 | $1,500 | **Dell Locked** (retail `100-000001142`, 3.2 GHz) — the ub-locked bin, POST risk. |
| 9755 | $1,639 | `9755 QS (ES)` at €3,299-class pricing; and the cheapest "New" 9755 is an **`EPYC 9B45`, "OEM of 9755"** — a re-badged OEM part, not a retail 9755. |
| 9965 | $2,085 | **A Ryzen Threadripper PRO 9965WX** — same number, wrong product line entirely. |
| 9845/9745/9275F | $1,387 / $3,499 / $660 | ES/QS bins (`1152-07`, `1.9 GHz`, QS). |

**The rule that falls out:** on eBay, the SKU token in a title is not evidence
the item is that SKU. Six of 25 here fail that test. Any price from this sweep
should be re-read against the title, and the buyer should ask for a **CPU-Z or
IHS photo** before paying — the same standard this project already applies to the
9555 sample market.

### The $660 "9275F" outlier — decoded 2026-11-16 (item `128080874643`, seller `tomboost`)

**It is a Dell-only PSB-locked server pull, and the listing admits it.** The
seller's own description reads:

> "AMD EPYC 9275F 4.10Ghz, 24 coeurs et 48 thread. 256Mo de cache 320W
> Compatible DDR5-6400. **From Dell server can be PSB lock dell only.** I have two
> CPU, contact me if you want two, special price."

That explains the €599 (≈$660) price: **PSB-locked, Dell-only.** It will not POST
in a Supermicro H14SSL-N — the exact vendor-lock risk this project already left
UNVERIFIED for the 9555 Dell bin, here **conceded by the seller**. Same reject
class as the "9555 Dell Locked $1,500" row; it slipped the sweep's filter only
because the disqualifier sits in the *description*, not the title.

**The photo gallery does not document the item.** Seven images: one **stock
marketing photo** ("Dawson Electronics", plane + "Quality assurance") showing OPN
**`100-000001245-08`** — *not* the 9275F's `100-000001144`; a **delidded** sTR5
part with a copper IHS and liquid metal; a Task Manager screenshot showing
**2 sockets / 48 cores / 512 MB L3** (a 2× 9275F host the seller owns, not the
CPU on sale); and **two unrelated Intel desktop CPUs** — a **Core i7-860 SLBJJ**
(2009, 2.80 GHz) and a **Core i7-2600 SR00B** (2011, 3.40 GHz, Costa Rica), both
with legible Intel heatspreaders.

**Verdict: reject on two independent grounds** — PSB-locked Dell-only, and a
gallery that shows other parts. The $660 is not a bargain; it is the price of a
part that will not boot in this build. **The 9275F's true floor is $3,180**, the
Brand New "AMD EPYC-9275F CPU II … 3 yr warranty" listing.

**Lesson for the classifier:** eBay sellers sometimes put the disqualifier in the
**description** and the give-away in the **gallery**, not the title. A title-only
filter misses those — for any listing far below the 25th-percentile price, read
the description and the images before believing the SKU.

## What is actually cheap in valid, retail-clocked form

- **9355 — $2,130 used / $2,299 new.** Still the value pick, and consistent with
  the EU €2,050 floor recorded in `RECOMMENDATION.md`. US channel is now bracketed
  on both sides.
- **9175F — $2,616 new.** Confirms the €2,673–3,500 EU range; the US channel is
  marginally cheaper.
- **9455 / 9655 — $3,857 / $4,286 new.** The cheapest 8-CCD 48-core and the
  cheapest 12-CCD 96-core respectively; both are real, brand-new listings.
- **9745 — $4,000 open-box**, the cheapest 8-CCD 128-core (SP5c), for the
  Zen5c-dense case.
- **9535 — $2,999 used** is valid but note the **2.4 GHz base**, the trap this
  project already flagged: same 8 CCDs as the 9555 for more money at a lower
  clock.

**Nothing here displaces the 9355.** The sweep's job was to test whether any
8-CCD part undercuts it in a buyable, retail-clocked form. None does.

## Caveats

1. **US listings, before shipping and import.** EU buyers add freight and (if not
   VAT-registered) ~23% import VAT; the EU floors in `RECOMMENDATION.md` are the
   comparable numbers, not these.
2. **Buy-It-Now only** (`LH_BIN=1`) — auctions excluded by design.
3. **One pass, one day.** eBay stock rotates hourly; treat as a snapshot, not a
   price list.
4. **The classifier is a regex, not a human.** It rejects on
   `ES|QS|1.9 GHz|1.8 GHz|Dell Locked|OEM of|9B45|9V64|refurb|1152-0*|976-1*|1247-1*|1252-0*`
   and requires the SKU token to appear standalone. It is deliberately
   conservative; a listing it rejected could still be genuine, but nothing it
   *passed* should be assumed checked by eye.
