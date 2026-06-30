"""Tests for mapping consistency between blocks.yaml and items.yaml."""

import json
from pathlib import Path

import pytest
import yaml


@pytest.fixture
def blocks_map():
    """Load blocks.yaml mapping."""
    path = Path(__file__).parent.parent / "mn2mc" / "data" / "blocks.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def items_map():
    """Load items.yaml mapping."""
    path = Path(__file__).parent.parent / "mn2mc" / "data" / "items.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def mc_blocks():
    """Load MC blocks.json."""
    path = Path(__file__).parent.parent / ".venv" / "lib" / "python3.14" / "site-packages" / "minebase" / "data" / "data" / "pc" / "1.21.11" / "blocks.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def mc_items():
    """Load MC items.json."""
    path = Path(__file__).parent.parent / ".venv" / "lib" / "python3.14" / "site-packages" / "minebase" / "data" / "data" / "pc" / "1.21.11" / "items.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class TestMappingConsistency:
    """Test mapping validity (note: MC block IDs and item IDs are separate namespaces)."""

    def test_blocks_mapping_has_all_mc_blocks(self, blocks_map, mc_blocks):
        """blocks.yaml should have an entry for every MC block."""
        block_ids = {b['id'] for b in mc_blocks}
        missing = block_ids - set(blocks_map.keys())
        assert len(missing) == 0, f"Missing MC blocks: {missing}"

    def test_items_mapping_has_all_mc_items(self, items_map, mc_items):
        """items.yaml should have an entry for every MC item."""
        item_ids = {i['id'] for i in mc_items}
        missing = item_ids - set(items_map.keys())
        assert len(missing) == 0, f"Missing MC items: {missing}"

    def test_blocks_values_are_non_negative(self, blocks_map):
        """All block mini IDs should be non-negative."""
        assert all(v >= 0 for v in blocks_map.values())

    def test_items_values_are_non_negative(self, items_map):
        """All item mini IDs should be non-negative."""
        assert all(v >= 0 for v in items_map.values())

    def test_items_high_ids_no_self_mapping(self, items_map):
        """No item with ID >= 1166 should map to itself (auto-generated placeholder)."""
        bad = [mc_id for mc_id, mini_id in items_map.items() if mc_id >= 1166 and mc_id == mini_id]
        assert len(bad) == 0, f"Self-mapping high IDs: {bad}"
