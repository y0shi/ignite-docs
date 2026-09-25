---
title: Hot Cache
tags: [knowledge-graph]
---
# Hot Cache

Recent ingest context. Read this first before re-reading full pages.

## 2026-09-25: capture drain, crimp video

- [[Silver-Cymbal-Crimp-Seam-Up-or-Down]]: a video on barrel seam orientation in the crimp die. It is linked from [[Connector and Crimp Quality]].
- **The transcript is missing** (YouTube returned HTTP 429). Fill in the page after watching the video.

## 2026-09-25: FRC electrical + 2027 SystemCore

**Source:** [[FRC-Electrical-Best-Practices-2027-SystemCore]]. It seeded the whole FRC-electrical cluster: 7 entities and 10 concepts.

**Key facts:**
- [[SystemCore]] has 5 CAN buses, each with 120 Ω termination built in at the controller. Add one terminator per bus at the far end.
- SystemCore takes power only through a Micro-Fit+ port, at raw battery voltage (no regulator).
- CAN connectors are now 2-pin Molex SL. The I2C SDA/SCL pinout is swapped vs the roboRIO. There are 6 SmartIO ports.
- The [[CANivore]] can add a bus in 2027 only; in 2028 it's a node only. Native [[CAN FD]] on SystemCore is not proven.
- 18-motor cap for 2027. See [[2027 FRC Rule Changes]].
- [[Frame Isolation]] is **>120 Ω**, not the 3 kΩ in older guides.

**Open gaps to revisit after the January 2027 manual:**
- 2027 controller-power rule
- a WPILib SystemCore wiring guide
- vendor FD support
- whether `can_s0` is independent from the Bridge (power) port
- Rule Preview Part 2
