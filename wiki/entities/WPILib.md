---
type: entity
title: "WPILib"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-software
  - entity
status: seed
related:
  - "[[SystemCore]]"
  - "[[CAN Bus Wiring]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: organization
role: "FRC software library and official documentation (docs.wpilib.org)"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
---

# WPILib

The official FRC control-system library and docs.

## Electrical-relevant docs

- **CAN Wiring Basics:** daisy chain, yellow = CAN-H, green = CAN-L. The roboRIO and PDP have built-in termination. See [[CAN Bus Wiring]].
- **SystemcoreTesting repo** (github.com/wpilibsuite/SystemcoreTesting), the best current primary source for [[SystemCore]]:
  - how to power it (beta units: Micro-Fit Bridge port only, no regulator)
  - the I2C SDA/SCL swap
  - the digital I/O pull direction
  - CTRE Phoenix notes
- **Gap as of 2026-09-25:** `docs.wpilib.org/en/2027/` "Intro to FRC Robot Wiring" still describes the roboRIO. There is no SystemCore wiring guide yet.

Thad_House, a WPILib developer, confirmed on [[Chief Delphi]] that SystemCore's Bridge port and CAN port 0 are physically the same.
