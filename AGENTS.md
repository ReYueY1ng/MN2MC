# AGENTS.md

MN2MC — Protocol translation proxy between 迷你世界 1.57.1 and Minecraft Java 1.21.11.

## Requirements

- Python 3.13+
- Node.js (for the MC client bridge)

## How to run

```bash
python main.py
```

Config is auto-generated on first run. `config.yaml` is gitignored.

## Dependencies (non-obvious)

These are **not on PyPI** — specified as git dependencies in `requirements.txt`:

```bash
pip install -r requirements.txt
```

`aiorak` and `minebase` are installed from GitHub. `minebase` requires `minecraft-data` cloned into its data directory — see README for manual setup if pip install fails.

Optional: KREN shared memory IPC (requires Rust toolchain):
```bash
pip install kren
```

Node.js deps are required for the MC client bridge:
```bash
npm install minecraft-protocol prismarine-chat prismarine-block prismarine-chunk vec3 msgpackr prismarine-item prismarine-registry
```

## Developer commands

```bash
python -m pytest                          # run all tests (pytest is not in requirements.txt — install separately)
python -m pytest tests/test_blocks.py     # run single test file
python -m pytest -k "test_name"           # run single test by name
ruff check mn2mc                          # lint (ruff)
ruff format mn2mc                         # format (ruff)
ty check mn2mc                            # typecheck (ty)
```

`ruff` and `ty` are configured in `pyproject.toml`. Proto files (`mn2mc/mini/proto/`) are excluded from both.

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
| `mn2mc/data/` | YAML mapping files (`blocks.yaml`, `items.yaml`, `mobs.yaml`) loaded by `loader.py` |
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

`config.yaml` is gitignored. `config.py` has defaults in `default_file` string. If the file doesn't exist, it's written with defaults. Config uses Pydantic models for validation. When editing config schema, update both the Pydantic model classes and the `default_file` YAML string.

### Protobuf files are pre-compiled

Files in `mn2mc/mini/proto/` are pre-compiled from `.proto` sources (not in the repo). To regenerate, you need the `.proto` files from the Mini World client. Do not edit `.py`/`.pyi` files directly.

### Tests

Tests exist in `tests/` (10 files). `pyproject.toml` configures pytest with `asyncio_mode = "auto"`, but pytest is not in `requirements.txt` — install separately. Tests cover mapping data, utils, packet encoding, and constants. No integration tests.

### Hardcoded authentication

`mini/auth.py` contains hardcoded MD5 key `2ddb7619717147439c83ab022e9d4d38` and `room.py` contains hardcoded `AUTH_KEY`. These are from the Mini World client binary. The auth module also hardcodes a login server URL.

### Block mapping

`mapping/blocks.py` loads from `data/blocks.yaml` via `data/loader.py`. The YAML files (`blocks.yaml`, `items.yaml`, `mobs.yaml`) are the primary mapping source. Unknown MC blocks default to Mini ID 470 (question mark block) — check the lookup logic before assuming fallback behavior. Reverse mappings (`mini_to_mc`) are auto-generated (last-wins on collisions).

### aiorak protocol

Mini World uses a custom RakNet-derived protocol. Packet format:
- Client→Server: `\x89` + 4-byte big-endian uin + 4-byte big-endian touin + 2-byte little-endian msgcode + 2-byte length + data
- Server→Client: `\x89` + 2-byte little-endian msgcode + 2-byte length + data

The `aiorak` server is created with `guid=666`.

### Global state

- `mn2mc.running` — set to `False` to shut down
- `mn2mc.mini.player.players` — global list of all connected MiniPlayer instances
- `mn2mc.config.mini`, `mn2mc.config.mc`, `mn2mc.config.debug` — global config (loaded at startup)
- Node.js globals via `javascript.eval_js` — shared across all MCClient instances

### Module `__getattr__` proxy pattern

`config`, `events`, `auth`, `room`, `wsconn` use `__getattr__` to expose singleton attributes at module level (e.g. `import mn2mc.config as config` then `config.mini`). `TYPE_CHECKING` guards provide static type hints. When adding attributes to these modules, update both the class and the `TYPE_CHECKING` block.

## Conventions

- **Logging**: `loguru` throughout. Logs go to `logs/{time}.log`. Use `logger.info/debug/error/exception`.
- **Pydantic** for config validation, otherwise mostly untyped
- **Async**: `aiorak` connections and `MCClient` packet handling are async. Node.js bridge calls are synchronous.
- **Threading**: `MCClient.get_chunk_thread` runs a separate thread for chunk polling. Thread safety is minimal.
- **Error handling**: Packet event handlers catch exceptions and log them via `logger.exception` — errors in one handler won't crash the server.
- **Config changes**: Update both the Pydantic model classes and the `default_file` YAML string in `config.py`.
