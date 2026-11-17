# Why SP5, and why 8 CCDs

<p class="muted">Two facts pick the platform: the expert lane is fed one link per CCD, and every sTR5 part tops out at 8 channels. Everything else follows.</p>

## The mechanism

On a spilling MoE the engine computes the experts the GPUs cannot hold. On
gfx12 (R9700) it deliberately sends only a small share over PCIe —
`--pcie-frac` **defaults to 0.15** — and computes the rest in a CPU pool reading
`--resident-cpu-experts` from host RAM. Measured on an R9700 with IQ3_S
(`AMD_HIP.md`): 8K decode **86.1 → 94.6 tok/s** and 32K **67.2 → 84.4 tok/s** when
the PCIe share dropped from 0.55 to 0.15.

So host RAM bandwidth sits on the decode path, and it is fed by the CPU's
Infinity Fabric links to the I/O die — **one per CCD**.

## The consequence

| | WRX90 / sTR5 | **SP5 / EPYC 9005** |
|---|---|---|
| Memory channels | 8 | **12** |
| Peak bandwidth | 409.6 GB/s | **614.4 GB/s** |
| 2-CCD part's usable share | cannot feed 8 channels | — |
| Boards | ASUS WRX90E-SAGE SE, ASRock WRX90 WS EVO (retired) | **GIGABYTE MZ23-SU0** |

A 2-CCD part has two fabric links, which cannot saturate an 8- or 12-channel
socket from the CPU side. The earlier book's 9955WX (16C, 64 MB L3, **2 CCDs**)
is disqualified for exactly this reason — the same disqualification that removed
the EPYC 9135 (16C, 2 CCDs).

## The pick

**EPYC 9355P** — 32C, **8 CCDs**, 256 MB L3, 3.55 GHz, **280 W**, 128 Gen5 lanes,
12-channel DDR5-6400. Eight CCDs is the minimum for a full set of fabric links to
a 12-channel socket; the `P` suffix is 1P-only, which is what this board is.

Every alternative either has fewer CCDs or costs more for cores this workload
cannot use:

| SKU | Cores | CCDs | Why not |
|---|---:|---:|---|
| 9135 | 16 | 2 | Cannot feed the socket |
| 9355 | 32 | 8 | Same silicon, 1P/2P; fine if cheaper |
| 9555 | 64 | 8 | +64 cores buy prefill, not decode |
| 9655 | 96 | 12 | 12 CCDs, but far dearer for no decode gain |
| 9755 | 128 | 16 | 450 W floor; forces a 2000 W PSU |

Decode is bandwidth-bound: one token reads each activated expert's weights once,
~4 FLOP/byte, so 614 GB/s caps useful compute at ~2.4 TFLOP/s. The cores sit
waiting on memory. Prefill is the opposite — compute-bound, roughly linear in
cores — which is where a 9555 would earn its price, on a phase that is not the
bottleneck.

!!! note "On the 9355 vs 9355P"
    Same cores, same CCDs, same TDP. The P is single-socket only. In the EU the P
    has been quoted higher than the plain 9355; take whichever is cheaper.

## VRAM-resident is not this workload

If every expert fits in 128 GB of VRAM, the CPU lane is idle, CCD count stops
mattering, and a 2-CCD part would be correct. Strata measures *fewer* pool
workers winning in that mode (15 workers 38–42 tok/s vs 24 workers 27 tok/s).
That is not the configuration this build is for.

## Full analysis

The CCD ladder, board comparisons, the RAM market audit and the €1,050 "9555 QS"
trap — a 1.9–3.0 GHz ES, not a 3.2 GHz 9555 — are in the repository:
`docs/research/RECOMMENDATION.md`.
