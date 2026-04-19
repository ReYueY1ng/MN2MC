from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_BlockUpdateHC
from mn2mc.utils.vector import Vector3
import mn2mc.utils.mini_block as mini_block
import mn2mc.mapping.blocks as block_mapping
import mn2mc.config as config
from javascript import require

prismarine_block = require("prismarine-block")(config.mc["version"])


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    pos = Vector3.from_dict(jsondata["location"]).convert()
    block = prismarine_block.fromStateId(jsondata["type"])
    # logger.debug(block.getProperties())
    if 0 <= pos.y <= 255:
        bid, bex = mini_block.encode_block(
            block_mapping.mc_to_mini(block.type), (pos.x - 1) % 16, pos.y, pos.z % 16
        )
        # logger.info(f'bid {bid}')
        # logger.info(f'x {pos.x // 16} y {pos.z // 16}')
        client.miniplayer.send_packet(
            ePBMsgCode.PB_BLOCK_DATA_UPDATE_HC,
            PB_BlockUpdateHC(
                ChunkX=(pos.x - 1) // 16,
                ChunkZ=pos.z // 16,
                MapID=0,
                Blocks=[bid],
                BlocksEx=[bex],
                BlockStateIndex=[0],
            ).SerializeToString(),
        )


add_event("block_change", on_recv)
