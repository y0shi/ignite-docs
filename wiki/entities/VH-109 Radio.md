---
type: entity
title: "VH-109 Radio"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - entity
status: developing
related:
  - "[[Radio Power Redundancy]]"
  - "[[SystemCore]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: product
role: "Vivid-Hosting FRC robot radio (field link)"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
aliases:
  - "VH-109"
  - "VH109"
---

# VH-109 Radio

The FRC robot radio from Vivid-Hosting. It is still the documented field link with [[SystemCore]] in 2027.

- **Input:** 4.5–19 V; accepts unregulated battery voltage.
- **Ports:** the RIO port accepts passive PoE. AUX1 and AUX2 can pass PoE out (DIP switches; off by default).
- **Firmware:** 2.0.0 (January 2026) added "Enable SystemCore Mode."

## Power rules (2026)

- **R616:** power the radio with passive PoE into the RIO port from a PD, and/or 12 V wired directly from a PD. **The VRM and REV RPM are no longer legal** for the VH-109.
- **R617:** use a non-switched PD channel with a **10 A** breaker/fuse and no other load on it.

Wiring practice is covered in [[Radio Power Redundancy]].
