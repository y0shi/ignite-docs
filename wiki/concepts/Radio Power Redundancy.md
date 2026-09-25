---
type: concept
title: "Radio Power Redundancy"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - radio
  - concept
status: developing
related:
  - "[[VH-109 Radio]]"
  - "[[Connector and Crimp Quality]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: basic
domain: "FRC electrical"
aliases:
  - "dual-feed radio"
---

# Radio Power Redundancy

**Recommendation: feed the [[VH-109 Radio]] both ways at once.**
- passive PoE into the RIO port
- 12 V wired to the radio's power input

Vivid-Hosting calls this "the recommended method." R616 allows it.

## Why

A CD user reported PoE dropouts when the robot got bumped. A lost radio means a dead robot for the rest of the match.

## Constraints

- **Both inputs must come from the SAME source at the same voltage.** Use the same dedicated 10 A PD channel (R617).
- **Don't:**
  - use the RPM and 12 V at the same time (damages the radio; the RPM isn't legal for the VH-109 anyway)
  - plug a switch into the RIO port without an injector (it can back-feed)

## Mounting

- Point the Ethernet connection up or sideways so the cable doesn't fight gravity.
- Use cut-to-length Cat6 with good RJ45s.
- Add strain relief close to the jack.
