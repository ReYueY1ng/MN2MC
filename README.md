# MN2MC

迷你世界转译代理，用于连接 Minecraft Java 版 1.21.11 服务器。  

## 支持版本

迷你世界 1.55.0 / Minecraft 1.21.11

## 已实现功能

- [x] 聊天
- [x] 慢速区块转换（先发空区块，后发方块包）
- [x] 方块映射（基础）
- [x] 移动
- [x] 方块操作
- [x] 物品映射（基础）
- [x] 背包
- [x] 实体（基础）
- [ ] 快速区块转换（直接构建区块包）
- [x] 创建房间
- [ ] 打洞直连
- [ ] 代理转发
- [ ] 自定义 UI

## 使用方法

请确保已安装 Python 3.13+ 和 Node.js。

### 安装依赖

1. 安装 Python 依赖：
```bash
pip install -r requirements.txt
```

2. 安装 `aiorak`：

```bash
git clone https://github.com/wu-vincent/aiorak.git
pip install ./aiorak
```

3. 安装最新版 `minebase`：

```bash
# depth 设为 1 可加快克隆速度
git clone https://github.com/py-mine/minebase.git --depth=1
git clone https://github.com/PrismarineJS/minecraft-data.git minebase/minebase/data --depth=1
pip install ./minebase
```

4. 安装 Node.js 依赖（可选）：

```bash
npm install minecraft-protocol prismarine-chat prismarine-block prismarine-chunk vec3 msgpackr prismarine-item prismarine-registry
```

### 启动代理

```bash
python main.py
```

### 进入代理

目前有两种方式：

#### 中间人替换（推荐）

只需将 http://cs-gsmgr.mini1.cn/v2/room/get 响应中的 ip 和 port 替换为代理的地址和端口即可。

Linux 示例：

```bash
mitmdump --mode local:wineserver -s tools/mitm.py
```

在迷你世界里面选择一个地图（最好是云服地图），点击“联机”即可进入。

#### 创建房间

构建 [raknet_proxy](https://github.com/ReYueY1ng/raknet-proxy)，将产物放进 tools 文件夹里

将 config.yaml 内的 auth 子项填完，host_to_room_server 改为 true 即可创建房间

启动代理后在联机大厅搜索迷你号，即可直接进入
