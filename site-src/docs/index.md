# Four R9700s. One 128 GB VRAM box. Three priced answers.

<div class="hero" markdown>
<span class="eyebrow">R9700 ×4 · EPYC 9355 / MZ33-CP1 · 2026-11-17</span>

# Four cards you own. One platform, three prices.

Four PowerColor AI PRO R9700 32 GB cards, 128 GB of VRAM, on an EPYC 9355 in a
GIGABYTE MZ33-CP1 with 12 channels of DDR5-6400. Three memory tiers, priced:
**€18,035 / €34,093 / €19,572** before the GPUs you already own.

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

-   **Board — MZ33-CP1**
    ---
    E-ATX 304.8 × 330.2 mm, single SP5, **3× Gen5 x16 at 2-slot pitch** + 1,
    12 DIMM, 4× Gen5 MCIO, AST2600 IPMI. **€896.97, in stock.**
    [:octicons-arrow-right-24: The build](build.md)

-   **CPU — EPYC 9355**
    ---
    32C / **8 CCDs**, 256 MB L3, 3.55 GHz, **280 W**, 128× Gen5, 12-channel. **€2,329 tray.**
    The CCD count is the Infinity Fabric link count — see
    [the platform verdict](reference/epyc-platform.md).

-   **Memory — three tiers**
    ---
    **A** 12×32 GB = 384 GB (**€18,035**) · **B** 12×64 GB = 768 GB (**€34,093**)
    · **C** 6×64 GB = 384 GB (€19,572). JEDEC SPD 6400 @ 1.1 V, QVL-passing.
    Live offers: <a href="ram-board.html">RAM board</a>.

-   **GPUs — 4× R9700**
    ---
    32 GB, 40 mm, 2-slot blower, 12V-2x6, 300 W. All four on **risers in slots
    1–4** — five slots at 1.0 pitch cannot hold four 2-slot cards natively.
    [:octicons-arrow-right-24: R9700 dossier](parts/radeon-r9700.md)

-   **Storage — 2× 2 TB Gen5**
    ---
    Samsung 9100 PRO, **€399.99 each**, on the MCIO 8i port via the KALEA
    adapter — 4 TB of Gen5, not two throttled Gen3 slots.
    [:octicons-arrow-right-24: 9100 PRO dossier](parts/samsung-9100-pro.md)

-   **Power**
    ---
    **1,306 W capped / 1,666 W stock.** 1600 W unit (€349.88) at a 210 W GPU
    cap; 2000 W (€520.89) at stock. Connectors are the real limit, not watts.
    [:octicons-arrow-right-24: Power & connectors](build.md#power)

</div>

## What changed

The earlier book on this site priced a Threadripper PRO platform across eight
variants (A–H, plus a used W790 bundle), then collapsed to a single build on a
board that cannot be bought in the EU. This revision keeps the platform finding
and restores the priced options — three of them, differing only in memory,
because memory is 72–85 % of the bill. Three findings retired the Threadripper
book:

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

!!! warning "The board was the weak line"
    The previous revision specified the **MZ23-SU0**, which is **not buyable new
    in the EU** (Galaxus: *Aktuell nicht lieferbar*; zero Geizhals listings; only
    a used offer at €1,290). The **MZ33-CP1 at €896.97 is in stock** and gives
    three natively-spaced 2-slot x16 slots plus a documented MCIO path for the
    fourth card — no risers.

!!! note "No SATA, and that is fine here"
    The CP1 has **no native SATA** (its one M.2 is Gen3). The build has no
    spinning disks: storage is 4× Gen5 NVMe on the MCIO ports. A cold in-box
    archive would be an MCIO→SATA or USB decision, priced separately.

!!! note "The RAM rule is JEDEC, not the label"
    A module counts only if its **JEDEC SPD default is 6400 at 1.1 V**. The rated
    speed on the box is irrelevant: a 7200-rated kit with a 6400 JEDEC default
    qualifies, a 6400-rated kit that defaults to 4800 does not. Rank and
    organisation are free choices.

## Reference

- [The build](build.md) — **three priced options**, parts, power, connectors, slots, storage.
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
