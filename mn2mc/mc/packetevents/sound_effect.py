"""Handle MC sound_effect — translate MC sounds to Mini World PB_PlayEffectHC."""

from __future__ import annotations

from loguru import logger

from mn2mc.mapping import sounds
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_EffectTriggerSound, PB_Vector3, ePBEffectType, ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayEffectHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    sound = jsondata.get("sound")
    if not sound:
        return

    if 'data' in sound:
        sound_name = sound['data']['soundName'].replace("minecraft:", "")
    else:
        sound_id = sound['soundId']
        sound_name = sounds.mc_id_to_name(sound_id)

    mini_path = sounds.mc_to_mini(sound_name)

    if not mini_path:
        logger.debug("unmapped MC sound: {}", sound_name)
        return

    # MC fixed-point coords (1/8 block) → Mini World block coords, X negated
    x = -jsondata.get("x", 0) // 8
    y = jsondata.get("y", 0) // 8
    z = jsondata.get("z", 0) // 8
    pos = PB_Vector3(X=x, Y=y, Z=z)

    volume = float(jsondata.get("volume", 1.0))
    pitch = float(jsondata.get("pitch", 1.0))

    msg = PB_PlayEffectHC(
        EffectType=ePBEffectType.PB_EFFECT_TIRGGERSOUND,
        TriggerSound=PB_EffectTriggerSound(
            Name=mini_path,
            Volume=volume,
            Pitch=pitch,
            PlayState=1,
            Pos=pos,
        ),
    )

    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYEFFECT_HC, msg.SerializeToString())
    logger.debug("sound {} -> {} at ({}, {}, {})", sound_name, mini_path, pos.X, pos.Y, pos.Z)


add_event("sound_effect", on_recv)
