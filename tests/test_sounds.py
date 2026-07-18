"""Tests for mn2mc.mapping.sounds — sound name mapping between MC and Mini World."""

from mn2mc.mapping import sounds


class TestSoundMappingData:
    def test_mc_to_mini_mapping_is_dict(self):
        assert isinstance(sounds.mc_to_mini_mapping, dict)

    def test_mc_to_mini_mapping_not_empty(self):
        assert len(sounds.mc_to_mini_mapping) > 0

    def test_mc_to_mini_mapping_keys_are_str(self):
        for key in sounds.mc_to_mini_mapping:
            assert isinstance(key, str)

    def test_mc_to_mini_mapping_values_are_str(self):
        for val in sounds.mc_to_mini_mapping.values():
            assert isinstance(val, str)

    def test_mini_to_mc_mapping_is_dict(self):
        assert isinstance(sounds.mini_to_mc_mapping, dict)

    def test_mini_to_mc_mapping_not_empty(self):
        assert len(sounds.mini_to_mc_mapping) > 0


class TestMcToMini:
    def test_known_block_stone_break(self):
        assert sounds.mc_to_mini("block.stone.break") == "blockd.stone1"

    def test_known_block_wood_step(self):
        assert sounds.mc_to_mini("block.wood.step") == "blocks.wood1"

    def test_known_entity_zombie_ambient(self):
        assert sounds.mc_to_mini("entity.zombie.ambient") == "ent.3101.idle1"

    def test_known_entity_pig_hurt(self):
        assert sounds.mc_to_mini("entity.pig.hurt") == "ent.3400.hit1"

    def test_unknown_returns_empty(self):
        assert sounds.mc_to_mini("nonexistent.sound") == ""

    def test_empty_string_returns_empty(self):
        assert sounds.mc_to_mini("") == ""


class TestMiniToMc:
    def test_known_blockd_stone1(self):
        result = sounds.mini_to_mc("blockd.stone1")
        assert result.startswith("block.") or result.startswith("entity.")

    def test_known_blocks_wood1(self):
        result = sounds.mini_to_mc("blocks.wood1")
        assert result.startswith("block.") or result.startswith("entity.")

    def test_known_ent_3101_idle1(self):
        result = sounds.mini_to_mc("ent.3101.idle1")
        assert result.startswith("entity.") or result.startswith("block.")

    def test_unknown_returns_empty(self):
        assert sounds.mini_to_mc("nonexistent.path") == ""

    def test_empty_string_returns_empty(self):
        assert sounds.mini_to_mc("") == ""
