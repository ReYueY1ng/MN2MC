import signal
import javascript
import asyncio
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
    prismarineItem = require("prismarine-item")
    prismarineRegistry = require("prismarine-registry")
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


stop_task: asyncio.Task | None = None


async def stop():
    logger.info("Shutting down...")
    await server.stop()


def signal_handler(sig, frame):
    global stop_task
    logger.info(f"Received signal {sig}")
    if not stop_task:
        stop_task = asyncio.get_running_loop().create_task(stop())


@logger.catch
async def main():
    global stop_task
    logger.add("logs/{time}.log")
    config.load()
    prepare_dependencies()
    if config.debug:
        protobuf_parser.init()
    try:
        signal.signal(signal.SIGINT, signal_handler)
        javascript.eval_js("""
            const process = require('node:process')
            process.on('SIGINT', () => {})
        """)
        await server.start(config.mini["server"]["ip"], config.mini["server"]["port"])
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        if not stop_task:
            stop_task = asyncio.get_running_loop().create_task(stop())
        await stop_task


if __name__ == "__main__":
    asyncio.run(main())
