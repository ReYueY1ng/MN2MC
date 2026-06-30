"""Effect/buff mapping between Minecraft (1.21.11) effects and Mini World buffs.

Mapping logic:
- MC effect ID → Mini World buff base ID (level 1)
- MC amplifier → Mini buff level via offset pattern
- Unmapped effects → 0 (no-op)

Mini World buffs use sequential IDs for levels:
  - Base ID like 4001 = 疾跑1级 (level 1)
  - 4002 = 疾跑2级 (level 2)
  - 4003 = 疾跑3级 (level 3)
  - etc.
"""

from pathlib import Path
import csv
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# MC effect ID → Mini buff base ID (level 1)
mc_to_mini_mapping: dict[int, int] = {}

# Reverse: Mini buff ID → MC effect ID (only for level-1 buffs)
mini_to_mc_mapping: dict[int, int] = {}


def _load_yaml_mapping() -> dict[int, int]:
    """Load MC→Mini effect ID mapping from effects.yaml."""
    import yaml

    path = DATA_DIR / "effects.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Mapping file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return {int(k): int(v) for k, v in raw.items() if v is not None}


def _load_buffdef_csv() -> dict[int, dict]:
    """Load Mini World buff definitions from buffdef.csv for level lookup."""
    # The CSV can be at multiple locations; try standard paths
    csv_paths = [
        Path("/run/media/yuey1ng/F25A9F0C5A9ECD2B/mini/dump/script_decompiled/csvdef/utf8/buffdef.csv"),
        DATA_DIR / "buffdef.csv",
    ]

    buffs: dict[int, dict] = {}
    for csv_path in csv_paths:
        if csv_path.exists():
            try:
                with open(csv_path, "r", encoding="utf-8") as f:
                    # CSV has Chinese header row 1, English header row 2
                    chinese_headers = next(f).strip().split(",")
                    english_headers = next(f).strip().split(",")

                    col_index = {h: i for i, h in enumerate(chinese_headers)}

                    id_col = col_index.get("状态ID")
                    name_col = col_index.get("名字")
                    lvl_col = col_index.get("等级", None)
                    type_col = col_index.get("类型", None)

                    if id_col is None:
                        continue

                    reader = csv.reader(f)
                    for row in reader:
                        if not row or len(row) <= id_col:
                            continue
                        try:
                            bid = int(row[id_col].strip())
                        except (ValueError, IndexError):
                            continue
                        buffs[bid] = {
                            "name": row[name_col].strip() if name_col is not None and len(row) > name_col else "",
                            "level": int(row[lvl_col].strip()) if lvl_col is not None and len(row) > lvl_col and row[lvl_col].strip() else 1,
                            "type": int(row[type_col].strip()) if type_col is not None and len(row) > type_col and row[type_col].strip() else 0,
                        }
            except Exception:
                pass  # Non-critical, mapping works without it
            break  # noqa: SIM113

    return buffs


def get_mini_buff_for_level(buff_base_id: int, mc_amplifier: int = 0) -> int:
    """Convert a buff base ID + MC amplifier to the correct Mini buff level ID.

    Mini buffs typically increment ID by 1 per level from the base:
      base (level 1) = X001
      level 2       = X002
      level 3       = X003
      etc.

    MC amplifier starts at 0, so amplifier 0 → level 1, amplifier 1 → level 2, etc.
    Clamps to available levels (4 max for most buffs).
    """
    # Parse the base pattern: last digit is the level
    level = mc_amplifier + 1
    if level < 1:
        level = 1
    if level > 10:
        level = 10  # safety cap, most have ≤4 levels

    # The base ID is the level-1 ID; add offset for higher levels
    return buff_base_id + (level - 1) if buff_base_id != 0 else 0


# Initialize mappings
mc_to_mini_mapping = _load_yaml_mapping()
mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items() if v != 0}

# Load buffdef for reference (not strictly required for basic mapping)
_buff_index = _load_buffdef_csv()

def mc_to_mini(effect_id: int, amplifier: int = 0) -> int:
    """Convert MC effect ID to Mini World buff ID.

    Args:
        effect_id: MC effect ID (0-39 per 1.21.11)

    Returns:
        Mini World buff ID, or 0 if no mapping exists
    """
    base_id = mc_to_mini_mapping.get(effect_id, 0)
    if base_id == 0:
        return 0
    return base_id

def mini_to_mc(buff_id: int) -> Optional[int]:
    """Reverse lookup: Mini World buff ID → MC effect ID.

    Only returns the base MC effect, without amplifier info.
    """
    # Need to find which base buff ID this corresponds to
    for base_id in sorted(mini_to_mc_mapping.keys(), reverse=True):
        if buff_id >= base_id and buff_id < base_id + 10:
            # Check if the offset is reasonable (within a few levels)
            offset = buff_id - base_id
            if offset <= 9:
                return mini_to_mc_mapping[base_id]
    return None


def lookup_buff_name(buff_id: int) -> Optional[str]:
    """Look up the Chinese name of a Mini World buff by its ID."""
    buff = _buff_index.get(buff_id)
    if buff:
        return buff["name"]
    # Try nearby IDs (might be a different level)
    for delta in range(-5, 6):
        if delta == 0:
            continue
        buff = _buff_index.get(buff_id + delta)
        if buff:
            return buff["name"]
    return None


# For direct import compatibility with other mapping modules
def mc_id_to_mini_id(effect_id: int) -> int:
    """Simple ID lookup without level handling (match other mapping APIs)."""
    return mc_to_mini_mapping.get(effect_id, 0)
