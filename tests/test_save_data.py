import unittest

from save_data import normalize_save_data


class NormalizeSaveDataTests(unittest.TestCase):
    def setUp(self):
        self.options = {
            "version": 1,
            "spawn": (110, 350),
            "world_width": 3000,
            "screen_height": 540,
            "crystal_spawns": [(420, 395), (1120, 295)],
        }

    def valid_payload(self):
        return {
            "version": 1,
            "player": [125, 360],
            "health": 2,
            "coins": 75,
            "inventory": {"Veil Shards": 3, "Moon Moss": 1},
            "found_places": ["outpost"],
            "owned_weapons": ["Shadow Blade", "Veil Scythe"],
            "selected_weapon": "Veil Scythe",
            "crystals": [[420, 395]],
            "won": False,
        }

    def test_valid_payload_is_normalized(self):
        result = normalize_save_data(self.valid_payload(), **self.options)
        self.assertIsNotNone(result)
        self.assertEqual(result["player"], (125, 360))
        self.assertEqual(result["inventory"]["Veil Shards"], 3)
        self.assertEqual(result["selected_weapon"], "Veil Scythe")
        self.assertEqual(result["crystals"], [(420, 395)])

    def test_invalid_inventory_container_is_rejected(self):
        payload = self.valid_payload()
        payload["inventory"] = None
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_invalid_discovery_container_is_rejected(self):
        payload = self.valid_payload()
        payload["found_places"] = None
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_malformed_crystal_does_not_silently_disappear(self):
        payload = self.valid_payload()
        payload["crystals"] = [[420], "bad"]
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_invalid_player_position_is_rejected(self):
        payload = self.valid_payload()
        payload["player"] = [1]
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_out_of_bounds_player_position_is_clamped(self):
        payload = self.valid_payload()
        payload["player"] = [99999, -5]
        result = normalize_save_data(payload, **self.options)
        self.assertEqual(result["player"], (2964, 0))

    def test_wrong_version_and_boolean_version_are_rejected(self):
        payload = self.valid_payload()
        payload["version"] = 2
        self.assertIsNone(normalize_save_data(payload, **self.options))
        payload["version"] = True
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_invalid_numeric_value_is_rejected(self):
        payload = self.valid_payload()
        payload["coins"] = "many"
        self.assertIsNone(normalize_save_data(payload, **self.options))

    def test_unknown_items_are_ignored_and_default_weapon_is_preserved(self):
        payload = self.valid_payload()
        payload["inventory"]["Unknown"] = 999
        payload["owned_weapons"] = ["Unknown"]
        payload["selected_weapon"] = "Unknown"
        result = normalize_save_data(payload, **self.options)
        self.assertEqual(set(result["inventory"]), {"Veil Shards", "Moon Moss", "Ancient Relics"})
        self.assertEqual(result["owned_weapons"], ["Shadow Blade"])
        self.assertEqual(result["selected_weapon"], "Shadow Blade")


if __name__ == "__main__":
    unittest.main()
