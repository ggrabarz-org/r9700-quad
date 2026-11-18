# The build — three priced options

One platform, three memory tiers. Everything below is the same machine except
RAM, because **memory is 47–82 % of the bill** and it is the only part where the
cost/benefit answer is genuinely open. Board, CPU and drives are live retail
reads from **2026-11-18**; RAM unit pricing is the **2026-11-17** read carried
forward. EUR incl. VAT, and exclude the four GPUs you already own.

| | Part | Price | Why this one |
|---|---|---:|---|
| Board | **GIGABYTE MZ23-SU0 Rev. 3.x** | **€1,030.90** | **5× native PCIe Gen5 x16**, 12 DIMM / 12 channel, 4× MCIO 8i, AST2600 IPMI, CEB. The only board that gives four native Gen5 x16 links — see [four native x16 slots](#four-native-x16-slots) |
| CPU | **AMD EPYC 9355** (tray) | **€2,329.00** | 32C / **8 CCD**, 256 MB L3, 3.55 GHz, 280 W, **12-channel** DDR5-6400 |
| GPU | 4× PowerColor R9700 32G-B | owned | 32 GB, 40 mm 2-slot blower, 12V-2x6 |
| GPU 4 | Gen5 x16 extender | €75.00 est. | Relocates the fourth card to a clear chassis slot. Still a **native x16** slot electrically — not an MCIO adapter |
| Array | **2× Samsung 9100 PRO 2 TB** | **€831.98** | €415.99 each. RAID 0 = **4 TB at ~29 GB/s** on one MCIO 8i port. Expands to 4× 2 TB |
| Array link | MCIO 8i → 2× M.2 NVMe adapter | €45.00 est. | One MCIO 8i (Gen5 x8) carries two x4 drives |
| Cold | **Samsung 870 EVO 1 TB SATA** | **€103.99** | OS + model archive. A full array image needs the 4 TB or an HDD — see [storage](#storage) |
| Cold link | MCIO 8i → 8× SATA cable | **included** | Ships in the retail box (`25CF9-6007A7-A4R`); the board has no native SATA ports |
| PSU | **be quiet! Dark Power Pro 13 1600 W** ATX 3.1 | €349.88 | 1,316 W capped / 1,676 W stock — see [power](#power) |
| Cooling | Noctua NH-U14S TR5-SP6 | €126.01 | 280 W part, air; no AIO plumbing |
| Case | Fractal Meshify 2 XL | €218.08 | E-ATX and CEB, 9+3 slots, 250 mm PSU, 480 mm top |
| Fans | 3× 140 mm | €45.00 | Bottom/rear for the MCIO and GPU zone |
| | **Platform, excl. RAM** | **€5,154.84** | |

!!! note "The board is the only part with a real buying problem"
    `MZ23-SU0` (GIGABYTE part `9MZ23SU0MR-000-3`) is **€1,030.90 at Multitronic (FI)**,
    the only new-in-box EU listing found, and it shows **no delivery date**. The one
    live in-stock offer is **Newegg US at $869**, sold and shipped by Newegg
    (`N82E16813145624`) — and Newegg does not ship to the EU. So an EU buyer is
    either backordering at ~€1,031 or importing at ~€805 plus shipping and duty.
    Confirm stock or get a distributor quote on that part number before committing.

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

**6400 is a board property here, not an overclock.** The MZ23-SU0 rates
**DDR5-6400 at 1DPC with an EPYC 9005** (4800 with 9004). The BIOS exposes
`Memory Target Speed` only, so a module runs at its **JEDEC SPD default** — see
[the memory ladder](reference/memory-ladder.md) for the exact gate.

## The three options

RAM is priced at **€2,349.55 per 64 GB module** (the 2026-11-17 read),
multiplied by count.

| | **A — Start (2×64)** | **B — Octa (8×64)** | **C — Full (12×64)** |
|---|---|---|---|
| Memory | **2× 64 GB** = 128 GB | **8× 64 GB** = 512 GB | **12× 64 GB** = 768 GB |
| Channels | 2 of 12 | 8 of 12 | **12 of 12** |
| Bandwidth | **102.4 GB/s** | 409.6 GB/s | **614.4 GB/s** |
| RAM cost | €4,699.10 | €18,796.41 | €28,194.61 |
| **Platform total** | **€9,853.94** | **€23,951.25** | **€33,349.45** |
| **+3 % contingency** | **€10,149.56** | **€24,669.79** | **€34,349.93** |
| QVL | ✓ | ✓ | ✓ |

### A — Start, 2×64 GB · €10,150

Two 64 GB modules in the A1/E1 sockets, ten channels idle.

- **Buy if:** you are staging — getting the machine up, proving the four cards and
  the array, and adding RAM when the model demands it.
- **What it does well:** every VRAM-resident workload. IQ3_S at 262K × 8 streams
  never asks the host for bandwidth.
- **What it cannot do:** spill a large MoE at speed. 102 GB/s against 614 is the
  difference between a usable DeepSeek box and a slow one.
- **It is the cheapest honest entry point** — and the only tier where the RAM
  bill is smaller than the rest of the machine.

### B — Octa, 8×64 GB · €24,670

Your stated expansion target, filled 8 of 12 channels.

- **Buy if:** you want capacity (512 GB) more than the last four channels, or you
  are matching a WRX90-style 8-channel expectation.
- **The trade:** leaves **four memory controllers idle — 205 GB/s (33 %) of the
  platform's bandwidth unused** for a **+€14,097.31** step from A.
- **Verdict: skip it.** A → C costs €23,495.51 and buys the whole 614 GB/s; B
  costs 60 % of that step and leaves a third of the bandwidth unused.

### C — Full, 12×64 GB · €34,350

All twelve channels. **The configuration the platform was chosen for.**

- **Buy if:** DeepSeek V4.1 or UD-Q8 will ever run on this box. At 614 GB/s the
  CPU expert lane runs at the speed the 8-CCD/12-channel decision was made for.
- **The trade:** **+€23,495 over A**, and RAM is then 82 % of the platform. That
  is the real cost of spilling large models on 128 GB of VRAM.
- **Every DIMM counts:** 12 modules populate 1 per channel (1DPC), which is the
  topology the 6400 MT/s rating assumes.

## Recommendation

**Buy A now, plan C.** A is the correct first purchase: it proves the platform,
the array and the four cards for €10,150, and every VRAM-resident workload runs
at full speed. Add 64 GB modules in pairs as a specific model demands them —
**go straight from 2 to 12** and skip the 8-DIMM stop, because B pays 60 % of the
A→C step for two-thirds of its bandwidth.

If you already know DeepSeek V4.1 is a primary workload, buy **C** and do not
buy A first — two 64 GB modules would be replaced, not extended.

## Power

| | Capped (210 W/card) | Stock (300 W/card) |
|---|---:|---:|
| 4× R9700 | 840 W | 1,200 W |
| EPYC 9355 (280 W) | 280 W | 280 W |
| 12× DDR5 RDIMM | 96 W | 96 W |
| Board, BMC, NIC, VRM loss | 40 W | 40 W |
| 2× NVMe, 1× SATA, fans | 50 W | 50 W |
| **Total** | **≈1,306 W** | **≈1,666 W** |
| **PSU** | **1,600 W** ✓ | **2,000 W** |

The 1600 W unit is comfortable at the 210 W cap (18 % headroom) and **over its
rating at stock** (1,666 W). Stock clocks need the **2,000 W** ToughPower i
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

## Four native x16 slots

This is the requirement that decides the board. The MZ23-SU0 has **five
PCIe Gen5 x16 slots, every one wired x16** — so all four cards sit on a native
Gen5 x16 link with **no MCIO-to-x16 adapter anywhere in the GPU path**.

That matters because the board this replaces (MZ33-CP1) has only **three Gen5
x16 plus one Gen4 x16**, and reaches a fourth card only through an MCIO→x16
adapter. On mainstream SP5 boards that is the normal limit: three x16 lanes for
cards, the rest cabled. **The MZ23-SU0 is the only board found that clears four
native Gen5 x16**, and that is why it is the pick.

### The mechanical caveat — read this before buying

The five slots are at **1.0-slot pitch (~20.4 mm)**, and the R9700 is a **40 mm
two-slot card**. So on the board itself:

| Slot | Seats a 40 mm card directly |
|---|---|
| Slot_1 | ✓ |
| Slot_2 | ✗ blocked by Slot_1's card |
| Slot_3 | ✓ (40.6 mm below Slot_1) |
| Slot_4 | ✗ blocked by Slot_3's card |
| Slot_5 | ✓ (40.6 mm below Slot_3) |

**Three cards seat directly. The fourth goes on a Gen5 x16 extender** plugged
into Slot_2 or Slot_4 and routed to a clear chassis position. That is a
*mechanical relocation of a native x16 slot*, not an electrical compromise:
unlike the MCIO adapter it replaces, the card still trains on a Gen5 x16 link
straight off the socket. Budget a quality Gen5-rated extender and **test-fit all
four before the return window closes**.

!!! warning "Extender quality is the risk, not the lane count"
    A Gen5 x16 extender is a passive high-speed path; a marginal one shows up as
    link-down or a Gen4/Gen3 retrain, not as a slow-but-working card. Buy a
    stated Gen5 part, confirm `lspci -vv` reports **32 GT/s x16** on all four
    cards, and treat any card that trains at 16 GT/s as a bad cable.

## Storage

The array uses **MCIO, not the onboard M.2 slots**, and this is the second
reason the board works: because the fourth GPU is a native slot and not an MCIO
adapter, **all four MCIO 8i connectors stay free for storage**.

| MCIO group | Width | Used for |
|---|---|---|
| #1 | Gen5 x8 | **2× 2 TB now** |
| #2 | Gen5 x8 | **Free — the expansion slot for drives 3 and 4** |
| #3 | Gen5 x8 or SATA | Cold SATA SSD, via the included cable |
| #4 | Gen5 x8 or SATA | Spare |

**Now:** 2× **Samsung 9100 PRO 2 TB** on MCIO #1 through one 8i→2× M.2 adapter.
Two Gen5 x4 drives on an x8 port: **RAID 0 = 4 TB at ~29 GB/s sequential**. Left
separate is also fine — one for models, one for checkpoints.

**Later:** add 2× 2 TB on MCIO #2 and the same RAID 0 becomes **8 TB at
~59 GB/s**. Nothing else changes; the adapter is identical. That is the four-drive
target, reached without touching the GPU slots.

**Why not the onboard M.2 slots:** they are **PCIe Gen3 x2** — about 2 GB/s, a
fifth of what the drive does. They work, and they are fine for a boot disk, but a
Gen5 array belongs on MCIO.

**Cold:** one **870 EVO 1 TB** on MCIO #3 through the **8× SATA cable that ships
in the box**. The board has no native SATA ports, so this is the documented path
and it costs nothing extra. 1 TB holds the OS and the model archive; it does
**not** hold an image of a 4 TB array. If you want array images, buy the 870 EVO
4 TB (€999.99 as of the 2026-11-17 read) or an 8 TB HDD — at 8 TB of array you
need the HDD either way.

## What is not in this price

- **The four GPUs.** Owned. Replacement at €1,930–2,249 each is **€7,721–8,996**.
- **A UPS, an OS, and the model downloads** (~79 GB for IQ3_S).
- **The cold archive drive upgrade** if you want full array images.

## Before you order

!!! warning "Board availability is the fragile line"
    The MZ23-SU0 is the only board with four native Gen5 x16 slots, and it is the
    hardest part here to buy. The live in-stock offer is **Newegg US, $869**,
    which does not ship to the EU. The only new EU listing is **Multitronic (FI)
    at €1,030.90 with no delivery date**. Confirm stock, or ask a distributor to
    quote part **`9MZ23SU0MR-000-3`** directly.

!!! note "BIOS, not the label, decides 6400"
    A module runs at its **JEDEC SPD default**. A 7200-rated kit with a 6400
    JEDEC default qualifies; a 6400-rated kit that defaults to 4800 does not.
    Every part priced is JEDEC-6400 at 1.1 V.

!!! note "2×64 is 2 of 12 channels"
    Fine for VRAM-resident IQ3_S. **Not** a spilling-MoE configuration. See the
    ladder above before treating it as the final memory plan.

!!! note "Slot pitch needs one extender"
    Five native x16 slots at 1.0 pitch means three 40 mm cards seat directly and
    the fourth needs a Gen5 x16 extender. All four still train on native Gen5
    x16. See [four native x16 slots](#four-native-x16-slots).
