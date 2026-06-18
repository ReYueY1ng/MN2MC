from typing import TYPE_CHECKING, TypedDict
import yaml
from pathlib import Path

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
  send_log_to_chat: false # 发送日志至聊天栏

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


class auth(TypedDict):
    uin: int
    passwd: str
    api_id: int
    device_id: str


class Mini(TypedDict):
    server: server
    auth: auth
    send_log_to_chat: bool


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
            "server": {"ip": "127.0.0.1", "port": 11155, "host_to_room_server": False},
            "auth": {"uin": 0, "passwd": "", "api_id": 110, "device_id": ""},
            "send_log_to_chat": False,
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
                self.mini = data["mini"]
                self.mc = data["mc"]
                self.debug = data["debug"]
        else:
            self.save(path)

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
