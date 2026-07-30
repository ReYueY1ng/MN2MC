import mn2mc.mini.proto.common as _proto_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCMouseKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    left: _ClassVar[PCMouseKeyType]
    right: _ClassVar[PCMouseKeyType]
    scroll: _ClassVar[PCMouseKeyType]

class PCMouseEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    down: _ClassVar[PCMouseEventType]
    up: _ClassVar[PCMouseEventType]
    click: _ClassVar[PCMouseEventType]

class TouchEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    touchDown: _ClassVar[TouchEventType]
    touchUp: _ClassVar[TouchEventType]
    touchCancel: _ClassVar[TouchEventType]

class CheatCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CCT_JumpHeight: _ClassVar[CheatCheckType]
    CCT_TackleRange: _ClassVar[CheatCheckType]
    CCT_GrabRange: _ClassVar[CheatCheckType]
    CCT_DribbleRange: _ClassVar[CheatCheckType]
    CCT_Clip: _ClassVar[CheatCheckType]
left: PCMouseKeyType
right: PCMouseKeyType
scroll: PCMouseKeyType
down: PCMouseEventType
up: PCMouseEventType
click: PCMouseEventType
touchDown: TouchEventType
touchUp: TouchEventType
touchCancel: TouchEventType
CCT_JumpHeight: CheatCheckType
CCT_TackleRange: CheatCheckType
CCT_GrabRange: CheatCheckType
CCT_DribbleRange: CheatCheckType
CCT_Clip: CheatCheckType

class PB_HeartBeatCH(_message.Message):
    __slots__ = ("BeatCode", "server_time", "client_time", "aceinfo", "Rtt")
    BEATCODE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIME_FIELD_NUMBER: _ClassVar[int]
    ACEINFO_FIELD_NUMBER: _ClassVar[int]
    RTT_FIELD_NUMBER: _ClassVar[int]
    BeatCode: int
    server_time: int
    client_time: int
    aceinfo: bytes
    Rtt: int
    def __init__(self, BeatCode: _Optional[int] = ..., server_time: _Optional[int] = ..., client_time: _Optional[int] = ..., aceinfo: _Optional[bytes] = ..., Rtt: _Optional[int] = ...) -> None: ...

class PB_SyncChunkDataCH(_message.Message):
    __slots__ = ("SectionCoord", "trunkmd5")
    SECTIONCOORD_FIELD_NUMBER: _ClassVar[int]
    TRUNKMD5_FIELD_NUMBER: _ClassVar[int]
    SectionCoord: _proto_common_pb2.PB_Vector3
    trunkmd5: str
    def __init__(self, SectionCoord: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., trunkmd5: _Optional[str] = ...) -> None: ...

class PB_RoleEnterWorldCH(_message.Message):
    __slots__ = ("Uin", "GeniusLv", "UICtrlMode", "RoleInfo", "VipInfo", "lang", "apiid", "reserved", "Auth", "country", "cltversion", "session_id", "game_session_id", "specify_team")
    UIN_FIELD_NUMBER: _ClassVar[int]
    GENIUSLV_FIELD_NUMBER: _ClassVar[int]
    UICTRLMODE_FIELD_NUMBER: _ClassVar[int]
    ROLEINFO_FIELD_NUMBER: _ClassVar[int]
    VIPINFO_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    APIID_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CLTVERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIFY_TEAM_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    GeniusLv: int
    UICtrlMode: int
    RoleInfo: _proto_common_pb2.PB_RoleInfo
    VipInfo: _proto_common_pb2.PB_PlayerVipInfo
    lang: int
    apiid: int
    reserved: int
    Auth: str
    country: str
    cltversion: int
    session_id: str
    game_session_id: str
    specify_team: int
    def __init__(self, Uin: _Optional[int] = ..., GeniusLv: _Optional[int] = ..., UICtrlMode: _Optional[int] = ..., RoleInfo: _Optional[_Union[_proto_common_pb2.PB_RoleInfo, _Mapping]] = ..., VipInfo: _Optional[_Union[_proto_common_pb2.PB_PlayerVipInfo, _Mapping]] = ..., lang: _Optional[int] = ..., apiid: _Optional[int] = ..., reserved: _Optional[int] = ..., Auth: _Optional[str] = ..., country: _Optional[str] = ..., cltversion: _Optional[int] = ..., session_id: _Optional[str] = ..., game_session_id: _Optional[str] = ..., specify_team: _Optional[int] = ...) -> None: ...

class PB_RoleLeaveWorldCH(_message.Message):
    __slots__ = ("Uin",)
    UIN_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    def __init__(self, Uin: _Optional[int] = ...) -> None: ...

class PB_RoleCheckJoinFromSrcCH(_message.Message):
    __slots__ = ("Uin", "JoinFromSrc")
    UIN_FIELD_NUMBER: _ClassVar[int]
    JOINFROMSRC_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    JoinFromSrc: str
    def __init__(self, Uin: _Optional[int] = ..., JoinFromSrc: _Optional[str] = ...) -> None: ...

class PB_RoleMoveCH(_message.Message):
    __slots__ = ("MoveMotion", "AddMotion", "rentToken", "speed", "VehiclePos", "RayOrigin", "RayDir")
    MOVEMOTION_FIELD_NUMBER: _ClassVar[int]
    ADDMOTION_FIELD_NUMBER: _ClassVar[int]
    RENTTOKEN_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    VEHICLEPOS_FIELD_NUMBER: _ClassVar[int]
    RAYORIGIN_FIELD_NUMBER: _ClassVar[int]
    RAYDIR_FIELD_NUMBER: _ClassVar[int]
    MoveMotion: _proto_common_pb2.PB_MoveMotion
    AddMotion: _proto_common_pb2.PB_Vector3
    rentToken: int
    speed: float
    VehiclePos: _proto_common_pb2.PB_Vector3
    RayOrigin: _proto_common_pb2.PB_Vector3
    RayDir: _proto_common_pb2.PB_Vector3
    def __init__(self, MoveMotion: _Optional[_Union[_proto_common_pb2.PB_MoveMotion, _Mapping]] = ..., AddMotion: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., rentToken: _Optional[int] = ..., speed: _Optional[float] = ..., VehiclePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., RayOrigin: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., RayDir: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_TrainMoveCH(_message.Message):
    __slots__ = ("ObjID", "MapID", "CarReverse", "OutIndex", "CurveT", "MotionX", "MotionY", "MotionZ", "RailKnot")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CARREVERSE_FIELD_NUMBER: _ClassVar[int]
    OUTINDEX_FIELD_NUMBER: _ClassVar[int]
    CURVET_FIELD_NUMBER: _ClassVar[int]
    MOTIONX_FIELD_NUMBER: _ClassVar[int]
    MOTIONY_FIELD_NUMBER: _ClassVar[int]
    MOTIONZ_FIELD_NUMBER: _ClassVar[int]
    RAILKNOT_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    MapID: int
    CarReverse: int
    OutIndex: int
    CurveT: float
    MotionX: float
    MotionY: float
    MotionZ: float
    RailKnot: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., MapID: _Optional[int] = ..., CarReverse: _Optional[int] = ..., OutIndex: _Optional[int] = ..., CurveT: _Optional[float] = ..., MotionX: _Optional[float] = ..., MotionY: _Optional[float] = ..., MotionZ: _Optional[float] = ..., RailKnot: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorTeleportCH(_message.Message):
    __slots__ = ("ObjID", "TargetMap", "TargetPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TARGETMAP_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    TargetMap: int
    TargetPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., TargetMap: _Optional[int] = ..., TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_GunInfoCH(_message.Message):
    __slots__ = ("CurSpread", "CurJaw", "CurPitch", "CurPos")
    CURSPREAD_FIELD_NUMBER: _ClassVar[int]
    CURJAW_FIELD_NUMBER: _ClassVar[int]
    CURPITCH_FIELD_NUMBER: _ClassVar[int]
    CURPOS_FIELD_NUMBER: _ClassVar[int]
    CurSpread: float
    CurJaw: float
    CurPitch: float
    CurPos: _proto_common_pb2.PB_Vector3
    def __init__(self, CurSpread: _Optional[float] = ..., CurJaw: _Optional[float] = ..., CurPitch: _Optional[float] = ..., CurPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_SetInfoCH(_message.Message):
    __slots__ = ("Color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    Color: int
    def __init__(self, Color: _Optional[int] = ...) -> None: ...

class PB_ItemGridUserData(_message.Message):
    __slots__ = ("Uin", "GridIndex", "UserDataStr", "Type")
    UIN_FIELD_NUMBER: _ClassVar[int]
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    USERDATASTR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    GridIndex: int
    UserDataStr: str
    Type: int
    def __init__(self, Uin: _Optional[int] = ..., GridIndex: _Optional[int] = ..., UserDataStr: _Optional[str] = ..., Type: _Optional[int] = ...) -> None: ...

class PB_BlockInteractCH(_message.Message):
    __slots__ = ("face", "colptx", "colpty", "colptz", "blockpos")
    FACE_FIELD_NUMBER: _ClassVar[int]
    COLPTX_FIELD_NUMBER: _ClassVar[int]
    COLPTY_FIELD_NUMBER: _ClassVar[int]
    COLPTZ_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    face: int
    colptx: int
    colpty: int
    colptz: int
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, face: _Optional[int] = ..., colptx: _Optional[int] = ..., colpty: _Optional[int] = ..., colptz: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BlockInteractEndCH(_message.Message):
    __slots__ = ("blockpos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BlockPunchCH(_message.Message):
    __slots__ = ("status", "face", "digmethod", "blockpos", "vehicleObjID", "clienttick")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    DIGMETHOD_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    CLIENTTICK_FIELD_NUMBER: _ClassVar[int]
    status: int
    face: int
    digmethod: int
    blockpos: _proto_common_pb2.PB_Vector3
    vehicleObjID: int
    clienttick: int
    def __init__(self, status: _Optional[int] = ..., face: _Optional[int] = ..., digmethod: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., vehicleObjID: _Optional[int] = ..., clienttick: _Optional[int] = ...) -> None: ...

class PB_ItemUseCH(_message.Message):
    __slots__ = ("itemid", "status", "shift", "CurSpread", "CurYaw", "CurPitch", "CurPos", "usetick", "itemindex", "fireInterval", "PickResultPos", "PickResultFace")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_FIELD_NUMBER: _ClassVar[int]
    CURSPREAD_FIELD_NUMBER: _ClassVar[int]
    CURYAW_FIELD_NUMBER: _ClassVar[int]
    CURPITCH_FIELD_NUMBER: _ClassVar[int]
    CURPOS_FIELD_NUMBER: _ClassVar[int]
    USETICK_FIELD_NUMBER: _ClassVar[int]
    ITEMINDEX_FIELD_NUMBER: _ClassVar[int]
    FIREINTERVAL_FIELD_NUMBER: _ClassVar[int]
    PICKRESULTPOS_FIELD_NUMBER: _ClassVar[int]
    PICKRESULTFACE_FIELD_NUMBER: _ClassVar[int]
    itemid: int
    status: int
    shift: int
    CurSpread: float
    CurYaw: float
    CurPitch: float
    CurPos: _proto_common_pb2.PB_Vector3
    usetick: int
    itemindex: int
    fireInterval: int
    PickResultPos: _proto_common_pb2.PB_Vector3
    PickResultFace: int
    def __init__(self, itemid: _Optional[int] = ..., status: _Optional[int] = ..., shift: _Optional[int] = ..., CurSpread: _Optional[float] = ..., CurYaw: _Optional[float] = ..., CurPitch: _Optional[float] = ..., CurPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., usetick: _Optional[int] = ..., itemindex: _Optional[int] = ..., fireInterval: _Optional[int] = ..., PickResultPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., PickResultFace: _Optional[int] = ...) -> None: ...

class PB_SpecialSkillCH(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class PB_SetHookCH(_message.Message):
    __slots__ = ("ObjID", "hookID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HOOKID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    hookID: int
    def __init__(self, ObjID: _Optional[int] = ..., hookID: _Optional[int] = ...) -> None: ...

class PB_ItemSkillUseCH(_message.Message):
    __slots__ = ("itemid", "status", "skillid", "CurSpread", "CurPos", "CurDirX", "CurDirY", "CurDirZ", "ClientParam", "itemindex")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKILLID_FIELD_NUMBER: _ClassVar[int]
    CURSPREAD_FIELD_NUMBER: _ClassVar[int]
    CURPOS_FIELD_NUMBER: _ClassVar[int]
    CURDIRX_FIELD_NUMBER: _ClassVar[int]
    CURDIRY_FIELD_NUMBER: _ClassVar[int]
    CURDIRZ_FIELD_NUMBER: _ClassVar[int]
    CLIENTPARAM_FIELD_NUMBER: _ClassVar[int]
    ITEMINDEX_FIELD_NUMBER: _ClassVar[int]
    itemid: int
    status: int
    skillid: int
    CurSpread: float
    CurPos: _proto_common_pb2.PB_Vector3
    CurDirX: float
    CurDirY: float
    CurDirZ: float
    ClientParam: str
    itemindex: int
    def __init__(self, itemid: _Optional[int] = ..., status: _Optional[int] = ..., skillid: _Optional[int] = ..., CurSpread: _Optional[float] = ..., CurPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., CurDirX: _Optional[float] = ..., CurDirY: _Optional[float] = ..., CurDirZ: _Optional[float] = ..., ClientParam: _Optional[str] = ..., itemindex: _Optional[int] = ...) -> None: ...

class PB_ActorInteractCH(_message.Message):
    __slots__ = ("itype", "target", "iplot", "CurYaw", "CurPitch", "CurPos", "CollidePos")
    ITYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    IPLOT_FIELD_NUMBER: _ClassVar[int]
    CURYAW_FIELD_NUMBER: _ClassVar[int]
    CURPITCH_FIELD_NUMBER: _ClassVar[int]
    CURPOS_FIELD_NUMBER: _ClassVar[int]
    COLLIDEPOS_FIELD_NUMBER: _ClassVar[int]
    itype: int
    target: int
    iplot: int
    CurYaw: float
    CurPitch: float
    CurPos: _proto_common_pb2.PB_Vector3
    CollidePos: _proto_common_pb2.PB_Vector3
    def __init__(self, itype: _Optional[int] = ..., target: _Optional[int] = ..., iplot: _Optional[int] = ..., CurYaw: _Optional[float] = ..., CurPitch: _Optional[float] = ..., CurPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., CollidePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PCMouseEventCH(_message.Message):
    __slots__ = ("target", "keyType", "eventType")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    KEYTYPE_FIELD_NUMBER: _ClassVar[int]
    EVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    target: int
    keyType: PCMouseKeyType
    eventType: PCMouseEventType
    def __init__(self, target: _Optional[int] = ..., keyType: _Optional[_Union[PCMouseKeyType, str]] = ..., eventType: _Optional[_Union[PCMouseEventType, str]] = ...) -> None: ...

class PB_RClickUpInteractCH(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: int
    def __init__(self, target: _Optional[int] = ...) -> None: ...

class PB_TrainFollowOpCH(_message.Message):
    __slots__ = ("op_type", "actor_id", "target_id", "spacing", "keep_follower_chain", "tail_actor_id")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    KEEP_FOLLOWER_CHAIN_FIELD_NUMBER: _ClassVar[int]
    TAIL_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    op_type: int
    actor_id: int
    target_id: int
    spacing: float
    keep_follower_chain: bool
    tail_actor_id: int
    def __init__(self, op_type: _Optional[int] = ..., actor_id: _Optional[int] = ..., target_id: _Optional[int] = ..., spacing: _Optional[float] = ..., keep_follower_chain: _Optional[bool] = ..., tail_actor_id: _Optional[int] = ...) -> None: ...

class PB_ActorAnimCH(_message.Message):
    __slots__ = ("anim", "anim1", "actid", "actidTrigger", "sideAct", "animSeq", "isLoop", "animweapon", "animname", "layer", "speed", "crossfade", "isSeqId")
    ANIM_FIELD_NUMBER: _ClassVar[int]
    ANIM1_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    ACTIDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    SIDEACT_FIELD_NUMBER: _ClassVar[int]
    ANIMSEQ_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    ANIMWEAPON_FIELD_NUMBER: _ClassVar[int]
    ANIMNAME_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    ISSEQID_FIELD_NUMBER: _ClassVar[int]
    anim: int
    anim1: int
    actid: int
    actidTrigger: int
    sideAct: bool
    animSeq: int
    isLoop: int
    animweapon: int
    animname: str
    layer: int
    speed: float
    crossfade: float
    isSeqId: bool
    def __init__(self, anim: _Optional[int] = ..., anim1: _Optional[int] = ..., actid: _Optional[int] = ..., actidTrigger: _Optional[int] = ..., sideAct: _Optional[bool] = ..., animSeq: _Optional[int] = ..., isLoop: _Optional[int] = ..., animweapon: _Optional[int] = ..., animname: _Optional[str] = ..., layer: _Optional[int] = ..., speed: _Optional[float] = ..., crossfade: _Optional[float] = ..., isSeqId: _Optional[bool] = ...) -> None: ...

class PB_BackPackGridSwapCH(_message.Message):
    __slots__ = ("FromGridId", "ToGridId")
    FROMGRIDID_FIELD_NUMBER: _ClassVar[int]
    TOGRIDID_FIELD_NUMBER: _ClassVar[int]
    FromGridId: int
    ToGridId: int
    def __init__(self, FromGridId: _Optional[int] = ..., ToGridId: _Optional[int] = ...) -> None: ...

class PB_BackPackMoveItemCH(_message.Message):
    __slots__ = ("FromIndex", "ToIndex", "Num")
    FROMINDEX_FIELD_NUMBER: _ClassVar[int]
    TOINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    FromIndex: int
    ToIndex: int
    Num: int
    def __init__(self, FromIndex: _Optional[int] = ..., ToIndex: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_BackPackGridDiscardCH(_message.Message):
    __slots__ = ("GridId", "Num")
    GRIDID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    GridId: int
    Num: int
    def __init__(self, GridId: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_BackPackEquipWeaponCH(_message.Message):
    __slots__ = ("GridId",)
    GRIDID_FIELD_NUMBER: _ClassVar[int]
    GridId: int
    def __init__(self, GridId: _Optional[int] = ...) -> None: ...

class PB_EquipWeaponCH(_message.Message):
    __slots__ = ("itemId", "uin")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    uin: int
    def __init__(self, itemId: _Optional[int] = ..., uin: _Optional[int] = ...) -> None: ...

class PB_NeedContainerPasswordCH(_message.Message):
    __slots__ = ("Pos", "Password", "VehicleObjID")
    POS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    Password: int
    VehicleObjID: int
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Password: _Optional[int] = ..., VehicleObjID: _Optional[int] = ...) -> None: ...

class PB_CloseContainerCH(_message.Message):
    __slots__ = ("BaseIndex",)
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    def __init__(self, BaseIndex: _Optional[int] = ...) -> None: ...

class PB_SetContainerTextCH(_message.Message):
    __slots__ = ("BaseIndex", "Text")
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    Text: str
    def __init__(self, BaseIndex: _Optional[int] = ..., Text: _Optional[str] = ...) -> None: ...

class PB_BackPackStoreCH(_message.Message):
    __slots__ = ("FromIndex", "Num")
    FROMINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    FromIndex: int
    Num: int
    def __init__(self, FromIndex: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_BackPackLootCH(_message.Message):
    __slots__ = ("FromIndex", "Num")
    FROMINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    FromIndex: int
    Num: int
    def __init__(self, FromIndex: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_BackPackSortCH(_message.Message):
    __slots__ = ("BaseIndex",)
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    def __init__(self, BaseIndex: _Optional[int] = ...) -> None: ...

class PB_BackPackSetItemCH(_message.Message):
    __slots__ = ("ItemId", "ToIndex", "Num")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    TOINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ItemId: int
    ToIndex: int
    Num: int
    def __init__(self, ItemId: _Optional[int] = ..., ToIndex: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_BackPackSetItemWithoutLimitCH(_message.Message):
    __slots__ = ("ItemId", "ToIndex", "Num", "Userdata_Str")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    TOINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    USERDATA_STR_FIELD_NUMBER: _ClassVar[int]
    ItemId: int
    ToIndex: int
    Num: int
    Userdata_Str: str
    def __init__(self, ItemId: _Optional[int] = ..., ToIndex: _Optional[int] = ..., Num: _Optional[int] = ..., Userdata_Str: _Optional[str] = ...) -> None: ...

class PB_StorageBoxSortCH(_message.Message):
    __slots__ = ("BaseIndex",)
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    def __init__(self, BaseIndex: _Optional[int] = ...) -> None: ...

class PB_CraftItemCH(_message.Message):
    __slots__ = ("CraftId", "Num")
    CRAFTID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    CraftId: int
    Num: int
    def __init__(self, CraftId: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_EnchantItemCH(_message.Message):
    __slots__ = ("GridIndex", "FrmGridIndex", "EnchantIds")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    FRMGRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    ENCHANTIDS_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    FrmGridIndex: int
    EnchantIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, GridIndex: _Optional[int] = ..., FrmGridIndex: _Optional[int] = ..., EnchantIds: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_EnchantItemRandomCH(_message.Message):
    __slots__ = ("GridIndex",)
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    def __init__(self, GridIndex: _Optional[int] = ...) -> None: ...

class PB_RuneOperateCH(_message.Message):
    __slots__ = ("OpType", "Index1", "Index2", "Index3", "Index4")
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX1_FIELD_NUMBER: _ClassVar[int]
    INDEX2_FIELD_NUMBER: _ClassVar[int]
    INDEX3_FIELD_NUMBER: _ClassVar[int]
    INDEX4_FIELD_NUMBER: _ClassVar[int]
    OpType: int
    Index1: int
    Index2: int
    Index3: int
    Index4: int
    def __init__(self, OpType: _Optional[int] = ..., Index1: _Optional[int] = ..., Index2: _Optional[int] = ..., Index3: _Optional[int] = ..., Index4: _Optional[int] = ...) -> None: ...

class PB_RepairItemCH(_message.Message):
    __slots__ = ("GridIndex", "MaterialID", "UseNum")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    USENUM_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    MaterialID: int
    UseNum: int
    def __init__(self, GridIndex: _Optional[int] = ..., MaterialID: _Optional[int] = ..., UseNum: _Optional[int] = ...) -> None: ...

class PB_GunDoReloadCH(_message.Message):
    __slots__ = ("BulletID", "Num", "usetick", "isCustomGun", "noCheck", "curShortcut")
    BULLETID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    USETICK_FIELD_NUMBER: _ClassVar[int]
    ISCUSTOMGUN_FIELD_NUMBER: _ClassVar[int]
    NOCHECK_FIELD_NUMBER: _ClassVar[int]
    CURSHORTCUT_FIELD_NUMBER: _ClassVar[int]
    BulletID: int
    Num: int
    usetick: int
    isCustomGun: bool
    noCheck: bool
    curShortcut: int
    def __init__(self, BulletID: _Optional[int] = ..., Num: _Optional[int] = ..., usetick: _Optional[int] = ..., isCustomGun: _Optional[bool] = ..., noCheck: _Optional[bool] = ..., curShortcut: _Optional[int] = ...) -> None: ...

class PB_GunRecoveryCH(_message.Message):
    __slots__ = ("bulletID", "shortcut", "curNum", "isCost", "costNum")
    BULLETID_FIELD_NUMBER: _ClassVar[int]
    SHORTCUT_FIELD_NUMBER: _ClassVar[int]
    CURNUM_FIELD_NUMBER: _ClassVar[int]
    ISCOST_FIELD_NUMBER: _ClassVar[int]
    COSTNUM_FIELD_NUMBER: _ClassVar[int]
    bulletID: int
    shortcut: int
    curNum: int
    isCost: bool
    costNum: int
    def __init__(self, bulletID: _Optional[int] = ..., shortcut: _Optional[int] = ..., curNum: _Optional[int] = ..., isCost: _Optional[bool] = ..., costNum: _Optional[int] = ...) -> None: ...

class PB_BackPackShortcutOpCH(_message.Message):
    __slots__ = ("OpType", "FromIndex", "ToIndex", "IsOpen")
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    FROMINDEX_FIELD_NUMBER: _ClassVar[int]
    TOINDEX_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    OpType: int
    FromIndex: int
    ToIndex: int
    IsOpen: bool
    def __init__(self, OpType: _Optional[int] = ..., FromIndex: _Optional[int] = ..., ToIndex: _Optional[int] = ..., IsOpen: _Optional[bool] = ...) -> None: ...

class PB_AccountHorseCH(_message.Message):
    __slots__ = ("HorseID", "CmdType", "CmdData")
    HORSEID_FIELD_NUMBER: _ClassVar[int]
    CMDTYPE_FIELD_NUMBER: _ClassVar[int]
    CMDDATA_FIELD_NUMBER: _ClassVar[int]
    HorseID: int
    CmdType: int
    CmdData: int
    def __init__(self, HorseID: _Optional[int] = ..., CmdType: _Optional[int] = ..., CmdData: _Optional[int] = ...) -> None: ...

class PB_ActorReviveCH(_message.Message):
    __slots__ = ("ObjID", "Type")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Type: int
    def __init__(self, ObjID: _Optional[int] = ..., Type: _Optional[int] = ...) -> None: ...

class PB_JruisdicTionCH(_message.Message):
    __slots__ = ("Uin",)
    UIN_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    def __init__(self, Uin: _Optional[int] = ...) -> None: ...

class PB_ChatCH(_message.Message):
    __slots__ = ("ChatType", "TargetUin", "Content", "Language", "Extend", "Translate", "wwtk1", "wwtk2", "wwParam")
    CHATTYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    TRANSLATE_FIELD_NUMBER: _ClassVar[int]
    WWTK1_FIELD_NUMBER: _ClassVar[int]
    WWTK2_FIELD_NUMBER: _ClassVar[int]
    WWPARAM_FIELD_NUMBER: _ClassVar[int]
    ChatType: int
    TargetUin: int
    Content: str
    Language: int
    Extend: str
    Translate: str
    wwtk1: str
    wwtk2: str
    wwParam: str
    def __init__(self, ChatType: _Optional[int] = ..., TargetUin: _Optional[int] = ..., Content: _Optional[str] = ..., Language: _Optional[int] = ..., Extend: _Optional[str] = ..., Translate: _Optional[str] = ..., wwtk1: _Optional[str] = ..., wwtk2: _Optional[str] = ..., wwParam: _Optional[str] = ...) -> None: ...

class PB_ActorInviteCH(_message.Message):
    __slots__ = ("InviteType", "TargetUin", "ActID", "inviterPosX", "inviterPosZ")
    INVITETYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    INVITERPOSX_FIELD_NUMBER: _ClassVar[int]
    INVITERPOSZ_FIELD_NUMBER: _ClassVar[int]
    InviteType: int
    TargetUin: int
    ActID: int
    inviterPosX: int
    inviterPosZ: int
    def __init__(self, InviteType: _Optional[int] = ..., TargetUin: _Optional[int] = ..., ActID: _Optional[int] = ..., inviterPosX: _Optional[int] = ..., inviterPosZ: _Optional[int] = ...) -> None: ...

class PB_PlayerMountActorCH(_message.Message):
    __slots__ = ("ActorID", "IsShapeShift", "InteractBlockId", "IsByNearPlayer")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSHAPESHIFT_FIELD_NUMBER: _ClassVar[int]
    INTERACTBLOCKID_FIELD_NUMBER: _ClassVar[int]
    ISBYNEARPLAYER_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    IsShapeShift: bool
    InteractBlockId: int
    IsByNearPlayer: bool
    def __init__(self, ActorID: _Optional[int] = ..., IsShapeShift: _Optional[bool] = ..., InteractBlockId: _Optional[int] = ..., IsByNearPlayer: _Optional[bool] = ...) -> None: ...

class PB_PlayerMoveInputCH(_message.Message):
    __slots__ = ("MoveForward", "MoveStrafing", "Jumping", "Sneaking", "HeroInputUp")
    MOVEFORWARD_FIELD_NUMBER: _ClassVar[int]
    MOVESTRAFING_FIELD_NUMBER: _ClassVar[int]
    JUMPING_FIELD_NUMBER: _ClassVar[int]
    SNEAKING_FIELD_NUMBER: _ClassVar[int]
    HEROINPUTUP_FIELD_NUMBER: _ClassVar[int]
    MoveForward: float
    MoveStrafing: float
    Jumping: int
    Sneaking: int
    HeroInputUp: int
    def __init__(self, MoveForward: _Optional[float] = ..., MoveStrafing: _Optional[float] = ..., Jumping: _Optional[int] = ..., Sneaking: _Optional[int] = ..., HeroInputUp: _Optional[int] = ...) -> None: ...

class PB_PlayerSleepCH(_message.Message):
    __slots__ = ("Flags",)
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    Flags: int
    def __init__(self, Flags: _Optional[int] = ...) -> None: ...

class PB_NpcTradeCH(_message.Message):
    __slots__ = ("OpType", "Index", "WatchAD", "RewardNum")
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    WATCHAD_FIELD_NUMBER: _ClassVar[int]
    REWARDNUM_FIELD_NUMBER: _ClassVar[int]
    OpType: int
    Index: int
    WatchAD: int
    RewardNum: int
    def __init__(self, OpType: _Optional[int] = ..., Index: _Optional[int] = ..., WatchAD: _Optional[int] = ..., RewardNum: _Optional[int] = ...) -> None: ...

class PB_YMVoiceCH(_message.Message):
    __slots__ = ("YMMemberID", "YMSpeakerSwitch", "YMMicSwitch", "YMMemberRole")
    YMMEMBERID_FIELD_NUMBER: _ClassVar[int]
    YMSPEAKERSWITCH_FIELD_NUMBER: _ClassVar[int]
    YMMICSWITCH_FIELD_NUMBER: _ClassVar[int]
    YMMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    YMMemberID: int
    YMSpeakerSwitch: int
    YMMicSwitch: int
    YMMemberRole: int
    def __init__(self, YMMemberID: _Optional[int] = ..., YMSpeakerSwitch: _Optional[int] = ..., YMMicSwitch: _Optional[int] = ..., YMMemberRole: _Optional[int] = ...) -> None: ...

class PB_GVChangeRoleCH(_message.Message):
    __slots__ = ("ChangeResult",)
    CHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    ChangeResult: int
    def __init__(self, ChangeResult: _Optional[int] = ...) -> None: ...

class PB_YMChangeRoleCH(_message.Message):
    __slots__ = ("ChangeResult",)
    CHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    ChangeResult: int
    def __init__(self, ChangeResult: _Optional[int] = ...) -> None: ...

class PB_GetAccountItemsCH(_message.Message):
    __slots__ = ("ItemId", "Num")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ItemId: int
    Num: int
    def __init__(self, ItemId: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_SpecialItemUseCH(_message.Message):
    __slots__ = ("GridIndex", "ItemId", "ItemNum")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    ItemId: int
    ItemNum: int
    def __init__(self, GridIndex: _Optional[int] = ..., ItemId: _Optional[int] = ..., ItemNum: _Optional[int] = ...) -> None: ...

class PB_SetSpectatorModeCH(_message.Message):
    __slots__ = ("Uin", "SpectatorMode")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SPECTATORMODE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    SpectatorMode: int
    def __init__(self, Uin: _Optional[int] = ..., SpectatorMode: _Optional[int] = ...) -> None: ...

class PB_SetSpectatorTypeCH(_message.Message):
    __slots__ = ("Uin", "SpectatorType")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SPECTATORTYPE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    SpectatorType: int
    def __init__(self, Uin: _Optional[int] = ..., SpectatorType: _Optional[int] = ...) -> None: ...

class PB_SetSpectatorPlayerCH(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ...) -> None: ...

class PB_SetPlayerModelAniCH(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin", "ModelAnimalType", "ModelAnimalExt")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    MODELANIMALTYPE_FIELD_NUMBER: _ClassVar[int]
    MODELANIMALEXT_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    ModelAnimalType: int
    ModelAnimalExt: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ..., ModelAnimalType: _Optional[int] = ..., ModelAnimalExt: _Optional[int] = ...) -> None: ...

class PB_SendMyViewmodeToSpectatorCH(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin", "MyViewmode")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    MYVIEWMODE_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    MyViewmode: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ..., MyViewmode: _Optional[int] = ...) -> None: ...

class PB_SetBobbingToSpectatorCH(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin", "Bobbing")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    BOBBING_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    Bobbing: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ..., Bobbing: _Optional[int] = ...) -> None: ...

class PB_BallOperateCH(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ...) -> None: ...

class PB_RocketTeleportCH(_message.Message):
    __slots__ = ("MapId",)
    MAPID_FIELD_NUMBER: _ClassVar[int]
    MapId: int
    def __init__(self, MapId: _Optional[int] = ...) -> None: ...

class PB_CloseDialogueCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_AnswerTaskCH(_message.Message):
    __slots__ = ("TaskID", "PlotID", "Type")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    PLOTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TaskID: int
    PlotID: int
    Type: int
    def __init__(self, TaskID: _Optional[int] = ..., PlotID: _Optional[int] = ..., Type: _Optional[int] = ...) -> None: ...

class PB_CompleteTaskCH(_message.Message):
    __slots__ = ("TaskID",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TaskID: int
    def __init__(self, TaskID: _Optional[int] = ...) -> None: ...

class PB_PlayActCH(_message.Message):
    __slots__ = ("ActID", "ActIDTrigger")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    ACTIDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    ActID: int
    ActIDTrigger: int
    def __init__(self, ActID: _Optional[int] = ..., ActIDTrigger: _Optional[int] = ...) -> None: ...

class PB_BluePrintPreBlockCH(_message.Message):
    __slots__ = ("blockpos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_GravityOperateCH(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ...) -> None: ...

class PB_MakeCustomModelCH(_message.Message):
    __slots__ = ("Point", "ModelName", "ModelDesc", "ModelType")
    POINT_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    MODELDESC_FIELD_NUMBER: _ClassVar[int]
    MODELTYPE_FIELD_NUMBER: _ClassVar[int]
    Point: _proto_common_pb2.PB_Vector3
    ModelName: str
    ModelDesc: str
    ModelType: int
    def __init__(self, Point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., ModelName: _Optional[str] = ..., ModelDesc: _Optional[str] = ..., ModelType: _Optional[int] = ...) -> None: ...

class PB_SelectMobSpawnerCH(_message.Message):
    __slots__ = ("Point", "MobResID", "SpawnCount", "MaxNearbyMobs", "SpawnWide", "SpawnHigh", "MinSpawnDelay", "IsNumberDetection", "IsSpawnDelay")
    POINT_FIELD_NUMBER: _ClassVar[int]
    MOBRESID_FIELD_NUMBER: _ClassVar[int]
    SPAWNCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXNEARBYMOBS_FIELD_NUMBER: _ClassVar[int]
    SPAWNWIDE_FIELD_NUMBER: _ClassVar[int]
    SPAWNHIGH_FIELD_NUMBER: _ClassVar[int]
    MINSPAWNDELAY_FIELD_NUMBER: _ClassVar[int]
    ISNUMBERDETECTION_FIELD_NUMBER: _ClassVar[int]
    ISSPAWNDELAY_FIELD_NUMBER: _ClassVar[int]
    Point: _proto_common_pb2.PB_Vector3
    MobResID: int
    SpawnCount: int
    MaxNearbyMobs: int
    SpawnWide: int
    SpawnHigh: int
    MinSpawnDelay: int
    IsNumberDetection: int
    IsSpawnDelay: int
    def __init__(self, Point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MobResID: _Optional[int] = ..., SpawnCount: _Optional[int] = ..., MaxNearbyMobs: _Optional[int] = ..., SpawnWide: _Optional[int] = ..., SpawnHigh: _Optional[int] = ..., MinSpawnDelay: _Optional[int] = ..., IsNumberDetection: _Optional[int] = ..., IsSpawnDelay: _Optional[int] = ...) -> None: ...

class PB_GetNpcShopInfoCH(_message.Message):
    __slots__ = ("ShopID",)
    SHOPID_FIELD_NUMBER: _ClassVar[int]
    ShopID: int
    def __init__(self, ShopID: _Optional[int] = ...) -> None: ...

class PB_BuyNpcShopItemCH(_message.Message):
    __slots__ = ("ShopID", "SkuID", "BuyCount")
    SHOPID_FIELD_NUMBER: _ClassVar[int]
    SKUID_FIELD_NUMBER: _ClassVar[int]
    BUYCOUNT_FIELD_NUMBER: _ClassVar[int]
    ShopID: int
    SkuID: int
    BuyCount: int
    def __init__(self, ShopID: _Optional[int] = ..., SkuID: _Optional[int] = ..., BuyCount: _Optional[int] = ...) -> None: ...

class PB_CloseEditActorModelCH(_message.Message):
    __slots__ = ("BoneModels", "OperateType", "ModelType", "ModelName", "SkinDisplay")
    BONEMODELS_FIELD_NUMBER: _ClassVar[int]
    OPERATETYPE_FIELD_NUMBER: _ClassVar[int]
    MODELTYPE_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    SKINDISPLAY_FIELD_NUMBER: _ClassVar[int]
    BoneModels: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ActorOneBoneModelData]
    OperateType: int
    ModelType: int
    ModelName: str
    SkinDisplay: bool
    def __init__(self, BoneModels: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ActorOneBoneModelData, _Mapping]]] = ..., OperateType: _Optional[int] = ..., ModelType: _Optional[int] = ..., ModelName: _Optional[str] = ..., SkinDisplay: _Optional[bool] = ...) -> None: ...

class PB_PackGiftNotifyItemChgCH(_message.Message):
    __slots__ = ("ShortCutIdx", "CostItemInfo", "addlist")
    SHORTCUTIDX_FIELD_NUMBER: _ClassVar[int]
    COSTITEMINFO_FIELD_NUMBER: _ClassVar[int]
    ADDLIST_FIELD_NUMBER: _ClassVar[int]
    ShortCutIdx: int
    CostItemInfo: int
    addlist: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ShortCutIdx: _Optional[int] = ..., CostItemInfo: _Optional[int] = ..., addlist: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_VehiclePreBlockCH(_message.Message):
    __slots__ = ("blockpos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_VehicleItemUseCH(_message.Message):
    __slots__ = ("ShortCutIdx", "dir", "pos")
    SHORTCUTIDX_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ShortCutIdx: int
    dir: int
    pos: _proto_common_pb2.PB_Vector3
    def __init__(self, ShortCutIdx: _Optional[int] = ..., dir: _Optional[int] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_VehicleStartBlockCH(_message.Message):
    __slots__ = ("blockpos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_VehicleAttribChangeCH(_message.Message):
    __slots__ = ("ObjID", "Fuel", "PartIndex", "EngineState", "NitroLevel", "NitroEnable")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    FUEL_FIELD_NUMBER: _ClassVar[int]
    PARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ENGINESTATE_FIELD_NUMBER: _ClassVar[int]
    NITROLEVEL_FIELD_NUMBER: _ClassVar[int]
    NITROENABLE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Fuel: int
    PartIndex: int
    EngineState: int
    NitroLevel: int
    NitroEnable: int
    def __init__(self, ObjID: _Optional[int] = ..., Fuel: _Optional[int] = ..., PartIndex: _Optional[int] = ..., EngineState: _Optional[int] = ..., NitroLevel: _Optional[int] = ..., NitroEnable: _Optional[int] = ...) -> None: ...

class PB_WorkshopItemInfoCH(_message.Message):
    __slots__ = ("ContainerPos",)
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    ContainerPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayerVehicleMoveInputCH(_message.Message):
    __slots__ = ("Accel", "Brake", "Left", "Right")
    ACCEL_FIELD_NUMBER: _ClassVar[int]
    BRAKE_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    Accel: float
    Brake: float
    Left: float
    Right: float
    def __init__(self, Accel: _Optional[float] = ..., Brake: _Optional[float] = ..., Left: _Optional[float] = ..., Right: _Optional[float] = ...) -> None: ...

class PB_PlayerResetVehicleCH(_message.Message):
    __slots__ = ("ActorID",)
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    def __init__(self, ActorID: _Optional[int] = ...) -> None: ...

class PB_PlayerMotionStateChangeCH(_message.Message):
    __slots__ = ("StateType", "StateSwitch")
    STATETYPE_FIELD_NUMBER: _ClassVar[int]
    STATESWITCH_FIELD_NUMBER: _ClassVar[int]
    StateType: int
    StateSwitch: bool
    def __init__(self, StateType: _Optional[int] = ..., StateSwitch: _Optional[bool] = ...) -> None: ...

class PB_PlayerClickCH(_message.Message):
    __slots__ = ("ObjID", "ActorID", "BlockID", "BlockPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    ActorID: int
    BlockID: int
    BlockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., ActorID: _Optional[int] = ..., BlockID: _Optional[int] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayerSelectShortcutCH(_message.Message):
    __slots__ = ("objid", "index")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    objid: int
    index: int
    def __init__(self, objid: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class PB_ReqDownLoadResUrlCH(_message.Message):
    __slots__ = ("Type", "ExternData")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNDATA_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ExternData: str
    def __init__(self, Type: _Optional[int] = ..., ExternData: _Optional[str] = ...) -> None: ...

class PB_CloseFullyCustomModelUICH(_message.Message):
    __slots__ = ("OperateType", "Url", "Skey", "version", "Name", "Desc")
    OPERATETYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SKEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    OperateType: int
    Url: str
    Skey: str
    version: int
    Name: str
    Desc: str
    def __init__(self, OperateType: _Optional[int] = ..., Url: _Optional[str] = ..., Skey: _Optional[str] = ..., version: _Optional[int] = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ...) -> None: ...

class PB_PlayerNavFinishedCH(_message.Message):
    __slots__ = ("objid",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    def __init__(self, objid: _Optional[int] = ...) -> None: ...

class PB_VehicleAssembleLineCH(_message.Message):
    __slots__ = ("ObjID", "to")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    to: int
    def __init__(self, ObjID: _Optional[int] = ..., to: _Optional[int] = ..., **kwargs) -> None: ...

class PB_VehicleAssembleLineOperateCH(_message.Message):
    __slots__ = ("ObjID", "Blockid", "BlockPos", "IsClicked", "Type", "KeyId", "IsFire")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ISCLICKED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYID_FIELD_NUMBER: _ClassVar[int]
    ISFIRE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Blockid: int
    BlockPos: _proto_common_pb2.PB_Vector3
    IsClicked: bool
    Type: int
    KeyId: int
    IsFire: bool
    def __init__(self, ObjID: _Optional[int] = ..., Blockid: _Optional[int] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., IsClicked: _Optional[bool] = ..., Type: _Optional[int] = ..., KeyId: _Optional[int] = ..., IsFire: _Optional[bool] = ...) -> None: ...

class PB_UpdateActionerDataCH(_message.Message):
    __slots__ = ("ObjID", "BlockPos", "datastr")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    DATASTR_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    BlockPos: _proto_common_pb2.PB_Vector3
    datastr: str
    def __init__(self, ObjID: _Optional[int] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., datastr: _Optional[str] = ...) -> None: ...

class PB_CSPlayerPermitCH(_message.Message):
    __slots__ = ("Uin", "Bit", "BitVal", "BanItem", "IsBan")
    UIN_FIELD_NUMBER: _ClassVar[int]
    BIT_FIELD_NUMBER: _ClassVar[int]
    BITVAL_FIELD_NUMBER: _ClassVar[int]
    BANITEM_FIELD_NUMBER: _ClassVar[int]
    ISBAN_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Bit: int
    BitVal: bool
    BanItem: int
    IsBan: bool
    def __init__(self, Uin: _Optional[int] = ..., Bit: _Optional[int] = ..., BitVal: _Optional[bool] = ..., BanItem: _Optional[int] = ..., IsBan: _Optional[bool] = ...) -> None: ...

class PB_VehicleWorkshopLineCH(_message.Message):
    __slots__ = ("ContainerPos", "FromPos", "ToPos")
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    FROMPOS_FIELD_NUMBER: _ClassVar[int]
    TOPOS_FIELD_NUMBER: _ClassVar[int]
    ContainerPos: _proto_common_pb2.PB_Vector3
    FromPos: _proto_common_pb2.PB_Vector3
    ToPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., FromPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., ToPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_CSChangePlayerTeamCH(_message.Message):
    __slots__ = ("Uin", "TeamId")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    TeamId: int
    def __init__(self, Uin: _Optional[int] = ..., TeamId: _Optional[int] = ...) -> None: ...

class PB_CSRentRoomAutoMuteCH(_message.Message):
    __slots__ = ("SpamPreventionMinutes",)
    SPAMPREVENTIONMINUTES_FIELD_NUMBER: _ClassVar[int]
    SpamPreventionMinutes: int
    def __init__(self, SpamPreventionMinutes: _Optional[int] = ...) -> None: ...

class PB_VehicleAssembleLineUpdateCH(_message.Message):
    __slots__ = ("BlockPos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_MapEditHandleCH(_message.Message):
    __slots__ = ("EditMode", "ShapeType", "HandleType", "ExtraParamLength", "ExtraParamWidth", "ExtraParamHeight", "ExtraParamRadius", "ExtraParamIsSolid", "ExtraParamScale", "ExtraParamIsContinue", "ExtraParamDir", "ExtraParamFillerId", "ExtraParamReplaceId", "ExtraParamDistance", "ExtraParamOffsetX", "ExtraParamOffsetY", "ExtraParamOffsetZ", "ExtraParamRotateAngle", "ExtraParamTwoPointCPDir", "ExtraParamIsOnlyFillAtmosphere", "CenterPos", "BeginPos", "EndPos", "SaveCmd")
    EDITMODE_FIELD_NUMBER: _ClassVar[int]
    SHAPETYPE_FIELD_NUMBER: _ClassVar[int]
    HANDLETYPE_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMLENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMWIDTH_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMHEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMRADIUS_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMISSOLID_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMSCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMISCONTINUE_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMDIR_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMFILLERID_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMREPLACEID_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMDISTANCE_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMOFFSETX_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMOFFSETY_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMOFFSETZ_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMROTATEANGLE_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMTWOPOINTCPDIR_FIELD_NUMBER: _ClassVar[int]
    EXTRAPARAMISONLYFILLATMOSPHERE_FIELD_NUMBER: _ClassVar[int]
    CENTERPOS_FIELD_NUMBER: _ClassVar[int]
    BEGINPOS_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    SAVECMD_FIELD_NUMBER: _ClassVar[int]
    EditMode: int
    ShapeType: int
    HandleType: int
    ExtraParamLength: int
    ExtraParamWidth: int
    ExtraParamHeight: int
    ExtraParamRadius: int
    ExtraParamIsSolid: bool
    ExtraParamScale: int
    ExtraParamIsContinue: bool
    ExtraParamDir: int
    ExtraParamFillerId: int
    ExtraParamReplaceId: int
    ExtraParamDistance: int
    ExtraParamOffsetX: int
    ExtraParamOffsetY: int
    ExtraParamOffsetZ: int
    ExtraParamRotateAngle: int
    ExtraParamTwoPointCPDir: int
    ExtraParamIsOnlyFillAtmosphere: bool
    CenterPos: _proto_common_pb2.PB_Vector3
    BeginPos: _proto_common_pb2.PB_Vector3
    EndPos: _proto_common_pb2.PB_Vector3
    SaveCmd: int
    def __init__(self, EditMode: _Optional[int] = ..., ShapeType: _Optional[int] = ..., HandleType: _Optional[int] = ..., ExtraParamLength: _Optional[int] = ..., ExtraParamWidth: _Optional[int] = ..., ExtraParamHeight: _Optional[int] = ..., ExtraParamRadius: _Optional[int] = ..., ExtraParamIsSolid: _Optional[bool] = ..., ExtraParamScale: _Optional[int] = ..., ExtraParamIsContinue: _Optional[bool] = ..., ExtraParamDir: _Optional[int] = ..., ExtraParamFillerId: _Optional[int] = ..., ExtraParamReplaceId: _Optional[int] = ..., ExtraParamDistance: _Optional[int] = ..., ExtraParamOffsetX: _Optional[int] = ..., ExtraParamOffsetY: _Optional[int] = ..., ExtraParamOffsetZ: _Optional[int] = ..., ExtraParamRotateAngle: _Optional[int] = ..., ExtraParamTwoPointCPDir: _Optional[int] = ..., ExtraParamIsOnlyFillAtmosphere: _Optional[bool] = ..., CenterPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., BeginPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., EndPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., SaveCmd: _Optional[int] = ...) -> None: ...

class PB_MapEditRevokeCH(_message.Message):
    __slots__ = ("Revoke",)
    REVOKE_FIELD_NUMBER: _ClassVar[int]
    Revoke: bool
    def __init__(self, Revoke: _Optional[bool] = ...) -> None: ...

class PB_CloudRoomOwnerStartGameCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_CSKickOffDataCH(_message.Message):
    __slots__ = ("Uin", "KickerType")
    UIN_FIELD_NUMBER: _ClassVar[int]
    KICKERTYPE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    KickerType: int
    def __init__(self, Uin: _Optional[int] = ..., KickerType: _Optional[int] = ...) -> None: ...

class PB_UsePackingFCMItemCH(_message.Message):
    __slots__ = ("ItemId", "UsePos")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    USEPOS_FIELD_NUMBER: _ClassVar[int]
    ItemId: int
    UsePos: _proto_common_pb2.PB_Vector3
    def __init__(self, ItemId: _Optional[int] = ..., UsePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_CreatePackingCMCH(_message.Message):
    __slots__ = ("OffsetPos", "RotateType", "Name", "Desc", "CreateType", "StartPos", "EndPos")
    OFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    ROTATETYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    CREATETYPE_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    OffsetPos: _proto_common_pb2.PB_Vector3
    RotateType: int
    Name: str
    Desc: str
    CreateType: int
    StartPos: _proto_common_pb2.PB_Vector3
    EndPos: _proto_common_pb2.PB_Vector3
    def __init__(self, OffsetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., RotateType: _Optional[int] = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ..., CreateType: _Optional[int] = ..., StartPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., EndPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_InputContentCH(_message.Message):
    __slots__ = ("objId", "content")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    objId: int
    content: str
    def __init__(self, objId: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class PB_InputKeyCH(_message.Message):
    __slots__ = ("objId", "keyType", "eventType", "canClick")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    KEYTYPE_FIELD_NUMBER: _ClassVar[int]
    EVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CANCLICK_FIELD_NUMBER: _ClassVar[int]
    objId: int
    keyType: int
    eventType: str
    canClick: bool
    def __init__(self, objId: _Optional[int] = ..., keyType: _Optional[int] = ..., eventType: _Optional[str] = ..., canClick: _Optional[bool] = ...) -> None: ...

class PB_SensorContainerDataCH(_message.Message):
    __slots__ = ("BlockPos", "SensorValue", "IsBreverse", "ObjID")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    SENSORVALUE_FIELD_NUMBER: _ClassVar[int]
    ISBREVERSE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    SensorValue: int
    IsBreverse: bool
    ObjID: int
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., SensorValue: _Optional[int] = ..., IsBreverse: _Optional[bool] = ..., ObjID: _Optional[int] = ...) -> None: ...

class PB_PlayerCarryActorCH(_message.Message):
    __slots__ = ("ActorID", "Pos")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    Pos: _proto_common_pb2.PB_Vector3
    def __init__(self, ActorID: _Optional[int] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorPickupActorCH(_message.Message):
    __slots__ = ("AtkObjid", "DefObjid", "IsChangeDefActor")
    ATKOBJID_FIELD_NUMBER: _ClassVar[int]
    DEFOBJID_FIELD_NUMBER: _ClassVar[int]
    ISCHANGEDEFACTOR_FIELD_NUMBER: _ClassVar[int]
    AtkObjid: int
    DefObjid: int
    IsChangeDefActor: bool
    def __init__(self, AtkObjid: _Optional[int] = ..., DefObjid: _Optional[int] = ..., IsChangeDefActor: _Optional[bool] = ...) -> None: ...

class PB_ActorDropPickupActorCH(_message.Message):
    __slots__ = ("AtkObjid", "speed", "dir", "hasInertance", "isThrow")
    ATKOBJID_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    HASINERTANCE_FIELD_NUMBER: _ClassVar[int]
    ISTHROW_FIELD_NUMBER: _ClassVar[int]
    AtkObjid: int
    speed: float
    dir: _proto_common_pb2.PB_Vector3f
    hasInertance: bool
    isThrow: bool
    def __init__(self, AtkObjid: _Optional[int] = ..., speed: _Optional[float] = ..., dir: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., hasInertance: _Optional[bool] = ..., isThrow: _Optional[bool] = ...) -> None: ...

class PB_VillagerModifyName(_message.Message):
    __slots__ = ("ObjId", "Name")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    Name: str
    def __init__(self, ObjId: _Optional[int] = ..., Name: _Optional[str] = ...) -> None: ...

class PB_PlayerGotoPosCH(_message.Message):
    __slots__ = ("ObjId", "Pos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    Pos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjId: _Optional[int] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_CustomModelPrepareCH(_message.Message):
    __slots__ = ("Index", "HaveFile")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    HAVEFILE_FIELD_NUMBER: _ClassVar[int]
    Index: int
    HaveFile: int
    def __init__(self, Index: _Optional[int] = ..., HaveFile: _Optional[int] = ...) -> None: ...

class PB_MoveMobBackpackItemCH(_message.Message):
    __slots__ = ("gridIndex", "moveType", "toGridIndex")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    MOVETYPE_FIELD_NUMBER: _ClassVar[int]
    TOGRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    gridIndex: int
    moveType: int
    toGridIndex: int
    def __init__(self, gridIndex: _Optional[int] = ..., moveType: _Optional[int] = ..., toGridIndex: _Optional[int] = ...) -> None: ...

class PB_InteractMobBackpackItemCH(_message.Message):
    __slots__ = ("fromIndex", "toIndex")
    FROMINDEX_FIELD_NUMBER: _ClassVar[int]
    TOINDEX_FIELD_NUMBER: _ClassVar[int]
    fromIndex: int
    toIndex: int
    def __init__(self, fromIndex: _Optional[int] = ..., toIndex: _Optional[int] = ...) -> None: ...

class PB_AltarLuckyDrawCH(_message.Message):
    __slots__ = ("Pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayerRestoreTransformSkinCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_PlayerDeformationSkinCH(_message.Message):
    __slots__ = ("ActorID", "IsShapeShift")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSHAPESHIFT_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    IsShapeShift: bool
    def __init__(self, ActorID: _Optional[int] = ..., IsShapeShift: _Optional[bool] = ...) -> None: ...

class PB_PlayerResetDeformationCH(_message.Message):
    __slots__ = ("ActorID", "IsShapeShift")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSHAPESHIFT_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    IsShapeShift: bool
    def __init__(self, ActorID: _Optional[int] = ..., IsShapeShift: _Optional[bool] = ...) -> None: ...

class PB_PlayerBaseAttrCH(_message.Message):
    __slots__ = ("CurHP", "MaxHP", "CurFoodLv", "MaxFoodLv", "BaseSpeed", "AttackPunch", "AttackRange", "DefensePunch", "DefenseRange", "CurExp", "CurSexp", "CurLevel", "OverflowHP", "CurStrength", "MaxStrength", "OverflowStrength", "CurMana", "MaxMana")
    CURHP_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    CURFOODLV_FIELD_NUMBER: _ClassVar[int]
    MAXFOODLV_FIELD_NUMBER: _ClassVar[int]
    BASESPEED_FIELD_NUMBER: _ClassVar[int]
    ATTACKPUNCH_FIELD_NUMBER: _ClassVar[int]
    ATTACKRANGE_FIELD_NUMBER: _ClassVar[int]
    DEFENSEPUNCH_FIELD_NUMBER: _ClassVar[int]
    DEFENSERANGE_FIELD_NUMBER: _ClassVar[int]
    CUREXP_FIELD_NUMBER: _ClassVar[int]
    CURSEXP_FIELD_NUMBER: _ClassVar[int]
    CURLEVEL_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWHP_FIELD_NUMBER: _ClassVar[int]
    CURSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    MAXSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    CURMANA_FIELD_NUMBER: _ClassVar[int]
    MAXMANA_FIELD_NUMBER: _ClassVar[int]
    CurHP: float
    MaxHP: float
    CurFoodLv: float
    MaxFoodLv: float
    BaseSpeed: float
    AttackPunch: float
    AttackRange: float
    DefensePunch: float
    DefenseRange: float
    CurExp: int
    CurSexp: int
    CurLevel: int
    OverflowHP: float
    CurStrength: float
    MaxStrength: float
    OverflowStrength: float
    CurMana: float
    MaxMana: float
    def __init__(self, CurHP: _Optional[float] = ..., MaxHP: _Optional[float] = ..., CurFoodLv: _Optional[float] = ..., MaxFoodLv: _Optional[float] = ..., BaseSpeed: _Optional[float] = ..., AttackPunch: _Optional[float] = ..., AttackRange: _Optional[float] = ..., DefensePunch: _Optional[float] = ..., DefenseRange: _Optional[float] = ..., CurExp: _Optional[int] = ..., CurSexp: _Optional[int] = ..., CurLevel: _Optional[int] = ..., OverflowHP: _Optional[float] = ..., CurStrength: _Optional[float] = ..., MaxStrength: _Optional[float] = ..., OverflowStrength: _Optional[float] = ..., CurMana: _Optional[float] = ..., MaxMana: _Optional[float] = ...) -> None: ...

class PB_PlayerArchEntityCH(_message.Message):
    __slots__ = ("UserData",)
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    UserData: bytes
    def __init__(self, UserData: _Optional[bytes] = ...) -> None: ...

class PB_PrayTreeTimeCH(_message.Message):
    __slots__ = ("uin", "stage")
    UIN_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    uin: int
    stage: int
    def __init__(self, uin: _Optional[int] = ..., stage: _Optional[int] = ...) -> None: ...

class PB_SUMMONPETCH(_message.Message):
    __slots__ = ("monsterid", "serverid", "petid", "stage", "quality", "petname")
    MONSTERID_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    PETID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    PETNAME_FIELD_NUMBER: _ClassVar[int]
    monsterid: int
    serverid: str
    petid: int
    stage: int
    quality: int
    petname: str
    def __init__(self, monsterid: _Optional[int] = ..., serverid: _Optional[str] = ..., petid: _Optional[int] = ..., stage: _Optional[int] = ..., quality: _Optional[int] = ..., petname: _Optional[str] = ...) -> None: ...

class PB_HomeLandRanchUpdateAnimalStateCH(_message.Message):
    __slots__ = ("objid", "enterstate", "serverid")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ENTERSTATE_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    enterstate: int
    serverid: str
    def __init__(self, objid: _Optional[int] = ..., enterstate: _Optional[int] = ..., serverid: _Optional[str] = ...) -> None: ...

class PB_RequestModelName(_message.Message):
    __slots__ = ("modelID",)
    MODELID_FIELD_NUMBER: _ClassVar[int]
    modelID: str
    def __init__(self, modelID: _Optional[str] = ...) -> None: ...

class PB_VoiceInformCH(_message.Message):
    __slots__ = ("uin", "type", "voiceId", "reportUin", "node", "dir")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VOICEID_FIELD_NUMBER: _ClassVar[int]
    REPORTUIN_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    uin: int
    type: int
    voiceId: str
    reportUin: int
    node: str
    dir: str
    def __init__(self, uin: _Optional[int] = ..., type: _Optional[int] = ..., voiceId: _Optional[str] = ..., reportUin: _Optional[int] = ..., node: _Optional[str] = ..., dir: _Optional[str] = ...) -> None: ...

class PB_FurnaceTemperatureCH(_message.Message):
    __slots__ = ("BlockPos", "lev")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    LEV_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    lev: int
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., lev: _Optional[int] = ...) -> None: ...

class PB_PlayerTakeContainerGridItemCH(_message.Message):
    __slots__ = ("x", "y", "z", "gridIndex")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    z: int
    gridIndex: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., gridIndex: _Optional[int] = ...) -> None: ...

class PB_PlayerPotSetMakeCH(_message.Message):
    __slots__ = ("objid", "x", "y", "z", "make", "craftID", "num")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    MAKE_FIELD_NUMBER: _ClassVar[int]
    CRAFTID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    objid: int
    x: int
    y: int
    z: int
    make: bool
    craftID: int
    num: int
    def __init__(self, objid: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., make: _Optional[bool] = ..., craftID: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class PB_PlayerRevivePointCH(_message.Message):
    __slots__ = ("uin", "mapid", "revivepoint", "spawnpoint")
    UIN_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    REVIVEPOINT_FIELD_NUMBER: _ClassVar[int]
    SPAWNPOINT_FIELD_NUMBER: _ClassVar[int]
    uin: int
    mapid: int
    revivepoint: _proto_common_pb2.PB_Vector3
    spawnpoint: _proto_common_pb2.PB_Vector3
    def __init__(self, uin: _Optional[int] = ..., mapid: _Optional[int] = ..., revivepoint: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., spawnpoint: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BlockExploitCH(_message.Message):
    __slots__ = ("status", "face", "blockpos", "picktype")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    PICKTYPE_FIELD_NUMBER: _ClassVar[int]
    status: int
    face: int
    blockpos: _proto_common_pb2.PB_Vector3
    picktype: int
    def __init__(self, status: _Optional[int] = ..., face: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., picktype: _Optional[int] = ...) -> None: ...

class PB_PlayerTransferByStarStationCH(_message.Message):
    __slots__ = ("uin", "srcStarStationID", "cabinPos", "destStarStationID", "destMapID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SRCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    DESTSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    srcStarStationID: int
    cabinPos: _proto_common_pb2.PB_Vector3
    destStarStationID: int
    destMapID: int
    def __init__(self, uin: _Optional[int] = ..., srcStarStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., destStarStationID: _Optional[int] = ..., destMapID: _Optional[int] = ...) -> None: ...

class PB_ActivateStarStationCH(_message.Message):
    __slots__ = ("mapID", "consolePos")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CONSOLEPOS_FIELD_NUMBER: _ClassVar[int]
    mapID: int
    consolePos: _proto_common_pb2.PB_Vector3
    def __init__(self, mapID: _Optional[int] = ..., consolePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_UpgradeStarStationCabinCH(_message.Message):
    __slots__ = ("starStationID", "cabinPos")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: _proto_common_pb2.PB_Vector3
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BackPackRemoveItemItemCH(_message.Message):
    __slots__ = ("GridIndex", "Num")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    Num: int
    def __init__(self, GridIndex: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_StarStationTransferDeductFeeCH(_message.Message):
    __slots__ = ("playerUin", "destStarStationId", "srcStarStationId", "cabinPos", "destMapId", "costStar", "transferType")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    DESTSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    SRCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    COSTSTAR_FIELD_NUMBER: _ClassVar[int]
    TRANSFERTYPE_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    destStarStationId: int
    srcStarStationId: int
    cabinPos: _proto_common_pb2.PB_Vector3
    destMapId: int
    costStar: int
    transferType: int
    def __init__(self, playerUin: _Optional[int] = ..., destStarStationId: _Optional[int] = ..., srcStarStationId: _Optional[int] = ..., cabinPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., destMapId: _Optional[int] = ..., costStar: _Optional[int] = ..., transferType: _Optional[int] = ...) -> None: ...

class PB_GainItemsToBackPackCH(_message.Message):
    __slots__ = ("playerUin", "itemId", "itemNum")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    itemId: int
    itemNum: int
    def __init__(self, playerUin: _Optional[int] = ..., itemId: _Optional[int] = ..., itemNum: _Optional[int] = ...) -> None: ...

class PB_GainItemsUserDatastrToBackPackCH(_message.Message):
    __slots__ = ("playerUin", "itemId", "itemNum", "userdata_str")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    USERDATA_STR_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    itemId: int
    itemNum: int
    userdata_str: str
    def __init__(self, playerUin: _Optional[int] = ..., itemId: _Optional[int] = ..., itemNum: _Optional[int] = ..., userdata_str: _Optional[str] = ...) -> None: ...

class PB_UseMusicYuPuCH(_message.Message):
    __slots__ = ("playerUin", "itemId", "itemindex", "itemNum")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMINDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    itemId: int
    itemindex: int
    itemNum: int
    def __init__(self, playerUin: _Optional[int] = ..., itemId: _Optional[int] = ..., itemindex: _Optional[int] = ..., itemNum: _Optional[int] = ...) -> None: ...

class PB_BuyAdShopGoods(_message.Message):
    __slots__ = ("tabid", "goodid", "step", "success")
    TABID_FIELD_NUMBER: _ClassVar[int]
    GOODID_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    tabid: int
    goodid: int
    step: int
    success: bool
    def __init__(self, tabid: _Optional[int] = ..., goodid: _Optional[int] = ..., step: _Optional[int] = ..., success: _Optional[bool] = ...) -> None: ...

class PB_ExchangeItemsToBackPackCH(_message.Message):
    __slots__ = ("playerUin", "useItemId", "useItemNum", "gainItemId", "gainItemNum", "opertype")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    USEITEMID_FIELD_NUMBER: _ClassVar[int]
    USEITEMNUM_FIELD_NUMBER: _ClassVar[int]
    GAINITEMID_FIELD_NUMBER: _ClassVar[int]
    GAINITEMNUM_FIELD_NUMBER: _ClassVar[int]
    OPERTYPE_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    useItemId: int
    useItemNum: int
    gainItemId: int
    gainItemNum: int
    opertype: int
    def __init__(self, playerUin: _Optional[int] = ..., useItemId: _Optional[int] = ..., useItemNum: _Optional[int] = ..., gainItemId: _Optional[int] = ..., gainItemNum: _Optional[int] = ..., opertype: _Optional[int] = ...) -> None: ...

class PB_AchievementUpdateCH(_message.Message):
    __slots__ = ("achievementList",)
    ACHIEVEMENTLIST_FIELD_NUMBER: _ClassVar[int]
    achievementList: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_AchievementInfo]
    def __init__(self, achievementList: _Optional[_Iterable[_Union[_proto_common_pb2.PB_AchievementInfo, _Mapping]]] = ...) -> None: ...

class PB_CoustomUIEvent(_message.Message):
    __slots__ = ("opertype", "uiid", "elementid", "content")
    OPERTYPE_FIELD_NUMBER: _ClassVar[int]
    UIID_FIELD_NUMBER: _ClassVar[int]
    ELEMENTID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    opertype: int
    uiid: str
    elementid: str
    content: str
    def __init__(self, opertype: _Optional[int] = ..., uiid: _Optional[str] = ..., elementid: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class PB_AddExpCH(_message.Message):
    __slots__ = ("op", "starNum")
    OP_FIELD_NUMBER: _ClassVar[int]
    STARNUM_FIELD_NUMBER: _ClassVar[int]
    op: int
    starNum: int
    def __init__(self, op: _Optional[int] = ..., starNum: _Optional[int] = ...) -> None: ...

class PB_AddStarCH(_message.Message):
    __slots__ = ("starNum",)
    STARNUM_FIELD_NUMBER: _ClassVar[int]
    starNum: int
    def __init__(self, starNum: _Optional[int] = ...) -> None: ...

class PB_OneHomelandFooderRanchAnimalCH(_message.Message):
    __slots__ = ("SeedID", "GrowthTime", "FeedTime", "Stage", "Serverid", "SowTime", "FooderLevel", "FooderInterval", "FooderID", "FooderTime", "FooderTimeStatr", "FooderDesc")
    SEEDID_FIELD_NUMBER: _ClassVar[int]
    GROWTHTIME_FIELD_NUMBER: _ClassVar[int]
    FEEDTIME_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    SOWTIME_FIELD_NUMBER: _ClassVar[int]
    FOODERLEVEL_FIELD_NUMBER: _ClassVar[int]
    FOODERINTERVAL_FIELD_NUMBER: _ClassVar[int]
    FOODERID_FIELD_NUMBER: _ClassVar[int]
    FOODERTIME_FIELD_NUMBER: _ClassVar[int]
    FOODERTIMESTATR_FIELD_NUMBER: _ClassVar[int]
    FOODERDESC_FIELD_NUMBER: _ClassVar[int]
    SeedID: int
    GrowthTime: int
    FeedTime: int
    Stage: int
    Serverid: str
    SowTime: int
    FooderLevel: int
    FooderInterval: int
    FooderID: int
    FooderTime: int
    FooderTimeStatr: int
    FooderDesc: str
    def __init__(self, SeedID: _Optional[int] = ..., GrowthTime: _Optional[int] = ..., FeedTime: _Optional[int] = ..., Stage: _Optional[int] = ..., Serverid: _Optional[str] = ..., SowTime: _Optional[int] = ..., FooderLevel: _Optional[int] = ..., FooderInterval: _Optional[int] = ..., FooderID: _Optional[int] = ..., FooderTime: _Optional[int] = ..., FooderTimeStatr: _Optional[int] = ..., FooderDesc: _Optional[str] = ...) -> None: ...

class PB_UseHearthCH(_message.Message):
    __slots__ = ("playerUin", "hearthPos", "playerPos", "isUse")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    HEARTHPOS_FIELD_NUMBER: _ClassVar[int]
    PLAYERPOS_FIELD_NUMBER: _ClassVar[int]
    ISUSE_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    hearthPos: _proto_common_pb2.PB_Vector3
    playerPos: _proto_common_pb2.PB_Vector3
    isUse: bool
    def __init__(self, playerUin: _Optional[int] = ..., hearthPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., playerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., isUse: _Optional[bool] = ...) -> None: ...

class PB_ExposePosChangeCH(_message.Message):
    __slots__ = ("isExpose",)
    ISEXPOSE_FIELD_NUMBER: _ClassVar[int]
    isExpose: bool
    def __init__(self, isExpose: _Optional[bool] = ...) -> None: ...

class PB_HomeLandMenuBuyCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_HomeLandSpecialFurnitureBuyCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_HomeLandShopCellCH(_message.Message):
    __slots__ = ("uin", "itemid", "num")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    uin: int
    itemid: int
    num: int
    def __init__(self, uin: _Optional[int] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class PB_AnswerLanternBird_CH(_message.Message):
    __slots__ = ("uin", "answer")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    uin: int
    answer: int
    def __init__(self, uin: _Optional[int] = ..., answer: _Optional[int] = ...) -> None: ...

class PB_ChangeQQMusicPlayerCH(_message.Message):
    __slots__ = ("type", "musicId", "state", "volume", "playMode", "isOpen")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUSICID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PLAYMODE_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    type: int
    musicId: int
    state: bool
    volume: int
    playMode: int
    isOpen: bool
    def __init__(self, type: _Optional[int] = ..., musicId: _Optional[int] = ..., state: _Optional[bool] = ..., volume: _Optional[int] = ..., playMode: _Optional[int] = ..., isOpen: _Optional[bool] = ...) -> None: ...

class PB_PlayeCloseUICH(_message.Message):
    __slots__ = ("uiName", "uiParam", "mapId")
    UINAME_FIELD_NUMBER: _ClassVar[int]
    UIPARAM_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    uiName: str
    uiParam: str
    mapId: int
    def __init__(self, uiName: _Optional[str] = ..., uiParam: _Optional[str] = ..., mapId: _Optional[int] = ...) -> None: ...

class PB_PlaySkinActCH(_message.Message):
    __slots__ = ("ActID", "ActIDTrigger", "InviteUin", "AcceptUin")
    ACTID_FIELD_NUMBER: _ClassVar[int]
    ACTIDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    INVITEUIN_FIELD_NUMBER: _ClassVar[int]
    ACCEPTUIN_FIELD_NUMBER: _ClassVar[int]
    ActID: int
    ActIDTrigger: int
    InviteUin: int
    AcceptUin: int
    def __init__(self, ActID: _Optional[int] = ..., ActIDTrigger: _Optional[int] = ..., InviteUin: _Optional[int] = ..., AcceptUin: _Optional[int] = ...) -> None: ...

class PB_ActorStopSkinActCH(_message.Message):
    __slots__ = ("ActorID1", "ActorID2")
    ACTORID1_FIELD_NUMBER: _ClassVar[int]
    ACTORID2_FIELD_NUMBER: _ClassVar[int]
    ActorID1: int
    ActorID2: int
    def __init__(self, ActorID1: _Optional[int] = ..., ActorID2: _Optional[int] = ...) -> None: ...

class PB_ChangeQQMusicClubCH(_message.Message):
    __slots__ = ("type", "fraction", "uin", "name", "actionId", "enterArea", "mapId", "itemId", "itemNum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIONID_FIELD_NUMBER: _ClassVar[int]
    ENTERAREA_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    type: int
    fraction: int
    uin: int
    name: str
    actionId: int
    enterArea: bool
    mapId: int
    itemId: int
    itemNum: int
    def __init__(self, type: _Optional[int] = ..., fraction: _Optional[int] = ..., uin: _Optional[int] = ..., name: _Optional[str] = ..., actionId: _Optional[int] = ..., enterArea: _Optional[bool] = ..., mapId: _Optional[int] = ..., itemId: _Optional[int] = ..., itemNum: _Optional[int] = ...) -> None: ...

class PB_ActorStopAnimCH(_message.Message):
    __slots__ = ("anim", "actorid", "isSeq")
    ANIM_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSEQ_FIELD_NUMBER: _ClassVar[int]
    anim: int
    actorid: int
    isSeq: bool
    def __init__(self, anim: _Optional[int] = ..., actorid: _Optional[int] = ..., isSeq: _Optional[bool] = ...) -> None: ...

class PB_MiniClubMusicPlayerCH(_message.Message):
    __slots__ = ("type", "musicId", "state", "volume", "playMode", "isOpen")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUSICID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PLAYMODE_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    type: int
    musicId: int
    state: bool
    volume: int
    playMode: int
    isOpen: bool
    def __init__(self, type: _Optional[int] = ..., musicId: _Optional[int] = ..., state: _Optional[bool] = ..., volume: _Optional[int] = ..., playMode: _Optional[int] = ..., isOpen: _Optional[bool] = ...) -> None: ...

class PB_SprayPaintInfoCH(_message.Message):
    __slots__ = ("paintid",)
    PAINTID_FIELD_NUMBER: _ClassVar[int]
    paintid: int
    def __init__(self, paintid: _Optional[int] = ...) -> None: ...

class PB_SyncClientActionLogCH(_message.Message):
    __slots__ = ("cheat", "event", "detail")
    CHEAT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    cheat: bool
    event: str
    detail: str
    def __init__(self, cheat: _Optional[bool] = ..., event: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class PB_GetAchievementAwardCH(_message.Message):
    __slots__ = ("taskId",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    def __init__(self, taskId: _Optional[int] = ...) -> None: ...

class PB_UploadCheckInfoCH(_message.Message):
    __slots__ = ("info_type", "detail")
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    info_type: int
    detail: bytes
    def __init__(self, info_type: _Optional[int] = ..., detail: _Optional[bytes] = ...) -> None: ...

class PB_GetAdShopExtraAwardCH(_message.Message):
    __slots__ = ("award_id", "item_id", "item_count")
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    award_id: int
    item_id: int
    item_count: int
    def __init__(self, award_id: _Optional[int] = ..., item_id: _Optional[int] = ..., item_count: _Optional[int] = ...) -> None: ...

class PB_ExtractStoreItemCH(_message.Message):
    __slots__ = ("store_index", "item_id", "item_count")
    STORE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    store_index: int
    item_id: int
    item_count: int
    def __init__(self, store_index: _Optional[int] = ..., item_id: _Optional[int] = ..., item_count: _Optional[int] = ...) -> None: ...

class PB_PlayEffectCH(_message.Message):
    __slots__ = ("EffectType", "SoundNew", "effectScale", "StringActorBody")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    SOUNDNEW_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    STRINGACTORBODY_FIELD_NUMBER: _ClassVar[int]
    EffectType: int
    SoundNew: _proto_common_pb2.PB_EffectSoundNew
    effectScale: int
    StringActorBody: _proto_common_pb2.PB_EffectStringActorBody
    def __init__(self, EffectType: _Optional[int] = ..., SoundNew: _Optional[_Union[_proto_common_pb2.PB_EffectSoundNew, _Mapping]] = ..., effectScale: _Optional[int] = ..., StringActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectStringActorBody, _Mapping]] = ...) -> None: ...

class PB_DanceByPlayingCH(_message.Message):
    __slots__ = ("mobUin", "playerUin")
    MOBUIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    mobUin: int
    playerUin: int
    def __init__(self, mobUin: _Optional[int] = ..., playerUin: _Optional[int] = ...) -> None: ...

class PB_StopDanceByPlayingCH(_message.Message):
    __slots__ = ("mobUin", "playerUin")
    MOBUIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    mobUin: int
    playerUin: int
    def __init__(self, mobUin: _Optional[int] = ..., playerUin: _Optional[int] = ...) -> None: ...

class PB_PvpActivityConfigCH(_message.Message):
    __slots__ = ("activityId", "reportAddr", "start_time", "end_time", "mapId", "commParam", "timeZone", "extraRule")
    ACTIVITYID_FIELD_NUMBER: _ClassVar[int]
    REPORTADDR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    COMMPARAM_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    EXTRARULE_FIELD_NUMBER: _ClassVar[int]
    activityId: int
    reportAddr: str
    start_time: int
    end_time: int
    mapId: int
    commParam: str
    timeZone: int
    extraRule: str
    def __init__(self, activityId: _Optional[int] = ..., reportAddr: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., mapId: _Optional[int] = ..., commParam: _Optional[str] = ..., timeZone: _Optional[int] = ..., extraRule: _Optional[str] = ...) -> None: ...

class PB_StartActCH(_message.Message):
    __slots__ = ("playerUin", "playingState", "actID")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    PLAYINGSTATE_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    playingState: int
    actID: int
    def __init__(self, playerUin: _Optional[int] = ..., playingState: _Optional[int] = ..., actID: _Optional[int] = ...) -> None: ...

class PB_StopActCH(_message.Message):
    __slots__ = ("playerUin", "actID")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    actID: int
    def __init__(self, playerUin: _Optional[int] = ..., actID: _Optional[int] = ...) -> None: ...

class PB_TopBrandCH(_message.Message):
    __slots__ = ("targetUin", "brandName")
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    BRANDNAME_FIELD_NUMBER: _ClassVar[int]
    targetUin: int
    brandName: str
    def __init__(self, targetUin: _Optional[int] = ..., brandName: _Optional[str] = ...) -> None: ...

class PB_STARTFISHINGCH(_message.Message):
    __slots__ = ("TargetPos",)
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    TargetPos: _proto_common_pb2.PB_Vector3
    def __init__(self, TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ENDFISHINGCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_QUITFISHINGCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_EndPlayFishCH(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_UploadClientInfoCH(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: str
    def __init__(self, info: _Optional[str] = ...) -> None: ...

class PB_CheatCheatSubJump(_message.Message):
    __slots__ = ("jumpHeight", "onground", "airjump")
    JUMPHEIGHT_FIELD_NUMBER: _ClassVar[int]
    ONGROUND_FIELD_NUMBER: _ClassVar[int]
    AIRJUMP_FIELD_NUMBER: _ClassVar[int]
    jumpHeight: float
    onground: bool
    airjump: bool
    def __init__(self, jumpHeight: _Optional[float] = ..., onground: _Optional[bool] = ..., airjump: _Optional[bool] = ...) -> None: ...

class PB_CheatCheatSubTackle(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: float
    def __init__(self, range: _Optional[float] = ...) -> None: ...

class PB_CheatCheatSubGrab(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: float
    def __init__(self, range: _Optional[float] = ...) -> None: ...

class PB_CheatCheatSubDribble(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: float
    def __init__(self, range: _Optional[float] = ...) -> None: ...

class PB_CheatCheckSubClip(_message.Message):
    __slots__ = ("radius", "half_height", "bound_height", "bound_size")
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    HALF_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BOUND_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BOUND_SIZE_FIELD_NUMBER: _ClassVar[int]
    radius: float
    half_height: float
    bound_height: int
    bound_size: int
    def __init__(self, radius: _Optional[float] = ..., half_height: _Optional[float] = ..., bound_height: _Optional[int] = ..., bound_size: _Optional[int] = ...) -> None: ...

class PB_HostCheckCheat(_message.Message):
    __slots__ = ("checkType", "jump", "tackle", "grab", "dribble", "clip")
    CHECKTYPE_FIELD_NUMBER: _ClassVar[int]
    JUMP_FIELD_NUMBER: _ClassVar[int]
    TACKLE_FIELD_NUMBER: _ClassVar[int]
    GRAB_FIELD_NUMBER: _ClassVar[int]
    DRIBBLE_FIELD_NUMBER: _ClassVar[int]
    CLIP_FIELD_NUMBER: _ClassVar[int]
    checkType: CheatCheckType
    jump: PB_CheatCheatSubJump
    tackle: PB_CheatCheatSubTackle
    grab: PB_CheatCheatSubGrab
    dribble: PB_CheatCheatSubDribble
    clip: PB_CheatCheckSubClip
    def __init__(self, checkType: _Optional[_Union[CheatCheckType, str]] = ..., jump: _Optional[_Union[PB_CheatCheatSubJump, _Mapping]] = ..., tackle: _Optional[_Union[PB_CheatCheatSubTackle, _Mapping]] = ..., grab: _Optional[_Union[PB_CheatCheatSubGrab, _Mapping]] = ..., dribble: _Optional[_Union[PB_CheatCheatSubDribble, _Mapping]] = ..., clip: _Optional[_Union[PB_CheatCheckSubClip, _Mapping]] = ...) -> None: ...

class PB_BlockDataCH(_message.Message):
    __slots__ = ("x", "y", "z", "mapid", "text")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    z: int
    mapid: int
    text: str
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., mapid: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class PB_PushSnowBallOperateCH(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData", "TargetPos")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    TargetPos: _proto_common_pb2.PB_Vector3
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ..., TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayWeaponEffectCH(_message.Message):
    __slots__ = ("EffectName", "EffectID", "EffectScale", "EffectStatus", "ObjId")
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTSTATUS_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EffectName: str
    EffectID: int
    EffectScale: int
    EffectStatus: int
    ObjId: int
    def __init__(self, EffectName: _Optional[str] = ..., EffectID: _Optional[int] = ..., EffectScale: _Optional[int] = ..., EffectStatus: _Optional[int] = ..., ObjId: _Optional[int] = ...) -> None: ...

class PB_ActorPlayAnimCH(_message.Message):
    __slots__ = ("objId", "seqId", "loop", "speed", "layer", "preSeqId", "preLayer", "triggerAttack", "crossfade")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SEQID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    PRESEQID_FIELD_NUMBER: _ClassVar[int]
    PRELAYER_FIELD_NUMBER: _ClassVar[int]
    TRIGGERATTACK_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    objId: int
    seqId: int
    loop: int
    speed: float
    layer: int
    preSeqId: int
    preLayer: int
    triggerAttack: bool
    crossfade: float
    def __init__(self, objId: _Optional[int] = ..., seqId: _Optional[int] = ..., loop: _Optional[int] = ..., speed: _Optional[float] = ..., layer: _Optional[int] = ..., preSeqId: _Optional[int] = ..., preLayer: _Optional[int] = ..., triggerAttack: _Optional[bool] = ..., crossfade: _Optional[float] = ...) -> None: ...

class PB_ActorAttackCH(_message.Message):
    __slots__ = ("objId", "targetIds", "attackDefName", "triggerAttackHit")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TARGETIDS_FIELD_NUMBER: _ClassVar[int]
    ATTACKDEFNAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGERATTACKHIT_FIELD_NUMBER: _ClassVar[int]
    objId: int
    targetIds: _containers.RepeatedScalarFieldContainer[int]
    attackDefName: str
    triggerAttackHit: bool
    def __init__(self, objId: _Optional[int] = ..., targetIds: _Optional[_Iterable[int]] = ..., attackDefName: _Optional[str] = ..., triggerAttackHit: _Optional[bool] = ...) -> None: ...

class PB_ActorDefanceStateCH(_message.Message):
    __slots__ = ("objId", "defanceState")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    DEFANCESTATE_FIELD_NUMBER: _ClassVar[int]
    objId: int
    defanceState: bool
    def __init__(self, objId: _Optional[int] = ..., defanceState: _Optional[bool] = ...) -> None: ...

class PB_MoveTick(_message.Message):
    __slots__ = ("opera", "yaw", "pitch", "flags", "changed_flags", "dt")
    OPERA_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DT_FIELD_NUMBER: _ClassVar[int]
    opera: int
    yaw: int
    pitch: int
    flags: int
    changed_flags: int
    dt: int
    def __init__(self, opera: _Optional[int] = ..., yaw: _Optional[int] = ..., pitch: _Optional[int] = ..., flags: _Optional[int] = ..., changed_flags: _Optional[int] = ..., dt: _Optional[int] = ...) -> None: ...

class PB_FlagOn(_message.Message):
    __slots__ = ("type", "on")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ON_FIELD_NUMBER: _ClassVar[int]
    type: int
    on: bool
    def __init__(self, type: _Optional[int] = ..., on: _Optional[bool] = ...) -> None: ...

class PB_MoveSyncCH(_message.Message):
    __slots__ = ("id", "move_opera", "pos", "motion", "flag_change", "tick", "RayOrigin", "RayDir")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_OPERA_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    FLAG_CHANGE_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    RAYORIGIN_FIELD_NUMBER: _ClassVar[int]
    RAYDIR_FIELD_NUMBER: _ClassVar[int]
    id: int
    move_opera: PB_MoveTick
    pos: _proto_common_pb2.PB_Vector3
    motion: _proto_common_pb2.PB_Vector3
    flag_change: _containers.RepeatedCompositeFieldContainer[PB_FlagOn]
    tick: int
    RayOrigin: _proto_common_pb2.PB_Vector3
    RayDir: _proto_common_pb2.PB_Vector3
    def __init__(self, id: _Optional[int] = ..., move_opera: _Optional[_Union[PB_MoveTick, _Mapping]] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., motion: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., flag_change: _Optional[_Iterable[_Union[PB_FlagOn, _Mapping]]] = ..., tick: _Optional[int] = ..., RayOrigin: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., RayDir: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class MoveSegmentData(_message.Message):
    __slots__ = ("seq", "timeStamp", "deltaTime", "opera", "flagchange", "acceleration", "endPos", "endMotion", "endEuler", "state")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DELTATIME_FIELD_NUMBER: _ClassVar[int]
    OPERA_FIELD_NUMBER: _ClassVar[int]
    FLAGCHANGE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    ENDMOTION_FIELD_NUMBER: _ClassVar[int]
    ENDEULER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    seq: int
    timeStamp: float
    deltaTime: float
    opera: int
    flagchange: int
    acceleration: _proto_common_pb2.PB_Vector3f
    endPos: _proto_common_pb2.PB_Vector3f
    endMotion: _proto_common_pb2.PB_Vector3f
    endEuler: _proto_common_pb2.PB_Vector3f
    state: int
    def __init__(self, seq: _Optional[int] = ..., timeStamp: _Optional[float] = ..., deltaTime: _Optional[float] = ..., opera: _Optional[int] = ..., flagchange: _Optional[int] = ..., acceleration: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., endPos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., endMotion: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., endEuler: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., state: _Optional[int] = ...) -> None: ...

class PB_ControlMoveV4CH(_message.Message):
    __slots__ = ("lastServerAckSeq", "moveDataList")
    LASTSERVERACKSEQ_FIELD_NUMBER: _ClassVar[int]
    MOVEDATALIST_FIELD_NUMBER: _ClassVar[int]
    lastServerAckSeq: int
    moveDataList: _containers.RepeatedCompositeFieldContainer[MoveSegmentData]
    def __init__(self, lastServerAckSeq: _Optional[int] = ..., moveDataList: _Optional[_Iterable[_Union[MoveSegmentData, _Mapping]]] = ...) -> None: ...

class PB_MoveMoveCH(_message.Message):
    __slots__ = ("seq", "tm", "move_opera")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TM_FIELD_NUMBER: _ClassVar[int]
    MOVE_OPERA_FIELD_NUMBER: _ClassVar[int]
    seq: int
    tm: int
    move_opera: PB_MoveTick
    def __init__(self, seq: _Optional[int] = ..., tm: _Optional[int] = ..., move_opera: _Optional[_Union[PB_MoveTick, _Mapping]] = ...) -> None: ...

class PB_MoveReconcileFailedLogCH(_message.Message):
    __slots__ = ("seq", "motion_diff", "pos_diff")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    MOTION_DIFF_FIELD_NUMBER: _ClassVar[int]
    POS_DIFF_FIELD_NUMBER: _ClassVar[int]
    seq: int
    motion_diff: _proto_common_pb2.PB_Vector3
    pos_diff: _proto_common_pb2.PB_Vector3
    def __init__(self, seq: _Optional[int] = ..., motion_diff: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., pos_diff: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_NewRepairItemCH(_message.Message):
    __slots__ = ("TgtGridIdx", "RepairDur", "mat1Id", "mat2Id", "RepairCount", "StarCount")
    TGTGRIDIDX_FIELD_NUMBER: _ClassVar[int]
    REPAIRDUR_FIELD_NUMBER: _ClassVar[int]
    MAT1ID_FIELD_NUMBER: _ClassVar[int]
    MAT2ID_FIELD_NUMBER: _ClassVar[int]
    REPAIRCOUNT_FIELD_NUMBER: _ClassVar[int]
    STARCOUNT_FIELD_NUMBER: _ClassVar[int]
    TgtGridIdx: int
    RepairDur: int
    mat1Id: int
    mat2Id: int
    RepairCount: int
    StarCount: int
    def __init__(self, TgtGridIdx: _Optional[int] = ..., RepairDur: _Optional[int] = ..., mat1Id: _Optional[int] = ..., mat2Id: _Optional[int] = ..., RepairCount: _Optional[int] = ..., StarCount: _Optional[int] = ...) -> None: ...

class PB_ActorPlaySoundCH(_message.Message):
    __slots__ = ("name", "volume", "pitch", "fixpitch")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FIXPITCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    volume: float
    pitch: float
    fixpitch: bool
    def __init__(self, name: _Optional[str] = ..., volume: _Optional[float] = ..., pitch: _Optional[float] = ..., fixpitch: _Optional[bool] = ...) -> None: ...

class PB_GunRayInfo(_message.Message):
    __slots__ = ("pos", "dir", "range", "muzzle", "effectEnd")
    POS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    MUZZLE_FIELD_NUMBER: _ClassVar[int]
    EFFECTEND_FIELD_NUMBER: _ClassVar[int]
    pos: _proto_common_pb2.PB_Vector3f
    dir: _proto_common_pb2.PB_Vector3f
    range: int
    muzzle: _proto_common_pb2.PB_Vector3f
    effectEnd: _proto_common_pb2.PB_Vector3f
    def __init__(self, pos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., dir: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., range: _Optional[int] = ..., muzzle: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., effectEnd: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_ShootData_Actor(_message.Message):
    __slots__ = ("livingID", "iRay", "hurtParam")
    LIVINGID_FIELD_NUMBER: _ClassVar[int]
    IRAY_FIELD_NUMBER: _ClassVar[int]
    HURTPARAM_FIELD_NUMBER: _ClassVar[int]
    livingID: int
    iRay: int
    hurtParam: float
    def __init__(self, livingID: _Optional[int] = ..., iRay: _Optional[int] = ..., hurtParam: _Optional[float] = ...) -> None: ...

class PB_ShootData_Block(_message.Message):
    __slots__ = ("blockID", "iRay", "blockPosition", "blockPoint", "faceDirType")
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    IRAY_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOSITION_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOINT_FIELD_NUMBER: _ClassVar[int]
    FACEDIRTYPE_FIELD_NUMBER: _ClassVar[int]
    blockID: int
    iRay: int
    blockPosition: _proto_common_pb2.PB_Vector3f
    blockPoint: _proto_common_pb2.PB_Vector3f
    faceDirType: int
    def __init__(self, blockID: _Optional[int] = ..., iRay: _Optional[int] = ..., blockPosition: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., blockPoint: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., faceDirType: _Optional[int] = ...) -> None: ...

class PB_ActorShootCH(_message.Message):
    __slots__ = ("gunId", "bulletId", "rayInfos", "isAim", "projectileId", "useTick", "bClientPredict", "actorDatas", "blockDatas")
    GUNID_FIELD_NUMBER: _ClassVar[int]
    BULLETID_FIELD_NUMBER: _ClassVar[int]
    RAYINFOS_FIELD_NUMBER: _ClassVar[int]
    ISAIM_FIELD_NUMBER: _ClassVar[int]
    PROJECTILEID_FIELD_NUMBER: _ClassVar[int]
    USETICK_FIELD_NUMBER: _ClassVar[int]
    BCLIENTPREDICT_FIELD_NUMBER: _ClassVar[int]
    ACTORDATAS_FIELD_NUMBER: _ClassVar[int]
    BLOCKDATAS_FIELD_NUMBER: _ClassVar[int]
    gunId: int
    bulletId: int
    rayInfos: _containers.RepeatedCompositeFieldContainer[PB_GunRayInfo]
    isAim: bool
    projectileId: int
    useTick: int
    bClientPredict: bool
    actorDatas: _containers.RepeatedCompositeFieldContainer[PB_ShootData_Actor]
    blockDatas: _containers.RepeatedCompositeFieldContainer[PB_ShootData_Block]
    def __init__(self, gunId: _Optional[int] = ..., bulletId: _Optional[int] = ..., rayInfos: _Optional[_Iterable[_Union[PB_GunRayInfo, _Mapping]]] = ..., isAim: _Optional[bool] = ..., projectileId: _Optional[int] = ..., useTick: _Optional[int] = ..., bClientPredict: _Optional[bool] = ..., actorDatas: _Optional[_Iterable[_Union[PB_ShootData_Actor, _Mapping]]] = ..., blockDatas: _Optional[_Iterable[_Union[PB_ShootData_Block, _Mapping]]] = ...) -> None: ...

class PB_PlayerTransferCH(_message.Message):
    __slots__ = ("uin", "targetpos", "destMapID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    targetpos: _proto_common_pb2.PB_Vector3
    destMapID: int
    def __init__(self, uin: _Optional[int] = ..., targetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., destMapID: _Optional[int] = ...) -> None: ...

class PB_ResetPosResponeCH(_message.Message):
    __slots__ = ("tick",)
    TICK_FIELD_NUMBER: _ClassVar[int]
    tick: int
    def __init__(self, tick: _Optional[int] = ...) -> None: ...

class PB_ActorFireworkCH(_message.Message):
    __slots__ = ("fireworkID",)
    FIREWORKID_FIELD_NUMBER: _ClassVar[int]
    fireworkID: int
    def __init__(self, fireworkID: _Optional[int] = ...) -> None: ...

class PB_PlayerGunActionCH(_message.Message):
    __slots__ = ("state", "action")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    state: bool
    action: int
    def __init__(self, state: _Optional[bool] = ..., action: _Optional[int] = ...) -> None: ...

class PB_ByMountCH(_message.Message):
    __slots__ = ("objID", "boneId", "boneoffsetpos", "rideindex")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BONEID_FIELD_NUMBER: _ClassVar[int]
    BONEOFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    RIDEINDEX_FIELD_NUMBER: _ClassVar[int]
    objID: int
    boneId: int
    boneoffsetpos: _proto_common_pb2.PB_Vector3f
    rideindex: int
    def __init__(self, objID: _Optional[int] = ..., boneId: _Optional[int] = ..., boneoffsetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., rideindex: _Optional[int] = ...) -> None: ...

class PB_CheckNewUnlockItem_CH(_message.Message):
    __slots__ = ("itemId",)
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    def __init__(self, itemId: _Optional[int] = ...) -> None: ...

class PB_RecentlyMakeCraft_CH(_message.Message):
    __slots__ = ("craftId",)
    CRAFTID_FIELD_NUMBER: _ClassVar[int]
    craftId: int
    def __init__(self, craftId: _Optional[int] = ...) -> None: ...

class PB_ContainerUIData_CH(_message.Message):
    __slots__ = ("blockpos", "mapid", "b1", "b2", "i1", "i2")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    B1_FIELD_NUMBER: _ClassVar[int]
    B2_FIELD_NUMBER: _ClassVar[int]
    I1_FIELD_NUMBER: _ClassVar[int]
    I2_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    mapid: int
    b1: bool
    b2: bool
    i1: int
    i2: int
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., mapid: _Optional[int] = ..., b1: _Optional[bool] = ..., b2: _Optional[bool] = ..., i1: _Optional[int] = ..., i2: _Optional[int] = ...) -> None: ...

class PB_WorkingLivingwheelCH(_message.Message):
    __slots__ = ("mapid", "blockPos", "work")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    WORK_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    work: bool
    def __init__(self, mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., work: _Optional[bool] = ...) -> None: ...

class PB_RequestLivingwheelCH(_message.Message):
    __slots__ = ("mapid", "blockPos")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PickTransferGoodItem_CH(_message.Message):
    __slots__ = ("objID",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    objID: int
    def __init__(self, objID: _Optional[int] = ...) -> None: ...

class PB_IronDomeEssenceDisEquip_CH(_message.Message):
    __slots__ = ("obj",)
    OBJ_FIELD_NUMBER: _ClassVar[int]
    obj: int
    def __init__(self, obj: _Optional[int] = ...) -> None: ...

class PB_UpdateLaserPointerCH(_message.Message):
    __slots__ = ("enable", "pos")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    pos: _proto_common_pb2.PB_Vector3
    def __init__(self, enable: _Optional[bool] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_LivingInteractNewCH(_message.Message):
    __slots__ = ("targetId", "prepare", "stepFlags", "failPost")
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    PREPARE_FIELD_NUMBER: _ClassVar[int]
    STEPFLAGS_FIELD_NUMBER: _ClassVar[int]
    FAILPOST_FIELD_NUMBER: _ClassVar[int]
    targetId: int
    prepare: bool
    stepFlags: int
    failPost: bool
    def __init__(self, targetId: _Optional[int] = ..., prepare: _Optional[bool] = ..., stepFlags: _Optional[int] = ..., failPost: _Optional[bool] = ...) -> None: ...

class PB_PlayerTouchEvtCH(_message.Message):
    __slots__ = ("targetId", "goNodeType", "targetPos", "mapId", "isMobile", "touchType", "pcMouseKey", "curToolID", "touchLayer")
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    GONODETYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ISMOBILE_FIELD_NUMBER: _ClassVar[int]
    TOUCHTYPE_FIELD_NUMBER: _ClassVar[int]
    PCMOUSEKEY_FIELD_NUMBER: _ClassVar[int]
    CURTOOLID_FIELD_NUMBER: _ClassVar[int]
    TOUCHLAYER_FIELD_NUMBER: _ClassVar[int]
    targetId: int
    goNodeType: int
    targetPos: _proto_common_pb2.PB_Vector3
    mapId: int
    isMobile: bool
    touchType: TouchEventType
    pcMouseKey: PCMouseKeyType
    curToolID: int
    touchLayer: int
    def __init__(self, targetId: _Optional[int] = ..., goNodeType: _Optional[int] = ..., targetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., mapId: _Optional[int] = ..., isMobile: _Optional[bool] = ..., touchType: _Optional[_Union[TouchEventType, str]] = ..., pcMouseKey: _Optional[_Union[PCMouseKeyType, str]] = ..., curToolID: _Optional[int] = ..., touchLayer: _Optional[int] = ...) -> None: ...

class PB_AI_ASR_AUDIO_CH_MSG(_message.Message):
    __slots__ = ("uin", "name", "text_content", "audio_data")
    UIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    uin: int
    name: str
    text_content: str
    audio_data: bytes
    def __init__(self, uin: _Optional[int] = ..., name: _Optional[str] = ..., text_content: _Optional[str] = ..., audio_data: _Optional[bytes] = ...) -> None: ...

class PB_WBPMsgCH(_message.Message):
    __slots__ = ("msgid", "createBPMsg", "clickMsg", "addMtlMsg", "autoplacemsg")
    MSGID_FIELD_NUMBER: _ClassVar[int]
    CREATEBPMSG_FIELD_NUMBER: _ClassVar[int]
    CLICKMSG_FIELD_NUMBER: _ClassVar[int]
    ADDMTLMSG_FIELD_NUMBER: _ClassVar[int]
    AUTOPLACEMSG_FIELD_NUMBER: _ClassVar[int]
    msgid: int
    createBPMsg: _proto_common_pb2.PB_WBPCreateBluePrintMsg
    clickMsg: _proto_common_pb2.PB_WBPClickResultGrid
    addMtlMsg: _proto_common_pb2.PB_WBPAddMtlMsg
    autoplacemsg: _proto_common_pb2.PB_WBPAutoPlaceMsg
    def __init__(self, msgid: _Optional[int] = ..., createBPMsg: _Optional[_Union[_proto_common_pb2.PB_WBPCreateBluePrintMsg, _Mapping]] = ..., clickMsg: _Optional[_Union[_proto_common_pb2.PB_WBPClickResultGrid, _Mapping]] = ..., addMtlMsg: _Optional[_Union[_proto_common_pb2.PB_WBPAddMtlMsg, _Mapping]] = ..., autoplacemsg: _Optional[_Union[_proto_common_pb2.PB_WBPAutoPlaceMsg, _Mapping]] = ...) -> None: ...

class PB_RakePlantItemId_CH(_message.Message):
    __slots__ = ("itemId",)
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    def __init__(self, itemId: _Optional[int] = ...) -> None: ...

class PB_DropItemInteractResult_CH(_message.Message):
    __slots__ = ("iResult", "mobID", "playerID")
    IRESULT_FIELD_NUMBER: _ClassVar[int]
    MOBID_FIELD_NUMBER: _ClassVar[int]
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    iResult: int
    mobID: int
    playerID: int
    def __init__(self, iResult: _Optional[int] = ..., mobID: _Optional[int] = ..., playerID: _Optional[int] = ...) -> None: ...

class PB_PlayerUseItem_CH(_message.Message):
    __slots__ = ("itemid", "blockId", "x", "y", "z", "dir", "useTag")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    USETAG_FIELD_NUMBER: _ClassVar[int]
    itemid: int
    blockId: int
    x: int
    y: int
    z: int
    dir: int
    useTag: int
    def __init__(self, itemid: _Optional[int] = ..., blockId: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., dir: _Optional[int] = ..., useTag: _Optional[int] = ...) -> None: ...

class PB_ActorPlayAnimFinishCH(_message.Message):
    __slots__ = ("animid", "msgtype")
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    animid: int
    msgtype: int
    def __init__(self, animid: _Optional[int] = ..., msgtype: _Optional[int] = ...) -> None: ...

class PB_TimelineReportCH(_message.Message):
    __slots__ = ("status", "timelineId")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMELINEID_FIELD_NUMBER: _ClassVar[int]
    status: int
    timelineId: str
    def __init__(self, status: _Optional[int] = ..., timelineId: _Optional[str] = ...) -> None: ...

class PB_RefinableTakeResultCH(_message.Message):
    __slots__ = ("mapid", "blockPos", "taketype")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    TAKETYPE_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    taketype: int
    def __init__(self, mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., taketype: _Optional[int] = ...) -> None: ...

class PB_SpellEnhanceOperateCH(_message.Message):
    __slots__ = ("gridIndex", "slotIndex", "countNow", "opType")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    SLOTINDEX_FIELD_NUMBER: _ClassVar[int]
    COUNTNOW_FIELD_NUMBER: _ClassVar[int]
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    gridIndex: int
    slotIndex: int
    countNow: int
    opType: int
    def __init__(self, gridIndex: _Optional[int] = ..., slotIndex: _Optional[int] = ..., countNow: _Optional[int] = ..., opType: _Optional[int] = ...) -> None: ...

class PB_SetPersonalCloudCardInfoCH(_message.Message):
    __slots__ = ("cardNum",)
    CARDNUM_FIELD_NUMBER: _ClassVar[int]
    cardNum: int
    def __init__(self, cardNum: _Optional[int] = ...) -> None: ...

class PB_SpacePortalTeleportReqCH(_message.Message):
    __slots__ = ("buf",)
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: bytes
    def __init__(self, buf: _Optional[bytes] = ...) -> None: ...

class PB_SpacePortalChunkReqCH(_message.Message):
    __slots__ = ("buf",)
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: bytes
    def __init__(self, buf: _Optional[bytes] = ...) -> None: ...

class PB_PlayerWorldReadyCH(_message.Message):
    __slots__ = ("MapID", "ChunkBootstrapSeq")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CHUNKBOOTSTRAPSEQ_FIELD_NUMBER: _ClassVar[int]
    MapID: int
    ChunkBootstrapSeq: int
    def __init__(self, MapID: _Optional[int] = ..., ChunkBootstrapSeq: _Optional[int] = ...) -> None: ...

class PB_SpacePortalAnchorListReqCH(_message.Message):
    __slots__ = ("buf",)
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: bytes
    def __init__(self, buf: _Optional[bytes] = ...) -> None: ...
