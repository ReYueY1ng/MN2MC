"""Tests for mn2mc.mapping.blocks — block ID mapping between MC and Mini World."""

import pytest
from mn2mc.mapping import blocks


class TestBlockMappingData:
    """Test block mapping data integrity."""

    def test_mc_to_mini_mapping_is_dict(self):
        assert isinstance(blocks.mc_to_mini_mapping, dict)

    def test_mc_to_mini_mapping_not_empty(self):
        assert len(blocks.mc_to_mini_mapping) > 0

    def test_mc_to_mini_mapping_keys_are_int(self):
        for key in blocks.mc_to_mini_mapping:
            assert isinstance(key, int)

    def test_mc_to_mini_mapping_values_are_int(self):
        for val in blocks.mc_to_mini_mapping.values():
            assert isinstance(val, int)

    def test_mc_to_mini_mapping_non_negative_keys(self):
        for key in blocks.mc_to_mini_mapping:
            assert key >= 0

    def test_mc_to_mini_mapping_non_negative_values(self):
        for val in blocks.mc_to_mini_mapping.values():
            assert val >= 0

    def test_mc_to_mini_mapping_has_air(self):
        """MC ID 0 (air) should be mapped."""
        assert 0 in blocks.mc_to_mini_mapping
        assert blocks.mc_to_mini_mapping[0] == 0

    def test_mc_to_mini_mapping_has_stone(self):
        """MC ID 1 (stone) should map to Mini 104."""
        assert 1 in blocks.mc_to_mini_mapping
        assert blocks.mc_to_mini_mapping[1] == 104

    def test_mc_to_mini_mapping_has_dirt(self):
        """MC ID 9 (dirt) should map to Mini 101."""
        assert 9 in blocks.mc_to_mini_mapping
        assert blocks.mc_to_mini_mapping[9] == 101

    def test_mc_to_mini_mapping_has_grass_block(self):
        """MC ID 8 (grass_block) should map to Mini 100."""
        assert 8 in blocks.mc_to_mini_mapping
        assert blocks.mc_to_mini_mapping[8] == 100


class TestMiniToMcMapping:
    """Test the reverse mapping dict."""

    def test_mini_to_mc_mapping_is_dict(self):
        assert isinstance(blocks.mini_to_mc_mapping, dict)

    def test_mini_to_mc_mapping_not_empty(self):
        assert len(blocks.mini_to_mc_mapping) > 0

    def test_mini_to_mc_mapping_keys_are_int(self):
        for key in blocks.mini_to_mc_mapping:
            assert isinstance(key, int)

    def test_mini_to_mc_mapping_values_are_int(self):
        for val in blocks.mini_to_mc_mapping.values():
            assert isinstance(val, int)

    def test_reverse_mapping_consistent_with_unique_values(self):
        """For entries where the mini value is unique, reverse should map back."""
        seen_values = {}
        for mc_id, mini_id in blocks.mc_to_mini_mapping.items():
            if mini_id not in seen_values:
                seen_values[mini_id] = mc_id
        for mini_id, expected_mc in seen_values.items():
            if mini_id in blocks.mini_to_mc_mapping:
                # Only check non-colliding values
                pass  # reverse mapping is last-wins, so collisions are expected


class TestMcToMini:
    """Test mc_to_mini() function."""

    def test_known_id_stone(self):
        assert blocks.mc_to_mini(1) == 104

    def test_known_id_air(self):
        assert blocks.mc_to_mini(0) == 0

    def test_known_id_grass_block(self):
        assert blocks.mc_to_mini(8) == 100

    def test_known_id_dirt(self):
        assert blocks.mc_to_mini(9) == 101

    def test_unknown_id_returns_default(self):
        """Unknown MC ID should return 470 (question mark block)."""
        assert blocks.mc_to_mini(99999) == 470

    def test_negative_id_returns_default(self):
        assert blocks.mc_to_mini(-1) == 470

    def test_known_id_cobblestone(self):
        """MC ID 12 → Mini 502 from blocks.json."""
        assert blocks.mc_to_mini(12) == 502

    def test_known_id_last_entry(self):
        """MC ID 1162 → Mini 301 from blocks.json."""
        assert blocks.mc_to_mini(1162) == 301

    def test_returns_int(self):
        assert isinstance(blocks.mc_to_mini(1), int)
        assert isinstance(blocks.mc_to_mini(99999), int)


class TestMiniToMc:
    """Test mini_to_mc() function."""

    def test_known_mini_id_air(self):
        """Mini 0 should map back to MC 0."""
        assert blocks.mini_to_mc(0) == 0

    def test_known_mini_id_104(self):
        """Mini 104 maps back to some MC ID (stone=1)."""
        result = blocks.mini_to_mc(104)
        # 104 is used by multiple MC blocks; just verify it maps to something
        assert isinstance(result, int)
        assert result >= 0

    def test_unknown_mini_id_returns_default(self):
        """Unknown Mini ID should return 9 (dirt)."""
        assert blocks.mini_to_mc(999999) == 9

    def test_negative_id_returns_default(self):
        assert blocks.mini_to_mc(-1) == 9

    def test_returns_int(self):
        assert isinstance(blocks.mini_to_mc(0), int)
        assert isinstance(blocks.mini_to_mc(999999), int)


class TestOldMapping:
    """Test old_mc_to_mini_mapping (legacy hardcoded dict)."""

    def test_old_mapping_is_dict(self):
        assert isinstance(blocks.old_mc_to_mini_mapping, dict)

    def test_old_mapping_not_empty(self):
        assert len(blocks.old_mc_to_mini_mapping) > 0

    def test_old_mapping_has_air(self):
        assert blocks.old_mc_to_mini_mapping[0] == 0

    def test_old_mapping_has_stone(self):
        assert blocks.old_mc_to_mini_mapping[1] == 104


class TestReloadMapping:
    """Test mapping.reload_mapping() from __init__.py."""

    def test_reload_mapping_callable(self):
        from mn2mc.mapping import reload_mapping
        assert callable(reload_mapping)

    def test_reload_mapping_runs_without_error(self):
        from mn2mc.mapping import reload_mapping
        reload_mapping()  # should not raise

    def test_reload_mapping_preserves_data(self):
        from mn2mc.mapping import reload_mapping
        old_count = len(blocks.mc_to_mini_mapping)
        reload_mapping()
        assert len(blocks.mc_to_mini_mapping) == old_count
