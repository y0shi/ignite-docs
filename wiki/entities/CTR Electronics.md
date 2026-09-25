---
type: entity
title: "CTR Electronics"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-vendor
  - entity
status: seed
related:
  - "[[CANivore]]"
  - "[[CAN FD]]"
  - "[[Multi-Bus CAN Architecture]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: organization
role: "FRC vendor: Kraken/TalonFX motor controllers, CANcoder, Pigeon 2, CANivore, Phoenix 6 software"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
aliases:
  - "CTRE"
---

# CTR Electronics (CTRE)

Makers of TalonFX / Kraken, CANcoder, Pigeon 2, the [[CANivore]], and the Phoenix 6 software stack.

## 2027 status on SystemCore

- **Phoenix 6 works** on native [[SystemCore]] buses (`CANPort.CAN_S*`) and on CANivores. Phoenix 5 is unavailable.
- **CTRE has not publicly committed to which Phoenix Pro / FD features run natively.** A Chief Delphi thread from March 2026 got no vendor answer. See [[CAN FD]].
- **Multi-color CAN wire:** CTRE sells it with green always as CAN-L and the CAN-H color varying per bus. FIRST confirmed it is legal for at least 2027. See [[Multi-Bus CAN Architecture]].
- The original Talon / Talon SR are removed from the 2027 legal list. See [[2027 FRC Rule Changes]].
