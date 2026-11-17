# Memory ladder

<p class="muted">12 channels on SP5, all at DDR5-6400 — 614 GB/s when all twelve are populated. Capacity is the only variable; bandwidth is not. This page is the capacity decision.</p>

## The rule

A module counts only if its **JEDEC SPD default is 6400 MT/s at 1.1 V**.

The MZ23-SU0 BIOS exposes `Memory Target Speed` (options end at `DDR5600`),
`PMIC SWC VDDIO = 1100` and `PMIC SWA/SWB VDD Core = 1100`. There is **no
EXPO/XMP menu and no DIMM voltage control**. So:

- A **7200-rated** kit whose JEDEC default is 6400 @ 1.1 V **qualifies** — it
  simply runs at its JEDEC default.
- A **6400-rated** kit that defaults to 4800 **does not**.

Rank and organisation are free choices. The earlier rule restricting this to
2Rx4 was dropped on 2026-11-17; the SPD default is the whole gate.

## Bandwidth by population

Every DIMM is one channel at 6400 = 51.2 GB/s. There is no partial-channel mode
worth using: 12 DIMMs is 1 DIMM per channel and the full 614 GB/s.

| DIMMs | Channels | Bandwidth |
|---:|---:|---:|
| 6 | 6 | 307 GB/s |
| 8 | 8 | 410 GB/s |
| **12** | **12** | **614 GB/s** |

Populating fewer than twelve is a capacity decision only — it costs bandwidth
linearly, and on a spilling MoE that bandwidth is on the decode path.

## Capacity against workload

| Model | Expert bytes outside VRAM | Plus PLE if `--ple-io ram` | Minimum useful |
|---|---:|---:|---:|
| IQ2_XXS 2.00 bpw (138 GB) | ~3.7 GB | +26.8 GiB | 128 GB total |
| IQ2_XS 2.25 bpw (155 GB) | ~20.7 GB | +26.8 GiB | 192 GB |
| **UD-Q8 (508 GB set)** | **~171.5 GB** | +26.8 GiB | **384 GB** |

`--ple-io ram` is not optional: it measured **+22.5 %** on an 8K prompt on this
card (2506 vs 2045 tok/s) because the PLE rows are random reads in a 26.8 GiB
table. Budget the RAM for it.

## What to buy

- **Never running UD-Q8:** 192 GB (12× 16 GB) gives the full 614 GB/s and costs
  the least. This is the rational default.
- **Running UD-Q8, or expecting to:** 384 GB (12× 32 GB). Nothing smaller holds
  a 508 GB set with the PLE table resident.
- **Do not buy 12× 64 GB** unless the model set grows past UD-Q8; at 768 GB the
  marginal €/GB is the worst in the catalogue.

Live offers, ranked by €/GB and tagged for QVL, are on the
<a href="../../ram-board.html">RAM offer board</a>.

!!! warning "12 modules is not a kit"
    Vendors sell kits of 8 and 4. Twelve modules means 8+4 of the same part
    number, ordered in one go so they are the same die revision. Mixing
    revisions across twelve channels at 6400 is the training risk, not the rank.
