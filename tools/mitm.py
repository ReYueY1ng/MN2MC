import json

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://cs-gsmgr.mini1.cn/v2/room/get":
        data = {
            "code": 0,
            "msg": "found",
            "aid": "10213705870553",
            "roomid": "MN2MC-MitmMode",
            "ip": "127.0.0.1",
            "port": 11155,
            "room_cap": 1,
            "player_num": 0,
            "mod_url": "",
            "room_mods": "",
            "room_ui_libs": "",
            "room_ver": "1.57.1",
            "room_name": "MN2MC",
            "room_audio_config": '{"editorSceneSwitch":0,"worldtype":4}',
            "room_translate": "",
            "czb_uuid": "",
            "uin": 1000,
            "nick_name": "ReYueY1ng",
            "is_cloud": False,
            "passwd_md5": "",
            "share_version": "1772094792",
            "team_id": 0,
            "public_type": 0,
            "can_trace": 0,
            "personal": 0,
            "teams": [],
            "room_from": "",
            "not_follow": False,
        }
        flow.response = http.Response.make(
            200,  # (optional) status code
            json.dumps(data),
            {"Content-Type": "application/json; charset=utf-8"},  # (optional) headers
        )
