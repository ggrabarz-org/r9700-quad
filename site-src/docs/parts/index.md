# Part dossiers

<p class="muted">Every part in the build has a page: the specification that matters, the pros and cons, and the trap in it. Board, CPU and drive prices are the 2026-11-18 read; RAM is the 2026-11-17 read. All incl. VAT unless marked.</p>

<div class="grid cards" markdown>

-   **GPU**
    ---
    PowerColor AI PRO R9700 32G-B — 32 GB, 40 mm, 2-slot blower, 12V-2x6.
    [R9700 dossier](radeon-r9700.md)

-   **Storage**
    ---
    Samsung 9100 PRO 2 TB — Gen5 x4, two now and four later, on MCIO rather than
    the Gen3 x2 onboard slot.
    [9100 PRO dossier](samsung-9100-pro.md)

-   **Board, CPU, memory, power**
    ---
    MZ23-SU0, EPYC 9355, the JEDEC-6400 rule and the PSU cable math are covered in
    [the build](../build.md) and the [platform verdict](../reference/epyc-platform.md)
    pages, because each one is a decision rather than a part.

</div>

## The three traps

- **The slots are 1.0 pitch.** Five native Gen5 x16 slots is the reason for this
  board, but at 20.4 mm spacing three 40 mm cards seat directly and the fourth
  needs a Gen5 x16 extender. All four still train on native Gen5 x16 — the
  extender is mechanical, not electrical. See
  [four native x16 slots](../build.md#four-native-x16-slots).
- **M.2 slots are Gen3 x2.** A 9100 PRO there runs at ~2 GB/s instead of ~14.8.
  The slot is fine for a boot drive, wrong for the array, which goes on MCIO.
- **No native SATA.** Fine for this build — the retail box ships an MCIO→8× SATA
  cable, so the cold SSD costs nothing extra. Spinners would need that same cable
  plus a bracket.
