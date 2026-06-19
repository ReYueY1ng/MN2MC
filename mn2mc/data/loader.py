"""Load block/item/mob ID mapping data from YAML files."""

import yaml
from pathlib import Path
from typing import Dict

from loguru import logger

_DATA_DIR = Path(__file__).parent


def _load_yaml(filename: str) -> Dict[int, int]:
    """Load a mapping YAML file and return dict with int keys/values."""
    path = _DATA_DIR / filename
    if not path.exists():
        logger.error("Mapping file not found: {}", path)
        raise FileNotFoundError(f"Mapping file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return {int(k): v for k, v in raw.items()}


def load_blocks() -> Dict[int, int]:
    """Load MC→Mini block ID mapping from blocks.yaml."""
    return _load_yaml("blocks.yaml")


def load_items() -> Dict[int, int]:
    """Load MC→Mini item ID mapping from items.yaml."""
    return _load_yaml("items.yaml")


def load_mobs() -> Dict[int, int]:
    """Load MC→Mini mob ID mapping from mobs.yaml."""
    return _load_yaml("mobs.yaml")
