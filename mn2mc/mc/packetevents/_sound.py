"""Shared sound-name resolution helper for MC→Mini World packet handlers."""

from __future__ import annotations

from loguru import logger

from mn2mc.mapping import sounds


def resolve_sound_path(jsondata: dict) -> tuple[str, str] | None:
    """Resolve an MC sound_effect / entity_sound_effect payload to a Mini World sound path.

    Returns ``(sound_name, mini_path)`` on success, or None when the sound is
    missing or unmapped (a debug log is emitted in the unmapped case).
    """
    sound = jsondata.get("sound")
    if not sound:
        return None

    if "data" in sound:
        sound_name = sound["data"]["soundName"].replace("minecraft:", "")
    else:
        sound_id = sound["soundId"]
        sound_name = sounds.mc_id_to_name(sound_id)

    mini_path = sounds.mc_to_mini(sound_name)

    if not mini_path:
        logger.debug("unmapped MC sound: {}", sound_name)
        return None

    return sound_name, mini_path
