# Samsung 9100 PRO 1 TB

<p class="muted"><strong>2 TB</strong> · PCIe 5.0 x4. In this build: <b>the storage pick</b> (or XPG Mars 980). Onboard M.2 slots are Gen3 x2 — see the trap below.</p>

## What it is

Samsung’s Gen5 consumer/workstation SSD, 1 TB, PCIe 5.0 x4. It is the array drive for the 3× Gen5 build and the four-drive ASUS build. The key fact is price: at **€264** it is the same price as the 1 TB Gen4 990 PRO, so Gen5 is the default where the board has the port.

## Specifications

| Feature | Detail |
|---|---|
| Capacity | 1 TB |
| Interface | PCIe 5.0 x4, NVMe |
| Sequential read / write | 14,800 / 13,400 MB/s |
| 4K random IOPS | 1.85M read / 2.6M write |
| Form factor | M.2 2280 |
| Price | **€264.00** |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **Gen5 at Gen4 price** (€264 vs €262 for the 990 PRO).
- **~14.8 GB/s read** per drive; a 3-drive array is ~42–44 GB/s.
- **M.2 2280**, fits the MZ23-SU0's onboard slot. Reads at ~2 GB/s there, the
  slot's Gen3 x2 ceiling, not the drive's.
- **The fastest array drive in the book.**
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **Gen5 runs hot**; needs airflow/heatsink, especially under GPUs.
- **1 TB per drive**, so the 3 TB array is only three drives.
- **DRAM/price can move**; the €264 is a snapshot.
- **No PLP** (power-loss protection); RAID 0 + consumer SSD.
</div>
</div>

## Where it is used

- [The build](../build.md)
