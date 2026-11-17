# Power connectors

<p class="muted">Connector count is the limit, not wattage. The MZ23-SU0 wants a 24-pin, two 8-pin EPS and a 6-pin aux; the four cards want a 12V-2x6 each. Count the plugs before you count the watts.</p>

## What the MZ23-SU0 needs

Verified against the datasheet and manual (Internal I/O and PSU Connectors), not
the product page.

| Connector | Purpose | Qty |
|---|---|---:|
| 24-pin ATX (`ATX1`) | main | 1 |
| 8-pin ATX 12V (`P12V_AUX1`, `P12V_AUX2`) | CPU (EPS) | **2** |
| 6-pin ATX 12V (`P12V_PCIE`) | board aux — **mandatory** | **1** |
| Molex (`FAN1_PWR`) | fan rail, only if a hub is used | 1 |

The 6-pin `P12V_PCIE` is easy to miss: the manual's power-connector section
states that the 12 V connector feeds the CPU and that **the system will not
start without it**.

## What the GPUs need

| Connector | Qty |
|---|---:|
| 12V-2x6 (16-pin) per R9700 | **4** |

Risers carry data only, so every card takes its 12 V from its own 16-pin feed.
Nothing is shared, nothing needs a splitter.

## The count

| Rail | Needed | Note |
|---|---:|---|
| 24-pin | 1 | |
| EPS 8-pin | 2 | |
| PCIe 6-pin | 1 | board aux |
| 12V-2x6 | **4** | one per card |
| Molex | 1 | fan hub, optional |
| SATA | — | the board has no SATA ports |

A 1600 W unit with **2× EPS, 8× PCIe 8-pin, 2× native 16-pin** covers this: two
cards on the native 16-pin, two on 2×8-pin→16-pin adapters (4 of the 8 PCIe
cables), leaving 4 PCIe 8-pin for the board aux. The Gigabyte GP-UD1600PM PG5
is one such unit and is the one priced in this book.

!!! danger "Do not split a 12V-2x6"
    Two 300 W cards from one output is not a supported configuration. One feed
    per card.

!!! warning "Adapter limit is 300 W"
    A 2×8-pin→12V-2x6 adapter is rated 300 W by PCI-SIG — exactly the card's
    TDP. That is why the build defaults to a **210 W cap**, which also matches
    the engine's own reference configuration.

## Watts

| | Stock (300 W/card) | Capped (210 W/card) |
|---|---:|---:|
| 4× R9700 | 1 200 W | 840 W |
| EPYC 9355P | 280 W | 280 W |
| 12× DDR5 RDIMM | 96 W | 96 W |
| Board, BMC, NIC, VRM loss | 40 W | 40 W |
| 2× M.2 | 20 W | 20 W |
| Fans | 30 W | 30 W |
| **Total** | **≈1 666 W** | **≈1 306 W** |
| **PSU** | **2 000 W** | **1 600 W** |

The CPU is not idle in this build: the expert pool runs across the 32 cores
during decode, so the 280 W is a sustained load, not a burst. Size the cooler
for continuous output.
