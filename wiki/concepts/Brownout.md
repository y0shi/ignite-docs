---
type: concept
title: "Brownout"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - concept
status: developing
related:
  - "[[FRC Battery Management]]"
  - "[[SystemCore]]"
  - "[[Wire and Breaker Sizing]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
complexity: intermediate
domain: "FRC electrical"
---

# Brownout

**What it is:** battery voltage sags under high current, and the controller disables outputs to protect itself.

| Controller | Trip | Restore | Behavior |
|---|---|---|---|
| roboRIO 2 | 6.8 V (configurable in code) | — | outputs disabled |
| [[SystemCore]] | **6.3 V** (configurable) | 7.5 V | PWM and digital outputs disabled |

> [!note] Source note
> The roboRIO 6.8 V figure is background knowledge, not from this session's searches. The SystemCore figures come from the alpha spec, where brownout protection was disabled in the alpha image.

## Causes

- a weak or deeply discharged battery (see [[FRC Battery Management]])
- loose lugs
- long 6 AWG leads (see [[Wire and Breaker Sizing]])
- too many motors pulling at once

## Prevention

- good batteries and tight connections
- short main leads
- current limits in code

SystemCore's lower trip point rides through deeper sags, but outputs still cut out.
