from pathlib import Path
from typing import TYPE_CHECKING, TypedDict

import yaml
from loguru import logger

# Default config as a string — used only for initial file generation and as documentation.
_default_file = """\
mini:
  auth:
    # 仅创建房间时才使用
    uin: 0
    passwd: ""
    api_id: 110
    device_id: "MN2MCDefault"
  server:
    ip: 127.0.0.1
    port: 11155
    host_to_room_server: false # 创建迷你房间，若启用则无法通过 mitm 方式进入
    max_players: 65535
  send_log_to_chat: false # 发送日志至聊天栏
  admin_uins: [] # 允许执行 /mn2mc reload 等命令的玩家 UIN 列表，留空则仅房主可执行

mc:
  ip: 127.0.0.1
  port: 25565
  username: "" # 指定玩家名称，留空则使用迷你玩家名称
  version: "1.21.11" # 指定 MC 版本，目前仅支持 1.21.11
  use_new_chunk_parser: true # 是否使用新版区块解析器，能够减小跨语言调用开销，但可能会超时，占用大量内存
  chunk_parse_thread: 4 # 区块解析线程数
  log_message: false # 记录聊天消息

debug: false

"""


class server(TypedDict):
    ip: str
    port: int
    host_to_room_server: bool
    max_players: int


class auth(TypedDict):
    uin: int
    passwd: str
    api_id: int
    device_id: str


class Mini(TypedDict):
    server: server
    auth: auth
    send_log_to_chat: bool
    admin_uins: list[int]


class MC(TypedDict):
    ip: str
    port: int
    username: str
    version: str
    chunk_parse_thread: int
    use_new_chunk_parser: bool
    log_message: bool


class ConfigManager:
    """Manages application configuration loaded from / saved to YAML."""

    def __init__(self) -> None:
        self.mini: Mini = {
            "server": {"ip": "127.0.0.1", "port": 11155, "host_to_room_server": False, "max_players": 65535},
            "auth": {"uin": 0, "passwd": "", "api_id": 110, "device_id": ""},
            "send_log_to_chat": False,
            "admin_uins": [],
        }
        self.mc: MC = {
            "ip": "127.0.0.1",
            "port": 25565,
            "username": "",
            "version": "1.21.11",
            "chunk_parse_thread": 4,
            "use_new_chunk_parser": True,
            "log_message": False,
        }
        self.debug: bool = False
        self._config_path: Path = Path("config.yaml")

    def load(self, path: Path = Path("config.yaml")) -> None:
        self._config_path = path
        if path.exists():
            with path.open() as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict):
                    self._validate_and_merge(data)
        else:
            self.save(path)

    def _validate_and_merge(self, data: dict) -> None:
        if not isinstance(data, dict):
            return

        mini_section = data.get("mini")
        if isinstance(mini_section, dict):
            server_section = mini_section.get("server")
            if isinstance(server_section, dict):
                if "ip" in server_section and isinstance(server_section["ip"], str):
                    self.mini["server"]["ip"] = server_section["ip"]
                else:
                    logger.warning("Config missing or invalid mini.server.ip; using default")
                if "port" in server_section and isinstance(server_section["port"], int):
                    self.mini["server"]["port"] = server_section["port"]
                else:
                    logger.warning("Config missing or invalid mini.server.port; using default")
                if "host_to_room_server" in server_section and isinstance(server_section["host_to_room_server"], bool):
                    self.mini["server"]["host_to_room_server"] = server_section["host_to_room_server"]
                else:
                    logger.warning("Config missing or invalid mini.server.host_to_room_server; using default")
                if "max_players" in server_section and isinstance(server_section["max_players"], int):
                    self.mini["server"]["max_players"] = server_section["max_players"]
                else:
                    logger.warning("Config missing or invalid mini.server.max_players; using default")

            auth_section = mini_section.get("auth")
            if isinstance(auth_section, dict):
                if "uin" in auth_section and isinstance(auth_section["uin"], int):
                    self.mini["auth"]["uin"] = auth_section["uin"]
                else:
                    logger.warning("Config missing or invalid mini.auth.uin; using default")
                if "passwd" in auth_section and isinstance(auth_section["passwd"], str):
                    self.mini["auth"]["passwd"] = auth_section["passwd"]
                else:
                    logger.warning("Config missing or invalid mini.auth.passwd; using default")
                if "api_id" in auth_section and isinstance(auth_section["api_id"], int):
                    self.mini["auth"]["api_id"] = auth_section["api_id"]
                else:
                    logger.warning("Config missing or invalid mini.auth.api_id; using default")
                if "device_id" in auth_section and isinstance(auth_section["device_id"], str):
                    self.mini["auth"]["device_id"] = auth_section["device_id"]
                else:
                    logger.warning("Config missing or invalid mini.auth.device_id; using default")

            if "send_log_to_chat" in mini_section and isinstance(mini_section["send_log_to_chat"], bool):
                self.mini["send_log_to_chat"] = mini_section["send_log_to_chat"]
            else:
                logger.warning("Config missing or invalid mini.send_log_to_chat; using default")

            if "admin_uins" in mini_section and isinstance(mini_section["admin_uins"], list):
                self.mini["admin_uins"] = [u for u in mini_section["admin_uins"] if isinstance(u, int)]
            else:
                logger.warning("Config missing or invalid mini.admin_uins; using default")
        else:
            logger.warning("Config missing or invalid mini section; using defaults")

        mc_section = data.get("mc")
        if isinstance(mc_section, dict):
            if "ip" in mc_section and isinstance(mc_section["ip"], str):
                self.mc["ip"] = mc_section["ip"]
            else:
                logger.warning("Config missing or invalid mc.ip; using default")
            if "port" in mc_section and isinstance(mc_section["port"], int):
                self.mc["port"] = mc_section["port"]
            else:
                logger.warning("Config missing or invalid mc.port; using default")
            if "username" in mc_section and isinstance(mc_section["username"], str):
                self.mc["username"] = mc_section["username"]
            else:
                logger.warning("Config missing or invalid mc.username; using default")
            if "version" in mc_section and isinstance(mc_section["version"], str):
                self.mc["version"] = mc_section["version"]
            else:
                logger.warning("Config missing or invalid mc.version; using default")
            if "chunk_parse_thread" in mc_section and isinstance(mc_section["chunk_parse_thread"], int):
                self.mc["chunk_parse_thread"] = mc_section["chunk_parse_thread"]
            else:
                logger.warning("Config missing or invalid mc.chunk_parse_thread; using default")
            if "use_new_chunk_parser" in mc_section and isinstance(mc_section["use_new_chunk_parser"], bool):
                self.mc["use_new_chunk_parser"] = mc_section["use_new_chunk_parser"]
            else:
                logger.warning("Config missing or invalid mc.use_new_chunk_parser; using default")
            if "log_message" in mc_section and isinstance(mc_section["log_message"], bool):
                self.mc["log_message"] = mc_section["log_message"]
            else:
                logger.warning("Config missing or invalid mc.log_message; using default")
        else:
            logger.warning("Config missing or invalid mc section; using defaults")

        if "debug" in data and isinstance(data["debug"], bool):
            self.debug = data["debug"]
        else:
            logger.warning("Config missing or invalid debug; using default")

    def save(self, path: Path | None = None) -> None:
        """Serialize the current config state to YAML.

        If *path* is ``None``, writes to the same file that was last loaded
        (or the default ``config.yaml`` on first run).
        """
        if path is None:
            path = self._config_path
        with path.open("w") as f:
            yaml.dump(
                {"mini": self.mini, "mc": self.mc, "debug": self.debug},
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
            )


# Module-level singleton — importers use ``import mn2mc.config as config``
# then access ``config.mini``, ``config.mc``, ``config.load()``, etc.
config = ConfigManager()

# Sentinel names that __getattr__ proxies to the singleton.
_CONFIG_ATTRS = frozenset({"mini", "mc", "debug", "load", "save"})

if TYPE_CHECKING:
    mini: Mini
    mc: MC
    debug: bool
    def load(path: Path = ...) -> None: ...
    def save(path: Path | None = ...) -> None: ...


def __getattr__(name: str):
    """Proxy attribute lookups to the singleton for live values."""
    if name in _CONFIG_ATTRS:
        return getattr(config, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
