from pathlib import Path
from typing import TYPE_CHECKING, Literal

import yaml
from loguru import logger
from pydantic import BaseModel, Field

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
  whitelist_uins: [] # 允许进入代理的玩家 UIN 列表，留空则允许所有玩家

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


class ServerConfig(BaseModel):
    ip: str = "127.0.0.1"
    port: int = Field(default=11155, ge=1, le=65535)
    host_to_room_server: bool = False
    max_players: int = Field(default=40, ge=1, le=65535)


class AuthConfig(BaseModel):
    uin: int = Field(default=0, ge=0)
    passwd: str = ""
    api_id: int = Field(default=110, ge=0)
    device_id: str = "MN2MCDefault"


class MiniConfig(BaseModel):
    server: ServerConfig = ServerConfig()
    auth: AuthConfig = AuthConfig()
    send_log_to_chat: bool = False
    admin_uins: list[int] = []
    whitelist_uins: list[int] = []


class MCConfig(BaseModel):
    ip: str = "127.0.0.1"
    port: int = Field(default=25565, ge=1, le=65535)
    username: str = ""
    version: Literal["1.21.11"] = "1.21.11"
    chunk_parse_thread: int = Field(default=4, ge=1, le=32)
    use_new_chunk_parser: bool = True
    log_message: bool = False


class AppConfig(BaseModel):
    mini: MiniConfig = MiniConfig()
    mc: MCConfig = MCConfig()
    debug: bool = False


class ConfigManager:
    """Manages application configuration loaded from / saved to YAML."""

    def __init__(self) -> None:
        self._config = AppConfig()
        self._config_path: Path = Path("config.yaml")

    def load(self, path: Path = Path("config.yaml")) -> None:
        self._config_path = path
        if path.exists():
            with path.open() as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict):
                    try:
                        self._config = AppConfig.model_validate(data)
                    except Exception as e:
                        logger.error(f"Config validation error: {e}")
                        logger.warning("Using defaults for invalid fields")
                        self._config = AppConfig()
        else:
            self.save(path)

    @property
    def mini(self) -> MiniConfig:
        return self._config.mini

    @property
    def mc(self) -> MCConfig:
        return self._config.mc

    @property
    def debug(self) -> bool:
        return self._config.debug

    def save(self, path: Path | None = None) -> None:
        """Serialize the current config state to YAML.

        If *path* is ``None``, writes to the same file that was last loaded
        (or the default ``config.yaml`` on first run).
        """
        if path is None:
            path = self._config_path
        with path.open("w") as f:
            yaml.dump(
                self._config.model_dump(),
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
    mini: MiniConfig
    mc: MCConfig
    debug: bool
    def load(path: Path = ...) -> None: ...
    def save(path: Path | None = ...) -> None: ...


def __getattr__(name: str):
    """Proxy attribute lookups to the singleton for live values."""
    if name in _CONFIG_ATTRS:
        return getattr(config, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
