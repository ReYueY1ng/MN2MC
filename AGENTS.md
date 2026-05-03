# AGENTS.md

MN2MC — Protocol translation proxy between 迷你世界 1.55.0 and Minecraft Java 1.21.11.

## How to run

```bash
python main.py
```

Config is auto-generated on first run. `config.yaml` is gitignored.

## Dependencies (non-obvious)

These are **not on PyPI** — must clone and `pip install` manually:

```bash
git clone https://github.com/wu-vincent/aiorak.git && pip install ./aiorak
git clone https://github.com/py-mine/minebase.git --depth=1 && \
  git clone https://github.com/PrismarineJS/minecraft-data.git minebase/minebase/data --depth=1 && \
  pip install ./minebase
```

`requirements.txt` has them commented out — read the README for full setup.

Node.js deps are required for the MC client bridge:
```bash
npm install minecraft-protocol prismarine-chat prismarine-block prismarine-chunk vec3 msgpackr prismarine-item prismarine-registry
```

## Architecture

```
Mini World client <--aiorak--> mn2mc/mini/ (server) <--bridge--> mn2mc/mc/ (client) <--TCP--> MC server
```

### Package boundaries

| Directory | Role |
|---|---|
| `mn2mc/mini/` | Mini World server side — RakNet (aiorak) server, packet codec, protobuf message handlers |
| `mn2mc/mc/` | Minecraft client side — wraps `minecraft-protocol` (Node.js via `javascript` bridge), MC event handlers |
| `mn2mc/mapping/` | ID translation tables: `blocks.py`, `items.py`, `mobs.py`, `face.py`, `slotid.py` |
| `mn2mc/mini/proto/` | Pre-compiled Protocol Buffer `.py`/`.pyi` files (ch, hc, common messages) |
| `mn2mc/utils/` | Utilities: XXTEA crypto, protobuf debug parser, color converter, vector math |
| `resources/` | Reference data, C++ test code, JSON — not imported at runtime |
| `tools/` | `mitm.py` for mitmproxy HTTP interception |

### Flow

1. `main.py` → `config.load()`, `prepare_dependencies()` (Node.js bridge init), `server.start()`
2. `server.start()` → Mini World auth login, room creation, start aiorak listener
3. On Mini World client connect → `server.handler()` creates `MiniPlayer`, pumps packets
4. `MiniPlayer` receives `PB_ROLE_ENTER_WORLD_CH` → `enter_world.py` creates `MCClient` connecting to MC server
5. `MCClient` ↔ `MiniPlayer` bidirectional translation via event handlers in `packetevents/`

### Event system

Both sides use identical patterns:
- `mn2mc/mc/packet.py` — `add_event(event_name, func)` for MC packets (string-keyed)
- `mn2mc/mini/packet.py` — `add_event(msgcode, func)` for Mini World packets (int-keyed by protobuf msgcode)
- Event handlers auto-imported from `packetevents/__init__.py` via `import_module` glob

## Key quirks

### Node.js bridge (`javascript` package)

The `javascript` PyPI package bridges Python ↔ Node.js. Used in `main.py` (`prepare_dependencies`) and `mc/client.py`. Shared globals like `global.mcprotocol`, `global.Vec3` are set via `javascript.eval_js()`. Do not assume these are available until `prepare_dependencies()` has run.

### Two chunk parsing modes

Config key `mc.use_new_chunk_parser`:
- `true` (default): Uses `chunk.js` + `parsed_chunk.py` — lower JS↔Py overhead, but may timeout
- `false`: Uses `map_chunk.py` — pure Python parsing

Old map_chunk files (`_map_chunk_old*.py`) are legacy, not imported at runtime.

### Config is auto-generated

`config.yaml` is gitignored. `config.py` has defaults in `default_file` string. If the file doesn't exist, it's written with defaults. When editing config schema, update both `default_file` and the TypedDict classes.

### Protobuf files are pre-compiled

Files in `mn2mc/mini/proto/` are pre-compiled from `.proto` sources (not in the repo). To regenerate, you need the `.proto` files from the Mini World client. Do not edit `.py`/`.pyi` files directly.

### No tests

There is no test suite. All testing is manual — start the proxy, connect a Mini World client, verify against an MC server.

### Hardcoded authentication

`mini/auth.py` contains hardcoded MD5 key `2ddb7619717147439c83ab022e9d4d38` and `room.py` contains hardcoded `AUTH_KEY`. These are from the Mini World client binary. The auth module also hardcodes a login server URL.

### Block mapping is enormous

`mapping/blocks.py` is ~1100 lines of `mc_to_mini_mapping` dict. This is the primary mapping source. Unknown MC blocks default to Mini ID 0 (air) — check the lookup logic before assuming fallback behavior.

### aiorak protocol

Mini World uses a custom RakNet-derived protocol. Packet format:
- Client→Server: `\x89` + 4-byte big-endian uin + 8-byte placeholder + 2-byte little-endian msgcode + 2-byte length + data
- Server→Client: `\x89` + 2-byte little-endian msgcode + 2-byte length + data

The `aiorak` server is created with `guid=666`.

### Global state

- `mn2mc.running` — set to `False` to shut down
- `mn2mc.mini.player.players` — global list of all connected MiniPlayer instances
- `mn2mc.config.mini`, `mn2mc.config.mc`, `mn2mc.config.debug` — global config (loaded at startup)
- Node.js globals via `javascript.eval_js` — shared across all MCClient instances

## Conventions

- **Logging**: `loguru` throughout. Logs go to `logs/{time}.log`. Use `logger.info/debug/error/exception`.
- **TypedDict** for config, otherwise mostly untyped
- **Async**: `aiorak` connections and `MCClient` packet handling are async. Node.js bridge calls are synchronous.
- **Threading**: `MCClient.get_chunk_thread` runs a separate thread for chunk polling. Thread safety is minimal.
- **Error handling**: Packet event handlers catch exceptions and log them via `logger.exception` — errors in one handler won't crash the server.
- **Config changes**: Update both the TypedDict classes and the `default_file` YAML string in `config.py`.
