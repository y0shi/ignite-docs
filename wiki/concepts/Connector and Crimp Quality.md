---
type: concept
title: "Connector and Crimp Quality"
created: 2026-09-25
updated: 2026-09-25
tags:
  - frc-electrical
  - concept
status: developing
related:
  - "[[CAN Bus Wiring]]"
  - "[[Radio Power Redundancy]]"
  - "[[SystemCore]]"
  - "[[Chief Delphi]]"
sources:
  - "[[FRC-Electrical-Best-Practices-2027-SystemCore]]"
  - "[[Silver-Cymbal-Crimp-Seam-Up-or-Down]]"
complexity: basic
domain: "FRC electrical"
aliases:
  - "strain relief"
  - "ferrules"
---

# Connector and Crimp Quality

**Robots die from terminations, not from electrical theory.**

## 1918's zero-failure routine (CD, Apr 2024)

They reported "exactly zero electrical related failures this season" from this routine:

1. Tug-test every crimp before the retention clip goes on.
2. Confirm every terminal is fully seated.
3. Have a **different** team member do a second inspection.

## Practices

- **Strain relief within inches of every connector.** Use stick-on zip-tie mounts.
- **Hot-melt glue** on Weidmüller, DuPont, and barrel connectors to stop vibration from walking them loose.
- **Anderson Powerpole (PP45)** at subsystem boundaries. Zip-tie mated pairs shut so they can't separate.
- **Lever nuts or WAGO blocks** for splicing 18 AWG and up, instead of soldering.
- **Bonded red/black zipcord** (matte finish) for easy tracing.
- **Plan wiring during mechanical design.** Use energy chain at moving joints.

## Crimp technique

- **Barrel seam orientation in the die** is a common hidden cause of bad crimps on closed-barrel terminals. See [[Silver-Cymbal-Crimp-Seam-Up-or-Down]] (transcript pending, low confidence).
- Match wire gauge to the terminal and die size.

## Tools

- one good crimper per connector family (e.g., Powerwerx TRIcrimp for Powerpoles)
- Greenlee 10–24 AWG strippers
- flush cutters that **never** touch wire larger than 18 AWG

## Ferrules: disputed

> [!contradiction] Ferrules: optional or mandatory?
> - 2019 CD advice: "not particularly hard to use without them."
> - 2024 practice (1918): no bare wire in any spring or lever terminal.
> - The [[SystemCore]] alpha spec *required* ferruled 18 AWG power and 22 AWG CAN wire.
>
> Recommendation: ferrule everything that goes into a spring or lever terminal.

## 2027 connector families to stock

- **Molex SL**, 2-, 3-, and 4-pin, with 22 AWG gold terminals: CAN, SmartIO, I2C, RSL
- **Molex Micro-Fit+** (gold only): SystemCore power

**Get a crimper rated for both.**
