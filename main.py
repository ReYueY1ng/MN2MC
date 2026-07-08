import asyncio
import signal

import javascript
from javascript import require
from loguru import logger

import mn2mc.config as config
import mn2mc.mini.server as server
import mn2mc.utils.protobuf_parser as protobuf_parser


def prepare_dependencies():
    global current_loop
    logger.info("Preparing Node.js dependencies...")

    javascript.globalThis.mcprotocol = require("minecraft-protocol")
    javascript.globalThis.prismarineChat = require("prismarine-chat")
    javascript.globalThis.prismarineBlock = require("prismarine-block")
    javascript.globalThis.prismarineChunk = require("prismarine-chunk")
    javascript.globalThis.Vec3 = require("vec3")
    javascript.globalThis.msgpackr = require("msgpackr")
    javascript.globalThis.prismarineItem = require("prismarine-item")
    javascript.globalThis.prismarineRegistry = require("prismarine-registry")
    javascript.globalThis.stop_mn2mc = create_stop_task
    javascript.globalThis.logger = logger

    current_loop = asyncio.get_running_loop()
    javascript.eval_js("""
        process.on('uncaughtException', (err) => {
            console.error('Uncaught javascript Exception:\\n' + err.stack)
        })
    """)


stop_task: asyncio.Task | None = None
current_loop: asyncio.AbstractEventLoop


async def stop():
    logger.info("Shutting down...")
    await server.stop()


def create_stop_task():
    global stop_task
    if not stop_task:
        stop_task = current_loop.create_task(stop())


def signal_handler(sig, frame):
    global stop_task
    logger.info(f"Received signal {sig}")
    create_stop_task()


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
        await server.start(config.mini.server.ip, config.mini.server.port)
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        create_stop_task()
        await stop_task  #ty:ignore[invalid-await]


if __name__ == "__main__":
    asyncio.run(main())
