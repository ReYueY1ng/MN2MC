import pytest
from mn2mc.constants import (
    UIN_MAX,
    MINI_OBJ_ID_BASE,
    DIMENSION_NETHER,
    DIMENSION_OVERWORLD,
    DIMENSION_END,
    SECTION_FLAGS,
    GAMEMODE_SURVIVAL,
    GAMEMODE_CREATIVE,
)


class TestConstantUinBoundary:
    """Test UIN boundary constants.

    UIN_MAX is the uint32 player UIN ceiling; MINI_OBJ_ID_BASE
    must be exactly one greater so entity IDs never collide.
    """

    def test_uin_max_is_uint32_maximum(self):
        assert UIN_MAX == 4294967295

    def test_mini_obj_id_base_is_uin_max_plus_one(self):
        assert MINI_OBJ_ID_BASE == UIN_MAX + 1

    def test_mini_obj_id_base_is_exact_expected_value(self):
        assert MINI_OBJ_ID_BASE == 4294967296


class TestDimensionConstants:
    def test_overworld_is_zero(self):
        assert DIMENSION_OVERWORLD == 0

    def test_nether_is_negative_one(self):
        assert DIMENSION_NETHER == -1

    def test_end_is_one(self):
        assert DIMENSION_END == 1

    def test_dimensions_are_distinct(self):
        assert len({DIMENSION_NETHER, DIMENSION_OVERWORLD, DIMENSION_END}) == 3


class TestSectionFlags:
    def test_section_flags_value(self):
        assert SECTION_FLAGS == 65535


class TestGameModeConstants:
    def test_survival_game_mode(self):
        assert GAMEMODE_SURVIVAL == 1

    def test_creative_game_mode(self):
        assert GAMEMODE_CREATIVE == 3

    def test_game_modes_are_distinct(self):
        assert GAMEMODE_SURVIVAL != GAMEMODE_CREATIVE
