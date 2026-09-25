---
type: concept
title: "CAN Bus Wiring"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - can-bus
  - concept
status: developing
related:
  - "[[Multi-Bus CAN Architecture]]"
  - "[[CAN FD]]"
  - "[[REV Power Distribution Hub]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: intermediate
domain: "FRC electrical"
aliases:
  - "CAN termination"
  - "CAN topology"
---

# CAN Bus Wiring

## Topology

**Daisy chain.** Start at the controller, go in and out of each device in turn, and end at a terminator.
- Star or stub layouts only if you have to. Keep each stub under about 6 in (ISO 11898 allows 0.3 m unterminated).
- **Never put a stub on a stub.**
- CTRE caps [[CANivore]] branches at about 12 in.
- Higher bit rates shrink the stub budget, so roboRIO-era shortcuts can fail on [[CAN FD]].

## Termination

**Exactly two 120 Ω resistors, one at each physical end of the bus.**

Test with power off: measure across CAN-H and CAN-L.
- about 60 Ω: correct
- about 120 Ω: one terminator is missing
- near 0 Ω: a short

Where the terminators live:
- **roboRIO era:** built into the roboRIO, plus the PDP/PDH jumper when the PD is at the end.
- **[[SystemCore]] era:** built in at every SystemCore port, so add one terminator at the far end of each bus.

## Wire and connections

- At least 22 AWG twisted pair. **Yellow = CAN-H, green = CAN-L.**
- Crimp, don't just twist. See [[Connector and Crimp Quality]].

## Bus health

- **Average utilization under about 80%.** If you're over, move devices to another bus or reduce status-frame rates.
- Unique device IDs, never 0. Firmware matched to the vendor library.
- **To find a fault:** check continuity and shorts with a meter, then disconnect devices one at a time.
