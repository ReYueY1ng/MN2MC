"""Load block/item/mob ID mapping data from YAML files."""

from pathlib import Path
from typing import Dict

import yaml
from loguru import logger

import mn2mc.config as config

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


def _load_yaml_str(filename: str) -> Dict[str, str]:
    """Load a mapping YAML file and return dict with string keys/values."""
    path = _DATA_DIR / filename
    if not path.exists():
        logger.error("Mapping file not found: {}", path)
        raise FileNotFoundError(f"Mapping file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return {str(k): str(v) if v is not None else "" for k, v in raw.items()}


def load_blocks() -> Dict[int, int]:
    """Load MC→Mini block ID mapping from blocks.yaml."""
    return _load_yaml("blocks.yaml")


def load_items() -> Dict[int, int]:
    """Load MC→Mini item ID mapping from items.yaml."""
    return _load_yaml("items.yaml")


def load_mobs() -> Dict[int, int]:
    """Load MC→Mini mob ID mapping from mobs.yaml."""
    return _load_yaml("mobs.yaml")


def load_block_face() -> Dict[int, int]:
    """Load Mini block ID → face capability mapping from block_face.yaml."""
    return _load_yaml("block_face.yaml")


def load_sounds() -> Dict[str, str]:
    """Load Mini SoundPath → MC sound name mapping from sounds.yaml."""
    return _load_yaml_str("sounds.yaml")


def load_mc_sounds() -> Dict[int, str]:
    """Load MC sound ID → name mapping from minecraft-data sounds.json."""
    try:
        import minebase

        minedata = minebase.load_version(config.mc.version)
        sounds = minedata["sounds"]

        return {int(s["id"]): str(s["name"]) for s in sounds}
    except Exception:
        return {}
