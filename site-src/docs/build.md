# The build — three priced options

One platform, three RAM tiers. Everything below is the same machine except the
memory, because **memory is 72–85 % of the bill** and it is the only part where
the cost/benefit answer is genuinely open. Prices are live Geizhals/retail reads
from **2026-11-17**, EUR incl. VAT, and exclude the four GPUs you already own.

| | Part | Price | Why this one |
|---|---|---:|---|
| Board | **GIGABYTE MZ33-CP1 Rev. 3.x** | **€896.97** | In stock. 3× Gen5 x16 at 2-slot pitch, 12 DIMM, 4× Gen5 MCIO, AST2600 IPMI, E-ATX 304.8×330.2 |
| CPU | **AMD EPYC 9355** (tray) | **€2,329.00** | 32C / **8 CCD**, 256 MB L3, 3.55 GHz, 280 W, 12-channel DDR5-6400 |
| GPU | 4× PowerColor R9700 32G-B | owned | 32 GB, 40 mm 2-slot blower, 12V-2x6 |
| GPU 4 | C-Payne MCIO→PCIe 5.0 x16 + 2× MCIO 8i cable | €140.00 | The fourth card on the documented MCIO path |
| SSD | 2× Samsung 9100 PRO **2 TB** | €800.00 | €399.99 each; the board's Gen5 M.2 slots |
| PSU | **be quiet! Dark Power Pro 13 1600 W** ATX 3.1 | €349.88 | 1,306 W capped / 1,666 W stock — see [power](#power) |
| Cooling | Noctua NH-U14S TR5-SP6 | €126.01 | 280 W part, 4U-class air; no AIO plumbing |
| Case | Fractal Meshify 2 XL | €218.08 | E-ATX, 9+3 slots, 250 mm PSU, 480 mm top |
| Fans | 3× 140 mm | €45.00 | Bottom/rear for the M.2 and GPU zone |
| | **Platform, excl. RAM** | **€4,904.92** | |

## Why the CP1 and not the SU0

The **MZ23-SU0** was the board in the previous revision of this page. It is
**not buyable in the EU**: Galaxus shows *"Verfügbarkeit unbekannt — Aktuell
nicht lieferbar"*, Geizhals has **zero listings** for it, and the only offer
anywhere is a used one at €1,290 (idealo). Newegg's $869 does not ship to the EU.

The **MZ33-CP1** is in stock at **€896.97** — cheaper than the used SU0 — and it
differs in two ways that both help:

| | MZ23-SU0 | **MZ33-CP1** |
|---|---|---|
| EU availability | **not buyable new** | **€896.97, in stock** |
| x16 slots | 5, all at **1.0 pitch** | 4: **three at 2.0 pitch** + 1 Gen4 |
| Four 2-slot cards | **four risers** | **three native + one MCIO adapter** |
| Form factor | CEB 304.8 × 266.7 | E-ATX 304.8 × 330.2 |
| M.2 | 2× at **Gen3 x2** | 1× Gen3 (not used for the array) |
| Storage | 2 onboard slots only | **4× Gen5 NVMe via 2× MCIO 8i** |

The CP1 gives **native 2-slot spacing for three cards and a documented MCIO path
for the fourth**, so no risers. Its Gen5 MCIO storage is also the reason the
array is 2× 2 TB at full speed rather than two throttled Gen3 slots.

## The three options

All three share the €4,904.92 platform. They differ only in memory: how much,
and how many channels are populated.

| | **A — Balanced** | **B — Capacity** | **C — Channels-first** |
|---|---|---|---|
| Memory | **12× 32 GB** = 384 GB | **12× 64 GB** = 768 GB | **6× 64 GB** = 384 GB |
| Channels | **12** | **12** | 6 |
| Bandwidth | **614 GB/s** | **614 GB/s** | 307 GB/s |
| RAM cost | €12,605.04 | €28,194.61 | €14,097.31 |
| €/GB | €32.83 | €36.71 | €36.71 |
| **Platform total** | **€17,509.96** | **€33,099.53** | €19,002.23 |
| **+3 % contingency** | **€18,035.26** | **€34,092.52** | €19,572.30 |
| Parts | 12× KSM64R52BD8-32MD | 12× KSM64R52BD4-64MD | 6× KSM64R52BD4-64MD |
| QVL | ✓ pass | ✓ pass | ✓ (6 of 12 slots) |

### A — Balanced, 384 GB on 12 channels · **€18,035**

Twelve 32 GB 2Rx8 modules fill all twelve channels at **€32.83/GB** — the
cheapest qualified 6400 part in the EU, and the cheapest route to full
614 GB/s. Capacity is 384 GB.

- **Buy if:** you want the bandwidth without paying the 64 GB premium. This is
  the middle of the cost/benefit triangle and the recommendation.
- **The trade:** 384 GB, so a spilling model below ~250 GB fits comfortably;
  a 508 GB UD-Q8 set does not.
- **Risk:** single merchant (barax, 1–3 days). The `-32MH` twin has 26 merchants
  at €35.96/GB (+€1,195) if supply certainty matters more than price.

### B — Capacity, 768 GB on 12 channels · **€34,093**

Twelve 64 GB 2Rx4 modules — 2× the capacity at **+11.8 % per GB**. Same 614 GB/s.

- **Buy if:** you intend to spill large models (DeepSeek 2.25 at ~155 GB, or a
  508 GB set that needs ~172 GB of CPU lane inside 768 GB).
- **The trade:** **+€16,057.26 over A** for 384 GB more. That delta is 1.7× the
  entire rest of the platform.
- **Risk:** the Allegro promo price; Vistula-crossed supply. Same QVL pass.

### C — Channels-first, 384 GB on 6 channels · €19,572

Six 64 GB modules, half the sockets filled, 307 GB/s.

- **Buy if:** you want 64 GB modules (so the 8×/12× upgrade is 6 more, not 12
  more) and 384 GB is enough today.
- **The trade:** **half the bandwidth** for the same capacity as A and
  **+€1,537 over A**. On a spilling MoE that ratio is the decode ratio.
- **Verdict: not recommended.** It is listed because "populate half now" is the
  obvious-seeming upgrade path, and it costs more for less. If you want a path
  to 768 GB, A's 12×32 → 12×64 replacement is a full swap either way.

## Recommendation

**A.** It is the cheapest route to the platform's real capability — 12 channels
of 6400 — and 384 GB clears every model that fits the cards' 128 GB VRAM with a
CPU lane. Move to **B** only when a specific model you intend to run needs more
than ~250 GB of host RAM; the €16k step should be justified by a model, not by
headroom.

## Power

| | Capped (210 W/card) | Stock (300 W/card) |
|---|---:|---:|
| 4× R9700 | 840 W | 1,200 W |
| EPYC 9355 (280 W) | 280 W | 280 W |
| 12× DDR5 RDIMM | 96 W | 96 W |
| Board, BMC, NIC, VRM loss | 40 W | 40 W |
| 2× M.2, fans | 50 W | 50 W |
| **Total** | **≈1,306 W** | **≈1,666 W** |
| **PSU** | **1,600 W** ✓ | **2,000 W** |

The 1600 W unit is comfortable at the 210 W cap (19 % headroom) and **under
water at stock** (1,666 W > 1,600 W). Stock clocks need the **2,000 W** unit:
Thermaltake ToughPower i 2000 W ATX 3.1 at **€520.89** (+€171.01).

The 210 W cap is what the engine's reference build uses (211 W/card). On a layer
split it is not a performance compromise — the cards are not the decode
bottleneck.

### Connectors — the real limit, not watts

| Need | Qty | Notes |
|---|---:|---|
| 12V-2x6 for the GPUs | **4** | one per card; no riser carries 12 V |
| 8-pin ATX 12V for the CPU | **2** | board `P12V_AUX1/2` |
| 6-pin ATX 12V (board aux) | **1** | mandatory on the CP1 |
| 24-pin ATX | 1 | |

The **Dark Power Pro 13** has 2× native 12V-2x6 and 6× PCIe 6+2, which covers
four cards via 2 native + 2 adapters and still leaves cables for the board aux.
The 1600 W Seasonic TX-1600 at €449.90 is the alternative if you prefer Seasonic;
the 2,000 W ToughPower covers the stock-power configuration.

## Slots and the fourth card

The CP1's four x16 slots are **three at 2.0 pitch** (3 × 40.6 mm centres) plus a
fourth. Three 40 mm cards sit natively in those three; the fourth goes on the
**C-Payne MCIO→x16 adapter** (€50) with **two MCIO 8i cables** (€45 each),
consuming the G0 group. That is the documented path, not a riser gamble.

Remaining MCIO after that: **G2 (2× MCIO 8i = 4 Gen5 NVMe)**, which is exactly
the storage plan, and G3 (Gen4).

## Storage

Two **Samsung 9100 PRO 2 TB** on one MCIO 8i port via the KALEA adapter
(§ parts below), giving **4 TB of Gen5 NVMe** at ~14 GB/s each. The array is
RAID 0 — a working set, not a backup, so keep the model archive on separate
media.

Gen4 cards are ~€30 cheaper per drive and warm the MCIO zone less; the Gen5
drives are the better €/GB at this tier (€200/TB) and the board's MCIO ports are
Gen5. Not a close call.

## What is not in this price

- **The four GPUs.** Owned. Replacement value at €2,249 each is **€8,996**, so
  the same box bought today is **A €27,031 / B €43,089**.
- **RAM beyond the tier** and any later expansion.
- **A cold-storage SATA SSD.** The CP1 has **no native SATA** — if you want a
  cold archive in-box, that is an MCIO/USB decision, priced separately.
- **UPS, OS, and the model downloads** (~79 GB for IQ3_S).

## Before you order

!!! warning "Board availability is the fragile line"
    The CP1 is in stock at €896.97 today with multiple sellers. It is the one
    part here with a history of EU availability gaps — confirm stock at checkout
    rather than assuming the price holds.

!!! note "BIOS, not the label, decides 6400"
    The CP1's BIOS exposes `Memory Target Speed` only; a module runs at its
    **JEDEC SPD default**. A 7200-rated kit with a 6400 JEDEC default qualifies;
    a 6400-rated kit that defaults to 4800 does not. Every part priced above is
    JEDEC-6400 at 1.1 V and QVL-passing on this board.

!!! note "`P` suffix is 1P-only"
    The 9355P is the same silicon with the second socket fused off. It is
    cheaper on list but has no street stock; the plain **9355** is the buy.
