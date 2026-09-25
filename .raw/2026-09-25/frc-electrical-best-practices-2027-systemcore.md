---
title: FRC Electrical Best Practices + 2027 SystemCore Wiring & CAN Changes
type: source
created: 2026-09-24
status: draft
audience: students
tags: [frc, electrical, wiring, can-bus, systemcore, 2027, battery, research]
---

# FRC Electrical Best Practices + 2027 SystemCore Wiring & CAN Changes

*Generated: 2026-09-24 | Routed: fallback (general research, thorough tier)*

## TL;DR

The basics of FRC electrical work haven't changed. Robots still die from loose battery lugs, bad crimps, missing strain relief, tired batteries, and radios that lose power in a hit, not from exotic failures. The 2026 rules are the baseline: 6 AWG main path, a breaker-matched wire table, >120 Ω frame isolation, and radio power from the PD on a dedicated 10 A breaker.

For 2027, the roboRIO is replaced by **SystemCore**, and the wiring changes are real:
- **Five native CAN-FD buses.** Each has 120 Ω termination built in at the SystemCore end.
- **Power only through a Molex Micro-Fit+ "Bridge" port**, at raw battery voltage with no regulator.
- **CAN on 2-pin Molex SL connectors.**
- **I2C SDA/SCL pinout is swapped** relative to the roboRIO.
- **Six SmartIO ports.** There are no relay, SPI, or MXP ports.
- **An 18-motor cap.**
- **CANivore is legal as an extra bus in 2027 only.** In 2028 every bus must originate at SystemCore.

**The biggest open risk** is that WPILib's 2027 "Intro to Robot Wiring" page still describes the roboRIO. There is no official SystemCore wiring guide yet, so some details below come from alpha/beta docs and may change before kickoff.

---

## 1. Core power-wiring practices (the stuff that still matters most)

### 1.1 The rules baseline (2026 manual, carrying into 2027 unless changed)

Quoted from the official 2026 Game Manual [1]:

- **R609, main power path:** battery → a single pair of Anderson SB connectors → a single 120 A surface-mount main breaker → a single PD (PDP, PDP 2.0, REV PDH, or AndyMark AMPD), all in **6 AWG copper or larger**.
- **R611, "The ROBOT frame is not a wire":** compliance is checked by observing **>120 Ω** between either APP post and any point on the robot. (Older guides say 3 kΩ; that value is outdated.) Some cameras, encoders, IR sensors, and decorative lights have grounded or conductive cases and must be isolated from the frame.
- **R612:** the main breaker must be quickly and safely accessible from outside the robot.
- **R613:** the PD, its wiring, and all breakers must be visible for inspection.
- **R617:** the radio power source goes on a **non-switched PD channel with a 10 A breaker/fuse and no other load**.
- **R618:** one wire per PD terminal. Splice before the PD if you need to split power.
- **R622 wire table (minimums):**

| Protection | Min wire |
|---|---|
| 31–40 A breaker | 12 AWG |
| 21–30 A breaker | 14 AWG |
| 6–20 A breaker / 11–20 A fuse | 18 AWG |
| 5 A breaker, 10 A fuse, VRM 2 A | 22 AWG |
| VH-109 passthrough | 24 AWG (Cat5e+ with 2 pairs) |
| roboRIO PWM / 1 A fuse | 26 AWG |

- **R624 colors:** positive wire is red, yellow, white, brown, or black-with-stripe. Negative is black or blue.

### 1.2 Community best practices

**Build the electrical layout during mechanical design, not after.** Keep runs short, use energy chain at moving joints, and label wire endpoints. (Drakxii, *Robust Electrical and Wiring Practices*, CD, Apr 2024 [2])

**Validate every termination.** 1918's mentor reported "exactly zero electrical related failures this season" from this routine:
- tug-test every crimp before the retention clip goes on
- confirm every terminal is fully seated
- have a *different* team member do a second inspection

(JimB1918 [2])

**Strain relief within inches of every connector.** Stick-on zip-tie mounts are the usual method. 1918 adds hot-melt glue on Weidmüller, DuPont, and barrel connectors to stop vibration from walking them loose. [2]

**Bonded red/black zipcord** makes wiring easy to trace. Keep 10 AWG and 18 AWG spools and buy the matte finish. [3]

**Anderson Powerpole (PP45)** at subsystem boundaries, such as an elevator or intake, makes swapping quick. Zip-tie mated Powerpoles shut so they can't separate. [2][3]

**Lever nuts and WAGO blocks** for splicing 18 AWG and up, instead of soldering. [4]

**Ferrules are disputed:**
- 2019 CD advice: "not particularly hard to use without them" [3]
- 2024 advice from 1918: no bare wire in any WAGO, Weidmüller, or lever lock [2]
- The SystemCore alpha spec *requires* ferruled 18 AWG (power) and 22 AWG (CAN) into its Weidmüller connectors [5]

**Recommendation: ferrule everything that goes into a spring or lever terminal.** Newer practice, and the vendor spec, both point that way.

**Main breaker:** use the Bussmann CB185/CB285. FRCElectrical.org "strongly" discourages the Optifuse, which is legal, over reliability issues. [4]

**Tools:** one good crimper per team (Powerwerx TRIcrimp for Powerpoles), Greenlee 10–24 AWG strippers, and flush cutters that never touch wire larger than 18 AWG. [3]

---

## 2. Batteries and brownouts

Most "electrical problems" at events are battery or battery-connection problems.

**Loose lugs are the first suspect, not the battery.** "Check the lugs on the battery leads and the lugs on the breaker panel." Use lock or star washers on battery bolts. [6][7]

**Keep main leads short.** At 100 A, each foot of 6 AWG drops about 0.1 V, and that counts both conductors: 3 ft of extra lead means 8 ft total, or about 0.4 V lost per 100 A. [7]

**Internal resistance.** A good battery measures about 0.012–0.018 Ω on a Battery Beak–style tester. Pull anything over about 0.025 Ω from match use. [7]
- A 2025 year-long bench test by JaredL measured higher absolute IR values (0.025–0.045 Ω) with a different method. [8]
- Neither number is wrong; the instruments differ. Compare batteries on the same tester, never across tools.

**Load-test, don't just Beak-test.** A battery can read "good" on a Beak and still collapse under load. A 100 A automotive load tester, or a CBA-style discharge test, catches it. [6][7]

**Never drain below about 11.5 V resting.** Deep discharge to 6–7 V "even [in] a single extended programming session" can destroy a battery. In practice sessions, lock out or disable the robot below about 11 V. [6]

**Rotate and track batteries:**
- keep them on chargers when idle
- give new batteries 2–3 break-in discharge cycles
- run annual capacity tests
- expect 1–2 seasons of competition life
- one reference team buys about 12 new batteries a year and moves last year's to practice

[6]

**Brand choice (JaredL, Nov 2025, 5 brands, 200+ cycles each).** Judge batteries by capacity under load, not by the label. [8]

| Brand | Capacity at 36 A |
|---|---|
| MK Powered | 15.59 Ah (best) |
| Duracell | 13.15 Ah (despite the highest 20-hr rating) |
| Mighty Max | 11.31 Ah (worst) |

**New for 2027:** a "no heating/cooling components for advantage" rule. That means no chilling breakers or warming batteries. Any COTS USB battery of 100 Wh or less is now legal, since the voltage/current requirement was removed. [9]

---

## 3. CAN bus practices (roboRIO era, and why they matter more under CAN-FD)

**Topology is a daisy chain.** Start at the controller, go in and out of each device, and end at a terminator. [10][11]
- Star/stub layouts: keep stubs under about 6 in; ISO 11898 allows up to 0.3 m unterminated. Never put stubs on stubs. [12]
- **What you got away with on the roboRIO's 1 Mbps CAN 2.0 may not work on CAN-FD.** Higher bit rates shrink the allowable stub length. [12] CTRE's CANivore guidance caps branches at about 12 in. [11]

**Termination: exactly two 120 Ω resistors, one at each physical end.** Check with a multimeter across CANH/CANL with power off: about 60 Ω is correct. Readings from 60–120 Ω are "acceptable" per the CD thread, but 120 Ω means one terminator is missing. [11]
- The roboRIO has built-in termination.
- The PDP/PDH has a termination jumper or switch. Leave it on only if the PD is at the end of the bus. [10]

**Wire:** twisted pair, at least 22 AWG, **yellow = CAN-H, green = CAN-L**. [10][11]

**Bus utilization:** keep average load under about 80%. If you're over, move devices to another bus or reduce status-frame rates. [11]

**Device hygiene:**
- unique IDs, never 0
- firmware matched to the vendor library
- non-FD devices kept off FD-only buses

[11]

**Troubleshooting:** run continuity and short checks with a meter, then isolate the fault by disconnecting devices one at a time. [11]

---

## 4. Radio (VH-109) power

**R616 (2026)** allows only two ways to power a VH-109 [1]:
- passive PoE injected into the radio's **RIO port**, straight from a PD
- 12 V wired directly to the radio's power input from a PD

The VRM and REV RPM are **no longer legal** for the VH-109. The VH-109 accepts unregulated battery voltage (4.5–19 V). [13][14]

**Recommendation: use both.** Vivid-Hosting's own docs call PoE plus redundant 12 V "the recommended method." Both inputs must come from the SAME source at the same voltage. [14]
- A CD user reported PoE dropouts when the robot got bumped, which argues for dual feed. [15]
- Mount the radio so the Ethernet cable doesn't fight gravity. Use cut-to-length Cat6 with good RJ45s. [2]

**Don'ts:**
- RPM and 12 V at the same time
- plugging a switch into the RIO port without an injector (it can back-feed)
- AUX PoE out while also powering a PoE camera from an RPM

[14]

**2027:** VH-109 firmware 2.0.0 (Jan 2026) adds "Enable SystemCore Mode." It is still the documented field radio. [16]

---

## 5. What changes in 2027 with SystemCore

### 5.1 Timeline and availability

- **Nov 18, 2026:** on sale via the FIRST Storefront. The 4 GB model is **$550**, one per team at launch. The 2 GB model comes "later this year." [17]
- **Aug 31, 2026:** the 2027 rule preview (Part 1) was published [9]. A Part 2 with more approved devices has been promised, and I could not find it published as of this date.

### 5.2 Hardware at a glance (vs roboRIO)

| | roboRIO 2 | SystemCore |
|---|---|---|
| Compute | Zynq | Raspberry Pi CM5 (quad A76) + RP2350 for I/O [18] |
| CAN | 1 bus, CAN 2.0 | **5 buses (`can_s0`–`can_s4`), FD-capable up to 8 Mbps**, each with **built-in 120 Ω termination** [5] |
| Power in | Weidmüller, from PD | **Only via the Micro-Fit+ Pwr/Bridge port** (MotionCore bridge cable, or the included Micro-Fit→XT30 cable) [19][20] |
| Input range | — | 5–26 V nominal, 4.5–35 V survivable, about 6 W idle / 40 W max, reverse-polarity protected [16][5] |
| Brownout | 6.8 V | **6.3 V, restore at 7.5 V, configurable**; disables PWM and digital outputs [5] |
| GPIO | DIO/PWM/AI/relay/SPI/MXP | **6 SmartIO** (3-pin Molex SL, each can be DIO, PWM, analog in, addressable LED, or quadrature). **No relay, SPI, MXP, or analog out** [16][18] |
| I2C | 1 | 2 ports (4-pin Molex SL), **SDA/SCL swapped vs roboRIO** [19] |
| IMU | none | built in (400 Hz fused yaw) [16] |
| RSL | DIO header | dedicated 2-pin Molex SL, 10 V / 100 mA [5] |
| Ethernet / USB | 1 GbE-ish / 2× USB-A | 1 GbE, 4× USB 3.0-A (2 A shared), USB-C device [16][18] |
| Extra | — | M.2 A+E (Hailo-8 class accelerator), OLED status display [16][18] |

### 5.3 Connector churn: don't build harnesses off alpha docs

- **March 2025 spec:** Weidmüller wire-to-board connectors for power and for all 5 CAN ports. [18]
- **December 2025 update:** FIRST removed the Weidmüller power input. Both FRC and FTC now power SystemCore through the Bridge port's Molex Micro-Fit+, and the CAN connectors moved to 2-pin Molex SL. [20]
- **Also changed in December 2025:** digital I/O switched **from pull-down to pull-up** (matching the roboRIO), and a configuration button was added. [20][19]
  - Alpha units have pull-downs, so a limit switch there shorts SIGNAL to 3.3 V instead of to ground. **Check your unit's hardware revision before wiring switches.** [19]

**Buy crimp stock for Molex SL (22 AWG gold terminals) and Micro-Fit+ (gold only).** Mating part numbers are listed in the spec [5]:
- SL housings 50579402/03/04, terminals 16021115/16021111
- Micro-Fit+ housing 2064610400

### 5.4 Powering SystemCore

> "Do not use a regulator to power the device. It expects to receive battery voltage directly." (WPILib SystemcoreTesting README [19])

**Likely FRC pattern:** PD channel → Micro-Fit+→XT30 cable → SystemCore Bridge port. [19]

**Unconfirmed:** which PD channel type, what breaker rating, and whether it must be dedicated. **No 2027 rule text for controller power has been published yet.**
- The roboRIO rule required a dedicated 10 A channel.
- Treat SystemCore the same way (dedicated, non-switched, 10 A, 18 AWG) until R6xx for 2027 drops.
- The alpha spec called for 18 AWG ferruled power wire. [5]

**Brownout floor is lower (6.3 V vs 6.8 V)**, so the controller will ride through deeper sags. But PWM and digital outputs still cut out at brownout. Good batteries and short leads still matter. [5]

### 5.5 CAN under SystemCore: what actually changes in the wiring

**1. Every bus starts at SystemCore, which is already terminated.** Per FIRST: "CAN wires originate at the Systemcore in one of the CAN bus ports, then go to each component in order, ending at the terminating resistor." [16] So each of your buses needs **exactly one** 120 Ω terminator at the far end:
- a standalone 120 Ω in a WAGO
- a terminator on a motor adapter board
- the PDH switch, if the PDH is last on that bus

This is the same idea as the roboRIO+PDP pattern, repeated up to 5 times. **Do not** leave the PDH terminator on if it's mid-bus.

**2. Split the robot into buses on purpose.** FIRST frames multiple buses as "near point-to-point CAN wiring for simple robots" and a way to "segment their robot onto different buses for reliability." [16] Sensible splits:
- one bus per swerve corner pair, or drive vs. mechanisms
- the PDH and noisy devices on their own bus
- vision/coprocessor nodes isolated

One bad crimp then takes out one subsystem, not the whole robot.

**3. Color-code the buses.** CTRE now sells multi-bus CAN wire with **green always CAN-L** and the CAN-H color varying:
- brown, orange, light blue, purple, grey, white, or pink per bus; yellow stays the default

FIRST confirmed these colors are legal "for at least the 2027 season." Some teams prefer keeping yellow/green conductors and using colored *jackets* instead. Either way, pick a scheme and write it down. (CD, Aug 2026 [21])

**4. The CAN-FD reality check for 2027:**
- The hardware is FD-capable. [5]
- But FIRST's own reason for keeping CANivore legal in 2027 is to give "additional time for development and testing of Systemcore CAN-FD compatibility." [9]
- As of CTRE's SystemCore testing notes, Phoenix 6 works on native `CANPort.CAN_S*` buses and on CANivores. Phoenix 5 is unavailable, and **CTRE hasn't publicly committed to which Pro/FD features run natively.** [22][23]
- A CD thread from March 2026 on this question has no vendor answer. [23]

**Practical read:** if you're a CTRE/Kraken team relying on FD timing or Pro features, plan to keep a CANivore in 2027. The option goes away in 2028, when CANivore is allowed only as a node on a native bus. [9]

**5. CAN port 0 is shared with the Bridge port.** Thad_House (WPILib): "The bridge port and CAN port 0 on systemcore are physically the same." [24]
- This matters if you ever use MotionCore.
- With the XT30 power-only adapter, it's **unclear** whether `can_s0` stays fully independent.
- **Verify on real hardware before you put drivetrain devices on s0.**

**6. Stub discipline gets stricter.** With FD bit rates on the table, the old "short star is fine on the roboRIO" habit is riskier. Wire every bus as a true daisy chain. [12][11]

### 5.6 Other 2027 electrical rule changes (preview Part 1 [9])

- **Max 18 motors.** About 10% of 2026 teams exceeded this. FIRST's stated goals are lower cost and eliminating "secondary power distribution or complex wire harnesses."
- **Removed controllers:** original Talon / Talon SR and VictorSP.
- **BAG and Mini-CIM** are off the explicit motor list (discontinued), but still usable as generic brushed motors behind 20 A breakers.
- **USB batteries:** any COTS pack of 100 Wh or less.
- **New thermal rule:** no heating or cooling components for advantage.
- **Pneumatics:** unchanged for 2027.

### 5.7 I/O migration gotchas

- **Six SmartIO is the whole budget.** Audit sensors now. Anything past 6 has to move to CAN (CANcoder, CANrange, CAN limit switches) or be dropped. [16]
- **The 3.3 V rail is 1 A total, shared across all I/O and I2C.** Don't power sensors off it carelessly. [16]
- **I2C cables must be rebuilt (SDA/SCL swap).** SystemCore uses the Qwiic / REV Control Hub pinout. [19][16]
- **No relay ports.** Anything using a Spike relay needs a different approach. [16]

---

## 6. Cross-cutting patterns

**Consensus.** Across FIRST, WPILib, vendors, FRCElectrical.org, and Chief Delphi, the failure modes that matter are mechanical, not electrical theory:
- termination seating
- strain relief
- lug torque
- battery health
- radio power continuity

SystemCore doesn't change any of that. It multiplies the CAN harness count by up to 5 and changes connector families, so **crimp quality and documentation discipline matter more in 2027, not less.**

**Disagreement.**
- Ferrules: optional (2019) vs. mandatory (2024 practice and the SystemCore spec).
- Battery IR thresholds vary a lot depending on the tester.
- Multi-bus identification: colored conductors (CTRE) vs. colored jackets (teams).

**Gaps. These can't be answered yet, so revisit after kickoff:**
1. The official 2027 R6xx text for controller power: channel, breaker, and gauge.
2. A WPILib SystemCore wiring guide. The `/en/2027/` wiring page is still roboRIO. [25]
3. Native CAN-FD support per vendor (CTRE, REV, Redux) on SystemCore buses.
4. Whether `can_s0` is usable independently when powering through the XT30 adapter.
5. Rule Preview Part 2 (additional approved devices).

---

## 7. Action checklist for Ignite (2026 fall → 2027 kickoff)

- [ ] Order SystemCore on **Nov 18** (one per team at launch).
- [ ] Stock Molex SL 2/3/4-pin housings and 22 AWG gold terminals, Micro-Fit+ housings and terminals, and a crimper rated for both. Don't reuse alpha-era Weidmüller or ferrule harnesses.
- [ ] Buy multi-color CAN wire, or pick a jacket-color scheme. Document the bus map in `2-areas/robot-engineering/`.
- [ ] Plan the bus split (e.g., s1 = left drive, s2 = right drive, s3 = mechanisms, s4 = PDH and misc) with **one terminator per bus at the far end**.
- [ ] Rebuild every I2C cable (SDA/SCL swap). Audit DIO/analog count against the 6-SmartIO limit.
- [ ] If on Phoenix Pro/Krakens: budget to keep a CANivore for 2027.
- [ ] Radio: dual-feed the VH-109 (PoE + 12 V, same PD source, 10 A dedicated), and update its firmware to 2.x.
- [ ] Batteries: IR and load test the whole fleet before the season, retire weak units, and log each battery by ID.
- [ ] Adopt 1918's QC routine: tug test, seat check, and second-person inspection on every harness.
- [ ] Re-check this note after the 2027 game manual drops (early January) and after Rule Preview Part 2.

---

## Sources

| # | Source | Tier |
|---|---|---|
| 1 | [2026 FRC Game Manual (official HTML)](https://firstfrc.blob.core.windows.net/frc2026/Manual/HTML/2026GameManual.htm); cross-checked with [frcmanual.com R rules](https://www.frcmanual.com/2026/robot-construction-rules-(r)) | primary |
| 2 | [CD: Robust Electrical and Wiring Practices (Apr 2024)](https://www.chiefdelphi.com/t/robust-electrical-and-wiring-practices/461768) | secondary |
| 3 | [CD: Favorite tools, materials, and techniques for FRC wiring (Apr 2019)](https://www.chiefdelphi.com/t/favorite-tools-materials-and-techniques-for-frc-wiring/353212) | secondary |
| 4 | [FRCElectrical.org: FRC Control System](https://frcelectrical.org/FRC-Control-System/) | secondary |
| 5 | [Limelight SystemCore Specifications, alpha, 2025-06-15 (PDF)](https://downloads.limelightvision.io/documents/systemcore_specifications_june15_2025_alpha.pdf) | primary (alpha, partly superseded) |
| 6 | [CD: Battery Lifespan Issue (Oct 2025)](https://www.chiefdelphi.com/t/battery-lifespan-issue-why-do-our-frc-batteries-fail-so-quickly/506783) | secondary |
| 7 | CD battery threads: [Internal battery resistance values](https://www.chiefdelphi.com/t/internal-battery-resistance-values/362285), [How long can 6 AWG wire be?](https://www.chiefdelphi.com/t/how-long-can-6-awg-wire-be/454448), [Brownout Prevention?](https://www.chiefdelphi.com/t/brownout-prevention/152001) (search snippets) | secondary |
| 8 | [CD: Detailed FRC Battery Comparison for 2026, JaredL (Nov 2025)](https://www.chiefdelphi.com/t/detailed-frc-battery-comparison-for-2026/508077) | secondary |
| 9 | [FIRST: 2027 Event & Robot Rule Preview, Part 1 (Aug 31, 2026)](https://community.firstinspires.org/2026-event-robot-rule-preview-for-2027-season-part-1), plus [CD discussion](https://www.chiefdelphi.com/t/frc-blog-2027-event-robot-rule-preview-part-1/523740) | primary |
| 10 | [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html) | primary |
| 11 | [CD: The 2025 ultimate CAN Bus thread (Feb 2025)](https://www.chiefdelphi.com/t/the-2025-ultimate-can-bus-thread/491147) | secondary |
| 12 | CD topology threads: [Merits of Star Topology for CAN Bus](https://www.chiefdelphi.com/t/merits-of-star-topology-for-can-bus/358995), [CAN Bus Star Topology](https://www.chiefdelphi.com/t/can-bus-star-topology/510135) (search snippets; the full fetch returned 503) | secondary |
| 13 | [REV: RPM compatibility with the new FRC radio](https://docs.revrobotics.com/ion-control/rpm/rpm-compatibility-with-the-new-frc-radio) (search snippet) | primary |
| 14 | [Vivid-Hosting: Wiring Your Radio](https://frc-radio.vivid-hosting.net/overview/wiring-your-radio) | primary |
| 15 | [CD: Powering the VH109 radio in 2026](https://www.chiefdelphi.com/t/powering-the-vh109-radio-in-2026-passive-poe-or-12vdc-if-not-both/511858) | secondary |
| 16 | [LearnFRC: SystemCore Explained (Aug 3, 2026)](https://learnfrc.com/blog/frc-systemcore) | tertiary (cross-checked against 5, 18, 19, 20) |
| 17 | [CD: Systemcore Pricing and Availability](https://www.chiefdelphi.com/t/frc-blog-systemcore-pricing-and-availability/524424) ([FIRST blog](https://community.firstinspires.org/2026-systemcore-pricing-and-availability)) | primary |
| 18 | [FIRST: Updates on the Future Robot Controller (Mar 19, 2025)](https://community.firstinspires.org/march-updates-on-the-future-robot-controller); [WPILib: Systemcore Introduction](https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html) | primary |
| 19 | [WPILib SystemcoreTesting README](https://github.com/wpilibsuite/SystemcoreTesting/blob/main/README.md) | primary |
| 20 | [FIRST: Control System Update, FTC Edition (Dec 8, 2025)](https://community.firstinspires.org/control-system-update-first-tech-challenge-edition); [CD #180](https://www.chiefdelphi.com/t/systemcore-motioncore-rollout-questions-frc-ftc/508694/180) | primary |
| 21 | [CD: Multi CAN Bus Color Standardization (Aug 2026)](https://www.chiefdelphi.com/t/multi-can-bus-color-standardization/523228) | secondary (includes vendor staff) |
| 22 | [WPILib SystemcoreTesting: CTR-Phoenix.md](https://github.com/wpilibsuite/SystemCoreTesting/blob/main/CTR-Phoenix.md) | primary |
| 23 | [CD: Phoenix Pro native on Systemcore in 2026-2027? (Mar 2026)](https://www.chiefdelphi.com/t/phoenix-pro-native-on-systemcore-in-2026-2027/516984) | secondary |
| 24 | [CD: SystemCore/MotionCore rollout questions #188, Thad_House (Dec 10, 2025)](https://www.chiefdelphi.com/t/systemcore-motioncore-rollout-questions-frc-ftc/508694/188) | primary (WPILib dev) |
| 25 | [WPILib 2027 docs: Intro to FRC Robot Wiring (source)](https://docs.wpilib.org/en/2027/_sources/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.rst.txt) | primary |

## Audit

```
Queries sent: 12 web searches + 29 page fetches (+1 direct curl of the official manual)
Sources received: 38 | Sources cited: 25 entries (≈32 URLs)
Failures: 4 (2× CD HTTP 503, retried once and recovered for one; 1 PDF parse, recovered via local extraction;
          1 truncated manual fetch, recovered via curl). 3-consecutive-failures triggered: no
Routing decision: fallback (no specialist matched; classifier scores all 0)
Sub-questions:
  1. Core FRC power-wiring practices and rules
  2. CAN bus practices (topology, termination, utilization, FD)
  3. Chief Delphi field lessons (connectors, strain relief, batteries, brownouts)
  4. SystemCore 2027: hardware, power, CAN, connectors, rules
  5. Radio (VH-109) power and inspection rules
Verification notes:
  - R611 frame-isolation value (>120 Ω) verified against the raw official manual HTML.
  - SystemCore CAN count / FD / built-in termination verified in the primary alpha spec PDF.
  - LearnFRC (tertiary) claims used only where corroborated, or flagged.
[Background — not from search]: roboRIO brownout of 6.8 V in the §5.2 table is from prior knowledge.
```
