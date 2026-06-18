"""Tests for mn2mc.mapping.items — item ID mapping between MC and Mini World."""

import pytest
from mn2mc.mapping import items


class TestItemMappingData:
    """Test item mapping data integrity."""

    def test_mc_to_mini_mapping_is_dict(self):
        assert isinstance(items.mc_to_mini_mapping, dict)

    def test_mc_to_mini_mapping_not_empty(self):
        assert len(items.mc_to_mini_mapping) > 0

    def test_mc_to_mini_mapping_keys_are_int(self):
        for key in items.mc_to_mini_mapping:
            assert isinstance(key, int)

    def test_mc_to_mini_mapping_values_are_int(self):
        for val in items.mc_to_mini_mapping.values():
            assert isinstance(val, int)

    def test_mc_to_mini_mapping_non_negative_keys(self):
        for key in items.mc_to_mini_mapping:
            assert key >= 0

    def test_mc_to_mini_mapping_non_negative_values(self):
        for val in items.mc_to_mini_mapping.values():
            assert val >= 0

    def test_mc_to_mini_mapping_has_air(self):
        """MC item ID 0 (air) should be mapped."""
        assert 0 in items.mc_to_mini_mapping
        assert items.mc_to_mini_mapping[0] == 0

    def test_mc_to_mini_mapping_has_stone(self):
        """MC item ID 1 (stone) should map to Mini 104."""
        assert 1 in items.mc_to_mini_mapping
        assert items.mc_to_mini_mapping[1] == 104

    def test_mapping_count_reasonable(self):
        """Should have at least 100 item mappings."""
        assert len(items.mc_to_mini_mapping) >= 100


class TestItemMiniToMcMapping:
    """Test the reverse mapping dict."""

    def test_mini_to_mc_mapping_is_dict(self):
        assert isinstance(items.mini_to_mc_mapping, dict)

    def test_mini_to_mc_mapping_not_empty(self):
        assert len(items.mini_to_mc_mapping) > 0

    def test_mini_to_mc_mapping_keys_are_int(self):
        for key in items.mini_to_mc_mapping:
            assert isinstance(key, int)

    def test_mini_to_mc_mapping_values_are_int(self):
        for val in items.mini_to_mc_mapping.values():
            assert isinstance(val, int)


class TestItemMcToMini:
    """Test items.mc_to_mini() function."""

    def test_known_id_air(self):
        assert items.mc_to_mini(0) == 0

    def test_known_id_stone(self):
        assert items.mc_to_mini(1) == 104

    def test_unknown_id_returns_default(self):
        """Unknown MC item ID should return 470 (question mark block)."""
        assert items.mc_to_mini(99999) == 470

    def test_negative_id_returns_default(self):
        assert items.mc_to_mini(-1) == 470

    def test_returns_int(self):
        assert isinstance(items.mc_to_mini(1), int)
        assert isinstance(items.mc_to_mini(99999), int)


class TestItemMiniToMc:
    """Test items.mini_to_mc() function."""

    def test_known_mini_id_0(self):
        """Mini 0 should map back to some MC ID (reverse mapping, last-wins)."""
        result = items.mini_to_mc(0)
        assert isinstance(result, int)
        assert result >= 0

    def test_unknown_mini_id_returns_default(self):
        """Unknown Mini item ID should return 28 (dirt)."""
        assert items.mini_to_mc(999999) == 28

    def test_negative_id_returns_default(self):
        assert items.mini_to_mc(-1) == 28

    def test_returns_int(self):
        assert isinstance(items.mini_to_mc(0), int)
        assert isinstance(items.mini_to_mc(999999), int)
