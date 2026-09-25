---
type: concept
title: "Frame Isolation"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - frc-rules
  - concept
status: developing
related:
  - "[[Wire and Breaker Sizing]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: basic
domain: "FRC electrical"
aliases:
  - "R611"
  - "The frame is not a wire"
---

# Frame Isolation

**R611 (2026), "The ROBOT frame is not a wire":** all wiring and electrical devices must be isolated from the frame.

**Inspection test:** there must be **>120 Ω** between either post of the Anderson connector on the PD and any point on the robot.

> [!warning] Outdated value in older guides
> Many older guides and checklists say **3 kΩ**. The 2026 manual says **>120 Ω**, verified against the official manual text.

## Common isolation failures

- Legal motor controllers with metal cases are already isolated and may mount straight to the frame.
- **Watch out for:**
  - some cameras
  - encoders
  - IR sensors
  - decorative lights
- These can have grounded or conductive (including conductive-plastic) enclosures. Insulate them from the frame.
