import mn2mc
import javascript
import asyncio
import sys
from loguru import logger
from javascript import require
import mn2mc.mini.server as server
import mn2mc.mini.room
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


@logger.catch
async def main():
    logger.add("logs/{time}.log")
    config.load()
    prepare_dependencies()
    if config.debug:
        protobuf_parser.init()
    try:
        await server.start(config.mini["server"]["ip"], config.mini["server"]["port"])
    except (KeyboardInterrupt, asyncio.CancelledError):
        logger.info("Shutting down...")
    finally:
        await server.stop()
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
