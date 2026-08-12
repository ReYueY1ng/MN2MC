"""Handle MC entity_sound_effect — translate entity sounds to Mini World PB_PlayEffectHC."""

from __future__ import annotations

from loguru import logger

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents._sound import resolve_sound_path
from mn2mc.mini.proto.common import PB_EffectTriggerSound, ePBEffectType, ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayEffectHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    result = resolve_sound_path(jsondata)
    if result is None:
        return
    sound_name, mini_path = result

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
