# Four R9700s. One 128 GB VRAM box. One build.

<div class="hero" markdown>
<span class="eyebrow">R9700 ×4 · EPYC 9355P / MZ23-SU0 · 2026-11-17</span>

# Four cards you own. One platform decision, already made.

Four PowerColor AI PRO R9700 32 GB cards, 128 GB of VRAM, on an EPYC 9355P in a
GIGABYTE MZ23-SU0 with 12 channels of DDR5-6400. This site is that build: what
it is, why each part is that part, and what has to be true before you order.

<div class="hero-meta" markdown>
<span class="chip accent">4× 32 GB = 128 GB VRAM</span>
<span class="chip">12-channel · 614 GB/s</span>
<span class="chip">8 CCDs</span>
<span class="chip">JEDEC 6400 @ 1.1 V</span>
<span class="chip">IPMI</span>
</div>
</div>

## The build

<div class="grid cards" markdown>

-   **Board — MZ23-SU0**
    ---
    CEB 304.8 × 266.7 mm, single SP5, **5× PCIe 5.0 x16**, 12 DIMM, 4× MCIO 8i,
    AST2600 IPMI, **no native SATA**, 2× M.2 at **Gen3 x2**.
    [:octicons-arrow-right-24: The build](build.md)

-   **CPU — EPYC 9355P**
    ---
    32C / **8 CCDs**, 256 MB L3, 3.55 GHz, **280 W**, 128× Gen5, 12-channel.
    The CCD count is the Infinity Fabric link count — see
    [the platform verdict](reference/epyc-platform.md).

-   **Memory — 12× RDIMM**
    ---
    **JEDEC SPD 6400 @ 1.1 V**, any rank or organisation. The BIOS has no
    EXPO/XMP and pins the PMIC at 1.1 V, so a 7200 kit runs at its JEDEC default.
    Live offers: <a href="ram-board.html">RAM board</a>.

-   **GPUs — 4× R9700**
    ---
    32 GB, 40 mm, 2-slot blower, 12V-2x6, 300 W. All four on **risers in slots
    1–4** — five slots at 1.0 pitch cannot hold four 2-slot cards natively.
    [:octicons-arrow-right-24: R9700 dossier](parts/radeon-r9700.md)

-   **Storage — 2× 2 TB M.2**
    ---
    XPG Mars 980 or Samsung 9100 PRO, in the two onboard slots. Those slots are
    Gen3 x2, so a Gen5 drive runs at a fifth of its rating. Accepted: the disk
    is read once at start, not per token.
    [:octicons-arrow-right-24: 9100 PRO dossier](parts/samsung-9100-pro.md)

-   **Power**
    ---
    **1 306 W capped / 1 666 W stock.** 1600 W PSU at a 210 W GPU cap, or 2000 W
    at stock. Connector count is the real limit, not watts.
    [:octicons-arrow-right-24: Power & connectors](build.md#power-and-connectors)

</div>

## What changed, and why there is only one build

The earlier book on this site priced a Threadripper PRO platform across eight
variants (A–H, plus a used W790 bundle). Those pages are gone. Three findings
retired them:

- **CCD count decides the CPU lane.** A spilling MoE feeds the CPU-side expert
  lane over the Infinity Fabric, one link per CCD. A 2-CCD part cannot feed a
  multi-channel socket, whatever its core count. sTR5 also tops out at 8
  channels — 410 GB/s against SP5's **614 GB/s**, on a workload where that ratio
  *is* the decode ratio.
- **The engine already owns this path.** On gfx12 (R9700) `--pcie-frac` defaults
  to **0.15** — only 15 % of missing expert rows are fetched over PCIe, the rest
  are computed by a CPU pool reading `--resident-cpu-experts` from host RAM.
  Host bandwidth is on the decode path; PCIe is not.
- **VRAM-resident is not the workload.** A TensTorrent-parallel build would fit
  IQ3_S entirely in 128 GB and make host RAM idle. That is not what runs here.
  That assumption was wrong in four earlier answers on this site, and it is why
  the platform moved to SP5.

## Read before ordering

!!! warning "Five slots, all at 1.0 pitch"
    A 40 mm two-slot card blocks the slot beside it. Three cards fit natively in
    slots 1/3/5 and bury slots 2 and 4 under their coolers. **Four cards need
    four risers.** Passive Gen4 x16 at 20–30 cm is the reliable choice; Gen5
    passive past ~20 cm is not. Tensor-parallel engines all-reduce over PCIe and
    would not accept this — a layer split does.

!!! warning "No SATA on this board"
    The MZ23-SU0 has **no native SATA ports**; `SATA_SGP1/2` are backplane SGPIO
    headers. This build has no spinning disks, so that is not a gap here. Adding
    one would need MCIO→SATA or USB, and that is a separate decision.

!!! note "The RAM rule is JEDEC, not the label"
    A module counts only if its **JEDEC SPD default is 6400 at 1.1 V**. The rated
    speed on the box is irrelevant: a 7200-rated kit with a 6400 JEDEC default
    qualifies, a 6400-rated kit that defaults to 4800 does not. Rank and
    organisation are free choices.

## Reference

- [The build](build.md) — parts, power, connectors, slots, storage.
- [Platform verdict](reference/epyc-platform.md) — why SP5 and why 8 CCDs.
- [Memory ladder](reference/memory-ladder.md) — capacity against workload.
- [Power connectors](reference/power-connectors.md) — the cable math.
- [Storage & lanes](reference/storage-lanes.md) — port map and lane budget.
- [Acceptance protocol](reference/validation.md) — what to measure first.
- <a href="ram-board.html">RAM offer board</a> — live DDR5-6400 RDIMM offers.
- [Sources](reference/sources.md) — every price and spec link.

## Parts wiki

A dossier per part that is actually in the build: the spec that matters, the
pros and cons, and the trap in each one.

[Open the Parts wiki →](parts/index.md){ .md-button .md-button--primary }
