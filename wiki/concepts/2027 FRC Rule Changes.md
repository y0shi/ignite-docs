---
type: concept
title: "2027 FRC Rule Changes"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-rules
  - frc-electrical
  - concept
status: seed
related:
  - "[[SystemCore]]"
  - "[[CANivore]]"
  - "[[FRC Battery Management]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: basic
domain: "FRC rules"
aliases:
  - "2027 rule preview"
---

# 2027 FRC Rule Changes

From FIRST's **2027 Event & Robot Rule Preview, Part 1** (Aug 31, 2026). This is a preview, not the manual.

## Electrical changes

- **[[SystemCore]] replaces the roboRIO.**
- **Motor cap: 18 motors.** About 10% of 2026 teams used more. FIRST's stated goals are lower cost and no more "secondary power distribution or complex wire harnesses."
- **[[CANivore]]:** legal as an extra bus in 2027 (interim). In 2028 every bus must originate at SystemCore; the CANivore can only be a node.
- **Removed controllers:** original Talon / Talon SR and VictorSP.
- **BAG and Mini-CIM:** off the explicit motor list (discontinued). They're still usable as generic brushed motors behind 20 A breakers.
- **USB batteries:** any COTS pack of 100 Wh or less. The voltage/current requirement is gone.
- **New thermal rule:** no heating or cooling components for advantage (breakers, batteries).
- **Pneumatics:** unchanged.

> [!gap] Still pending
> - Rule Preview Part 2 (more approved devices).
> - Full 2027 R6xx text, including how the controller must be powered.
>
> Update this page after kickoff (January 2027).
