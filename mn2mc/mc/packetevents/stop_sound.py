"""Handle MC stop_sound — send stop command via TriggerSound."""

from __future__ import annotations

from loguru import logger

from mn2mc.mapping import sounds
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_EffectTriggerSound, ePBEffectType, ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayEffectHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    sound = jsondata.get("sound", None)
    if not sound:
        return

    if 'data' in sound:
        sound_name = sound['data']['soundName'].replace("minecraft:", "")
    else:
        sound_id = sound['soundId']
        sound_name = sounds.mc_id_to_name(sound_id)

    mini_path = sounds.mc_to_mini(sound_name)
    if not mini_path:
        logger.debug("unmapped MC stop_sound: {}", sound_name)
        return

    msg = PB_PlayEffectHC(
        EffectType=ePBEffectType.PB_EFFECT_TIRGGERSOUND,
        TriggerSound=PB_EffectTriggerSound(
            Name=mini_path,
            PlayState=2,
        ),
    )

    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYEFFECT_HC, msg.SerializeToString())
    logger.debug("stop_sound {} -> {}", sound_name, mini_path)


add_event("stop_sound", on_recv)
