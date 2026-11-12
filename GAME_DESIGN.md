# PURPLE HAZE — Complete Game Design

> Canonical design document. This describes the intended full game, not a claim that every feature is already implemented.

## 1. High concept

**Genre:** atmospheric open-world action-adventure / survival exploration  
**World:** VESPER, an alien world connected by ancient Veil energy  
**Tone:** dark, lonely, mysterious and psychological  
**Core pillars:** exploration and combat have equal importance; discover and tame creatures; choices shape multiple endings.  
**Visual direction:** high-quality pixel art, layered atmospheric environments, purple shadow effects and readable silhouettes.  
**Target:** Android-first prototype, with PC as a future development target.

## 2. The world: VESPER

The Veil is an energy system connecting ecosystems, ancient technology and living creatures. The Fading is a spreading disturbance that weakens light, disrupts machines, changes creatures and damages memory.

### Regions and intended progression
1. **Shattered Isles** — opening region; floating land, broken paths, first Veil shards and the first encounter with HILPO.
2. **Forgotten Forest** — dense alien growth, hidden paths, creatures, old settlements and environmental puzzles.
3. **Silent City** — abandoned architecture, exploration, records, traders or survivors where appropriate, and evidence about the Fading.
4. **Distortion** — unstable terrain, altered physics, dangerous creatures and unreliable signals.
5. **Observatory** — ancient research site that reveals more about the Veil and ECHO.
6. **Beyond the Haze** — late-game region where accumulated choices and discoveries influence the final path.

Regions should connect through traversable routes, gates, caves, lifts, ancient structures and unlockable shortcuts. Avoid disconnected menu-only levels where a physical connection makes sense.

## 3. Main characters

### THE HOLLOW
The player character: a faceless, floating shadow silhouette with restrained violet glow details and a purple smoke trail. The character's identity and origin are deliberately mysterious. Movement and combat should feel responsive, readable and expressive without relying on a visible human face.

### HILPO
A small floating drone that mysteriously appears beside THE HOLLOW. It follows the player, speaks with a mysterious electronic voice and responds to commands. HILPO supports scanning, navigation, climbing and combat utility, but does not independently explore or attack without direction.

Planned HILPO functions:
- Map and route guidance
- Scanner for objects, creatures and Veil traces
- Inventory and quest notifications
- Skill-tree access and upgrade explanations
- Contextual hints, companion dialogue and memory log
- Limited combat support and traversal assistance

### ECHO
A mysterious intelligence encountered through ancient structures. ECHO knows fragments of VESPER's history but may be incomplete or unreliable. Dialogue should invite interpretation rather than explain every mystery.

## 4. Core gameplay loop

Explore a region → notice a signal or landmark → investigate and scan → solve a traversal, environmental or combat challenge → collect resources and lore → meet creatures and build trust → unlock routes and abilities → return to earlier areas with new tools.

Exploration rewards should include discoveries, lore, materials, creature knowledge, shortcuts, cosmetics and Veil Coins. Combat should create meaningful decisions rather than being the only way to progress.

## 5. Combat and abilities

Weapons are formed from purple shadow energy rather than carried as ordinary physical weapons.

### Weapon forms
- **Shadow Blade:** fast, balanced attacks.
- **Veil Scythe:** slower, wider sweeping attacks.
- **Void Gauntlet:** heavy close-range impact.

Planned combat features:
- Weapon summon and dismiss effects
- Weapon-specific attack animations and hit reactions
- Combos with clear timing and feedback
- Dodge / evasive movement
- Enemy telegraphs and readable attack patterns
- Ability cooldowns and resource feedback
- Boss encounters built around observation and learning
- Accessibility options for input timing and touch controls

### Ability tree
- **Shadow Strike:** focused offensive move.
- **Veil Pulse:** reveals nearby hidden traces and interactables.
- **Phase Step:** short evasive reposition.
- **Void Barrier:** temporary defensive protection.
- **Shadow Surge:** stronger movement or attack burst.

Unlocks should have meaningful trade-offs and should not require grinding for basic progression.

## 6. Creatures and taming

Creatures are part of VESPER's ecology, not just enemies. The player should observe their behavior, learn their needs and decide whether to avoid, befriend, tame or defend against them.

Planned creature states:
- Unaware / roaming
- Curious
- Cautious
- Hostile or defensive
- Trust-building
- Tamed / companion

Taming should be earned through discovery and interaction, not a single universal button. Creature abilities can support traversal, sensing, gathering or combat. Creature names such as LUMI, CRAG and NYX are working concepts until finalized.

## 7. Settlements, caves and quests

### Villages and outposts
Settlements should become real explorable spaces with interiors, readable landmarks, NPC schedules or routines where practical, traders, side quests, local stories, safe points and optional discoveries. VESPER OUTPOST is the first settlement concept.

### Caves
Caves should be actual traversable levels with branching paths, crystals, environmental hazards, hidden chambers, creature habitats, lore and connections or shortcuts. THE HOLLOWING CAVES is the first cave concept.

### Quest types
- Main story investigations
- Settlement requests
- Creature discovery and trust tasks
- Ancient structure puzzles
- Optional exploration challenges
- Multi-step region quests with consequences

## 8. Inventory, resources and economy

The inventory is called **HOLLOW'S PACK**.

Planned categories:
- Veil Shards
- Moon Moss
- Ancient Relics
- Quest items
- Creature-related materials
- Upgrade materials
- Cosmetic unlocks

**Veil Coins** are earned through exploration, encounters and quests. The prototype currently awards coins for shard collection and first cave discovery. There are no real-money purchases in the prototype.

### VEIL MARKET
Planned shop categories:
- Weapon forms
- Ability upgrades
- HILPO upgrades
- Cosmetic shadow effects
- Optional convenience items that do not undermine balance

Current prototype weapon prices: Shadow Blade is free, Veil Scythe costs 75 Veil Coins, and Void Gauntlet costs 120.

## 9. Progression and multiple endings

Player choices, discoveries, relationships, creature treatment and story decisions should influence the ending. The game should track meaningful choices and reveal their consequences through later dialogue, environmental changes and character responses.

Do not lock an ending behind a hidden arbitrary score alone. Make the important decisions understandable in hindsight while preserving mystery.

## 10. Atmosphere, audio and presentation

- High-quality pixel art with consistent scale and animation timing
- Deep black-purple environments with controlled violet highlights
- Distinct visual identity for each region
- Atmospheric haze, particles, distant silhouettes and environmental storytelling
- Original ambient music and sound design
- Planned full voice acting for major characters and key story moments
- Subtitles, dialogue history and adjustable audio levels
- Clear UI contrast and readable touch targets

## 11. Interface

Planned interface screens:
- Title screen and continue / new game
- In-game HUD: health, region, companion status and currency
- HOLLOW'S PACK inventory
- World map and discovery markers
- Skill tree
- VEIL MARKET
- Quest and journal log
- Creature discovery / trust journal
- Dialogue and subtitles
- Settings: audio, controls, display, language and accessibility
- Save slots and save confirmation

## 12. Save data

Save data should include:
- Current region and safe respawn point
- Player progression and unlocked abilities
- Inventory quantities and Veil Coins
- Owned and equipped weapon forms
- Discovered landmarks, opened routes and collected one-time rewards
- Creature discoveries, trust and taming state
- Quest progress and consequential story choices
- Settings

Saving should be versioned, validated and resilient to interrupted writes. Never store API keys or private credentials in the game client.

## 13. Scope boundaries

The first vertical slice focuses on THE HOLLOW, HILPO, ECHO, one island, one creature to discover and tame, one enemy, basic combat and one ability, crystals, a portal and a save point.

Deferred until the core game is stable: multiplayer, seamless 3D world, hundreds of creatures, procedural planet generation, a large autonomous AI NPC population, complex base building, multiple playable characters and voice-command gameplay.
