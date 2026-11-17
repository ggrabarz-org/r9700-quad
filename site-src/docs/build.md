# The build — three priced options

One platform, three memory tiers. Everything below is the same machine except
RAM, because **memory is 47–82 % of the bill** and it is the only part where the
cost/benefit answer is genuinely open. Prices are live Geizhals/retail reads from
**2026-11-17**, EUR incl. VAT, and exclude the four GPUs you already own.

| | Part | Price | Why this one |
|---|---|---:|---|
| Board | **GIGABYTE MZ33-CP1 Rev. 3.x** | **€896.97** | In stock. 3× Gen5 x16 at 2-slot pitch, 12 DIMM, 4× Gen5 MCIO + 2× MCIO (Gen4 **or SATA**), AST2600 IPMI, E-ATX |
| CPU | **AMD EPYC 9355** (tray) | **€2,329.00** | 32C / **8 CCD**, 256 MB L3, 3.55 GHz, 280 W, **12-channel** DDR5-6400 |
| GPU | 4× PowerColor R9700 32G-B | owned | 32 GB, 40 mm 2-slot blower, 12V-2x6 |
| GPU 4 | C-Payne MCIO→PCIe 5.0 x16 + 2× MCIO 8i cable | €140.00 | The fourth card on the documented MCIO path |
| Array | **4× Samsung 9100 PRO 1 TB** | **€855.60** | €213.90 each. RAID 0 = **4 TB of Gen5** on one MCIO 8i port |
| Cold | **Samsung 870 EVO 1 TB SATA** | **€103.99** | OS + model/tokenizer archive + array image |
| Cold link | MCIO 8i → 4× SATA breakout | €40.00 est. | The CP1's G3 group is **Gen4 x8 or SATA** — no native SATA ports |
| PSU | **be quiet! Dark Power Pro 13 1600 W** ATX 3.1 | €349.88 | 1,306 W capped / 1,666 W stock — see [power](#power) |
| Cooling | Noctua NH-U14S TR5-SP6 | €126.01 | 280 W part, air; no AIO plumbing |
| Case | Fractal Meshify 2 XL | €218.08 | E-ATX, 9+3 slots, 250 mm PSU, 480 mm top |
| Fans | 3× 140 mm | €45.00 | Bottom/rear for the MCIO and GPU zone |
| | **Platform, excl. RAM** | **€5,104.53** | |

## The memory question, answered straight

Your spec says **2×64 GB now, extensible to 8×** — that was a WRX90 (8-channel)
plan. **This board is 12-channel**, so the ladder is 2 / 8 / 12, and the
multiples matter differently:

| DIMMs | Capacity | Channels | Bandwidth | Note |
|---:|---:|---:|---:|---|
| **2×64** | **128 GB** | **2** | **102.4 GB/s** | Your literal start. 2 of 12 channels. |
| 8×64 | 512 GB | 8 | 409.6 GB/s | Your "8×" target |
| 12×64 | 768 GB | **12** | **614.4 GB/s** | Full platform |

**The honest warning about 2×64:** on a 12-channel socket, two DIMMs leave ten
memory controllers idle. For a **fully VRAM-resident** IQ3_S that is fine — the
CPU lane is idle and 102 GB/s is ample for PLE reads and checkpoints. For a
**spilling** MoE (DeepSeek, UD-Q8) it is a 6× bandwidth penalty against the same
board fully populated, and bandwidth *is* the decode ratio on that path. So 2×64
is the right *start* only if you accept that the expansion to 8×/12× is planned,
not optional.

## The three options

| | **A — Start (2×64)** | **B — Octa (8×64)** | **C — Full (12×64)** |
|---|---|---|---|
| Memory | **2× 64 GB** = 128 GB | **8× 64 GB** = 512 GB | **12× 64 GB** = 768 GB |
| Channels | 2 of 12 | 8 of 12 | **12 of 12** |
| Bandwidth | **102.4 GB/s** | 409.6 GB/s | **614.4 GB/s** |
| RAM cost | €4,699.10 | €18,796.41 | €28,194.61 |
| **Platform total** | **€9,803.63** | **€23,900.94** | **€33,299.14** |
| **+3 % contingency** | **€10,097.74** | **€24,617.96** | **€34,298.11** |
| QVL | ✓ | ✓ | ✓ |

### A — Start, 2×64 GB · €10,098

Two 64 GB 2Rx4 modules in the A1/E1 sockets, ten channels idle.

- **Buy if:** you are staging — getting the machine up, proving the four cards and
  the array, and adding RAM when the model demands it.
- **What it does well:** every VRAM-resident workload. IQ3_S at 262K × 8 streams
  never asks the host for bandwidth.
- **What it cannot do:** spill a large MoE at speed. 102 GB/s against 614 is the
  difference between a usable DeepSeek box and a slow one.
- **It is the cheapest honest entry point** — and the only tier where the RAM
  bill is smaller than the rest of the machine.

### B — Octa, 8×64 GB · €24,618

Your stated expansion target, filled 8 of 12 channels.

- **Buy if:** you want capacity (512 GB) more than the last four channels, or you
  are matching a WRX90-style 8-channel expectation.
- **The trade:** leaves **four memory controllers idle — 205 GB/s (33 %) of the
  platform's bandwidth unused** for a **+€14,520.22** step from A. If you are
  paying for twelve channels of silicon, this is the one tier that under-uses it.
- **Verdict: skip it.** Going A → C costs **€24,200 more** than A and buys the whole 614 GB/s;
  B costs **60 %** of that step and leaves a third of the bandwidth unused.

### C — Full, 12×64 GB · €34,298

All twelve channels. **The configuration the platform was chosen for.**

- **Buy if:** DeepSeek V4.1 or UD-Q8 will ever run on this box. At 614 GB/s the
  CPU expert lane runs at the speed the 8-CCD/12-channel decision was made for.
- **The trade:** **+€24,200 over A**, and RAM is then 82 % of the platform. That
  is the real cost of spilling large models on 128 GB of VRAM.
- **Every DIMM counts:** 12 modules populate 1 per channel (1DPC), which is the
  topology the 6400 MT/s rating assumes.

## Recommendation

**Buy A now, plan C.** A is the correct first purchase: it proves the platform,
the array and the four cards for €10,098, and every VRAM-resident workload runs
at full speed. Add 64 GB modules in pairs as a specific model demands them —
**go straight from 2 to 12** and skip the 8-DIMM stop, because B pays 60 % of the A→C step
for two-thirds of its bandwidth.

If you already know DeepSeek V4.1 is a primary workload, buy **C** and do not
buy A first — two 64 GB modules would be replaced, not extended.

## Power

| | Capped (210 W/card) | Stock (300 W/card) |
|---|---:|---:|
| 4× R9700 | 840 W | 1,200 W |
| EPYC 9355 (280 W) | 280 W | 280 W |
| 12× DDR5 RDIMM | 96 W | 96 W |
| Board, BMC, NIC, VRM loss | 40 W | 40 W |
| 4× NVMe, 1× SATA, fans | 60 W | 60 W |
| **Total** | **≈1,316 W** | **≈1,676 W** |
| **PSU** | **1,600 W** ✓ | **2,000 W** |

The 1600 W unit is comfortable at the 210 W cap (18 % headroom) and **over its
rating at stock** (1,676 W). Stock clocks need the **2,000 W** ToughPower i
(€520.89, +€171.01).

The 210 W cap is what the engine's reference build uses (211 W/card) on 4× R9700.
On a layer split it is not a performance compromise — the cards are not the
decode bottleneck.

### Connectors

| Need | Qty |
|---|---:|
| 12V-2x6 for the GPUs | **4** |
| 8-pin ATX 12V for the CPU | 2 |
| 6-pin ATX 12V (board aux) | 1 |
| 24-pin ATX | 1 |

The Dark Power Pro 13 carries 2× native 12V-2x6 + 6× PCIe 6+2, which covers four
cards via 2 native + 2 adapters and still leaves cables for the board aux.

## Slots and the fourth card

Three x16 slots are at **2.0 pitch** — three 40 mm cards sit natively. The fourth
goes on the **C-Payne MCIO→x16 adapter** with **two MCIO 8i cables**, consuming
the G0 group. That is the documented path, not a riser gamble.

Remaining MCIO: **G2 (2× MCIO 8i = 4 Gen5 NVMe)** for the array, and **G3
(Gen4 x8 or SATA)** for the cold SATA drive.

## Storage

**4× Samsung 9100 PRO 1 TB on one MCIO 8i port** via the KALEA adapter — RAID 0,
**4 TB, ~56–59 GB/s sequential**. That is your four-drive spec, and it uses one
of the two Gen5 MCIO groups.

**Cold:** one **870 EVO 1 TB** SATA on the G3 group through an MCIO→4× SATA
breakout. The CP1 has **no native SATA ports**; G3 is the documented SATA path.
1 TB holds the OS, the model archive and an image of the 4 TB array — but check
that fit, because a 4 TB RAID 0 image needs 4 TB of destination and 1 TB does
not hold it. **If you want a full image of the array, buy the 870 EVO 4 TB
(€999.99) or a 4 TB HDD instead**; the 2 TB (€547.13) and 4 TB SATA SSDs are
priced badly right now, so a 4 TB spinner is the cheaper archive.

## What is not in this price

- **The four GPUs.** Owned. Replacement at €1,930–2,249 each is **€7,721–8,996**.
- **A UPS, an OS, and the model downloads** (~79 GB for IQ3_S).
- **The 8 TB HDD** if you want a full array image (see Storage).

## Before you order

!!! warning "Board availability is the fragile line"
    The CP1 is in stock at €896.97 with multiple sellers — but it is the one part
    here with a history of EU stock gaps. Confirm at checkout.

!!! note "BIOS, not the label, decides 6400"
    The CP1 exposes `Memory Target Speed` only; a module runs at its **JEDEC SPD
    default**. A 7200-rated kit with a 6400 JEDEC default qualifies; a 6400-rated
    kit that defaults to 4800 does not. Every part priced is JEDEC-6400 at 1.1 V
    and QVL-passing.

!!! note "2×64 is 2 of 12 channels"
    Fine for VRAM-resident IQ3_S. **Not** a spilling-MoE configuration. See the
    ladder above before treating it as the final memory plan.
