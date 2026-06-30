"""Handle Mini World enter world and initialize the MC client connection."""

from __future__ import annotations
from mn2mc.mini.proto.hc import PB_PlayerAttrChangeHC

import asyncio
import time

from loguru import logger

import mn2mc
import mn2mc.config as config
import mn2mc.mini.proto as proto
import mn2mc.mini.proto.common as common
from mn2mc.utils.vector import Vector3f
from mn2mc.mc.client import MCClient
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.proto.common import ePBMsgCode
from google.protobuf import json_format

player_permit = proto.hc.PB_PlayerPermitHC()
json_format.Parse(
    """{
  "RoomFlags": 12862,
  "PlayerFlags": 12862,
  "SpamPreventionMinutes": 0,
  "BanItems": []
}""",
    player_permit,
)
player_permit_str = player_permit.SerializeToString()


global_bin = common.PB_GlobalBin(
    BinLen=1142,
    # BinContent="""(\xb5/\xfd`\xa0\x10-<\x00Jn\xb8\x14@pl\xd5\x1c\xac\xa5(\x17\xea4\xfa\x03\x03\x1fm\x81P\xdf\x0e\x0cgj\xe0\xe7\xff\xdc\xc7\x83\xb6 \xe1\x85D\xa0\x15\x92\x82\x0b\xdf\xa1\xa7\xfe[\x13\xe9v\xbe\xdf\'\xa9\xe7h[A\xbc\x03 n\x88~?\x91R\xa6\x08\x01"\x01\x7f\x01q>\x85\xf3\xe9\x9bO\xdd|\xda\xe6S6\x9f\xae\xf9T\xcd\xa7i>E\xf3\xe9\x99O\xa1|\xfa\xe4{\xbd\xe7\xa5y\x1e\x9a\xe7\x9dy\x9e\x99\xe7\x95y\x1e\x99\xe7\x8dy\x9e\x97\xe7uy\x1e\x97\xdf%\xf8\x1d\x82\xdf\xd9~w\xe0u\xb5\xd7\x01x\x1d\xedsc\x9fK\xf4\xb9C\x8f\xeax\xf4\xc5\xa3\xbaGs\x8f\xe2\x1eE\x1f}zT\xc2\xa3\x11\x1euz\xf4\xf6(\x84G\x1f<\xea\xe0\xd1\x06\x8f2x\xb4\xe9\xd1\x05\x8f\x9e\x8f*x\t\xb9\x97\xf0\xf4NE\xef${\x08;~\xa6\xe7eT/\x8b\xf0\xb2\xdb\xcb \xbc\xec\xc1\x9b\x81\xde\x8c\xf2&\x8f7/\xbc\x89\xf5\xa5\x9a\'\x0b\xfd9\xfe\xd9_\xf4\x13\xcd\x0c\x0e\xae~h0q\x85\xbcV\x05\xf8\xe5_*}\xc9{\x93}\x93\xc8\x9bb\xff\xd3\xcf{\xae\xa7\xd5\x98\xec\x91o\xd4\xe6i\x83\xbelp\xef\xbd\x1b-\xc0\xcd\x97$&\x8b\xcf\xe6Z\xf8\x8aS|b\x12k\xfd\x1e\xdep\xd61\xbe\xda7\xd5\xbco?\xd3\x03>\xfak\xdab\x93\xf8O\x04\xe3\xb0\x8c\x9c\r>\xda\xf6\xd2\x7f\x8c\xbf\xc1\xadh\xdaK\x0f\xb83\xc872T\xfa\xc0a^[\x9b$\x93\xa2\xa4\xa8\xd5]\x91?(\x9a\x8dm\xf9\xb8\xcaP\x8b_\xbf\x95U\x8b_]++\xac%\xad\x00\xd1\xcd"\x976\x9a\xe9%\x13\xd05\xe1QG\xe4\xedI(_\xda\xbe\x04\xf2&\xedM /\xb3Q\xfd\x87\x9e\xc0JG\xd3\x96m\x9b\x80\x99\x84\xe7q;\xaeMN\x96\x1b\x8a\x96\xa1-H\x07\x97\x1b\x94j\xd3V\x9am\xdb\xbd\x84/f\xa0\xbf\xeb\\\x81\x8b6Z&\xe5\xb7\xf2\x13\x8f\xcb\x8f.\xf2\xf1O\xfd\xd3\x04s?\xcf\xa0\xfcKL\xa46\x97\xcf6"7\xdc{S\xfc\x0e6\x91\xe0|\x0f\xcb\xb5\x85\xd36|\x9d\xbf\x8f\xfd\x81\xfc^\xfeA?\xcd\xf6\xd3\xe7J?`\xdd6\xd9\xbd\xed\xd5#\x95\xf9\xa4\xacO\xf2\xb2\x99$\xe6}S\xde\x07\xe5}O\xde\xe7\xe4}M\xde\xc7\xe4}K\xde\xa7\xe4}I\xde\x87\xe4}G\xdeg\xe4}E\xdeG\xe4}C\xde\'\xe4}A>\xed\xf3)\x9fO\xf7|\xaa\xe7\xd3<\x9f\xe2\xf9\xf4\xce\xa7v>\xad\xf3)\x9dO\xe7|*\xe7\xd3k\xf1\x18&4\xae\xbfsH|\xcbHd\x87\xea1\x98;z\x11_\xa8\\+0\xa7\xab\x02\xee\x82@\xa8(\xa8\xe0p\n]\x87\xbd*\x14(5\xc5C\x81U:)T\xd8\xeb\t{""",  # noqa: E501
    BinContent="""(\xb5/\xfd`\xd8\x0ee#\x00\xb6\xfa\xa9C\xb0\x9aMk\x82\xfd)\xff\x11\x1c\xde9\xc3\xc1k#\xf4\x98s^\xf3\x89\xda\x92\xd4\r\xd6\xdd"}\x7fg\xb9\xeb\x0b+\xfda\xba\x8f\x87\xc4\x8ab\xbc\x9aI0\x85\x15Fy\xe2]\xce6F\xe34I\x08\xed\xb6\xa5\x94[\xa6\x8d\x00\x9f\x00\x8a\x00\xff\x0c\x9f\x01{R\x1f?\xccCt7\xdd\x15m\xbb\xcb\xf47X\xdaXy\tE~\xed\xf4g\xa3\n\xff\x0b\xff\xd2\xd5\xef\xe4\'\xf3\x7f\xe0<\x87\xcf^vmp\xee\xd6\x9b\xdc&\xebcG\x1f\xc3\xfa\xa5\x02\\\xce\x83/L\\\xd4\xf8\xe3\x02\x8an\x7f\xd3\xf3\xf8x\xe5\xe3\xd6\xc7.VI\xba\x1c\xf9_x[\x8e\x13\xb2\xde\x85\xb4\xbb\xeb\xfaD\x83?w\xfc\x8f\xda\x1bj\x14;\xdd4\xd3K\xbf\xd2H\xff\xd1\xb8\x8d\x8e\xf1\xed\x0b\xdb\x0e\x9a\xf6\xeb,\x1b\xb6\xd4\xdfT+\xcd\x14{Q\xbf\xcf\xc4\xa9\x89\xb3\xefy\xa96\xcf\xb4ufOQ\x8f\x90\xc1\xb0\xc1q\xa0\x18\xd0\xe8\xdf8\xcbv*\xbek\x99g\xa6\xab\xa2!\x17\xac\xb1yeEk-\xe8oq\x07\xd4[\xb3d\x16O0J@E\x91x\x92*\x01\x15\xa5\xe2I\xc0N\xaf\xd8\t\xd2\xacQ\xc4\xd9\xb5\xce8N@?/\xc3\xfc\xfa\x1a,\xd2>\x06\xf9\x0e\xfcN\xc7\xcb\xef\xa5\x8e\x9f\xe0[\x7f\xf3\x0c\xf6\xf7\x1c\xfcF\xc6\xb4|\xcf\x8d_\xc7cg\xa3\xcfst\xbf\xee\xb4~\xe7\x89\xb4\xfd\xf4\xd7\xdf3o0\xc1\xceN\x94\xbb\xe5\xf3\xc0\xfb\xcc\xe48\xa6Y\x01H\x8ev+\x02\x10\xbb\xf5&\xc4n\xf5\x86r#\xed\xaeA\xd3$\xf7\x0b\x9d\xb3\xbbf\xcc\xdd\x0bv+\x8b\xbb1\xec\xd6\x14?9jq\x14\xa0pC\xd5K\x1f/\xaf^\x1ay)\xe5\xe5\x95\x97`^n\xfd\x94\xfd\x0c\x7f\xd6~\xde~"\xfdl\xfa\x19\xf53\xc6\xcf\xaa\x9f?~\n\xf9\x99\xe4\'\xd6O,?\xb5~\x9ey\xfa=\x05\x9f\xd2\x9e\xda\x9e\xe2\x9e.=E\xf1\xf4\xc5S\xaa\xa7<\x9e\x06y\xba\xe4)\xd6S,O\xb5\x9e\x9ey\xef{\x0f|\x8f\xf6\x9e\xedeTt^\x984\xd39\xa9\xdb\xdd,E\x1f\xac\xfbb\xb7\xa9;\xecn\x99\x02\xbbK%\xc3\xeeB\x19\xca\xc9\xddEB\xb4\xbbC\x88\x8e\xbb\x0b\x04\xb7\xbb;\x86r\xdf\xee\xda\xb8;\xc2\xfc\x0b\xda]\x19\x03\xd8\xc0\xee\x8a\xf9;iw\xbd(\xed.\x85\xdd\x15\xaa@\x14\xfe<\x8b\xd8]\x079\x1bv7\xe6\xedn\xc7\xc1\xb5[\xc5h\xd8\xad\\\xe8n\xadb\xb4[\xa7\x84\xbbU\t\xb8[\x89\xcca\x02\xbb\xfb\x03a\xb7Z\xfd\xec\xd6\x1cw\xd7v\xf7\xc3n\x9d\xbaY\xd8f\xb7\xae\x00\xda\xad&&\xec\xd6\x11\x12v""",  # noqa: E501
)

room_info = proto.hc.PB_Custom_Msg(
    msgname="MULTII_NOR_ROOM_INFO_CHANGED_TOCLIENT",
    # content="\u000b\u0000\u0000\u0000XcanTraceZhostGameTk\\8000273640665001778395651c9f5c2406bca37d6c1c46b699b3dd275\\\fhostPasswordP\\\rmapCanRecruit\\\fmaxPlayerNum\\\u0011maxPlayerSetLimitZpublicType\\\u000froomConnectModeTtagsI`\u001dw\"abcde\u0002f\u0016g\u001c(h\u0010i\u0011j@",
    content='\u000b\u0000\u0000\u0000XcanTraceZhostGameTk\\80002736406650017783978936d2f27c7bf9bfcd9c64dd8a59ded8704\\\fhostPasswordP\\\rmapCanRecruit\\\fmaxPlayerNum\\\u0011maxPlayerSetLimitZpublicType\\\u000froomConnectModeTtagsI`\u001dw"abcde\u0002f\u001c(g\u001c(h\u0010i\u0011j@',
    ziplen=201,
    unziplen=0,
).SerializeToString()


def _build_player_info(player: MiniPlayer) -> common.PB_PlayerInfo:
    """Build the PlayerInfo protobuf for enter world response."""
    return common.PB_PlayerInfo(
        ObjID=player.uin,
        anim=0,
        anim1=-1,
        RoleData=common.PB_RoleData(
            Uin=player.uin,
            OWID=10213705870553,
            HP=100,
            Oxygen=10,
            FoodLevel=100,
            FoodSatLevel=100,
            UsedStamina=0,
            Exp=0,
            Level=1,
            LastLoginTime=int(time.time()),
            LoginNum=1,
            FallDist=0,
            Flags=0,
            LiveTicks=0,
            RideActorID=0,
            Pos=common.PB_Pos(X=0, Y=6400, Z=0, Map=0),
            Dir=common.PB_BodyDir(
                RotationYaw=0,
                RotationPitch=0,
                Motion=common.PB_Vector3(X=0, Y=0, Z=0),
            ),
            Package=common.PB_RolePackage(
                ShortcutPak=common.PB_ShortcutPak(
                    HandIdx=0,
                    Grids=[
                        common.PB_ItemGrid(
                            ItemGridData=common.PB_ItemGridData(
                                Item=common.PB_Item(DefID=100)
                            )
                        )
                    ],
                )
            ),
            Buff=common.PB_ActorBuffList(),
            CarringActorID=0,
            STRENGTH=100,
            ENABLE_STRENGTH=False,
            max_strength=100,
            Armor=0,
            Perseverance=0,
            MaxHP=100,
            StrengthFoodShowState=1,
            StarDebuffStage=0,
            StarDebuffTime=0,
            CanThrow=False,
        ),
        BodyColor=0,
        customscale=1,
        actSeqId=-1,
        animweapon=-1,
        scale=common.PB_Vector3f(X=1.1, Y=1, Z=1.1),
    )


def _build_global_info() -> common.PB_OWGlobal:
    """Build the GlobalInfo protobuf for enter world response."""
    return common.PB_OWGlobal(
        SvrStart=26149,
        Misc=common.PB_OWGlobalMisc(
            GlobalFlag=4056,
            InitPos=common.PB_Pos(X=0, Y=64, Z=0, Map=0),
            RevicePos=common.PB_Pos(X=0, Y=64, Z=0, Map=0),
            GlobalBin=global_bin,
        ),
    )


def _build_world_desc() -> common.PB_WorldDesc:
    """Build the WorldDesc protobuf for enter world response."""
    return common.PB_WorldDesc(
        WorldId=10213705870553,
        WorldType=1,  # 0普通生存 1普通创造 2极限生存 3模拟生存 4开发创造 5玩法生存
        OwnerUin=273640665,
        CreateData=common.PB_WorldCreateData(
            TerrType=0,
            RandSeed1=0,
            RandSeed2=0,
            RoleModel=0,
            SeedStr="",
            TilesX=0,
            TilesZ=0,
        ),
        FromOWID=10213705870553,
        RealOwnerUin=273640665,
        WorldOpen=2,
        WorldName=f"MN2MC {mn2mc.version}",
        TempType=0,
        pwid=0,
        SpecialType=0,
        editorSceneSwitch=1,
        ctype=1,
        extraInfo='{"editSceneSw": 1,"modpacksDesc": "{}","openCode": 5}',
    )


async def _send_init_packets(player: MiniPlayer) -> None:
    """Send additional initialization packets after enter world response."""
    # 进世界
    player.send_packet(
        ePBMsgCode.PB_CUSTOM_MSG,
        proto.hc.PB_Custom_Msg(
            msgname="WGLOBAL_EX_TO_CLIENT",
            content="\u0000\u0000\u0000\u0000@",
            ziplen=18,
            unziplen=0,
        ).SerializeToString(),
    )
    player.send_packet(
        ePBMsgCode.PB_SS_SYNC_TASK_HC,
        proto.hc.PB_SSTaskHC(
            TargetUin=player.uin, TaskId=7, ParamJson='{"code":0}'
        ).SerializeToString(),
    )
    player.send_packet(ePBMsgCode.PB_PLAYERPERMIT_HC, player_permit_str)
    player.send_packet(ePBMsgCode.PB_CUSTOM_MSG, room_info)
    player.send_packet(
        ePBMsgCode.PB_PLAYER_ATTR_CHANGE_HC,
        PB_PlayerAttrChangeHC(
            Scale=Vector3f(x=1.1, y=1, z=1.1).to_mini()
        ).SerializeToString(),
    )


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Complete Mini World world entry and start the MC client connection.

    Sends the enter world response with player/world data, runs init
    packets, then creates MCClient connected to the configured server.
    """
    if player.name != "Unknown":
        return
    player_enter = proto.ch.PB_RoleEnterWorldCH()
    player_enter.ParseFromString(mcp.data)
    # player.uin = player_enter.Uin
    player.name = player_enter.RoleInfo.NickName
    player.cltversion = player_enter.cltversion
    player.send_packet(
        ePBMsgCode.PB_ROLE_ENTER_WORLD_HC,
        proto.hc.PB_RoleEnterWorldHC(
            Uin=player.uin,
            PlayerInfo=_build_player_info(player),
            GlobalInfo=_build_global_info(),
            WorldDesc=_build_world_desc(),
            SkillCDData=common.PB_SkillCDData(NumSkillCD=0),
            HasRole=False,
            TeleportMsg="",
            ActorSyncFrequency=4,
        ).SerializeToString(),
    )

    logger.info(f"{player.name} ({player.uin}) joined")
    await _send_init_packets(player)
    await asyncio.sleep(1)
    player.mcclient = MCClient(
        options={
            "version": config.mc["version"],
            "username": config.mc["username"]
            if config.mc["username"] != ""
            else player.name,
            "host": config.mc["ip"],
            "port": config.mc["port"],
        },
        miniplayer=player,
    )


add_event(proto.common.ePBMsgCode.PB_ROLE_ENTER_WORLD_CH, on_recv)
