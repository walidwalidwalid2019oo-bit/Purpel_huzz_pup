# PURPLE HAZE — Systems Specifications

This document turns the design into implementation contracts. It is a specification, not evidence that the systems are already built.

## Player controller
- Responsive horizontal movement and jump
- Collision resolution that behaves consistently across frame rates
- Coyote time and jump buffering as optional feel improvements
- Dash / Phase Step with cooldown and clear feedback
- Touch and keyboard input mapped to the same action layer
- Safe respawn and checkpoint support

## Combat
- Central combat state machine: idle, startup, active, recovery, dodge, hurt and defeated
- Weapon definitions contain range, damage, speed, recovery, hit shape and effects
- Hit detection is separate from rendering
- Enemies telegraph attacks and respect cooldowns
- Damage, invulnerability and knockback are handled by gameplay logic, not animation code
- Combat events can trigger particles, sound and UI feedback without owning game state

## Creature framework
Each creature definition should specify habitat, movement, senses, temperament, trust actions, rewards, abilities and animation states. Creature state must persist in the save file.

## Interactions
Use a shared interaction interface for ECHO, doors, outpost objects, cave entrances, traders, save points, pickups and quest objects. Show the correct contextual action only when the player is in range.

## Inventory and economy
- Item definitions are data-driven: ID, display name, category, stack limit, description and optional icon.
- Inventory operations validate quantity and never permit negative counts.
- Veil Coins are a separate integer currency.
- Shop purchases check ownership and balance before changing either.
- One-time discovery rewards must not be awarded repeatedly after loading or revisiting.

## Quest and story state
- Quests have stable IDs, stages, objectives, completion state and rewards.
- Story choices are recorded by stable IDs and values.
- Dialogue can check quest and choice state, but dialogue text should not directly mutate unrelated systems.
- Ending selection reads the saved decision state and discovered story evidence.

## HILPO
HILPO follows at a controlled distance and returns smoothly if separated. It does not autonomously attack or leave the player to explore. Scanner output should be grounded in nearby objects and creatures. Map, journal and skill-tree interfaces should remain accessible on touchscreens.

## Save system
- Use a version number and schema migration path.
- Validate loaded values and use safe defaults for missing fields.
- Write to a temporary file and replace the old save only after a complete write.
- Track one-time pickups and discovery rewards.
- Do not store secrets, API tokens or account credentials.
- Provide a clear save error message without destroying the previous valid save.

## UI and accessibility
- Keep touch targets large and separated.
- Support landscape Android layout and different aspect ratios.
- Provide readable text, subtitles, volume controls and input settings.
- Avoid communicating critical information through color alone.
- Allow pausing and changing settings without losing progress.
