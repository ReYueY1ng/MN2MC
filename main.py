import mn2mc
import atexit
import javascript
import asyncio
import sys
import signal
from loguru import logger
from javascript import require
import mn2mc.mini.server as server
import mn2mc.config as config
import mn2mc.utils.protobuf_parser as protobuf_parser


def prepare_dependencies():
    logger.info("Preparing Node.js dependencies...")
    mcprotocol = require("minecraft-protocol")
    prismarineChat = require("prismarine-chat")
    prismarineBlock = require("prismarine-block")
    prismarineChunk = require("prismarine-chunk")
    Vec3 = require("vec3")
    msgpackr = require("msgpackr")
    prismarineItem = require('prismarine-item')
    prismarineRegistry = require('prismarine-registry')
    javascript.eval_js("""
        global.mcprotocol = mcprotocol
        global.prismarineChat = prismarineChat
        global.prismarineBlock = prismarineBlock
        global.prismarineChunk = prismarineChunk
        global.Vec3 = Vec3
        global.msgpackr = msgpackr
        global.prismarineItem = prismarineItem
        global.prismarineRegistry = prismarineRegistry
    """)


@atexit.register
def signal_handler(signal=None, frame=None):
    if mn2mc.running:
        logger.info("Stopping server")
        if "mn2mc.mc.packetevents.chunk.parsed_chunk" in sys.modules:
            sys.modules["mn2mc.mc.packetevents.chunk.parsed_chunk"].stop()
        elif "mn2mc.mc.packetevents.chunk.map_chunk" in sys.modules:
            sys.modules["mn2mc.mc.packetevents.chunk.map_chunk"].stop()
        server.stop()
        sys.exit(0)


async def main():
    logger.add("logs/{time}.log")
    config.load()
    prepare_dependencies()
    if config.debug:
        protobuf_parser.init()
    signal.signal(signal.SIGINT, signal_handler)
    await server.start(config.mini["server"]["ip"], config.mini["server"]["port"])


if __name__ == "__main__":
    asyncio.run(main())
