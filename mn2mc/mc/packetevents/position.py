from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_MoveSyncHC, PB_PlayerCameraRotateHC
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    # logger.debug(jsondata)
    if jsondata["flags"]["x"]:
        client.position.x += jsondata["x"]
    else:
        client.position.x = jsondata["x"]
    if jsondata["flags"]["y"]:
        client.position.y += jsondata["y"]
    else:
        client.position.y = jsondata["y"]
    if jsondata["flags"]["z"]:
        client.position.z += jsondata["z"]
    else:
        client.position.z = jsondata["z"]
    if jsondata["flags"]["yaw"]:
        client.angle += (jsondata["yaw"], 0)
    else:
        client.angle = Angle(jsondata["yaw"], client.angle.get_pitch())
    if jsondata["flags"]["pitch"]:
        client.angle += (0, jsondata["pitch"])
    else:
        client.angle = Angle(client.angle.get_yaw(), jsondata["pitch"])

    pos = client.position.convert().to_vec3().to_mini()
    pos.X -= 1
    move = PB_MoveSyncHC(id=client.miniplayer.uin, pos=pos).SerializeToString()
    rotate = PB_PlayerCameraRotateHC(
        Yaw=client.angle.to_mini_yaw_float(), Pitch=client.angle.to_mini_pitch_float()
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_SYNC_MOVE_HC, move)
    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYER_CAMERAROTATE_HC, rotate)
    """
        yaw, pitch = converted_angle.to_mini()
        client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_MOVE_HC, PB_ActorMoveHC(
            ObjID=client.miniplayer.uin,
            MoveMotion=PB_MoveMotion(
                Position=pos,
                Yaw=yaw,
                Pitch=pitch,
                MapID=0
            )
        ).SerializeToString())
        """
    client.send("teleport_confirm", {"teleportId": jsondata["teleportId"]})


add_event("position", on_recv)
