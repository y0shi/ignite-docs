---
type: entity
title: "SystemCore"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - entity
status: developing
related:
  - "[[CAN FD]]"
  - "[[Multi-Bus CAN Architecture]]"
  - "[[CANivore]]"
  - "[[WPILib]]"
  - "[[Brownout]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
entity_type: product
role: "FRC/FTC robot controller replacing the roboRIO from the 2027 season"
first_mentioned: "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
aliases:
  - "Systemcore"
---

# SystemCore

The robot controller that replaces the roboRIO in FRC for 2027. It is built by Limelight and uses a Raspberry Pi CM5 with an RP2350 handling I/O.

**Price and availability:**
- On sale **Nov 18, 2026** on the FIRST Storefront, one per team at launch
- 4 GB model: $550
- 2 GB model: later

## Wiring-relevant specs

| Item | Detail |
|---|---|
| CAN | 5 buses, `can_s0`–`can_s4`; FD-capable up to 8 Mbps; **120 Ω termination built in at each port**; 2-pin Molex SL |
| Power | **Only** through the Micro-Fit+ Pwr/Bridge port (a MotionCore cable, or the included Micro-Fit→XT30 cable). Needs raw battery voltage; "do not use a regulator" |
| Input range | 5–26 V nominal, 4.5–35 V survivable, about 6 W idle / 40 W max |
| Brownout | 6.3 V trip, 7.5 V restore, configurable. PWM and digital outputs are disabled during brownout. See [[Brownout]] |
| I/O | 6 SmartIO (3-pin Molex SL). No relay, SPI, MXP, or analog out. 3.3 V rail is 1 A total, shared |
| I2C | 2 ports; **SDA and SCL are swapped vs the roboRIO** (Qwiic pinout) |
| Other | Built-in IMU, OLED status display, 4× USB 3.0, 1 GbE, M.2 A+E slot, RSL port (10 V / 100 mA) |

## Gotchas

- **Connectors changed in December 2025.** The Weidmüller power and CAN connectors were replaced by Micro-Fit+ and Molex SL. Don't build harnesses from the alpha docs.
- **Digital I/O pull direction:** alpha units pull down, beta and later units pull up.
- **The Bridge port and CAN port 0 are physically the same** (per Thad_House, [[WPILib]]).
- **The 2027 WPILib wiring guide still describes the roboRIO.** No official SystemCore wiring guide exists yet.

See [[Multi-Bus CAN Architecture]] for how to use the five buses.
