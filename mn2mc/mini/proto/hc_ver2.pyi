from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PB_ThornBallHC(_message.Message):
    __slots__ = ("objid", "pos", "anchorId", "atkpoints", "dir", "impactInjured", "num")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ANCHORID_FIELD_NUMBER: _ClassVar[int]
    ATKPOINTS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    IMPACTINJURED_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    objid: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    anchorId: int
    atkpoints: int
    dir: int
    impactInjured: bool
    num: int
    def __init__(self, objid: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ..., anchorId: _Optional[int] = ..., atkpoints: _Optional[int] = ..., dir: _Optional[int] = ..., impactInjured: _Optional[bool] = ..., num: _Optional[int] = ...) -> None: ...

class PB_ActorOperationHC(_message.Message):
    __slots__ = ("objid", "data", "data2", "value", "sdata")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA2_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SDATA_FIELD_NUMBER: _ClassVar[int]
    objid: int
    data: int
    data2: int
    value: bool
    sdata: str
    def __init__(self, objid: _Optional[int] = ..., data: _Optional[int] = ..., data2: _Optional[int] = ..., value: _Optional[bool] = ..., sdata: _Optional[str] = ...) -> None: ...

class PB_ProfessionChangeHC(_message.Message):
    __slots__ = ("objid", "profession")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_FIELD_NUMBER: _ClassVar[int]
    objid: str
    profession: int
    def __init__(self, objid: _Optional[str] = ..., profession: _Optional[int] = ...) -> None: ...

class PB_ActorSandwormHC(_message.Message):
    __slots__ = ("objid", "isshow", "canmove", "scale", "objid2", "isfly")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ISSHOW_FIELD_NUMBER: _ClassVar[int]
    CANMOVE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    OBJID2_FIELD_NUMBER: _ClassVar[int]
    ISFLY_FIELD_NUMBER: _ClassVar[int]
    objid: int
    isshow: bool
    canmove: bool
    scale: int
    objid2: int
    isfly: bool
    def __init__(self, objid: _Optional[int] = ..., isshow: _Optional[bool] = ..., canmove: _Optional[bool] = ..., scale: _Optional[int] = ..., objid2: _Optional[int] = ..., isfly: _Optional[bool] = ...) -> None: ...

class PB_SkillplayanimHC(_message.Message):
    __slots__ = ("objid", "tpsanimid", "fpsanimid", "loop", "playLayer")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TPSANIMID_FIELD_NUMBER: _ClassVar[int]
    FPSANIMID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    PLAYLAYER_FIELD_NUMBER: _ClassVar[int]
    objid: int
    tpsanimid: int
    fpsanimid: int
    loop: int
    playLayer: int
    def __init__(self, objid: _Optional[int] = ..., tpsanimid: _Optional[int] = ..., fpsanimid: _Optional[int] = ..., loop: _Optional[int] = ..., playLayer: _Optional[int] = ...) -> None: ...

class PB_SkillstopanimHC(_message.Message):
    __slots__ = ("objid", "tpsanimid", "fpsanimid", "isReset")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TPSANIMID_FIELD_NUMBER: _ClassVar[int]
    FPSANIMID_FIELD_NUMBER: _ClassVar[int]
    ISRESET_FIELD_NUMBER: _ClassVar[int]
    objid: int
    tpsanimid: int
    fpsanimid: int
    isReset: bool
    def __init__(self, objid: _Optional[int] = ..., tpsanimid: _Optional[int] = ..., fpsanimid: _Optional[int] = ..., isReset: _Optional[bool] = ...) -> None: ...

class PB_SkillplaybodyeffectHC(_message.Message):
    __slots__ = ("objid", "path", "loopPlayTime", "OffsetPosition", "rote", "scale", "loop", "motionclass")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOOPPLAYTIME_FIELD_NUMBER: _ClassVar[int]
    OFFSETPOSITION_FIELD_NUMBER: _ClassVar[int]
    ROTE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    MOTIONCLASS_FIELD_NUMBER: _ClassVar[int]
    objid: int
    path: str
    loopPlayTime: float
    OffsetPosition: _containers.RepeatedScalarFieldContainer[int]
    rote: _containers.RepeatedScalarFieldContainer[int]
    scale: _containers.RepeatedScalarFieldContainer[int]
    loop: bool
    motionclass: int
    def __init__(self, objid: _Optional[int] = ..., path: _Optional[str] = ..., loopPlayTime: _Optional[float] = ..., OffsetPosition: _Optional[_Iterable[int]] = ..., rote: _Optional[_Iterable[int]] = ..., scale: _Optional[_Iterable[int]] = ..., loop: _Optional[bool] = ..., motionclass: _Optional[int] = ...) -> None: ...

class PB_SkillworldplaybodyeffectHC(_message.Message):
    __slots__ = ("uin", "path", "ptime", "isLoop", "x", "y", "z", "yaw", "pitch", "roll", "sx", "sy", "sz", "maxtdist")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PTIME_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    SX_FIELD_NUMBER: _ClassVar[int]
    SY_FIELD_NUMBER: _ClassVar[int]
    SZ_FIELD_NUMBER: _ClassVar[int]
    MAXTDIST_FIELD_NUMBER: _ClassVar[int]
    uin: int
    path: str
    ptime: int
    isLoop: int
    x: int
    y: int
    z: int
    yaw: float
    pitch: float
    roll: float
    sx: float
    sy: float
    sz: float
    maxtdist: int
    def __init__(self, uin: _Optional[int] = ..., path: _Optional[str] = ..., ptime: _Optional[int] = ..., isLoop: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ..., sx: _Optional[float] = ..., sy: _Optional[float] = ..., sz: _Optional[float] = ..., maxtdist: _Optional[int] = ...) -> None: ...

class PB_AccumulatorHC(_message.Message):
    __slots__ = ("uin", "progress")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    progress: float
    def __init__(self, uin: _Optional[int] = ..., progress: _Optional[float] = ...) -> None: ...

class PB_SkillplaytoolanimHC(_message.Message):
    __slots__ = ("objid", "animid")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    animid: int
    def __init__(self, objid: _Optional[int] = ..., animid: _Optional[int] = ...) -> None: ...

class PB_SkillsetchargemoveHC(_message.Message):
    __slots__ = ("uin", "chargemove")
    UIN_FIELD_NUMBER: _ClassVar[int]
    CHARGEMOVE_FIELD_NUMBER: _ClassVar[int]
    uin: int
    chargemove: float
    def __init__(self, uin: _Optional[int] = ..., chargemove: _Optional[float] = ...) -> None: ...

class PB_SkillmoveHC(_message.Message):
    __slots__ = ("objid", "x", "y", "z")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    objid: int
    x: int
    y: int
    z: int
    def __init__(self, objid: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class PB_SkillcameraHC(_message.Message):
    __slots__ = ("uin", "val", "isReset")
    UIN_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    ISRESET_FIELD_NUMBER: _ClassVar[int]
    uin: int
    val: float
    isReset: int
    def __init__(self, uin: _Optional[int] = ..., val: _Optional[float] = ..., isReset: _Optional[int] = ...) -> None: ...

class PB_SetlocotypeHC(_message.Message):
    __slots__ = ("objid", "locotype", "isno")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    LOCOTYPE_FIELD_NUMBER: _ClassVar[int]
    ISNO_FIELD_NUMBER: _ClassVar[int]
    objid: int
    locotype: int
    isno: int
    def __init__(self, objid: _Optional[int] = ..., locotype: _Optional[int] = ..., isno: _Optional[int] = ...) -> None: ...

class PB_BasestateHC(_message.Message):
    __slots__ = ("objid", "SetAbilityGroupState", "eGroupID", "bOpen", "SetAbilityState", "eAbilityID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SETABILITYGROUPSTATE_FIELD_NUMBER: _ClassVar[int]
    EGROUPID_FIELD_NUMBER: _ClassVar[int]
    BOPEN_FIELD_NUMBER: _ClassVar[int]
    SETABILITYSTATE_FIELD_NUMBER: _ClassVar[int]
    EABILITYID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    SetAbilityGroupState: int
    eGroupID: int
    bOpen: int
    SetAbilityState: int
    eAbilityID: int
    def __init__(self, objid: _Optional[int] = ..., SetAbilityGroupState: _Optional[int] = ..., eGroupID: _Optional[int] = ..., bOpen: _Optional[int] = ..., SetAbilityState: _Optional[int] = ..., eAbilityID: _Optional[int] = ...) -> None: ...

class PB_SetmovementModeHC(_message.Message):
    __slots__ = ("objid", "movementModeOrAuto")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MOVEMENTMODEORAUTO_FIELD_NUMBER: _ClassVar[int]
    objid: int
    movementModeOrAuto: int
    def __init__(self, objid: _Optional[int] = ..., movementModeOrAuto: _Optional[int] = ...) -> None: ...

class PB_HorseflystateHC(_message.Message):
    __slots__ = ("objid", "uin", "flying")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    FLYING_FIELD_NUMBER: _ClassVar[int]
    objid: int
    uin: int
    flying: int
    def __init__(self, objid: _Optional[int] = ..., uin: _Optional[int] = ..., flying: _Optional[int] = ...) -> None: ...

class PB_PlayerCameraconfigHC(_message.Message):
    __slots__ = ("obj", "ops", "posx", "posy", "posz", "fov", "dirx", "diry", "dirz")
    OBJ_FIELD_NUMBER: _ClassVar[int]
    OPS_FIELD_NUMBER: _ClassVar[int]
    POSX_FIELD_NUMBER: _ClassVar[int]
    POSY_FIELD_NUMBER: _ClassVar[int]
    POSZ_FIELD_NUMBER: _ClassVar[int]
    FOV_FIELD_NUMBER: _ClassVar[int]
    DIRX_FIELD_NUMBER: _ClassVar[int]
    DIRY_FIELD_NUMBER: _ClassVar[int]
    DIRZ_FIELD_NUMBER: _ClassVar[int]
    obj: int
    ops: _containers.RepeatedScalarFieldContainer[int]
    posx: int
    posy: int
    posz: int
    fov: float
    dirx: float
    diry: float
    dirz: float
    def __init__(self, obj: _Optional[int] = ..., ops: _Optional[_Iterable[int]] = ..., posx: _Optional[int] = ..., posy: _Optional[int] = ..., posz: _Optional[int] = ..., fov: _Optional[float] = ..., dirx: _Optional[float] = ..., diry: _Optional[float] = ..., dirz: _Optional[float] = ...) -> None: ...

class PB_BackpackNumChangeHC(_message.Message):
    __slots__ = ("uin", "num")
    UIN_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    uin: int
    num: int
    def __init__(self, uin: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class PB_PlaySkinVoiceHC(_message.Message):
    __slots__ = ("skinId", "voiceType", "pos")
    SKINID_FIELD_NUMBER: _ClassVar[int]
    VOICETYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    skinId: int
    voiceType: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skinId: _Optional[int] = ..., voiceType: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_NewYearBossStageHC(_message.Message):
    __slots__ = ("objid", "stage", "hp", "totalhp")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    TOTALHP_FIELD_NUMBER: _ClassVar[int]
    objid: int
    stage: int
    hp: int
    totalhp: int
    def __init__(self, objid: _Optional[int] = ..., stage: _Optional[int] = ..., hp: _Optional[int] = ..., totalhp: _Optional[int] = ...) -> None: ...

class PB_NewYearHpHC(_message.Message):
    __slots__ = ("objid", "hp", "totalhp")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    TOTALHP_FIELD_NUMBER: _ClassVar[int]
    objid: int
    hp: int
    totalhp: int
    def __init__(self, objid: _Optional[int] = ..., hp: _Optional[int] = ..., totalhp: _Optional[int] = ...) -> None: ...

class PB_NewYearMonsterPosHC(_message.Message):
    __slots__ = ("objid", "pos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    objid: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, objid: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_PedalBlockCH(_message.Message):
    __slots__ = ("handletype", "srcpos", "despos", "dropitem")
    HANDLETYPE_FIELD_NUMBER: _ClassVar[int]
    SRCPOS_FIELD_NUMBER: _ClassVar[int]
    DESPOS_FIELD_NUMBER: _ClassVar[int]
    DROPITEM_FIELD_NUMBER: _ClassVar[int]
    handletype: int
    srcpos: _containers.RepeatedScalarFieldContainer[int]
    despos: _containers.RepeatedScalarFieldContainer[int]
    dropitem: bool
    def __init__(self, handletype: _Optional[int] = ..., srcpos: _Optional[_Iterable[int]] = ..., despos: _Optional[_Iterable[int]] = ..., dropitem: _Optional[bool] = ...) -> None: ...

class PB_CustomPbcHC(_message.Message):
    __slots__ = ("type", "payload", "ziplen", "unziplen", "islua")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ZIPLEN_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    ISLUA_FIELD_NUMBER: _ClassVar[int]
    type: str
    payload: bytes
    ziplen: int
    unziplen: int
    islua: bool
    def __init__(self, type: _Optional[str] = ..., payload: _Optional[bytes] = ..., ziplen: _Optional[int] = ..., unziplen: _Optional[int] = ..., islua: _Optional[bool] = ...) -> None: ...

class PB_DynamicProtoHC(_message.Message):
    __slots__ = ("payload", "ziplen", "unziplen", "type")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ZIPLEN_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    ziplen: int
    unziplen: int
    type: int
    def __init__(self, payload: _Optional[bytes] = ..., ziplen: _Optional[int] = ..., unziplen: _Optional[int] = ..., type: _Optional[int] = ...) -> None: ...
