import json
import javascript
from loguru import logger
from javascript import require

import mn2mc.config as config
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode, PB_ChunkSaveDB, PB_ChunkBlob
from mn2mc.mini.proto.hc import PB_SyncChunkDataHC, PB_BlockUpdateHC

Buffer = require("Buffer")
prismarine_chunk = require("prismarine-chunk")(config.mc["version"])
Vec3 = require("vec3")

with open("air", "rb") as f:
    air = f.read()


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    # threading.Thread(target=parse_chunk, args=(client, jsondata)).start()
    parse_chunk(client, jsondata)


def parse_chunk(client: MCClient, jsondata: dict):
    chunk = prismarine_chunk()
    chunk.load(Buffer["from"](jsondata["chunkData"]["data"]))

    minichunk = PB_SyncChunkDataHC(
        SectionFlags=65535,
        Initialize=1,
        ChunkData=PB_ChunkSaveDB(
            OWID=10239475674329,
            MapID=0,
            x=jsondata["x"],
            z=jsondata["z"],
            ChunkBlob=PB_ChunkBlob(UnzipLen=805308264, BlobLen=554, BlobDetail=air),
        ),
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_SYNC_CHUNK_DATA_HC, minichunk)
    blocks = []
    blocksex = []
    for y in range(256):
        # ms = time.time()

        # 跨进程多次调用，太卡了，不用这个
        """
        for x in range(16):
            for z in range(16):
                block = chunk.getBlock(Vec3(x, y, z))
                if hasattr(block, 'name') and block.name != 'air':
                    bid, bex = mini_block.encode_block(100, x, y, z)
                    blocks.append(bid)
                    blocksex.append(bex)
        """
        try:
            bjson = javascript.eval_js("""
                const Vec3 = require('vec3')
                let bs = [];
                let bsex = [];
                for (let x = 0; x < 16; x++) {
                    for (let z = 0; z < 16; z++) {
                        let block = chunk.getBlock(Vec3(x, y, z));
                        if (block.name != "air")
                        {
                            let be = MiniBlock.encodeBlock(100, x, y, z);
                            //console.log(b);
                            bs.push(be.encoded);
                            bsex.push(be.quotient);
                        }
                    }
                }
                return JSON.stringify({blocks: bs, blocksex: bsex});
            """)
        except Exception as e:
            logger.exception(f"Failed to parse chunk: {str(e)}")
            return
        bdata = json.loads(bjson)
        blocks += bdata["blocks"]
        blocksex += bdata["blocksex"]
        # logger.debug(f'Decode 256 blocks cost {(time.time() - ms) * 1000}ms')
        if y % 8 == 0 and len(blocksex) > 0:
            client.miniplayer.send_packet(
                ePBMsgCode.PB_BLOCK_DATA_UPDATE_HC,
                PB_BlockUpdateHC(
                    ChunkX=jsondata["x"],
                    ChunkZ=jsondata["z"],
                    MapID=0,
                    Blocks=blocks,
                    BlocksEx=blocksex,
                    BlockStateIndex=[0 for _ in range(len(blocksex))],
                ).SerializeToString(),
            )
            blocks.clear()
            blocksex.clear()


add_event("map_chunk", on_recv)
