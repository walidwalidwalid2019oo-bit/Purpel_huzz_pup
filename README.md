# PURPLE HAZE

A phone-first 2D atmospheric exploration platformer prototype built with Python + Pygame.

## Current prototype
- THE HOLLOW, a shadow-like protagonist with violet glow and a drifting trail
- HILPO, a floating companion with follow behavior, scanner feedback and status HUD
- VESPER / SHATTERED ISLES: connected platform route and atmospheric night world
- ECHO encounter with dialogue
- Veil Shard collectibles, Veil Coins and a basic inventory panel
- Vesper Outpost and Hollowing Caves discovery landmarks
- Veil Market with Shadow Blade, Veil Scythe and Void Gauntlet
- Shadow dash, basic weapon attacks, health indicators and particle effects
- Touchscreen and keyboard controls

## Controls
- Move: A/D or Left/Right arrows; mobile left/right buttons
- Jump: Space, W, Up arrow, or JUMP
- Interact / talk: E or F, or ACT
- Scan: Q or SCAN
- Shadow dash: Left or Right Shift
- Attack: J or ATTACK
- Inventory: I
- Shop: B
- Buy/equip shop items: 1 / 2 / 3 while the shop is open
- Escape: return to title / exit

## Run on desktop
```bash
python -m pip install -r requirements.txt
python main.py
```

## Android
The project includes a Buildozer configuration and GitHub Actions workflow for an Android debug APK. The workflow checks Python syntax, builds with Buildozer, and uploads an APK artifact if successful. A configured workflow is not proof that a build has succeeded; check the Actions tab for the latest run and artifact.

## Prototype limitations
This is an early playable prototype, not the finished game. The village and cave are currently discovery landmarks, not full explorable interiors. Inventory/discovery data is not yet saved between app launches. Shop, combat, creature taming, NPCs, quests, full cave levels, final pixel-art assets, music and voice acting are still under development. HILPO's responses are scripted, not connected to an AI model.

## Direction
PURPLE HAZE is a dark, lonely, psychological open-world adventure on VESPER, with connected regions, exploration and combat, discoverable/tameable creatures, and multiple endings shaped by player decisions.
