"""Load block/item/mob ID mapping data from JSON files."""

import json
from pathlib import Path
from typing import Dict

from loguru import logger

_DATA_DIR = Path(__file__).parent


def _load_json(filename: str) -> Dict[int, int]:
    """Load a mapping JSON file and return dict with int keys/values.

    The JSON file stores string keys (JSON requires string keys),
    so we convert them back to int for the mapping dicts.
    """
    path = _DATA_DIR / filename
    if not path.exists():
        logger.error("Mapping file not found: {}", path)
        raise FileNotFoundError(f"Mapping file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw: Dict[str, int] = json.load(f)

    return {int(k): v for k, v in raw.items()}


def load_blocks() -> Dict[int, int]:
    """Load MC→Mini block ID mapping from blocks.json."""
    return _load_json("blocks.json")


def load_items() -> Dict[int, int]:
    """Load MC→Mini item ID mapping from items.json."""
    return _load_json("items.json")


def load_mobs() -> Dict[int, int]:
    """Load MC→Mini mob ID mapping from mobs.json."""
    return _load_json("mobs.json")
