"""Sound name mapping between Minecraft (1.21.11) and Mini World.

Mapping logic:
- MC sound name → Mini World SoundPath (from sound.csv)
- Unmapped sounds → "" (silent no-op)

The YAML file (sounds.yaml) maps MC sound name → Mini SoundPath.
"""

from mn2mc.data.loader import load_mc_sounds, load_sounds

# MC sound name → Mini World SoundPath
mc_to_mini_mapping: dict[str, str] = load_sounds()

# Mini World SoundPath → MC sound name (reversed)
mini_to_mc_mapping: dict[str, str] = {v: k for k, v in mc_to_mini_mapping.items()}

# MC sound ID → name (from minecraft-data)
_mc_id_to_name: dict[int, str] = load_mc_sounds()


def mc_to_mini(name: str) -> str:
    """Convert MC sound name to Mini World SoundPath."""
    return mc_to_mini_mapping.get(name, "")

def mc_id_to_name(sound_id: int) -> str:
    """Convert MC sound ID to MC sound name."""
    # sound id 有偏移问题，https://github.com/PrismarineJS/minecraft-data/issues/897
    name = _mc_id_to_name.get(sound_id + 1, "")
    return name or ""

def mc_id_to_mini(sound_id: int) -> str:
    """Convert MC sound ID to Mini World SoundPath."""
    name = _mc_id_to_name.get(sound_id, "")
    if not name:
        return ""
    return mc_to_mini_mapping.get(name, "")


def mini_to_mc(name: str) -> str:
    """Convert Mini World SoundPath to MC sound name."""
    return mini_to_mc_mapping.get(name, "")
