# EPYC 9005 — every SKU with 8 or more CCDs, with prices

**Source:** [`Template:AMD Epyc 9005 series`](https://en.wikipedia.org/wiki/Template:AMD_Epyc_9005_series),
read **2026-11-15**. CCD counts are the template's own *Chiplets* column
(`n × CCD 1 × I/OD`). Release prices are the template's *Release price (USD)*.

**Why 8 CCDs is the cut.** Each Zen 5 CCD carries **32 MB of L3** and one fabric
link into the IOD. The project's own threshold (see `RECOMMENDATION.md`, "Why the
8-CCD point is the right instinct") is that a part needs the full 8-CCD topology
before it can feed a 12-channel SP5 socket on a CPU-offloaded expert lane. Parts
below 8 CCDs are listed at the end so the filter is auditable, not silent.

Units: "Release $" is the page's launch price. "Recorded" is what this project
read off **AMD's own product pages in Nov 2026** (1kU or EU street, labelled).
Where the two disagree they are both shown — see the note at the bottom.

---

## SP5 · Zen 5 "Turin" — the parts that matter for this build

| SKU | Cores | **CCDs** | Core cfg | L3 | Base GHz | TDP | Release $ | Recorded / street |
|---|---:|---:|---|---:|---:|---:|---:|---|
| 9175F | 16 | **16** | 16 × 1 | 512 MB | 4.20 | 320 W | $4,256 | — |
| 9275F | 24 | **8** | 8 × 3 | 256 MB | 4.10 | 320 W | $3,439 | — |
| **9355P** | 32 | **8** | 8 × 4 | 256 MB | 3.55 | 280 W | **$2,998** | no QS tier; EU €3,718–4,706 |
| **9355** | 32 | **8** | 8 × 4 | 256 MB | 3.55 | 280 W | $3,694 | **€2,050 street** (eBay DE, new) |
| 9375F | 32 | **8** | 8 × 4 | 256 MB | 3.80 | 320 W | $5,306 | — |
| 9455P | 48 | **8** | 8 × 6 | 256 MB | 3.15 | 300 W | $4,819 | — |
| 9455 | 48 | **8** | 8 × 6 | 256 MB | 3.15 | 300 W | $5,412 | $4,959 rec |
| 9475F | 48 | **8** | 8 × 6 | 256 MB | 3.65 | 400 W | $7,592 | $6,539 rec |
| 9535 | 64 | **8** | 8 × 8 | 256 MB | **2.40** | 300 W | $8,992 | — |
| 9555P | 64 | **8** | 8 × 8 | 256 MB | 3.20 | 360 W | $7,983 | EU €4,493–4,509 (no QS) |
| **9555** | 64 | **8** | 8 × 8 | 256 MB | 3.20 | 360 W | $9,826 | €4,529 DE; **QS €932–1,050** |
| 9575F | 64 | **8** | 8 × 8 | 256 MB | 3.30 | 400 W | $11,791 | $9,238 rec |
| 9565 | 72 | **12** | 12 × 6 | 384 MB | 3.15 | 400 W | $10,468 | $8,233 rec |
| 9655P | 96 | **12** | 12 × 8 | 384 MB | 2.50 | 400 W | $10,811 | — |
| 9655 | 96 | **12** | 12 × 8 | 384 MB | 2.50 | 400 W | $11,852 | €4,129+ retail |
| 9755 | 128 | **16** | 16 × 8 | 512 MB | 2.70 | 500 W | $12,984 | €3,299 QS; $10,931 rec |

## SP5 · Zen 5c "Turin Dense"

| SKU | Cores | **CCDs** | Core cfg | L3 | Base GHz | TDP | Release $ | Recorded / street |
|---|---:|---:|---|---:|---:|---:|---:|---|
| 9645 | 96 | **8** | 8 × 12 | 256 MB | 2.30 | 320 W | $11,048 | — |
| 9745 | 128 | **8** | 8 × 16 | 256 MB | 2.40 | 400 W | $12,141 | — |
| 9845 | 160 | **10** | 10 × 16 | 320 MB | 2.10 | 390 W | $13,564 | — |
| 9825 | 144 | **12** | 12 × 12 | 384 MB | 2.20 | 390 W | $13,006 | — |
| 9965 | 192 | **12** | 12 × 16 | 384 MB | 2.25 | 500 W | $14,813 | €5,049.59 QS; $11,988 rec |

## SP6 "Sorano" — 8+ CCDs, but a six-channel platform

| SKU | Cores | **CCDs** | Core cfg | L3 | Base GHz | TDP | Release $ |
|---|---:|---:|---|---:|---:|---:|---:|
| 8325P | 32 | **8** | 8 × 4 | 256 MB | 2.70 | 175 W | $2,299 |
| 8435P | 48 | **8** | 8 × 6 | 256 MB | 2.45 | 200 W | $3,099 |
| 8535P | 64 | **8** | 8 × 8 | 256 MB | 2.00 | 210 W | $5,499 |
| 8635P | 84 | **12** | 12 × 7 | 384 MB | 1.60 | 225 W | $5,799 |

**These do not qualify.** SP6 is **six-channel** (6 × 6400 ≈ 307 GB/s), so an
8-CCD part there has *more* fabric than the socket can feed. Listed for
completeness only — the 8-CCD rule assumes SP5's 12 channels.

---

## Notes

1. **Cheapest 8-CCD on list price is the 9355P at $2,998**, then the 9275F
   ($3,439), then the 9355 ($3,694). But **list order inverts at street**: the
   P-SKU list discount does not reach retail, the 9355P has **no sample market
   at all**, and the 9275F has no recorded street price. The **practical entry
   point stays the 9355 at €2,050** — the only 8-CCD part with confirmed cheap
   stock.
2. **9535 is a trap for this build:** same 8 CCDs as the 9555, but **2.4 GHz base
   vs 3.2 GHz** for nearly the same list price ($8,992 vs $9,826). CPU expert
   compute runs at base clock, so the 9555 dominates it.
3. **The F parts are the odd corner:** the 9175F is **16 CCDs of one core each**
   (16c, 4.2 GHz base, $4,256) and the 9275F is **8 CCDs of three** (24c,
   4.1 GHz, $3,439). Both clear the fabric bar with very high clocks and few
   cores — plausibly interesting for latency-bound decode, but neither has a
   recorded street price and both sit outside the 24–40-core knee's sweet spot
   in cores/CCD terms.
4. **Price-source divergence, flagged not resolved.** For the high-core SKUs the
   page's *release* figures run **10–25 % above** the 1kU figures this project
   read from AMD's product pages in Nov 2026 (e.g. 9555 $9,826 here vs $7,973
   recorded; 9965 $14,813 vs $11,988; 9655 $11,852 vs $8,999). The two sources
   agree exactly on the small skus (9135 $1,214, 9355 $3,694). Likely the page
   carries launch prices while our figures were current 1kU — **not confirmed**;
   re-check AMD's product page before quoting a list price for anything above
   9355.
5. **Excluded by the 8-CCD filter** (2/4/6-CCD parts, listed so the cut is
   auditable): SP5 — 9015, 9115, **9135**, 9255, 9335, 9365; SP6 — 8025P, 8125P,
   8225P; AM5 "Grado" — 4245P, 4345P, 4465P, 4545P, 4565P, 4585PX (all ≤2 CCD,
   dual-channel). Note the 9135's exclusion is the load-bearing one for this
   project: it is a 2-CCD part, which is why it was rejected for a spilling MoE.
6. **Verification pass (2026-11-15):** all 37 SKUs were checked against the
   derived rule `CCDs == L3 ÷ 32 MB` and `cores ÷ CCDs` integral. **36 of 37
   agree**; the single exception is **4585PX** (2 CCDs, 128 MB = 64 MB/CCD),
   which is the **3D V-Cache** corner — a stacked CCD carries 32 MB base + up to
   64 MB stacked, so the ÷32 MB rule **understates** CCDs on X3D-style parts.
   No SP5 part in this list is affected (the exception is AM5-only), so every
   CCD count above rests on the template's own *Chiplets* column, not on the
   rule. The rule was used to *cross-check* the column, not to replace it.
