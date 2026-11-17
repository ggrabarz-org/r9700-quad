# Part dossiers

<p class="muted">Every part in the build has a page: the specification that matters, the pros and cons, and the trap in it. Prices are the 2026-11-17 snapshot, incl. VAT unless marked.</p>

<div class="grid cards" markdown>

-   **GPU**
    ---
    PowerColor AI PRO R9700 32G-B — 32 GB, 40 mm, 2-slot blower, 12V-2x6.
    [R9700 dossier](radeon-r9700.md)

-   **Storage**
    ---
    Samsung 9100 PRO 2 TB (or XPG Mars 980) — Gen5 x4, and the Gen3 x2 slot that
    wastes it.
    [9100 PRO dossier](samsung-9100-pro.md)

-   **Board, CPU, memory, power**
    ---
    MZ23-SU0, EPYC 9355P, the RDIMM rule and the PSU cable math are covered in
    [the build](../build.md) and the [reference](../reference/) pages, because
    each one is a decision rather than a part.

</div>

## The three traps

- **M.2 slots are Gen3 x2.** A 9100 PRO there runs at ~2 GB/s instead of ~14.
  The slot is fine for a boot drive, wrong for the array.
- **No native SATA.** Fine for this build, which has no spinning disks.
- **Slots are all 1.0 pitch.** Four 40 mm cards need four risers, not three
  slots plus one adapter.
