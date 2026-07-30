from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PB_ThornBallCH(_message.Message):
    __slots__ = ("atkpoints", "num", "dir")
    ATKPOINTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    atkpoints: int
    num: int
    dir: int
    def __init__(self, atkpoints: _Optional[int] = ..., num: _Optional[int] = ..., dir: _Optional[int] = ...) -> None: ...

class PB_ActorOperationCH(_message.Message):
    __slots__ = ("blockid", "pos", "blockdata", "dropitem", "waterPress", "lowerWaterPress", "mapid")
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    BLOCKDATA_FIELD_NUMBER: _ClassVar[int]
    DROPITEM_FIELD_NUMBER: _ClassVar[int]
    WATERPRESS_FIELD_NUMBER: _ClassVar[int]
    LOWERWATERPRESS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    blockid: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    blockdata: int
    dropitem: bool
    waterPress: int
    lowerWaterPress: int
    mapid: int
    def __init__(self, blockid: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ..., blockdata: _Optional[int] = ..., dropitem: _Optional[bool] = ..., waterPress: _Optional[int] = ..., lowerWaterPress: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class PB_StorageBoxPutAllCH(_message.Message):
    __slots__ = ("playeruin", "baseindex", "blockid", "pos")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    playeruin: int
    baseindex: int
    blockid: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, playeruin: _Optional[int] = ..., baseindex: _Optional[int] = ..., blockid: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_SyncDyeableItemCH(_message.Message):
    __slots__ = ("playeruin", "index", "itemid", "num", "sdata")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    SDATA_FIELD_NUMBER: _ClassVar[int]
    playeruin: int
    index: int
    itemid: int
    num: int
    sdata: str
    def __init__(self, playeruin: _Optional[int] = ..., index: _Optional[int] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ..., sdata: _Optional[str] = ...) -> None: ...

class PB_StoveTakeCH(_message.Message):
    __slots__ = ("pos", "uin", "index", "taketype")
    POS_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TAKETYPE_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedScalarFieldContainer[int]
    uin: int
    index: int
    taketype: int
    def __init__(self, pos: _Optional[_Iterable[int]] = ..., uin: _Optional[int] = ..., index: _Optional[int] = ..., taketype: _Optional[int] = ...) -> None: ...

class PB_StopweaponanimCH(_message.Message):
    __slots__ = ("objid", "animid")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    animid: int
    def __init__(self, objid: _Optional[int] = ..., animid: _Optional[int] = ...) -> None: ...

class PB_StopweaponmotionCH(_message.Message):
    __slots__ = ("objid", "mclass")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MCLASS_FIELD_NUMBER: _ClassVar[int]
    objid: int
    mclass: int
    def __init__(self, objid: _Optional[int] = ..., mclass: _Optional[int] = ...) -> None: ...

class PB_PlaySkinVoiceCH(_message.Message):
    __slots__ = ("skinId", "voiceType", "pos", "uinlist")
    SKINID_FIELD_NUMBER: _ClassVar[int]
    VOICETYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    UINLIST_FIELD_NUMBER: _ClassVar[int]
    skinId: int
    voiceType: int
    pos: _containers.RepeatedScalarFieldContainer[int]
    uinlist: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skinId: _Optional[int] = ..., voiceType: _Optional[int] = ..., pos: _Optional[_Iterable[int]] = ..., uinlist: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_BoxPlayAniCH(_message.Message):
    __slots__ = ("objid",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    def __init__(self, objid: _Optional[int] = ...) -> None: ...

class PB_CustomPbcCH(_message.Message):
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
