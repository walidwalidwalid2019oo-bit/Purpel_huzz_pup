# PURPLE HAZE — Development Roadmap

This roadmap is ordered to produce a playable game rather than a collection of disconnected menus. Items marked planned are not yet implemented.

## Milestone 0 — Project foundation
- [x] Standalone GitHub repository
- [x] Python / Pygame prototype source
- [x] Android Buildozer configuration
- [x] GitHub Actions Android build workflow
- [x] Basic title screen and touch controls
- [ ] Confirm reproducible desktop run
- [ ] Confirm successful Android build and install on a real device
- [ ] Add automated syntax / smoke checks

## Milestone 1 — Stable playable foundation
- [ ] Fix and test reset / new-game state handling
- [ ] Add versioned save and load for player progress
- [ ] Persist inventory, coins, weapon ownership, discoveries and settings
- [ ] Add pause menu and safe respawn points
- [ ] Add input remapping and touch layout settings
- [ ] Add basic automated tests for save data and progression

## Milestone 2 — Shattered Isles vertical slice
- [x] THE HOLLOW placeholder character
- [x] HILPO follow companion prototype
- [x] ECHO dialogue prototype
- [x] Veil shard pickups
- [x] Portal objective
- [x] Outpost and cave discovery landmarks
- [x] Basic inventory and Veil Coin counter
- [x] VEIL MARKET with three weapon forms
- [ ] Final pixel-art character and companion sprites
- [ ] Actual enemy with health, behavior and damage feedback
- [ ] One discoverable creature with a complete trust / taming loop
- [ ] Fully explorable village area
- [ ] Fully explorable cave level
- [ ] Save point and persistent progress
- [ ] Region exit / transition and return route
- [ ] First boss or major encounter

## Milestone 3 — Core game systems
- [ ] Weapon-specific attacks, combos and hit reactions
- [ ] Dodge and ability cooldown system
- [ ] Skill tree and unlock requirements
- [ ] Creature journal and creature behavior states
- [ ] Quest tracker and journal
- [ ] NPC dialogue framework
- [ ] Trader inventory and economy balancing
- [ ] HILPO map, scanner and upgrade progression
- [ ] Environmental puzzle framework
- [ ] Audio settings, sound effects and original ambient music

## Milestone 4 — Region expansion
- [ ] Forgotten Forest
- [ ] Silent City
- [ ] Distortion
- [ ] Observatory
- [ ] Beyond the Haze
- [ ] Region-specific creatures, hazards, quests and secrets
- [ ] Connected shortcuts and backtracking rewards

## Milestone 5 — Story and endings
- [ ] Main narrative chapter outline
- [ ] Choice and consequence tracking
- [ ] Companion and ECHO story arcs
- [ ] Multiple endings with clear causal links
- [ ] Full dialogue pass and subtitles
- [ ] Voice acting production plan and recordings

## Milestone 6 — Art, polish and release
- [ ] High-quality pixel-art asset pipeline
- [ ] Character animation sets
- [ ] Region tilesets and parallax backgrounds
- [ ] UI and accessibility pass
- [ ] Performance and memory profiling on Android
- [ ] Device compatibility testing
- [ ] Credits, settings, save migration and release checklist
- [ ] Signed release build and store preparation

## Current truth
The existing source is an early playable prototype. Its outpost and cave are currently discovery landmarks, not full interior levels. The inventory and discoveries are not yet persistent between app launches. The current companion dialogue is scripted. No successful APK build has been confirmed in this repository yet.

## Working rule
Each milestone must end with a tested playable build. A visible button is not considered a completed feature unless it performs its intended action and its state behaves correctly.
