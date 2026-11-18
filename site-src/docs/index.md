# Four R9700s. Four native Gen5 x16. Three memory tiers.

<div class="hero" markdown>
<span class="eyebrow">R9700 ×4 · EPYC 9355 / MZ23-SU0 · 2026-11-18</span>

# Four cards you own. One platform decision, already made.

Four PowerColor AI PRO R9700 32 GB cards, 128 GB of VRAM, on an EPYC 9355 in a
GIGABYTE MZ23-SU0 — **four native PCIe Gen5 x16 links**, 12 channels of
DDR5-6400. Three memory tiers, priced: **€10,150 / €24,670 / €34,350** before the
GPUs you already own.

<div class="hero-meta" markdown>
<span class="chip accent">4× 32 GB = 128 GB VRAM</span>
<span class="chip">4× native Gen5 x16</span>
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
    CEB 304.8 × 266.7 mm, single SP5, **5× PCIe Gen5 x16 — every one wired x16**,
    12 DIMM / 12 channel, 4× MCIO 8i, AST2600 IPMI. **€1,030.90 (EU list)**;
    in stock at **$869 Newegg US**. The only board found with four native Gen5
    x16 links — the fourth card is a slot, not an adapter.
    [:octicons-arrow-right-24: The build](build.md)

-   **CPU — EPYC 9355**
    ---
    32C / **8 CCDs**, 256 MB L3, 3.55 GHz, **280 W**, 128× Gen5, 12-channel.
    **€2,329 tray.** The CCD count is the Infinity Fabric link count — see
    [the platform verdict](reference/epyc-platform.md).

-   **Memory — three tiers**
    ---
    **A** 2×64 GB = 128 GB, 2 of 12 channels (**€10,150**) · **B** 8×64 GB =
    512 GB, 8ch (**€24,670**) · **C** 12×64 GB = 768 GB, **614 GB/s**
    (**€34,350**). JEDEC SPD 6400 @ 1.1 V, QVL-passing.
    Live offers: <a href="ram-board.html">RAM board</a>.

-   **GPUs — 4× R9700**
    ---
    32 GB, 40 mm, 2-slot blower, 12V-2x6, 300 W. **Four native Gen5 x16 slots.**
    Three 40 mm cards seat directly; the fourth sits on a Gen5 x16 extender
    because the slots are at 1.0 pitch — still a native x16 link.
    [:octicons-arrow-right-24: R9700 dossier](parts/radeon-r9700.md)

-   **Storage — 2× 2 TB now, 4× 2 TB later**
    ---
    **2× Samsung 9100 PRO 2 TB** (€415.99 each) on one MCIO 8i = **4 TB at
    ~29 GB/s**; add two more on the second MCIO group for **8 TB at ~59 GB/s**.
    **1 TB 870 EVO** (€103.99) on SATA — the board ships an MCIO→8× SATA cable.
    [:octicons-arrow-right-24: 9100 PRO dossier](parts/samsung-9100-pro.md)

-   **Power**
    ---
    **1,306 W capped / 1,666 W stock.** 1600 W (€349.88) at a 210 W GPU cap; 2000 W
    (€520.89) at stock. Connector count is the real limit, not watts.
    [:octicons-arrow-right-24: Power & connectors](build.md#power)

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
- **VRAM-resident is not the workload.** A tensor-parallel build would fit
  IQ3_S entirely in 128 GB and make host RAM idle. That is not what runs here.
  That assumption was wrong in four earlier answers on this site, and it is why
  the platform moved to SP5.

## Read before ordering

!!! warning "The board is four slots, and only this one has them"
    Every other SP5 board found gives **three** Gen5 x16 lanes for cards plus a
    MCIO adapter for the fourth. The **MZ23-SU0 gives five x16 slots, all native
    Gen5** — the thing this build is actually for. Its catch is mechanical, not
    electrical: the slots are at **1.0 pitch**, so three 40 mm cards seat
    directly and the fourth needs a **Gen5 x16 extender**. All four still train
    on native Gen5 x16. See [four native x16 slots](build.md#four-native-x16-slots).

!!! warning "And it is the hardest part to buy in the EU"
    The live in-stock offer is **Newegg US at $869**, which does not ship to the
    EU. The only new EU listing is **Multitronic (FI) at €1,030.90 with no
    delivery date**. Confirm stock, or get a distributor quote on part
    `9MZ23SU0MR-000-3`.

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
