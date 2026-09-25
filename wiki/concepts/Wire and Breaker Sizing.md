---
type: concept
title: "Wire and Breaker Sizing"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - frc-rules
  - concept
status: developing
related:
  - "[[REV Power Distribution Hub]]"
  - "[[Frame Isolation]]"
  - "[[FRC Battery Management]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: basic
domain: "FRC electrical"
aliases:
  - "R622"
  - "R609"
  - "wire gauge"
---

# Wire and Breaker Sizing

## Main power path (R609)

- **Order:** battery → a single pair of Anderson SB connectors → a single **120 A** surface-mount main breaker → a single PD.
- **All of it in 6 AWG copper or larger.**
- **Placement:**
  - R612: the main breaker must be quickly and safely reachable from outside the robot.
  - R613: the PD, its wiring, and all breakers must be visible.
- **Recommendation: use a Bussmann CB185/CB285 main breaker.** The Optifuse is legal, but FRCElectrical.org strongly discourages it.

## Branch circuits (R622, minimum wire)

| Protection | Min wire |
|---|---|
| 31–40 A breaker | 12 AWG |
| 21–30 A breaker | 14 AWG |
| 6–20 A breaker / 11–20 A fuse | 18 AWG |
| 5 A breaker, 10 A fuse, VRM 2 A | 22 AWG |
| VH-109 passthrough | 24 AWG (Cat5e+, 2 pairs) |
| roboRIO PWM / 1 A fuse | 26 AWG |

## Related rules

- **R617:** the radio gets its own 10 A channel. See [[VH-109 Radio]].
- **R618:** one wire per PD terminal. Splice before the PD, not at it.
- **R624 wire colors:**
  - positive: red, yellow, white, brown, or black-with-stripe
  - negative: black or blue

## Voltage drop

At 100 A, 6 AWG drops about 0.1 V per foot, and that counts both conductors. **Keep main leads short.** See [[Brownout]].
