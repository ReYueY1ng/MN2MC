"""Handle MC entity_sound_effect — translate entity sounds to Mini World PB_PlayEffectHC."""

from __future__ import annotations

from loguru import logger

from mn2mc.mapping import sounds
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_EffectTriggerSound, ePBEffectType, ePBMsgCode
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

    entityid = jsondata.get("entityId", 0)
    objid = client.resolve_objid(entityid)
    if objid is None:
        logger.debug("entity_sound_effect: unknown entity {}", entityid)
        return

    volume = float(jsondata.get("volume", 1.0))
    pitch = float(jsondata.get("pitch", 1.0))

    msg = PB_PlayEffectHC(
        EffectType=ePBEffectType.PB_EFFECT_TIRGGERSOUND,
        TriggerSound=PB_EffectTriggerSound(
            Name=mini_path,
            Volume=volume,
            Pitch=pitch,
            PlayState=1,
            ObjId=objid,
        ),
    )

    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYEFFECT_HC, msg.SerializeToString())
    logger.debug("entity sound {} -> {} on entity {}", sound_name, mini_path, objid)


add_event("entity_sound_effect", on_recv)
