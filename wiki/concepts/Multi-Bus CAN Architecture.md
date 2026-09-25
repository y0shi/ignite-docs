---
type: concept
title: "Multi-Bus CAN Architecture"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - can-bus
  - systemcore
  - concept
status: developing
related:
  - "[[SystemCore]]"
  - "[[CAN Bus Wiring]]"
  - "[[CAN FD]]"
  - "[[CANivore]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: intermediate
domain: "FRC electrical"
aliases:
  - "CAN bus segmentation"
---

# Multi-Bus CAN Architecture

With five native buses on [[SystemCore]], the 2027 robot stops being one long CAN chain. FIRST describes it as "near point-to-point CAN wiring for simple robots," and a way for complex robots to "segment their robot onto different buses for reliability."

## Rules of thumb

**1. One terminator per bus, at the far end.** The SystemCore end is already terminated. Don't leave the [[REV Power Distribution Hub]] switch on if the PDH sits mid-bus.

**2. Split buses by failure domain.** Example plan:

| Bus | Devices |
|---|---|
| s1 | left drive |
| s2 | right drive |
| s3 | mechanisms |
| s4 | PDH and misc |

A bad crimp then kills one subsystem, not the robot.

**3. Keep drivetrain devices off `can_s0` until it's proven.** Port 0 is physically shared with the Bridge (power) port. It's unclear whether it stays independent when you power through the XT30 adapter.

**4. Color-code each bus.**
- CTRE multi-color wire: green is always CAN-L, and the CAN-H color varies (brown, orange, light blue, purple, grey, white, pink; yellow stays the default). FIRST says it's legal for at least 2027.
- Alternative: keep yellow/green conductors and use colored outer jackets.
- Either way, pick one scheme and document it.

**5. A [[CANivore]] can originate a sixth-plus bus in 2027 only.** In 2028 it can only be a node on a native bus.

> [!note] Why fewer devices per bus helps
> Shorter buses mean fewer connectors in series, less stub risk at [[CAN FD]] bit rates, and lower per-bus utilization.
