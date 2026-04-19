from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayerCameraRotateHC
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    client.angle = Angle(jsondata["yaw"], jsondata["pitch"])
    rotate = PB_PlayerCameraRotateHC(
        Yaw=client.angle.to_mini_yaw_float(), Pitch=client.angle.to_mini_pitch_float()
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYER_CAMERAROTATE_HC, rotate)


add_event("position", on_recv)
