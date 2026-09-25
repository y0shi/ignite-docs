---
title: Knowledge Graph Index
tags: [moc, knowledge-graph]
---
# Knowledge Graph

Ingested research: external docs, code, articles, vendor material.
Maintained by `claude-obsidian:wiki-ingest`. Sources are immutable in `.raw/`.

## Sources

- [[FRC-Electrical-Best-Practices-2027-SystemCore]]: FRC electrical best practices plus the 2027 SystemCore wiring and CAN changes (2026-09-24)
- [[Silver-Cymbal-Crimp-Seam-Up-or-Down]]: YouTube, crimp seam orientation; transcript pending (low confidence)

## Entities

- [[SystemCore]]: 2027 robot controller replacing the roboRIO
- [[CANivore]]: CTRE USB-to-CAN-FD adapter; can add a bus in 2027 only
- [[VH-109 Radio]]: Vivid-Hosting robot radio and its power rules
- [[REV Power Distribution Hub]]: main PD; CAN termination switch
- [[CTR Electronics]]: CTRE; Phoenix 6 on SystemCore, multi-color CAN wire
- [[WPILib]]: official docs; SystemcoreTesting repo
- [[Chief Delphi]]: FRC forum; index of referenced threads

## Concepts

- [[CAN Bus Wiring]]: daisy chain, termination, utilization, troubleshooting
- [[Multi-Bus CAN Architecture]]: splitting a robot across SystemCore's five buses
- [[CAN FD]]: faster CAN; 2027 native-support gap
- [[Frame Isolation]]: R611, >120 Ω (not 3 kΩ)
- [[Wire and Breaker Sizing]]: R609 main path, R622 table, colors
- [[FRC Battery Management]]: testing, care, brand data
- [[Brownout]]: roboRIO vs SystemCore thresholds
- [[Radio Power Redundancy]]: dual-feed the VH-109
- [[Connector and Crimp Quality]]: QC routine, strain relief, ferrules, 2027 connectors
- [[2027 FRC Rule Changes]]: 18 motors, CANivore timeline, removed parts
