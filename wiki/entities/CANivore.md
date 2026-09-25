---
type: entity
title: "CANivore"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - entity
status: developing
related:
  - "[[CTR Electronics]]"
  - "[[CAN FD]]"
  - "[[SystemCore]]"
  - "[[2027 FRC Rule Changes]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: product
role: "CTRE USB-to-CAN-FD adapter that adds CAN buses to the robot controller"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
---

# CANivore

[[CTR Electronics]]' USB-to-CAN-FD adapter (P/N 21-678682, WCP-1522).

- **2026:** legal under R717 as an additional bus. Motor controllers may run on it.
- **Termination:** a programmable 120 Ω resistor, turned on in Phoenix Tuner X.
- **Topology:** CTRE caps branches at about 12 in because of FD bit rates.

## Legality timeline

| Season | Status |
|---|---|
| 2026 | Legal as an extra bus on the roboRIO |
| 2027 | Legal as an extra bus on [[SystemCore]]. This is an interim allowance while SystemCore's native CAN-FD compatibility matures |
| 2028 | **Cannot originate a bus.** It stays legal only as a node on a native SystemCore bus (e.g., for coprocessors) |

**Recommendation for Phoenix Pro / Kraken teams: keep one for 2027.** CTRE hasn't said which Pro or FD features will run on the native SystemCore buses. See [[CAN FD]].
