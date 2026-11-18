# Sources

<p class="muted">Every specification link used in this site, and what each one verifies. Prices are the 2026-11-17 snapshot, incl. VAT unless marked. Listed offers are not quotes.</p>

## Board

| Source | What it verifies |
|---|---|
| [GIGABYTE MZ23-SU0 (Rev. 3.x) product page](https://www.gigabyte.com/Enterprise/Server-Motherboard/MZ23-SU0-rev-3x) | CEB 304.8 × 266.7 mm, single SP5, 5× PCIe 5.0 x16, 12 DIMM, 4× MCIO 8i, AST2600, cTDP up to 500 W. |
| [MZ23-SU0 datasheet (PDF)](https://download.gigabyte.com/FileList/DataSheet/GIGABYTE%20MZ23-SU0%20(Rev.%203.x)_datasheet.pdf) | Internal I/O list: 24-pin, **2× 8-pin**, **1× 6-pin**, 1× CPU + 5× SYS fan, **2× M.2 Gen3 x2**, no SATA ports. |
| [MZ23-SU0 user manual (PDF)](https://download.gigabyte.com/FileList/Manual/server_manual_mz23_su0_e.pdf) | Connector legend; `P12V_PCIE` pinout; `Memory Target Speed` options ending at DDR5600; `PMIC SWC VDDIO 1100`; no EXPO/XMP menu; fan header pinout. |
| [MZ23-SU0 QVL](https://www.gigabyte.com/Enterprise/Server-Motherboard/MZ23-SU0-rev-3x/Support-QVL) | CPU and memory qualification lists. The memory tab needs a category click; the direct spreadsheet URL 404s. |
| [Multitronic FI — MZ23-SU0, `9MZ23SU0MR-000-3`](https://www.multitronic.fi/en/products/4624349) | **€1,030.90 incl. VAT, "no delivery date yet", not in stock** (2026-11-18). The only new-in-box EU listing found. Confirms 5× PCIe x16 Gen5, 12 DIMM, CEB, EAN 4719331881696. |
| [Newegg US — MZ23-SU0, `N82E16813145624`](https://www.newegg.com/gigabyte-mz23-su0/p/N82E16813145624) | **$869.00, in stock, sold and shipped by Newegg** (2026-11-18). Does not ship to the EU. |
| [Samsung 9100 PRO 2 TB (`MZ-VAP2T0BW`)](https://geizhals.de/samsung-ssd-9100-pro-2tb-mz-vap2t0bw-a3427162.html) | **€415.99** (Geizhals DE, 2026-11-18); 14,800 / 13,400 MB/s, PCIe 5.0 x4, M.2 2280. |

## CPU

| Source | What it verifies |
|---|---|
| [AMD EPYC 9355P](https://www.amd.com/en/products/processors/server/epyc/9005-series/amd-epyc-9355p.html) | 32C, 256 MB L3, 3.55 GHz, 280 W, SP5, 128× PCIe 5.0, 12-channel DDR5-6400. |
| [AMD EPYC 9005 specification table](https://www.amd.com/en/products/specifications/server-processor.html) | The full SKU ladder; CCD counts and cTDP ranges for every 9005 part. |
| `docs/research/epyc-9005-8ccd-list.md` (repository) | CCD count derived from L3 ÷ 32 MB per SKU; the 8-CCD filter this build uses. |

## GPU

| Source | What it verifies |
|---|---|
| [AMD Radeon AI PRO R9700](https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html) | 32 GB GDDR6, 300 W, 2-slot blower, 1× 12V-2x6. |
| [PowerColor AI PRO R9700 32G-B](https://www.powercolor.com/product-detail258.htm) | The exact SKU: 266.7 × 111.2 × **40 mm**, 2-slot. |
| [R9700 spec sheet (gpus.net)](https://www.gpus.net/gpus/amd_ai_pro_r9700/powercolor_radeon_ai_pro_r9700) | 40 mm, 2 slots, 1× 16-pin, 300 W TDP, 644.6 GB/s. |

## Memory

| Source | What it verifies |
|---|---|
| [Kingston FURY Renegade Pro DDR5 RDIMM](https://www.kingston.com/en/memory/gaming/fury-renegade-ddr5-pro-rdimm) | The 7200-rated kits, and that their aluminium heat-spreader line starts at 7200. |
| [Kingston KF572RH38RBK8-256 datasheet (PDF)](https://www.kingston.com/dataSheets/KF572RH38RBK8-256.pdf) | **JEDEC default DDR5-6400 CL52 @ 1.1 V**; EXPO profiles are 7200/6800 @ 1.4 V. This is the document that decides eligibility under the JEDEC rule. |
| [Kingston part-number decoder](https://www.kingston.com/en/memory/memory-part-number-decoder) | How to read `KF572RH38RBK8-256`: FURY, DDR5, 7200, EC8 RDIMM, CL38, kit of 8, 256 GB. |

## Storage

| Source | What it verifies |
|---|---|
| [Samsung 9100 PRO](https://semiconductor.samsung.com/consumer-storage/internal-ssd/9100-pro/) | PCIe 5.0 x4, capacity ladder, TBW. |
| [Samsung 9100 PRO 2 TB (Newegg)](https://www.newegg.com/samsung-2tb-9100-pro-nvme-2-0/p/N82E16820147903) | The `MZ-VAP2T0B` part number and the retail listing. |

## Engine behaviour

| Source | What it verifies |
|---|---|
| `/root/git/strata/docs/AMD_HIP.md` (repository) | `--pcie-frac` default **0.15** on gfx12: 8K decode 86.1 → 94.6 tok/s, 32K 67.2 → 84.4 tok/s. `--ple-io ram` +22.5 % on an 8K prompt. |
| `/root/git/strata/docs/MULTI_GPU.md` (repository) | Layer split, not tensor parallel: contiguous layer ranges, one hand-off per verify window, no NCCL, no all-reduce, no P2P requirement. |
| `/root/git/strata/docs/AMD_HIP_PERFORMANCE.md` (repository) | `--resident-cpu-experts` copies the complement of the static GPU cache to ordinary RAM; the pool reads it during decode. |
| `docs/DECISIONS.md` (repository) | The settled flag decisions and the claims they superseded. |
| `docs/research/RECOMMENDATION.md` (repository) | The CCD ladder, the 9555-sample trap, and the RAM market audit. |
