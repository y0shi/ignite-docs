---
type: source
title: "FRC Electrical Best Practices + 2027 SystemCore Wiring & CAN Changes"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - source
status: developing
related:
  - "[[SystemCore]]"
  - "[[CAN Bus Wiring]]"
  - "[[Multi-Bus CAN Architecture]]"
  - "[[2027 FRC Rule Changes]]"
sources:
  - "[[.raw/2026-09-25/frc-electrical-best-practices-2027-systemcore.md]]"
source_type: data
author: "Claude (research router, fallback workflow) for FRC 6829"
date_published: 2026-09-24
url: ""
confidence: medium
key_claims:
  - "Most robot electrical failures are mechanical: lugs, crimps, strain relief, batteries, radio power."
  - "2026 rules: 6 AWG main path, breaker-matched wire table, >120 Ω frame isolation, radio on a dedicated 10 A PD channel."
  - "SystemCore has 5 CAN-FD-capable buses, each with built-in 120 Ω termination at the controller end."
  - "SystemCore is powered only through a Micro-Fit+ Bridge port at raw battery voltage; CAN moved to 2-pin Molex SL."
  - "CANivore is legal as an extra bus in 2027 only; in 2028 all buses must originate at SystemCore."
  - "2027 caps robots at 18 motors."
---

# FRC Electrical Best Practices + 2027 SystemCore Wiring & CAN Changes

A research synthesis from 25 cited sources: the FIRST game manual and blog, WPILib, vendor docs, and 12 [[Chief Delphi]] threads. It covers:
- general FRC electrical practice
- the 2027 move from the roboRIO to [[SystemCore]]

Confidence is **medium**. Several SystemCore details come from alpha/beta docs, and the 2027 wiring rules are not yet published.

## Key takeaways

**Reliability is mechanical.** See [[Connector and Crimp Quality]], [[FRC Battery Management]], and [[Radio Power Redundancy]].

**2026 rules baseline:**
- [[Wire and Breaker Sizing]] (R609, R622)
- [[Frame Isolation]] (R611, >120 Ω)
- radio power (R616/R617), see [[VH-109 Radio]]

**CAN wiring:**
- daisy chain
- exactly two 120 Ω terminators, one at each end
- a powered-off meter reading of about 60 Ω means both are present
- keep average bus load under about 80%

See [[CAN Bus Wiring]].

**SystemCore:**
- five buses, each already terminated at the controller, so you add one terminator per bus at the far end
- split buses by subsystem and color-code them

See [[Multi-Bus CAN Architecture]].

**CAN-FD support on SystemCore's native buses is not proven for 2027.** FIRST kept [[CANivore]] legal for one more year for exactly that reason. See [[CAN FD]].

**Rule changes** (18 motors, removed controllers, thermal rule, USB batteries): see [[2027 FRC Rule Changes]].

**[[Brownout]]:** SystemCore trips at 6.3 V (configurable) vs the roboRIO's 6.8 V.

## Open questions (as of 2026-09-25)

> [!gap] Not yet answerable
> - 2027 R6xx text for how the controller must be powered (channel, breaker, gauge).
> - A WPILib SystemCore wiring guide. The 2027 wiring page still shows the roboRIO.
> - Per-vendor native CAN-FD support on SystemCore buses ([[CTR Electronics]], REV, Redux).
> - Whether `can_s0` is independent when you power through the XT30 adapter. The Bridge port and CAN port 0 are physically the same.
> - 2027 Rule Preview Part 2.

Revisit after the 2027 game manual comes out (January 2027).

## Internal disagreements in the source

- **Ferrules:**
  - 2019 CD advice: optional
  - 2024 CD practice: mandatory
  - SystemCore alpha spec: requires ferruled power and CAN wire
- **Battery internal-resistance thresholds** depend on the tester. See [[FRC Battery Management]].
- **Multi-bus identification:** colored conductors (CTRE) vs colored jackets (teams).
