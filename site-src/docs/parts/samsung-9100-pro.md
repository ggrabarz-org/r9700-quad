# Samsung 9100 PRO 2 TB

<p class="muted"><strong>2 TB</strong> · PCIe 5.0 x4. In this build: <b>the array drive</b>, two of them now and four after expansion. Runs on MCIO — the onboard M.2 slots are Gen3 x2, see the trap below.</p>

## What it is

Samsung's Gen5 consumer/workstation SSD, 2 TB, PCIe 5.0 x4. It is the array
drive because at **€415.99 for 2 TB** it is the cheapest way to put Gen5
bandwidth on this board's MCIO ports, and two of them in RAID 0 give 4 TB at
roughly 29 GB/s before you buy a third.

## Specifications

| Feature | Detail |
|---|---|
| Capacity | 2 TB |
| Interface | PCIe 5.0 x4, NVMe |
| Sequential read / write | 14,800 / 13,400 MB/s |
| 4K random IOPS | 1.85M read / 2.6M write |
| Form factor | M.2 2280 |
| Price | **€415.99** (Geizhals DE, 2026-11-18) |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **14.8 GB/s per drive**, and two of them saturate an MCIO 8i (Gen5 x8) port
  almost exactly — 29 GB/s of a theoretical 32.
- **2 TB each**, so the 4 TB target is two drives, not four.
- **The expansion is free of decisions:** adding two more is the same model, the
  same adapter, and the second MCIO group. 8 TB at ~59 GB/s.
- **MCIO, not the onboard slot**, so it runs at full Gen5 x4 instead of the
  Gen3 x2 the board's M.2 connectors offer.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **Gen5 runs hot**; needs airflow/heatsink, especially under the GPU zone.
- **No PLP** (power-loss protection). RAID 0 on consumer drives has no
  redundancy — keep a separate backup of anything you cannot re-download.
- **Price is a snapshot** and NAND pricing is moving through 2026.
- **RAID 0 doubles the failure surface** for throughput a model load barely
  notices. Keeping the two drives separate is a valid choice.
</div>
</div>

## Where it is used

- [The build](../build.md) — 2× on MCIO #1 now, 4× across #1 and #2 later.
