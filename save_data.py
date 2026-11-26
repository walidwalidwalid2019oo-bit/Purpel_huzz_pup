"""Pure validation helpers for PURPLE HAZE local save files.

This module intentionally has no Pygame dependency so save validation can be
unit-tested on desktop CI before the Android build runs.
"""

ITEMS = ("Veil Shards", "Moon Moss", "Ancient Relics")
PLACES = ("outpost", "caves")
WEAPONS = ("Shadow Blade", "Veil Scythe", "Void Gauntlet")


def _to_int(value):
    if isinstance(value, bool):
        raise ValueError("Boolean is not a valid saved integer.")
    return int(value)


def normalize_save_data(
    data,
    *,
    version,
    spawn,
    world_width,
    screen_height,
    crystal_spawns,
    player_size=(36, 58),
):
    """Return a fully validated save payload, or None without mutating state."""
    if not isinstance(data, dict):
        return None
    saved_version = data.get("version")
    if type(saved_version) is not int or saved_version != version:
        return None

    try:
        raw_inventory = data.get("inventory", {})
        if not isinstance(raw_inventory, dict):
            return None
        inventory = {
            name: max(0, _to_int(raw_inventory.get(name, 0)))
            for name in ITEMS
        }

        raw_places = data.get("found_places", [])
        if not isinstance(raw_places, (list, tuple)):
            return None
        found_places = {
            place for place in raw_places
            if isinstance(place, str) and place in PLACES
        }

        raw_weapons = data.get("owned_weapons", ["Shadow Blade"])
        if not isinstance(raw_weapons, (list, tuple)):
            return None
        owned_weapons = [
            weapon for weapon in raw_weapons
            if isinstance(weapon, str) and weapon in WEAPONS
        ]
        if "Shadow Blade" not in owned_weapons:
            owned_weapons.insert(0, "Shadow Blade")

        selected_weapon = data.get("selected_weapon", "Shadow Blade")
        if not isinstance(selected_weapon, str):
            return None
        if selected_weapon not in owned_weapons:
            selected_weapon = "Shadow Blade"

        raw_crystals = data.get("crystals", crystal_spawns)
        if not isinstance(raw_crystals, (list, tuple)):
            return None
        crystals = []
        for position in raw_crystals:
            if not isinstance(position, (list, tuple)) or len(position) != 2:
                return None
            crystals.append((_to_int(position[0]), _to_int(position[1])))

        raw_player = data.get("player", list(spawn))
        if not isinstance(raw_player, (list, tuple)) or len(raw_player) != 2:
            return None
        player_x, player_y = _to_int(raw_player[0]), _to_int(raw_player[1])
        max_x = max(0, int(world_width) - int(player_size[0]))
        max_y = max(0, int(screen_height) - int(player_size[1]))
        player = (max(0, min(max_x, player_x)), max(0, min(max_y, player_y)))

        won = data.get("won", False)
        if type(won) is not bool:
            return None

        health = max(1, min(3, _to_int(data.get("health", 3))))
        coins = max(0, _to_int(data.get("coins", 0)))
    except (TypeError, ValueError, OverflowError):
        return None

    return {
        "player": player,
        "health": health,
        "coins": coins,
        "inventory": inventory,
        "found_places": found_places,
        "owned_weapons": owned_weapons,
        "selected_weapon": selected_weapon,
        "crystals": crystals,
        "won": won,
    }
