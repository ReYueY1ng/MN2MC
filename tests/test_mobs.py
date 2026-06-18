"""Tests for mn2mc.mapping.mobs — mob ID mapping between MC and Mini World."""

import pytest
from mn2mc.mapping import mobs


class TestMobMappingData:
    """Test mob mapping data integrity."""

    def test_mc_to_mini_mapping_is_dict(self):
        assert isinstance(mobs.mc_to_mini_mapping, dict)

    def test_mc_to_mini_mapping_not_empty(self):
        assert len(mobs.mc_to_mini_mapping) > 0

    def test_mc_to_mini_mapping_keys_are_int(self):
        for key in mobs.mc_to_mini_mapping:
            assert isinstance(key, int)

    def test_mc_to_mini_mapping_values_are_int(self):
        for val in mobs.mc_to_mini_mapping.values():
            assert isinstance(val, int)

    def test_mc_to_mini_mapping_non_negative_keys(self):
        for key in mobs.mc_to_mini_mapping:
            assert key >= 0

    def test_mc_to_mini_mapping_non_negative_values(self):
        for val in mobs.mc_to_mini_mapping.values():
            assert val >= 0

    def test_mc_to_mini_mapping_has_pig(self):
        """MC mob ID 100 (pig) should map to Mini 3284."""
        assert 100 in mobs.mc_to_mini_mapping
        assert mobs.mc_to_mini_mapping[100] == 3284

    def test_mc_to_mini_mapping_has_chicken(self):
        """MC mob ID 10 (chicken) should map to Mini 3107."""
        assert 10 in mobs.mc_to_mini_mapping
        assert mobs.mc_to_mini_mapping[10] == 3107

    def test_mc_to_mini_mapping_has_cow(self):
        """MC mob ID 11 (cow) should map to Mini 3418."""
        assert 11 in mobs.mc_to_mini_mapping
        assert mobs.mc_to_mini_mapping[11] == 3418

    def test_mapping_count_expected(self):
        """Should have 33 mob mappings (matching mobs.json)."""
        assert len(mobs.mc_to_mini_mapping) == 33


class TestMobMiniToMcMapping:
    """Test the reverse mapping dict."""

    def test_mini_to_mc_mapping_is_dict(self):
        assert isinstance(mobs.mini_to_mc_mapping, dict)

    def test_mini_to_mc_mapping_not_empty(self):
        assert len(mobs.mini_to_mc_mapping) > 0

    def test_mini_to_mc_mapping_keys_are_int(self):
        for key in mobs.mini_to_mc_mapping:
            assert isinstance(key, int)

    def test_mini_to_mc_mapping_values_are_int(self):
        for val in mobs.mini_to_mc_mapping.values():
            assert isinstance(val, int)

    def test_reverse_mapping_unique_values_count(self):
        """Reverse mapping should have fewer entries than forward (due to collisions)."""
        # Multiple MC mobs can map to the same Mini mob
        assert len(mobs.mini_to_mc_mapping) <= len(mobs.mc_to_mini_mapping)


class TestMobMcToMini:
    """Test mobs.mc_to_mini() function."""

    def test_known_id_pig(self):
        assert mobs.mc_to_mini(100) == 3284

    def test_known_id_chicken(self):
        assert mobs.mc_to_mini(10) == 3107

    def test_known_id_cow(self):
        assert mobs.mc_to_mini(11) == 3418

    def test_unknown_id_returns_default(self):
        """Unknown MC mob ID should return 3284 (pig)."""
        assert mobs.mc_to_mini(99999) == 3284

    def test_negative_id_returns_default(self):
        assert mobs.mc_to_mini(-1) == 3284

    def test_returns_int(self):
        assert isinstance(mobs.mc_to_mini(100), int)
        assert isinstance(mobs.mc_to_mini(99999), int)


class TestMobMiniToMc:
    """Test mobs.mini_to_mc() function."""

    def test_known_mini_id_pig(self):
        """Mini 3284 should map back to an MC mob ID."""
        result = mobs.mini_to_mc(3284)
        assert isinstance(result, int)
        assert result >= 0

    def test_unknown_mini_id_returns_default(self):
        """Unknown Mini mob ID should return 100 (pig)."""
        assert mobs.mini_to_mc(999999) == 100

    def test_negative_id_returns_default(self):
        assert mobs.mini_to_mc(-1) == 100

    def test_returns_int(self):
        assert isinstance(mobs.mini_to_mc(3284), int)
        assert isinstance(mobs.mini_to_mc(999999), int)
