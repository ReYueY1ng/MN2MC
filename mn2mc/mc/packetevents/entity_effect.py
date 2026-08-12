"""Handle MC entity_effect — apply status effects to Mini World entities."""

from __future__ import annotations

from loguru import logger

from mn2mc.mapping import effects as eff_map
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_ActorBuff, ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorBuffChangeHC

_next_buff_instance = 1


def _next_instance() -> int:
    global _next_buff_instance
    i = _next_buff_instance
    _next_buff_instance += 1
    return i


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Apply or refresh a status effect on an entity."""
    entityid = jsondata.get("entityId", 0)
    objid = client.resolve_objid(entityid)
    if objid is None:
        return

    effect_id = jsondata.get("effectId", 0)  # MC effect ID (1-33)
    amplifier = jsondata.get("amplifier", 0)  # 0-based
    duration = jsondata.get("duration", 0)   # ticks
    if duration == -1:
        duration = 21474836
    if amplifier < 0:
        logger.warning(f'Effect {effect_id} amplifier {amplifier} value out of range')
        return
    # flags: 0x01=show_particles, 0x02=show_icon, 0x04=ambient

    # Look up Mini World BuffID
    buff_id = eff_map.mc_to_mini(effect_id, amplifier)
    if buff_id == 0:
        logger.warning("unmapped MC effect {} on entity {}", effect_id, entityid)
        return

    if amplifier > 3:
        logger.warning(f"effect {effect_id} (->buff {buff_id}) lv{amplifier} may not be supported")

    # Build the buff instance
    buff = PB_ActorBuff(
        BuffID=buff_id,
        BuffLV=amplifier,          # Mini LV is 1-based
        Ticks=duration,                 # same tick unit
        BuffInstanceId=_next_instance(),
        RandomValue=0,
    )

    # Track buffs on the entity
    entity = client.entities.get(entityid)
    if entity is None:
        logger.warning("entity_effect: unknown entity {}", entityid)
        return

    entity.buffs[effect_id] = {
        "buff_id": buff_id,
        "amplifier": amplifier,
        "duration": duration,
        "instance_id": buff.BuffInstanceId,
    }

    # Build full buff list for this entity
    buffs_list = [buff]
    for eid, data in entity.buffs.items():
        if eid == effect_id:
            continue  # already added
        buffs_list.append(PB_ActorBuff(
            BuffID=data["buff_id"],
            BuffLV=data["amplifier"] + 1,
            Ticks=data["duration"],
            BuffInstanceId=data["instance_id"],
            RandomValue=0,
        ))

    msg = PB_ActorBuffChangeHC(
        ObjID=objid,
        Buffs=buffs_list,
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_BUFF_CHANGE_HC, msg)

    logger.debug(
        "effect {} (->buff {}) lv{} {}t applied to entity {}",
        effect_id, buff_id, amplifier + 1, duration, objid,
    )


add_event("entity_effect", on_recv)
