from typing import TypedDict
import yaml
from pathlib import Path

default_file = """
mini:
  auth:
    # 暂时没有实现
    uin: 0
    type: passwd
    passwd: ""
  server:
    ip: 127.0.0.1
    port: 11155
    host_to_room_server: false # 暂时没有实现
  send_log_to_chat: false

mc:
  ip: 127.0.0.1
  port: 25565
  username: "" # 指定玩家名称，留空则使用迷你玩家名称
  version: "1.21.11" # 指定 MC 版本，目前仅支持 1.21.11
  use_new_chunk_parser: true # 是否使用新版区块解析器，能够减小跨语言调用开销，但可能会超时
  chunk_parse_thread: 4 # 区块解析线程数

debug: false

"""


class server(TypedDict):
    ip: str
    port: int
    host_to_room_server: bool


class auth(TypedDict):
    uin: int
    type: str
    passwd: str


class Mini(TypedDict):
    server: server
    auth: auth
    send_log_to_chat: bool


mini: Mini = {
    "server": {"ip": "127.0.0.1", "port": 11155, "host_to_room_server": False},
    "auth": {"uin": 0, "type": "passwd", "passwd": ""},  # 暂时还没啥用
    "send_log_to_chat": False,
}


class MC(TypedDict):
    ip: str
    port: int
    username: str
    version: str
    chunk_parse_thread: int
    use_new_chunk_parser: bool


mc: MC = {
    "ip": "127.0.0.1",
    "port": 25565,
    "username": "",  # use mini player name
    "version": "1.21.11",
    "chunk_parse_thread": 4,
    "use_new_chunk_parser": True,
}

debug: bool = False


def load(path: Path = Path("config.yaml")) -> None:
    global mini, mc, debug
    if path.exists():
        with path.open() as f:
            config = yaml.safe_load(f)
            mini = config["mini"]
            mc = config["mc"]
            debug = config["debug"]
    else:
        save(path)


def save(path: Path = Path("config.yaml")):
    with path.open("w") as f:
        f.write(default_file)
