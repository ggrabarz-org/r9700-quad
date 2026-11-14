# Beam EU research — DDR5-6400 ECC RDIMM, obscure-shop sweep — 2026-11-13

Scope: cheapest DDR5- **ECC Registered DIMM (RDIMM)**, 288-pin, JEDEC-6400 **SPD at 1.1 V**
(Supermicro H14SSL-NT BIOS is JEDEC-only, no EXPO/XMP), accepting only 16/32/64 GB modules or
kits of 4/8; rejecting UDIMM/SODIMM/CUDIMM and anything that needs EXPO/XMP (1.35–1.4 V) to reach
6400 MHz.

Conv.: PLN → EUR × 4.4070. UK shop prices exclude UK VAT and are post-Brexit imports — **not
directly comparable**. Today: 2026-11-13.

## Slice: DE/AT/FR/IT/ES

### A. Mainstream DE consumer/IT big-box + marketplace slice

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 128 GB (4×32) Quad Channel Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC ("JEDEC standard at 1.1 V"); SPD = 6400 MT/s - 1.1 V - CL52 - 52-52-52 | **€5,392.42**, OutOfStock (JSON-LD price; tile showed €5,371.78) | OOS | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |
| Caseking (DE) | G.Skill Zeta R5 DDR5-6400 CL32, XMP, ECC reg., 128 GB Octa-Kit (8×16) | **REJECTS** — CL32 @ 1.4 V via XMP → not JEDEC-6400/1.1 V | **€1,580.08**, OutOfStock, MEGS-318 | OOS | https://www.caseking.de/en/g.skill-zeta-r5-ddr5-6400-ram-cl32-xmp-ecc-reg.-128-gb-octo-kit-black/MEGS-318.html |
| Caseking (DE) | KLEVV / PATRIOT / V-Color Manta DDR5-6400 CL30–38 kits | **REJECTS** — 6400 reached via XMP 3.0 / EXPO only | various, mostly OutOfStock; e.g. KLEVV CRAS V RGB EXPO CL32 32GB **€517.26** OOS, MEGV/MEKV | mixed | https://www.caseking.de/en/pc-components/memory/ddr5/6400-mhz-ddr5-ram |

### B. Server-specialist slice (DE/AT/FR/IT/ES)

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| ibfusion (DE/ES) | Kingston KSM64R52BD4-64MD (64 GB, 2Rx4) | **QUALIFIES** — "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | **€2,481.00 excl. VAT (€2,681.96 incl. 8.1 % CH VAT)**, 4 in stock | EU delivery 7–21 business days | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 256 GB (8×32) Octa-Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€12,784.85**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-ddr5-6400-ram-cl52-jedec-256-gb-octa-kit-black/MEVC-033.html |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 64 GB (4×16) Quad Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€3,386.92**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-64-gb-4-x-16-gb-quad-channel-kit-black/MEVC-025.html |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 128 GB (8×16) Octa-Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€6,775.97**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-ddr5-6400-ram-cl52-jedec-128-gb-octa-kit-black/MEVC-027.html |

### C. Other slice shops checked this pass

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL | Note |
|---|---|---|---|---|---|---|
| Proshop (PL/DE) | Kingston FURY Renegade PRO `KF576RH40RBK4-128` (4×32 GB) | **QUALIFIES** — SPD 6400 MT/s - 1.1 V - CL52 - 52-52-52; XMP 7600 @ 1.4 V (not used) | **€4,791 net** (25 969 zł / 21 113,01 zł netto; ×4.4070) | max 2 szt./client; sourced from Proshop | https://www.proshop.pl/RAM/Kingston-Fury-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 | €37.43/GB net — baseline to beat |
| Thomas-Krenn (DE) | — | — | — | no relevant 6400 RDIMM hit retrieved | — | no product result |
| Happyware (DE) | — | — | — | no relevant 6400 RDIMM hit retrieved | — | no product result |
| Plexcom (FR) | — | — | — | — | — | no relevant hit retrieved |
| itsco (IT) | — | — | — | — | — | no relevant hit retrieved |
| servershop24 (DE) | — | — | — | only server bundles w/ DDR5, no bare DIMM | — | no DIMM hit |
| memorysolution (DE) | — | — | — | no relevant hit retrieved | — | no DIMM hit |

## Blocked / unreachable (this pass)

- **Alternate.de** — search endpoints returned 404 / no result rows retrieved (blocked/no data).
- **Mindfactory** — Cloudflare managed challenge ("Just a moment…") → blocked.
- **Cyberport** — Cloudflare managed challenge → blocked.
- **notebooksbilliger.de** — 404 → unreachable/no data.
- **computeruniverse.de** — 403 → blocked.
- **Snogard** — request timeout → unreachable.
- **Kaufland.de** (marketplace) — 403 → blocked; no verified server-RAM seller retrieved.
- **Galaxus.de / Galaxus.at** — 403 → blocked.
- **senetic.fr** — "Rien trouvé" (no 6400 RDIMM results); senetic.de/.it/.es not re-verified this pass.
- **Fujitsu TS parts channel** — HTTP 429 rate-limited → blocked.
- **Interdiscount.ch** — 403 → blocked (CH VAT note applies if retried).
- **digitec.ch** — 403 → blocked.
- **Terra PC** — SSL certificate mismatch → unreachable.
- **server-warehouse.de / raidlinks.de** — DNS unresolvable → unreachable.
- **Tonitrus** — r.jina.ai returned 403 Forbidden (bot-wall tightened); last verified state €2,667.65 net / 50 in stock (17:4xZ) — BLOCKED this pass.
- **Proshop.de** — Cloudflare 403 "Attention Required" — unchanged since prior pass.
- **geizhals.eu / skinflint.co.uk** — Cloudflare bot-wall / CAPTCHA → blocked (index-only lead list, unverified).

## Verdict — does anything beat €37.43/GB net?

**No.** Nothing verified this pass beat the €37.43/GB net baseline (Kingston `KF576RH40RBK4-128` 4×32 GB Proshop.pl kit, €4,791 net / 128 GB).

- Best qualifying single module this pass: **ibfusion `KSM64R52BD4-64MD`** — €2,481 net (VAT 0 %) / 64 GB = **€38.77/GB net** → does **not** beat €37.43/GB, and was already known.
- Caseking's only in-stock JEDEC-6400 ECC RDIMM listings (V-Color R-DIMM JEDEC) are **OutOfStock**; its cheaper ECC kit (G.Skill Zeta R5 CL32 XMP ECC) was rejected (XMP 1.4 V, not JEDEC-1.1 V) and the V-Color JEDEC 128 GB kit sits at **€42.13/GB** OOS.
- Everything cheaper seen on Caseking (KLEVV/PATRIOT/V-Color Manta, EXPO) was **rejected** (needs EXPO).
- ibfusion KSM64R52BD4-64MD remains the cheapest confirmed qualifying source at **~€2,481 net / 64 GB (€38.77/GB)**; the 4×32 GB Proshop.pl kit at **€4,791 net (€37.43/GB)** stays the current net-best per GB.

**Bottom line:** no new or obscure-shop offer this pass beat the €37.43/GB net bar; the bar stands.

---

### Slice notes (DE/AT/FR/IT/ES)

- Caseking (DE) is the only DE slice shop that surfaced JEDEC-6400 ECC RDIMM stock data; all of it OutOfStock, and its only in-stock 6400 kits were EXPO/XMP gaming modules → correctly excluded.
- ibfusion (DE/ES) is the only confirmed qualifying, in-stock, VAT-excluded source this pass; no competitor undercut it on a per-GB basis.
- All other slice shops (Mindfactory, Cyberport, Galaxus, Kaufland, Otto, Interdiscount, digitec, notebooksbilliger, computeruniverse, Snogard, Happyware, Plexcom, itsco, Thomas-Krenn, senetic*, servershop24, memorysolution, Dell/HP/Fujitsu/PC-Specialist outlets, Terra PC, raidlinks, server-warehouse) returned no verifiable qualifying price this pass — blocked, unreachable, or no relevant hit.

## Slice: UK + niche/refurb specialists (2026-11-14 pass, supersedes the earlier partial UK draft)

Rules applied: 288-pin DDR5 **ECC Registered** DIMM only, 16/32/64 GB single modules (no kit found
in this slice, so no 4/8 kits listed), 6400 must come from the **JEDEC SPD at 1.1 V** — H14SSL-NT
BIOS is JEDEC-only. UDIMM / SODIMM / CUDIMM / MRDIMM rejected. 96 GB and 128 GB modules and
MRDIMMs (PC5-70400 / 8800) were seen and excluded by the capacity rule.

**UK caveat (binding for every £ figure below):** UK retail display prices include UK VAT unless the
shop marks them "(ex. VAT)"; the shop name is given with the basis in each row. Post-Brexit, buying
into the EU means **no UK VAT only on a B2B/export sale**, then **EU import VAT (23 % PL / 19 % DE)
+ customs handling on landing** — so a UK ex-VAT price is the best case, never the landed price.
Conversion used: **£1 = €1.1968** (Frankfurter/ECB reference, 2026-11-13; its GBP→PLN 5.2793 implies
PLN/EUR 4.411, i.e. consistent with the 4.4070 in the brief). UK VAT = 20 %, so ex-VAT = display/1.2
where the shop displays inc-VAT.

### Kingston SPD sentences (verified from kingston.com/datasheets/<PN>.pdf with pdftotext, 2026-11-14)

| Part | Sentence as printed in the datasheet |
|---|---|
| KSM64R52BD4-64HA / -64MH / -64MD, KSM64R52BS8-16MH | "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." |
| KSM64R52BD8-32MH | "The SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." |
| KF576RH40RB (FURY Renegade PRO 7600 — baseline family) | "The SPDs are programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." (XMP 7600/1.4 V is the extra) |
| KF564R32RBE (FURY Renegade 6400 CL32) | "The SPDs are programmed to JEDEC standard latency DDR5-4800 timing of 40-39-39 at 1.1V." → 6400 only via XMP 1.4 V → **REJECT** |

For Samsung / SK hynix / Micron / Silicon Power / Supermicro-branded modules: **no SPD sentence
published** by the vendor; the shop spec (6400 / CL52 / 1.1 V, RDIMM) is quoted instead.

### Crucial UK (uk.crucial.com — Micron's own storefront; display prices **inc VAT**, site flag "Inc. Vat*")

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Micron MTC40F2046S1RC64BR 64 GB DDR5-6400 RDIMM 2Rx4 CL52 1.1 V | PASS on spec — no SPD sentence published; Crucial/Micron title + spec say DDR5-6400, RDIMM, 2Rx4, CL52, 1.1 V (no XMP on server RDIMM) | Crucial UK | **£2,161.19 inc VAT** (= £1,800.99 ex VAT; £28.14/GB ex = **€33.68/GB**) | In stock (JSON-LD `InStock`, Add-to-Cart live) | https://uk.crucial.com/memory/server-ddr5/mtc40f2046s1rc64br |
| Micron MTC20F2085S1RC64BR 32 GB DDR5-6400 RDIMM 2Rx8 CL52 | PASS on spec — no SPD sentence published | Crucial UK | **£1,243.19 inc VAT** (= £1,035.99 ex; £32.37/GB ex = €38.75/GB) | In stock | https://uk.crucial.com/memory/server-ddr5/mtc20f2085s1rc64br |
| Micron MTC10F1084S1RC64BR 16 GB DDR5-6400 RDIMM 1Rx8 CL52 | PASS on spec — no SPD sentence published | Crucial UK | **£811.19 inc VAT** (= £675.99 ex; £42.25/GB ex = €50.56/GB) | In stock | https://uk.crucial.com/memory/server-ddr5/mtc10f1084s1rc64br |

### SCAN UK (scan.co.uk — mainstream; display prices **inc VAT**, page has an "Inc VAT" toggle)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Silicon Power SP064GBRVE640J02 64 GB PC5-51200 (6400) ECC RDIMM CL52 2Rx8 1.1 V | PASS on spec — no SPD sentence published; listing spec "PC5-51200 (6400), ECC RDIMM, CAS 52, 2Rx8, 1.1 V" | SCAN | **£2,399.99 inc VAT** (= £1,999.99 ex; £31.25/GB ex = **€37.40/GB** — dead level with baseline) | In stock, "Get it Tomorrow, 15 Nov" | https://www.scan.co.uk/products/64gb-1-x-64gb-silicon-power-ddr5-server-memory-pc5-51200-6400-ecc-rdimm-cas-52-2rx8-11v |
| SK hynix HMCG94AHBRA487N 64 GB 6400 ECC RDIMM CL52 2Rx4 1.1 V | PASS on spec — no SPD sentence published | SCAN | **£2,999.99 inc VAT** (= £2,499.99 ex; £39.06/GB ex = €46.75/GB) | In stock, next-day | https://www.scan.co.uk/products/64gb-1-x-64gb-sk-hynix-ddr5-server-memory-pc5-51200-6400-ecc-rdimm-cas-52-2rx4-11v |
| Samsung M321R8GA0EB2-CCP 64 GB PC5-51200 (6400) ECC Registered CL52 2Rx4 1.1 V | PASS on spec — no SPD sentence published (same part as the Tonitrus competitor) | SCAN | **£3,599.99 inc VAT** (= £2,999.99 ex; £46.87/GB ex = €56.10/GB) | In stock, next-day | https://www.scan.co.uk/products/64gb-1x64gb-samsung-m321r8ga0eb2-ccp-ddr5-server-ram-pc5-51200-6400-ecc-registered-cas-52-dual-rank |
| Micron MTC10F1084S1RC64BR 16 GB 6400 ECC RDIMM CL52 1Rx8 1.1 V | PASS on spec — no SPD sentence published | SCAN | **£899.99 inc VAT** (= £749.99 ex; £46.87/GB ex = €56.10/GB) | In stock, next-day | https://www.scan.co.uk/products/16gb-1-x-16gb-micron-ddr5-server-memory-pc5-51200-6400-ecc-rdimm-cas-52-1rx8-11v |
| Samsung 16 GB 6400 ECC DDR5 server RAM (LN168123) | PASS on spec — no SPD sentence published | SCAN | **£1,019.99 inc VAT** (£63.75/GB) | **Out of stock** ("Notify me when available") | https://www.scan.co.uk/products/16gb-samsung-6400-mhz-ecc-ddr5-server-ram |
| Samsung 32 GB M327R4GA3EB0-CLVXB 8800 / Micron 64 GB 8800 (PC5-70400) | **REJECT** — MRDIMM 8800 CL36, not a 6400 RDIMM | SCAN | £1,019.99 / £3,599.99 inc VAT | in stock | https://www.scan.co.uk/shop/computer-hardware/memory-ram/ddr5-server-ram-memory-kits-6400mhz |

### EuroPC (europc.co.uk — used/refurb server parts, 1-yr EuroPC warranty, UK VAT invoices; listing prices marked **ex VAT**)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| SK hynix HMCG88AHBRA478N 32 GB DDR5-6400MT/s ECC RDIMM (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£999.99 ex VAT** (£31.25/GB = **€37.40/GB**) | "From" price, listed live | https://www.europc.co.uk/search?s=DDR5-6400 |
| Micron MTC40F2046S1RC64BH1 64 GB DDR5-6400 ECC RDIMM (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£2,299.99 ex VAT / £2,759.99 inc VAT** (£35.94/GB ex = €43.01/GB) | In stock (JSON-LD `InStock`) | https://www.europc.co.uk/micron-64gb-ddr5-6400mt-s-ecc-rdimm-server-memory-p-n-mtc40f2046s1rc64bh1-173613.html |
| Micron MTC40F2046S1RC64BD2 64 GB DDR5-6400 ECC RDIMM (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£2,299.99 ex VAT / £2,759.99 inc VAT** (€43.01/GB ex) | In stock | https://www.europc.co.uk/micron-64gb-ddr5-6400mt-s-ecc-rdimm-server-memory-p-n-mtc40f2046s1rc64bd2-173830.html |
| SK hynix HMCG94AHBRA283N 64 GB DDR5-6400 ECC RDIMM (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£2,299.99 ex VAT** (€43.01/GB) | listed live | https://www.europc.co.uk/search?s=DDR5-6400 |
| Samsung M321R8GA0PB2-CCPEC 64 GB DDR5-6400 ECC RDIMM (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£2,299.99 ex VAT** (€43.01/GB) | listed live | https://www.europc.co.uk/search?s=DDR5-6400 |
| Micron MTC20F2085S1RC64BH1 32 GB / Samsung M321R4GA3EB2-CCPKF 32 GB 6400 (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£1,199.99 ex VAT** each (£37.50/GB = €44.88/GB) | listed live | https://www.europc.co.uk/search?s=DDR5-6400 |
| SK hynix HMCG78AHBRA478N 16 GB / Micron MTC10F1084S1RC64BH1 16 GB 6400 (refurb) | PASS on spec — no SPD sentence published | EuroPC | **£699.99 ex VAT** each (£43.75/GB = €52.36/GB) | listed live | https://www.europc.co.uk/search?s=DDR5-6400 |

### ServerO (servero.co.uk — niche UK server-parts dealer; prices marked **ex. VAT**)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Supermicro MEM-DR564MC-ER64 64 GB 2Rx4 DDR5-6400 ECC RDIMM (new) | PASS on spec — no SPD sentence published (Supermicro "64GB DDR5-6400 2Rx4 (16Gb) LP, ECC RDIMM"; no SPD sheet surfaced) | ServerO | **£2,395.00 ex VAT** (£37.42/GB = €44.79/GB) | In stock (JSON-LD `InStock`); "brand may vary", stock moves fast | https://servero.co.uk/supermicro-mem-dr564mc-er64-64gb-2rx4-ddr5-6400mhz-ecc-rdimm-new |
| Micron MTC20F2085S1RC64BR 32 GB 2Rx8 DDR5-6400 ECC RDIMM (new) | PASS on spec — no SPD sentence published | ServerO | **£1,250.00 ex VAT** (£39.06/GB = €46.75/GB) | In stock | https://servero.co.uk/micron-mtc20f2085s1rc64br-32gb-2rx8-6400mhz-rdimm-ddr5-new |
| Micron MTC20F2085S1RC64BD2 32 GB 2Rx8 DDR5-6400 ECC RDIMM (new) | PASS on spec — no SPD sentence published | ServerO | **£1,501.25 ex VAT** (£46.91/GB) | **Out of stock** | https://servero.co.uk/components/memory/ddr5-ecc-server/micron-mtc20f2085s1rc64bd2-32gb-2rx8-ddr5-6400mhz-ecc-rdimm-new |

### KahnServers (kahnservers.co.uk — used/refurb server parts, UK VAT invoices; display **inc VAT**)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| SK hynix HMCG94AHBRA277N 64 GB 2Rx4 PC5-51200B-R DDR5-6400 RDIMM (refurb) | PASS on spec — no SPD sentence published | KahnServers | **£2,569.98 inc VAT** (= £2,141.65 ex; £33.46/GB ex = €40.05/GB) | In stock | https://kahnservers.co.uk/collections/server-rdimm-memory |
| Samsung UCS-MRX32G2RE5 32 GB 2Rx8 PC5-51200B-R DDR5-6400 RDIMM (refurb) | PASS on spec — no SPD sentence published | KahnServers | **£1,572.79 inc VAT** (= £1,310.66 ex; £40.96/GB ex = €49.02/GB) | In stock | https://kahnservers.co.uk/collections/server-rdimm-memory |

### MemoryCow (memorycow.co.uk — UK server-RAM reseller, lifetime warranty; **inc/ex VAT both shown**)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Micron MTC40F2046S1RC64BR 64 GB DDR5-6400 ECC RDIMM | PASS on spec — no SPD sentence published | MemoryCow | **£3,418.48 inc / £2,848.73 ex VAT** (£44.51/GB ex = €53.27/GB) | live listing (order-to-stock, ships from UK) | https://www.memorycow.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm |
| Micron MTC20F2085S1RC64BR 32 GB DDR5-6400 ECC RDIMM | PASS on spec — no SPD sentence published | MemoryCow | **£2,053.16 inc / £1,710.97 ex VAT** (£53.47/GB ex) | live listing | https://www.memorycow.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm |
| Kingston KSM64R52BD4-64MH 64 GB DDR5-6400 ECC RDIMM | **PASS** — "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | MemoryCow | **£3,861.99 inc / £3,218.33 ex VAT** (£50.29/GB ex = €60.18/GB) | live listing | https://www.memorycow.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm |
| Kingston KTL-TS564D4-64G 64 GB DDR5-6400 (Lenovo OEM code) | no SPD sentence published (OEM-coded; kingston.com datasheet PDF 404) | MemoryCow | **£3,906.15 inc / £3,255.13 ex VAT** (£50.86/GB ex) | live listing | https://www.memorycow.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm |

### Kingston Memory Shop (kingstonmemoryshop.co.uk — Kingston's UK webstore, VAT reg 944 2818 09; inc/ex both shown)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| KSM64R52BD4-64MH 64 GB 2Rx4 DDR5-6400 ECC RDIMM (Micron H-Die) | **PASS** — "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | Kingston Memory Shop | **£3,861.99 inc / £3,218.33 ex VAT** (£50.29/GB ex = €60.18/GB) | "Available To Order – 4-5 business day delivery" | https://www.kingstonmemoryshop.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm/64gb-kingston-ksm64r52bd4-64mh-ddr5-6400mt-s-ecc-registered-memory-dimm |
| KSM64R52BD8-32MH 32 GB DDR5-6400 ECC RDIMM | **PASS** — "The SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | Kingston Memory Shop | **£1,882.18 inc / £1,568.48 ex VAT** (£49.01/GB ex = €58.66/GB) | Available To Order – 4-5 BD | https://www.kingstonmemoryshop.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm/32gb-kingston-ksm64r52bd8-32mh-ddr5-6400mt-s-ecc-registered-memory-dimm |
| KSM64R52BS8-16MH 16 GB DDR5-6400 ECC RDIMM | **PASS** — "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | Kingston Memory Shop | **£961.37 inc / £801.14 ex VAT** (£50.07/GB ex = €59.93/GB) | Available To Order – 4-5 BD | https://www.kingstonmemoryshop.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm/16gb-kingston-ksm64r52bs8-16mh-ddr5-6400mt-s-ecc-registered-memory-dimm |
| OEM-coded 64 GB 6400 RDIMMs: KTD-PE564D4-64G (Dell), KTH-PL564D4-64G (HPE), KTL-TS564D4-64G (Lenovo), KCS-UC564D4-64G (Cisco) | no SPD sentence published (kingston.com datasheet PDFs 404 for the OEM codes) | Kingston Memory Shop | **£3,906.15 inc / £3,255.13 ex VAT** each (£50.86/GB ex = €60.87/GB) | live listings | https://www.kingstonmemoryshop.co.uk/memory-ram/server-ram-memory/ddr5-ecc-rdimm?page=2 |

### Hard Disk Direct (harddiskdirect.co.uk — UK server-parts dealer; **no VAT wording on the page — basis unconfirmed**)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Micron MTC40F2046S1RC64BD2R 64 GB DDR5-6400/PC5-51200 ECC Registered CL52 1.1 V 2Rx4 RDIMM (new) | PASS on spec — no SPD sentence published | Hard Disk Direct | **£2,815.97 GBP** (as priced on page; VAT basis not stated → £44.00/GB) | In stock (qty 200), NewCondition | https://harddiskdirect.co.uk/mtc40f2046s1rc64bd2r-1706359.html |
| Dell N66RP 64 GB DDR5-6400 ECC RDIMM CL52 (title says 1.2 V — Dell marketing; DDR5 RDIMM core is 1.1 V) | no SPD sentence published (Dell OEM code) | Hard Disk Direct | **£3,060.75 GBP** (£47.82/GB) | In stock, NewCondition | https://harddiskdirect.co.uk/n66rp-1713176.html |
| Micron MTC10F1084S1RC64BH1 16 GB DDR5-6400 1Rx8 CL52 1.1 V RDIMM (refurb) | PASS on spec — no SPD sentence published | Hard Disk Direct | **£886.87 GBP** (£55.43/GB) | In stock, **RefurbishedCondition** | https://harddiskdirect.co.uk/mtc10f1084s1rc64bh1-1719636.html |

### ETB Technologies (etb-tech.com — refurb Dell/HPE parts, 3-yr ETB warranty; **currency is geo-detected: our fetch was served US$**, the £/€ switch is a JS POST we could not drive)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| SK hynix HMCG94AHBRA480N 64 GB PC5-6400B-R 2Rx4 EC8 RDIMM (ETB refurbished) | PASS on spec — no SPD sentence published | ETB Technologies | **US$3,572.74 as displayed** (= US$55.8/GB; GBP figure not retrievable from this host) | In stock, 4+ units, "ships Monday", same-day pre-2 PM | https://www.etb-tech.com/hynix-64gb-pc5-6400b-r-2rx4-ec8-hmcg94ahbra480n-mem0607.html |
| Micron MTC20F2085S1RC64BH1 32 GB PC5-6400B-R EC8 RDIMM (ETB refurbished) | PASS on spec — no SPD sentence published | ETB Technologies | **US$1,984.86 as displayed** (= US$62.0/GB) | In stock | https://www.etb-tech.com/micron-32gb-pc5-6400b-r-2rx8-ecc-mtc20f2085s1rc64bh1-mem0420.html |

### ServerBasket (serverbasket.co.uk — UK refurb/OEM parts, 1-yr warranty)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| "PC5-4800 to PC5-6400 64 GB DDR5 Server Memory" (HPE/Dell/Cisco OEM, 2Rx4/4Rx4, RDIMM/3DS) | PASS on spec for the 6400 configuration — no SPD sentence published | ServerBasket | **£879.00 (was £975.00) GBP** — but this is the **from-price across the 4800–6400 config range**, so no 6400 price is pinned (16 GB DDR5 siblings on the same page sit at £219.00) | In stock, express UK shipping | https://www.serverbasket.co.uk/p/64gb-ddr5-server-memory/ |

### Shops checked with no qualifying hit (not blocked — checked and empty)

| Shop | Result |
|---|---|
| ebuyer | Search "DDR5-6400 RDIMM" → 35 loose matches, **no DDR5-6400 RDIMM in catalogue** (only DDR4 RDIMM, e.g. Origin 32 GB DDR4-2666 £280.00, and desktop DDR5). https://www.ebuyer.com/search?q=DDR5-6400+RDIMM |
| Senetic UK | `search/?query=DDR5-6400 RDIMM` and `DDR5 6400` → **"No product has been found"**. https://www.senetic.co.uk/search/?query=DDR5%206400 |
| Offtek | HPE DDR5 category is 4800-dominated (50× DDR5-4800, 1× 5600, **no 6400**); their search is machine-model based, so no generic 6400 RDIMM row. https://www.offtek.co.uk/hpe/ram-memory/ddr5 |
| SVP Communications (svp.co.uk) | Live site ("Svp – Tech & Media Supplies", 0125-972-5200) but a catalogue/template shell — **no DDR5/RDIMM products listed**; svp.co.uk also times out to direct curl. https://www.svp.co.uk/ |
| Komputerbay | Site up, **no DDR5-6400 RDIMM** product found via site search or index (consumer/DIY range). https://www.komputerbay.com/ |
| Servnet UK | Reachable, DDR5 RDIMM guide + insight pages only, **no 6400 RDIMM SKU priced**. https://www.servnetuk.com/computing-components/memory-ram |

## Blocked / unreachable (this UK + niche/refurb pass)

- **Mr Memory** (mrmemory.co.uk — note: `mr-memory.co.uk` has **no DNS record**; the live domain is `mrmemory.co.uk`): Cloudflare bot-wall — direct curl **403 "Just a moment…"**, r.jina.ai shows the same challenge, webfetch 403. Page is indexed and does exist for exactly our part (Samsung 64 GB DDR5-6400 MHz RDIMM ECC Registered); the **£4,320.00 inc-VAT figure carried in the earlier draft is NOT re-verified this pass** — treat it as an unverified search-snippet price. https://www.mrmemory.co.uk/memory-ram-products/samsung-64gb-ddr5-6400mhz-rdimm-ecc-registered
- **CCL Computers** (cclcomputers.co.uk): **HTTP 522** twice via curl + r.jina.ai `page.goto` 15 s timeout → origin down/unreachable.
- **Bargain Hardware** (bargainhardware.co.uk): curl **403**, jina → Cloudflare "Performing security verification" → blocked; no refurb DDR5-6400 RDIMM price captured.
- **ETB Technologies**: reachable only via r.jina.ai; the **display currency is geo-detected and served US$** to us, so the GBP ticket price is not readable from this host (direct curl 403).
- **Domains that no longer resolve (NXDOMAIN via DoH 1.1.1.1, so not a network glitch):** `ramexpert.co.uk`, `po-memory.com`, `datamem.co.uk` (Datamation), `mem-tek.fr`, `serverhome.co.uk`, `mr-memory.co.uk`. (Their `.com` variants `ramexpert.com`, `datamem.com`, `serverhome.com` resolve but are US/other businesses, not the UK shop named in the brief.)
- **eBay UK** via r.jina.ai: search URL redirected to `/n/error` (404) → no listing sweep; eBay on this host is blocked as before.
- **MemoryCow category page** is Cloudflare-403 to r.jina.ai but **200 to curl** — the product-level data above is from curl; the 32 GB Micron MTC20F2085S1RC64BD2R page reports **OutOfStock**.
- **DDG lite** is anomaly-challenged (HTTP 202 empty page) for direct curl from this host; all searches in this pass went through `r.jina.ai` or the webfetch tool.

## Verdict — does anything in the UK/niche slice beat €37.43/GB net?

**Yes, but only on a strict ex-VAT basis and only one clear winner:** **Crucial UK's Micron
MTC40F2046S1RC64BR 64 GB DDR5-6400 RDIMM at £2,161.19 inc VAT = £1,800.99 ex VAT = €33.68/GB**,
which is **€3.75/GB ≈ 10 % under** the €37.43/GB net baseline (and the cheapest qualifying 6400
SPD module in this whole UK pass). Two offers sit at dead parity — **SCAN's Silicon Power
SP064GBRVE640J02 64 GB (€37.40/GB ex VAT)** and **EuroPC's refurb SK hynix HMCG88AHBRA478N 32 GB
(€37.40/GB ex VAT)** — so neither is a real win. Everything else in the slice is 40–60 €/GB
(Kingston's own UK shop is the most expensive at €60/GB). The UK numbers only survive as a
saving if bought **B2B with no UK VAT and shipped**; once EU import VAT (23 % PL / 19 % DE) +
customs handling land, the Crucial advantage shrinks to roughly break-even against the Proshop.pl
4×32 GB kit, and the Proshop.pl kit (256 GB, single delivery, EU invoice, 2-year-plus warranty,
in-EU RMA) stays the practical recommendation. The 64 GB Crucial modules are also 2Rx4
high-density, which is the safer Turin 12-channel population than 1Rx8 (the 16 GB MTC10F…1Rx8 is
€50.56/GB — not competitive).

### Slice notes (UK + niche/refurb)

- Every UK 6400 part found is a **JEDEC-only server RDIMM with no XMP/EXPO profile**, so the
  H14SSL-NT JEDEC-only constraint is satisfied by all of them; the Kingston ones are additionally
  confirmed by the datasheet SPD sentence quoted above.
- Kingston's UK webstore (Kingston Memory Shop) and its reseller clone MemoryCow price the same
  Server Premier parts at ~£50/GB ex VAT — i.e. **the "obscure" Kingston channel is the *dearest*,
  not the cheapest**; the value in the UK is Micron's own storefront (Crucial UK) and the
  refurb dealers (EuroPC, KahnServers).
- No UK shop in this pass offered a 4- or 8-piece **kit** of 6400 RDIMMs — all listings are single
  modules, so a 12-DIMM H14SSL-NT build means 12 separate modules and per-module packaging cost.
- Refurb is only offered with short warranties: EuroPC 1 yr, ETB 3 yr (ETB warranty is unusually
  good for refurb), KahnServers unquantified on the collection page, ServerBasket 1 yr. For a
  256 GB 12-channel build that risk, not price, is the reason to prefer the Proshop.pl kit.

---

## Slice: DE/AT/FR/IT/ES — Pass 3 (2026-11-14)

> Note on file history: the DE-slice Pass 2 rows I wrote yesterday were **overwritten** by a later
> editor (the file was rewritten keeping only Pass 1 + the UK slice). They are **restored below** with
> prices re-read today, 2026-11-14. Nothing else in this file was touched.

### Qualifying JEDEC-6400 ECC RDIMMs found in the DE/AT slice (live re-read 2026-11-14)

| Part | JEDEC SPD verdict | Shop | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Kingston Server Premier DDR5-6400 CL52 **ECC Reg** retail, 1×32 GB | **QUALIFIES** — Server Premier 6400 CL52 family; Kingston datasheet sentence: "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | Galaxus.de | **EUR 1 449,92** gross (= EUR 45,31/1GB; page shows per-GB) — 1 445,54 on 13.11. | product page = CAPTCHA, stock unverifiable | https://www.galaxus.de/de/s1/product/kingston-ddr5-32gb-pc-6400-cl52-server-premier-ecc-reg-retail-1-x-32gb-6400-mhz-ddr5-ram-dimm-ram-69848466 |
| Kingston Server Premier DDR5-6400 CL52 ECC Reg retail, 1×16 GB | **QUALIFIES** | Galaxus.de | **EUR 778,64** gross (= EUR 48,67/1GB) | stock unverifiable | https://www.galaxus.de/de/s1/product/kingston-ddr5-16gb-pc-6400-cl52-server-premier-ecc-reg-retail-1-x-16gb-6400-mhz-ddr5-ram-dimm-ram-69848467 |
| Kingston Server Premier DDR5-6400 CL52 ECC Reg retail, 1×64 GB | **QUALIFIES** | Galaxus.de | **EUR 3 262,26** gross (= EUR 50,97/1GB) | stock unverifiable | https://www.galaxus.de/de/s1/product/kingston-ddr5-64gb-pc-6400-cl52-server-premier-ecc-reg-retail-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-69848470 |
| Kingston Server Premier DDR5-6400 CL52 ECC Reg retail, 1×16 / 1×32 / 1×64 GB | **QUALIFIES** | Galaxus.at | **EUR 793,44 / 1 585,33 / 3 129,–** gross (EUR 49,60 / 49,54 / 48,89 per GB) | stock unverifiable | https://www.galaxus.at/de/s1/product/kingston-ddr5-64gb-pc-6400-cl52-server-premier-ecc-reg-retail-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-69848470 |
| V-Color RDIMM JEDEC DDR5-6400 CL52, 128 GB (4×32) Quad Kit | **QUALIFIES** — "JEDEC standard at 1.1 V, ECC" | Caseking.de | **€5 392,42** gross (= €42,13/GB) | **OutOfStock** | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |
| V-Color RDIMM JEDEC DDR5-6400 CL52, 64 GB (4×16) / 128 GB (8×16) / 256 GB (8×32) | **QUALIFIES** | Caseking.de | **€3 386,92 / €6 775,97 / €12 784,85** gross (€52,92 / €52,94 / €49,94 per GB) | all **OutOfStock** | https://www.caseking.de/en/pc-components/memory/ddr5/6400-mhz-ddr5-ram |

### Rejected in this slice (6400 only via EXPO/XMP, i.e. not JEDEC 1.1 V SPD)

| Part | Shop | Price | Stock | Why rejected | URL |
|---|---|---|---|---|---|
| G.Skill Zeta R5 `F5-6400R3239G16GQ4-G5`, 64 GB (4×16) Registered ECC | Alternate.de | **€2 219,00** (= **€34,67/GB**) | **OutOfStock** (JSON-LD `"availability":"OutOfStock"`) | Alternate lists "Profil: INTEL XMP (Version 3.0)", CL32 → 6400 needs the XMP profile | https://www.alternate.de/G-Skill/RIMM-64-GB-DDR5-6400-4x-16-GB-Quad-Kit-ECC-Arbeitsspeicher/html/product/100130572 |
| G.Skill Zeta R5 `F5-6400R3239G32GQ4-G5`, 128 GB (4×32) ECC Reg | Alternate.de | **€6 025,00** (€47,07/GB) | listed | INTEL XMP 3.0, CL32 39-39 | https://www.alternate.de/G-Skill/RIMM-128-GB-DDR5-6400-4x-32-GB-Quad-Kit-ECC-Arbeitsspeicher/html/product/100130574 |
| G.Skill T5 NEO `F5-6400R3239F32GQ4-T5N`, 128 GB (4×32) ECC Reg | Alternate.de | **€6 882,00** (€53,77/GB) | listed | AMD EXPO, CL32 39-39-102 | https://www.alternate.de/G-Skill/RIMM-128-GB-DDR5-6400-4x-32-GB-Quad-Kit-ECC-Arbeitsspeicher/html/product/100142743 |
| G.Skill Zeta R5 `F5-6400R3239G32GE8-G5`, 256 GB (8×32) ECC Reg | Alternate.de | **€12 075,00** (€47,17/GB) | listed | INTEL XMP 3.0 | https://www.alternate.de/G-Skill/RIMM-256-GB-DDR5-6400-8x-32-GB-Octo-Kit-ECC-Arbeitsspeicher/html/product/100130575 |
| G.Skill Zeta R5 DDR5-6400 CL32 XMP ECC reg., 128 GB (8×16) Octo-Kit | Caseking.de | **€1 580,08** (MEGS-318) | OutOfStock | CL32 @ 1.4 V XMP, not JEDEC-1.1 V | https://www.caseking.de/en/g.skill-zeta-r5-ddr5-6400-ram-cl32-xmp-ecc-reg.-128-gb-octo-kit-black/MEGS-318.html |
| Kingston CUDIMM 64 GB DDR5-6400 | Alternate.de | **€1 555,00** | listed | **CUDIMM** — wrong form factor per task rules | https://www.alternate.de/html/search.html?query=KSM64R52BD4-64 |

**Alternate.de note:** its whole DDR5-6400 Registered-ECC range is G.Skill RIMM (Zeta R5 / T5 NEO) with
XMP/EXPO profiles only — it carries **no Kingston Server Premier / Samsung 6400 CL52 JEDEC RDIMM**.
The only sub-€37,43/GB figure in the entire slice (Zeta R5 4×16 at €34,67/GB) is both rejected *and*
out of stock. Alternate search that works anonymously: `https://www.alternate.de/html/search.html?query=<q>`
(the `/search?query=` path 404s).

### Verified absent (checked-and-empty, not blocked)

| Shop | Query | Result |
|---|---|---|
| senetic.de | `search?query=DDR5 RDIMM 64GB 6400` | "Nichts gefunden" |
| senetic.fr | `search?query=DDR5 6400 RDIMM` | "Rien trouvé" |
| Plexcom (plexcom.de) | `advanced_search_result.php?keywords=DDR5 6400 RDIMM` / `KSM64R52BD4` / `M321R` | "Die Suche ergab keine genauen Treffer". NB **plexcom.com is a parked domain for sale (USD 14 888)**, not the shop |
| memorysolution.de | `search?search=DDR5 6400 RDIMM` | "»DDR5 6400 RDIMM« wurde kein Produkt gefunden" — house sells DDR5 **SDRAM components**, not retail RDIMMs |
| servershop24.de | `?s=DDR5 6400 RDIMM` | only complete servers with DDR5; no bare 6400 RDIMM SKU |
| Happyware (happyware.com/de) | `search?sSearch=DDR5 6400 RDIMM` | page loads, **no 6400 RDIMM product row**; B2B-only ("Wir verkaufen nur an Unternehmen i.S.d. § 14 BGB"), prices ex works + VAT |

### Blocked / unreachable this pass (DE/AT/FR/IT/ES)

- **Mindfactory** — search redirects to `/` with "SECURITY CHECK" (Cloudflare) → blocked.
- **Cyberport** — Cloudflare "Just a moment…" → blocked.
- **Computeruniverse** — Cloudflare "Performing security verification" → blocked.
- **Kaufland.de** — "Verifizierung erforderlich" → blocked.
- **Otto.de** — `/suche/<q>/` returns **HTTP 400** for this query form → no result served.
- **notebooksbilliger.de** — both `/search?query=` and the category path → **404 "uups..."**.
- **digitec.ch** — search page renders, **no product rows in the fetched HTML** (JS catalogue) → no price.
- **Interdiscount.ch** — 403 → blocked (CH VAT would apply anyway).
- **Galaxus.de/.at product pages** — redirect to `/captcha` ("Are you a robot?"); only search/listing pages readable → per-SKU stock unverifiable.
- **Proshop.de** — search page loads but **ignores the query** anonymously (returns a generic bestseller list), so no DE search results; Proshop.pl product pages remain readable.
- **Fujitsu TS parts channel** — `ts.fujitsu.com/ts/searchresults.aspx` now redirects to `global.fujitsu/en-global` (parts-shop search dead end) → unreachable.
- **Thomas-Krenn** — every shop path tried 404s (`/de/suche`, `/de/arbeitsspeicher`, `/de/shop/`, `…-c1020.html`); only `/de/wiki/*` resolves → no shop result retrievable.
- **ITSCO (itsco.de)** — `/suche?…` → **HTTP 500**.
- **Dell Outlet / HP parts store EU / PC-Specialist parts** — no qualifying 6400 ECC RDIMM listing retrievable anonymously.
- **server-warehouse.de, raidlinks.de** — DNS unresolvable; **Terra PC** — SSL cert hostname mismatch.

### Pass-3 verdict (DE/AT/FR/IT/ES)

**No — nothing in this slice beats €37.43/GB net on 2026-11-14.**

- The slice's cheapest *qualifying* per-GB figure is Galaxus.de's 1×32 GB Server Premier 6400 CL52 ECC Reg at **€45,31/GB gross**; stripped of 19 % DE VAT that is **€38,08/GB net** (1 449,92 ÷ 1,19 ÷ 32) — still above €37,43.
- Galaxus.at is worse (~€49,5/GB gross). Caseking's V-Color JEDEC kits are €42,13–52,94/GB **and all out of stock**.
- Alternate.de's only sub-baseline 6400 Registered kit (€34,67/GB) is XMP-only and out of stock.
- Standing bests are unchanged: **Proshop.pl `KF576RH40RBK4-128` €4 791 net / 128 GB = €37,43/GB net**, and **ibfusion `KSM64R52BD4-64MD` €2 481 net / 64 GB = €38,77/GB net**.

### Price-spread observation (DE slice) — decision-relevant

G.Skill's **Zeta R5 / T5 NEO DDR5-6400 Registered ECC** kits are the cheap end of the German market:
Caseking priced the Zeta R5 **64 GB (4×16) at €723,43 (€11,30/GB)** and the **128 GB (8×16) Octo-Kit at
€1 580,08 (€12,34/GB)**, both CL32 / 1,4 V / **XMP-or-EXPO only** and both **OutOfStock**. The same
Zeta R5 4×16 kit at Alternate.de is listed at **€2 219,00 (€34,67/GB)** — a **3× shop-to-shop spread**
on an identical part number, and neither shop has it in stock.

Read literally: in the DE slice the JEDEC-only constraint is worth roughly **3–4×** per GB — the cheap
6400 Registered ECC DDR5 (G.Skill, XMP) sits at **€11–12/GB**, while every module whose SPD actually
programs 6400 CL52 at 1,1 V (Kingston Server Premier, V-Color JEDEC) sits at **€42–53/GB gross**.
The Proshop.pl FURY Renegade PRO 4×32 kit at **€37,43/GB net** is therefore already near the floor for
*JEDEC-6400* silicon in this slice, which is why nothing beat it.
