---
type: concept
title: "CAN FD"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - can-bus
  - concept
status: developing
related:
  - "[[CAN Bus Wiring]]"
  - "[[CANivore]]"
  - "[[SystemCore]]"
  - "[[CTR Electronics]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: intermediate
domain: "FRC electrical"
aliases:
  - "CAN-FD"
  - "CAN Flexible Data-rate"
---

# CAN FD

CAN with Flexible Data-rate: bigger payloads and a faster data phase than classic CAN 2.0B. The roboRIO's 1 Mbps bus is CAN 2.0.

| Platform | CAN FD in FRC |
|---|---|
| [[CANivore]] | FD today |
| [[SystemCore]] native ports | FD-capable hardware (up to 8 Mbps) |

## Wiring consequence

At FD bit rates the stub budget shrinks. Short star layouts that worked on the roboRIO may fail. **Wire true daisy chains.** See [[CAN Bus Wiring]].

## 2027 reality check

> [!gap] Native FD on SystemCore not proven
> FIRST kept the CANivore legal for 2027 specifically to allow "additional time for development and testing of Systemcore CAN-FD compatibility." [[CTR Electronics]] hasn't said which Phoenix Pro / FD features will run on native SystemCore buses.

**Recommendation for teams that depend on FD timing or Pro features: plan on a CANivore for 2027.**
