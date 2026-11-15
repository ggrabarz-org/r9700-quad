# Platform verdict: WRX90 → EPYC/SP5 (superseded 2026-11-15)

**The WRX90 builds on this site are superseded for any workload where experts
spill to system RAM.** The reason is the CPU's CCD count, not the board:

- The CPU expert lane on a spilling MoE is fed by the CPU's Infinity Fabric
  links to the I/O die, **one per CCD**.
- The book's chosen TR PRO 9955WX is a **2-CCD** part (64 MB L3) — 2 fabric
  links cannot feed the 8-channel sTR5 platform's 409.6 GB/s from the CPU side.
- sTR5 is 8-channel on **every** TR PRO SKU; SP5 EPYC is 12-channel, **614 GB/s**
  (+33 %). That ratio is the decode ratio on the CPU-expert path.

## The replacement platform

| | WRX90 (this site's builds) | **EPYC 9005 / SP5 (replacement)** |
|---|---|---|
| Memory channels | 8 | **12** |
| Peak bandwidth | 409.6 GB/s | **614.4 GB/s** |
| CPU CCD options | 2–12 (but 8ch ceiling regardless) | up to 16 CCDs, 12 channels wired to the IOD |
| 8-CCD CPU | 9985WX, $7,999 | **9555** ($4,529 retail) / **9355** (8 CCDs, €2,050) |
| Board | ASUS WRX90E-SAGE SE €1,288 | **Supermicro H14SSL-N €975 / Gigabyte MZ33-CP1 €877** |
| 4 dual-slot GPUs | 3 native (ASUS guidance) + unsupported slot | 3 native + 1 documented MCIO adapter (€140) |
| PSU | 2,200 W | 1,600 W |

## What stays valid on WRX90

A **strictly VRAM-resident** workload — IQ3_S/IQ3_XXS with all experts on the
four cards, no spilling MoE ever. There the CPU lane is idle, CCD count is
irrelevant, and the WRX90 builds below are correctly sized. Strata measures
*fewer* CPU workers winning in that mode (15 workers 38–42 tok/s vs 24 workers
27 tok/s).

## Full analysis

The complete CCD-ladder argument, board comparisons, RAM market audit and the
EPYC 9555-sample trap (the €1,050 "9555 QS" is a 1.9–3.0 GHz 9535-class ES, not
a 3.2 GHz 9555) live in the repository:
`docs/research/RECOMMENDATION.md`.
