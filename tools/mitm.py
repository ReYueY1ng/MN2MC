from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://cs-gsmgr.mini1.cn/v2/room/get":
        flow.response = http.Response.make(
            200,  # (optional) status code
            '{"code":0,"msg":"found","aid":"85440341897026","roomid":"273640665_9a4612b3-e2b5-4478-bc7f-1decd6d486f4","ip":"127.0.0.1","port":11155,"room_cap":10,"player_num":0,"mod_url":"","room_mods":"","room_ui_libs":"http://map4.mini1.cn/map/4/plugin20260403/92a3aa4a70bb9cda4d49320328034545","room_ver":"1.55.0","room_name":"血战-枪战精英","room_audio_config":"{"audiourl":"http:\\/\\/map1.mini1.cn\\/map\\/1\\/time20260403\\/ffc757963d4a688363302a16ac8bea71","editorSceneSwitch":1,"worldtype":5 } ","room_translate":"","czb_uuid":"","uin":1000,"nick_name":"迷你小队长","is_cloud":false,"passwd_md5":"","share_version":"1772094792","team_id":0,"public_type":0,"can_trace":0,"personal":0,"teams":[{"team_id":0,"cap":40,"uin_list":["273640665"]}],"room_from":"","not_follow":false}',
            {"Content-Type": "application/json; charset=utf-8"},  # (optional) headers
        )
