---
type: concept
title: "FRC Battery Management"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - battery
  - concept
status: developing
related:
  - "[[Brownout]]"
  - "[[Wire and Breaker Sizing]]"
  - "[[Chief Delphi]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: basic
domain: "FRC electrical"
aliases:
  - "battery care"
---

# FRC Battery Management

**Most "electrical problems" at events are battery or battery-connection problems.**

## Connections first

- **Loose lugs are the first suspect, not the battery.** Check both the battery leads and the breaker/PD lugs.
- Use lock or star washers on battery bolts. Crimp the 6 AWG properly.
- Don't carry batteries by their cables.

## Testing

- **Internal resistance (Battery Beak–style tester):** a good battery reads about 0.012–0.018 Ω. Pull anything over about 0.025 Ω from match use.
- **Load-test too.** A battery can pass the Beak and still collapse under load. A 100 A automotive load tester or a CBA-style discharge test catches it.

> [!note] IR numbers depend on the tester
> JaredL's 2025 bench test measured 0.025–0.045 Ω across brands with a different method. Compare batteries on the same instrument, never across tools.

## Care

- **Never drain below about 11.5 V resting.** Deep discharge to 6–7 V can kill a battery in one long programming session.
- In practice sessions, disable or lock out the robot below about 11 V.
- Keep batteries on chargers when idle.
- Give new batteries 2–3 break-in discharge cycles.
- Run an annual capacity test.
- Expect 1–2 seasons of competition life. Rotate old batteries to practice.
- Track each battery by ID.

## Brand data (JaredL, Nov 2025, 5 brands, 200+ cycles each)

**Judge batteries by capacity under load, not by the label.**

| Brand | Capacity at 36 A |
|---|---|
| MK Powered | 15.59 Ah (best) |
| Duracell | 13.15 Ah (despite the top 20-hr rating) |
| Mighty Max | 11.31 Ah (worst) |

## 2027

- **New thermal rule:** no heating or cooling of batteries or breakers for advantage.
- **USB batteries:** any COTS pack of 100 Wh or less is legal.

See [[2027 FRC Rule Changes]].
