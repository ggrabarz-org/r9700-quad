# The build

One build. There are no options A–H, no ASUS/ASRock fork, no W790 bundle — those
pages are excluded from this site and kept in the repository only as history.

| | Part | Qty |
|---|---|---:|
| Board | **GIGABYTE MZ23-SU0 (Rev. 3.x)** — CEB 304.8 × 266.7 mm, single SP5, 5× PCIe 5.0 x16, 12 DIMM, 4× MCIO 8i, AST2600 IPMI | 1 |
| CPU | **AMD EPYC 9355P** — 32C, 8 CCD, 256 MB L3, 3.55 GHz, 280 W, 128× Gen5, 12-channel DDR5-6400 | 1 |
| Memory | **12× DDR5 RDIMM, JEDEC SPD 6400 @ 1.1 V** (any rank/org; rated speed irrelevant, the BIOS has no EXPO/XMP) | 12 |
| GPU | **PowerColor AI PRO R9700 32G-B** — 32 GB, 2-slot, 40 mm, blower, 12V-2x6, 300 W | 4 |
| SSD | **2 TB M.2 NVMe** — XPG Mars 980 or Samsung 9100 PRO, in the two onboard slots | 2 |
| PSU | 1600 W (210 W GPU cap) or 2000 W (stock 300 W) — see [power](#power-and-connectors) | 1 |
| Cooling | SP5 4U-class heatsink or 360 mm SP5 AIO + case fans | — |

## Why this and nothing else

- **SP5, not sTR5.** 12 channels at 6400 is **614 GB/s**; WRX90's 8 channels is
  410 GB/s. On a spilling MoE the engine reads experts from host RAM on the
  decode path (`--resident-cpu-experts`), so that ratio is the decode ratio.
- **8 CCDs minimum.** The CPU-side lane is fed by the Infinity Fabric links to
  the I/O die, one per CCD. The 9355P has eight; a 2-CCD part cannot feed a
  12-channel socket. See [the platform verdict](reference/epyc-platform.md).
- **JEDEC SPD, not XMP.** The MZ23-SU0 BIOS exposes only `Memory Target Speed`
  (list ends at DDR5600) and `PMIC VIDEO/VDD Core = 1100`. A 7200-rated kit runs
  at its **JEDEC default**, which must be 6400 @ 1.1 V. That is the only gate;
  rank and organisation do not matter.
- **`P` suffix is 1P-only**, which is what this board is.

## Power and connectors

### What the board needs

Verified against the MZ23-SU0 datasheet and manual, not the product page:

| Connector | Purpose | Qty |
|---|---|---:|
| 24-pin ATX | main | 1 |
| 8-pin ATX 12V (`P12V_AUX1/2`) | CPU | **2** |
| 6-pin ATX 12V (`P12V_PCIE`) | board aux — **mandatory** | 1 |
| Molex (`FAN1_PWR`) | fan rail, if a hub is used | 1 |

### What the cards need

| Connector | Qty |
|---|---:|
| 12V-2x6 (16-pin) per R9700 | **4** |

None of the four cards draws 12 V through a riser, so every card needs its own
16-pin feed.

### Fan headers

**1× CPU_FAN + 5× SYS_FAN**, all 4-pin (GND / +12 V / Sense / PWM). Six fans
without a hub; more needs `FAN1_PWR`. Header current limit is not published —
do not chain five fans on one header.

### Totals

| | Stock (300 W/card) | Capped (210 W/card) |
|---|---:|---:|
| 4× R9700 | 1 200 W | 840 W |
| EPYC 9355P | 280 W | 280 W |
| 12× DDR5 RDIMM | 96 W | 96 W |
| Board, BMC, NIC, VRM loss | 40 W | 40 W |
| 2× M.2 | 20 W | 20 W |
| Fans | 30 W | 30 W |
| **Total** | **≈1 666 W** | **≈1 306 W** |
| **PSU** | **2 000 W** | **1 600 W** |

The 210 W cap is the configuration the engine's own reference build uses
(211 W/card, 4× R9700, EPYC). It is not a performance compromise on a layer
split — the cards are not the decode bottleneck.

## Slots and risers

Five x16 slots, **all at 1.0 pitch (20.4–20.7 mm)**. A 40 mm two-slot card
occupies its slot plus the next one, so three cards natively fill slots 1/3/5
and leave 2 and 4 buried under their neighbours' coolers.

**Four cards therefore need four risers in slots 1–4.** Slot 5 stays free.
Four identical passive Gen4 x16 risers at 20–30 cm are the reliable choice;
Gen5 passive past ~20 cm is not. The engine fetches at most 15 % of missing
expert rows over PCIe (`--pcie-frac 0.15` on gfx12), so 32 GB/s per card is an
order of magnitude more than the link is asked to carry.

> **Exception:** tensor-parallel engines (Radiance, vLLM) all-reduce every layer
> over PCIe. Gen4 risers are free for a layer split, not for TP4.

## Storage

Two drives, two onboard slots. The slots are **PCIe Gen3 x2**, so a Gen5 drive
runs at about 2 GB/s each — a fifth of its rating. That is the board's limit and
this build accepts it: the drives hold an OS and model files that are read once
at start, and the engine's hot path is VRAM and host RAM, not disk.
