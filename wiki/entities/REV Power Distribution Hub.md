---
type: entity
title: "REV Power Distribution Hub"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - entity
status: seed
related:
  - "[[Wire and Breaker Sizing]]"
  - "[[CAN Bus Wiring]]"
  - "[[Multi-Bus CAN Architecture]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: product
role: "Main power distribution device (PD)"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
aliases:
  - "PDH"
  - "REV-11-1850"
---

# REV Power Distribution Hub (PDH)

A legal main PD under R609 (REV-11-1850). The other legal PDs are the CTRE PDP and PDP 2.0 and the AndyMark AMPD.

**Channels:**
- 20 × 40 A channels
- 4 low-current 15 A channels, one of them switchable

**Rules that apply:**
- R617: the radio gets a non-switched channel with a 10 A breaker. See [[VH-109 Radio]].
- R618: one wire per terminal.

**CAN termination switch:** turn it on **only** when the PDH is the physical end of its bus.
- roboRIO era: the classic chain runs roboRIO → devices → PDH.
- 2027 with [[SystemCore]]: the PDH can be the far end of one of the five buses, or sit on its own bus. See [[Multi-Bus CAN Architecture]].
