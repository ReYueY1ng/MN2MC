import proto_common_pb2 as _proto_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkSyncInitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHUNK_SYNC_INIT_UPDATE: _ClassVar[ChunkSyncInitType]
    CHUNK_SYNC_INIT_INITIALIZE: _ClassVar[ChunkSyncInitType]
    CHUNK_SYNC_INIT_REQUEST: _ClassVar[ChunkSyncInitType]
    CHUNK_SYNC_INIT_MD5_MATCH: _ClassVar[ChunkSyncInitType]
CHUNK_SYNC_INIT_UPDATE: ChunkSyncInitType
CHUNK_SYNC_INIT_INITIALIZE: ChunkSyncInitType
CHUNK_SYNC_INIT_REQUEST: ChunkSyncInitType
CHUNK_SYNC_INIT_MD5_MATCH: ChunkSyncInitType

class PB_MsgErrorHC(_message.Message):
    __slots__ = ("ErrCode",)
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    ErrCode: int
    def __init__(self, ErrCode: _Optional[int] = ...) -> None: ...

class PB_HeartBeatHC(_message.Message):
    __slots__ = ("BeatCode",)
    BEATCODE_FIELD_NUMBER: _ClassVar[int]
    BeatCode: int
    def __init__(self, BeatCode: _Optional[int] = ...) -> None: ...

class PB_regionfileInfo(_message.Message):
    __slots__ = ("posx", "posz", "url", "worldid")
    POSX_FIELD_NUMBER: _ClassVar[int]
    POSZ_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    posx: int
    posz: int
    url: str
    worldid: int
    def __init__(self, posx: _Optional[int] = ..., posz: _Optional[int] = ..., url: _Optional[str] = ..., worldid: _Optional[int] = ...) -> None: ...

class PB_RoomExtraInfoHC(_message.Message):
    __slots__ = ("room_extra", "CMURL", "MapMD5", "MapID", "regionfile_info")
    ROOM_EXTRA_FIELD_NUMBER: _ClassVar[int]
    CMURL_FIELD_NUMBER: _ClassVar[int]
    MAPMD5_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    REGIONFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    room_extra: bytes
    CMURL: str
    MapMD5: str
    MapID: int
    regionfile_info: _containers.RepeatedCompositeFieldContainer[PB_regionfileInfo]
    def __init__(self, room_extra: _Optional[bytes] = ..., CMURL: _Optional[str] = ..., MapMD5: _Optional[str] = ..., MapID: _Optional[int] = ..., regionfile_info: _Optional[_Iterable[_Union[PB_regionfileInfo, _Mapping]]] = ...) -> None: ...

class PB_SyncChunkDataHC(_message.Message):
    __slots__ = ("SectionFlags", "Initialize", "ChunkData")
    SECTIONFLAGS_FIELD_NUMBER: _ClassVar[int]
    INITIALIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNKDATA_FIELD_NUMBER: _ClassVar[int]
    SectionFlags: int
    Initialize: int
    ChunkData: _proto_common_pb2.PB_ChunkSaveDB
    def __init__(self, SectionFlags: _Optional[int] = ..., Initialize: _Optional[int] = ..., ChunkData: _Optional[_Union[_proto_common_pb2.PB_ChunkSaveDB, _Mapping]] = ...) -> None: ...

class PB_SyncSectionLightDataHC(_message.Message):
    __slots__ = ("SectionLightData",)
    SECTIONLIGHTDATA_FIELD_NUMBER: _ClassVar[int]
    SectionLightData: _proto_common_pb2.PB_SectionLightDB
    def __init__(self, SectionLightData: _Optional[_Union[_proto_common_pb2.PB_SectionLightDB, _Mapping]] = ...) -> None: ...

class PB_OverrideLightDataHC(_message.Message):
    __slots__ = ("OverrideLightData",)
    OVERRIDELIGHTDATA_FIELD_NUMBER: _ClassVar[int]
    OverrideLightData: _proto_common_pb2.PB_OverrideLightDB
    def __init__(self, OverrideLightData: _Optional[_Union[_proto_common_pb2.PB_OverrideLightDB, _Mapping]] = ...) -> None: ...

class PB_GameLeaderSwitchHC(_message.Message):
    __slots__ = ("Uin",)
    UIN_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    def __init__(self, Uin: _Optional[int] = ...) -> None: ...

class PB_BlockUpdateHC(_message.Message):
    __slots__ = ("ChunkX", "ChunkZ", "MapID", "Blocks", "ContainerBuf", "BlocksEx", "ContainerBufUnzipLen", "BlockStateIndex")
    CHUNKX_FIELD_NUMBER: _ClassVar[int]
    CHUNKZ_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    CONTAINERBUF_FIELD_NUMBER: _ClassVar[int]
    BLOCKSEX_FIELD_NUMBER: _ClassVar[int]
    CONTAINERBUFUNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOCKSTATEINDEX_FIELD_NUMBER: _ClassVar[int]
    ChunkX: int
    ChunkZ: int
    MapID: int
    Blocks: _containers.RepeatedScalarFieldContainer[int]
    ContainerBuf: str
    BlocksEx: _containers.RepeatedScalarFieldContainer[int]
    ContainerBufUnzipLen: int
    BlockStateIndex: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ChunkX: _Optional[int] = ..., ChunkZ: _Optional[int] = ..., MapID: _Optional[int] = ..., Blocks: _Optional[_Iterable[int]] = ..., ContainerBuf: _Optional[str] = ..., BlocksEx: _Optional[_Iterable[int]] = ..., ContainerBufUnzipLen: _Optional[int] = ..., BlockStateIndex: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_RoleEnterWorldHC(_message.Message):
    __slots__ = ("Uin", "PlayerInfo", "GlobalInfo", "WorldDesc", "SkillCDData", "UnlockItems", "Url", "HasRole", "SkillExpandCDDataGather", "TeleportMsg", "MoveSyncType", "ActorSyncFrequency")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERINFO_FIELD_NUMBER: _ClassVar[int]
    GLOBALINFO_FIELD_NUMBER: _ClassVar[int]
    WORLDDESC_FIELD_NUMBER: _ClassVar[int]
    SKILLCDDATA_FIELD_NUMBER: _ClassVar[int]
    UNLOCKITEMS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HASROLE_FIELD_NUMBER: _ClassVar[int]
    SKILLEXPANDCDDATAGATHER_FIELD_NUMBER: _ClassVar[int]
    TELEPORTMSG_FIELD_NUMBER: _ClassVar[int]
    MOVESYNCTYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORSYNCFREQUENCY_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    PlayerInfo: _proto_common_pb2.PB_PlayerInfo
    GlobalInfo: _proto_common_pb2.PB_OWGlobal
    WorldDesc: _proto_common_pb2.PB_WorldDesc
    SkillCDData: _proto_common_pb2.PB_SkillCDData
    UnlockItems: _containers.RepeatedScalarFieldContainer[int]
    Url: str
    HasRole: bool
    SkillExpandCDDataGather: _proto_common_pb2.PB_SkillExpandCDDataGather
    TeleportMsg: str
    MoveSyncType: int
    ActorSyncFrequency: int
    def __init__(self, Uin: _Optional[int] = ..., PlayerInfo: _Optional[_Union[_proto_common_pb2.PB_PlayerInfo, _Mapping]] = ..., GlobalInfo: _Optional[_Union[_proto_common_pb2.PB_OWGlobal, _Mapping]] = ..., WorldDesc: _Optional[_Union[_proto_common_pb2.PB_WorldDesc, _Mapping]] = ..., SkillCDData: _Optional[_Union[_proto_common_pb2.PB_SkillCDData, _Mapping]] = ..., UnlockItems: _Optional[_Iterable[int]] = ..., Url: _Optional[str] = ..., HasRole: _Optional[bool] = ..., SkillExpandCDDataGather: _Optional[_Union[_proto_common_pb2.PB_SkillExpandCDDataGather, _Mapping]] = ..., TeleportMsg: _Optional[str] = ..., MoveSyncType: _Optional[int] = ..., ActorSyncFrequency: _Optional[int] = ...) -> None: ...

class PB_RoleLeaveWorldHC(_message.Message):
    __slots__ = ("Uin",)
    UIN_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    def __init__(self, Uin: _Optional[int] = ...) -> None: ...

class PB_ActorEnterAOIHC(_message.Message):
    __slots__ = ("ObjID", "ActorType", "ActorInfo", "Spectator_Mode", "Spectator_Type", "HookID", "PlayMode", "PlayOperate", "childUUID", "TeamID", "ActorCompData", "hitBoundW", "hitBoundH", "BoundW", "BoundH", "laserPointerPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ACTORTYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORINFO_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_MODE_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOOKID_FIELD_NUMBER: _ClassVar[int]
    PLAYMODE_FIELD_NUMBER: _ClassVar[int]
    PLAYOPERATE_FIELD_NUMBER: _ClassVar[int]
    CHILDUUID_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    ACTORCOMPDATA_FIELD_NUMBER: _ClassVar[int]
    HITBOUNDW_FIELD_NUMBER: _ClassVar[int]
    HITBOUNDH_FIELD_NUMBER: _ClassVar[int]
    BOUNDW_FIELD_NUMBER: _ClassVar[int]
    BOUNDH_FIELD_NUMBER: _ClassVar[int]
    LASERPOINTERPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    ActorType: int
    ActorInfo: _proto_common_pb2.PB_ActorInfo
    Spectator_Mode: int
    Spectator_Type: int
    HookID: int
    PlayMode: int
    PlayOperate: int
    childUUID: int
    TeamID: int
    ActorCompData: _proto_common_pb2.PB_ActorCompData
    hitBoundW: int
    hitBoundH: int
    BoundW: int
    BoundH: int
    laserPointerPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., ActorType: _Optional[int] = ..., ActorInfo: _Optional[_Union[_proto_common_pb2.PB_ActorInfo, _Mapping]] = ..., Spectator_Mode: _Optional[int] = ..., Spectator_Type: _Optional[int] = ..., HookID: _Optional[int] = ..., PlayMode: _Optional[int] = ..., PlayOperate: _Optional[int] = ..., childUUID: _Optional[int] = ..., TeamID: _Optional[int] = ..., ActorCompData: _Optional[_Union[_proto_common_pb2.PB_ActorCompData, _Mapping]] = ..., hitBoundW: _Optional[int] = ..., hitBoundH: _Optional[int] = ..., BoundW: _Optional[int] = ..., BoundH: _Optional[int] = ..., laserPointerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_GeneralEnterAOIHC(_message.Message):
    __slots__ = ("ObjID", "MapId", "effectList", "soundList", "ActorMob", "ActorItem", "ActorNpc", "ActorAquaticMob", "ActorFlyBlock", "ActorProjectile", "ActorFlyMob", "ActorGhost", "ActorThornBall", "ActorFishhook", "ActorPipeline", "ActorSnowHare", "ActorObj", "ActorCompData", "ActorBlockStruct", "ActorBlockStructWormTab", "ActorBlockAwaken")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    EFFECTLIST_FIELD_NUMBER: _ClassVar[int]
    SOUNDLIST_FIELD_NUMBER: _ClassVar[int]
    ACTORMOB_FIELD_NUMBER: _ClassVar[int]
    ACTORITEM_FIELD_NUMBER: _ClassVar[int]
    ACTORNPC_FIELD_NUMBER: _ClassVar[int]
    ACTORAQUATICMOB_FIELD_NUMBER: _ClassVar[int]
    ACTORFLYBLOCK_FIELD_NUMBER: _ClassVar[int]
    ACTORPROJECTILE_FIELD_NUMBER: _ClassVar[int]
    ACTORFLYMOB_FIELD_NUMBER: _ClassVar[int]
    ACTORGHOST_FIELD_NUMBER: _ClassVar[int]
    ACTORTHORNBALL_FIELD_NUMBER: _ClassVar[int]
    ACTORFISHHOOK_FIELD_NUMBER: _ClassVar[int]
    ACTORPIPELINE_FIELD_NUMBER: _ClassVar[int]
    ACTORSNOWHARE_FIELD_NUMBER: _ClassVar[int]
    ACTOROBJ_FIELD_NUMBER: _ClassVar[int]
    ACTORCOMPDATA_FIELD_NUMBER: _ClassVar[int]
    ACTORBLOCKSTRUCT_FIELD_NUMBER: _ClassVar[int]
    ACTORBLOCKSTRUCTWORMTAB_FIELD_NUMBER: _ClassVar[int]
    ACTORBLOCKAWAKEN_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    MapId: int
    effectList: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_AOIBodyEffectBrief]
    soundList: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_AOIEffectTriggerSound]
    ActorMob: _proto_common_pb2.PB_ActorMob
    ActorItem: _proto_common_pb2.PB_ActorItem
    ActorNpc: _proto_common_pb2.PB_ActorMob
    ActorAquaticMob: _proto_common_pb2.PB_ActorAquaticMob
    ActorFlyBlock: _proto_common_pb2.PB_ActorFlyBlock
    ActorProjectile: _proto_common_pb2.PB_ActorProjectile
    ActorFlyMob: _proto_common_pb2.PB_ActorFlyMob
    ActorGhost: _proto_common_pb2.PB_ActorGhost
    ActorThornBall: _proto_common_pb2.PB_ActorThornBall
    ActorFishhook: _proto_common_pb2.PB_ActorFishhook
    ActorPipeline: _proto_common_pb2.PB_ActorPipeline
    ActorSnowHare: _proto_common_pb2.PB_ActorSnowHare
    ActorObj: _proto_common_pb2.PB_ActorObj
    ActorCompData: _proto_common_pb2.PB_ActorCompData
    ActorBlockStruct: _proto_common_pb2.PB_ActorBlockStruct
    ActorBlockStructWormTab: _proto_common_pb2.PB_ActorBlockStructWormTab
    ActorBlockAwaken: _proto_common_pb2.PB_ActorBlockAwaken
    def __init__(self, ObjID: _Optional[int] = ..., MapId: _Optional[int] = ..., effectList: _Optional[_Iterable[_Union[_proto_common_pb2.PB_AOIBodyEffectBrief, _Mapping]]] = ..., soundList: _Optional[_Iterable[_Union[_proto_common_pb2.PB_AOIEffectTriggerSound, _Mapping]]] = ..., ActorMob: _Optional[_Union[_proto_common_pb2.PB_ActorMob, _Mapping]] = ..., ActorItem: _Optional[_Union[_proto_common_pb2.PB_ActorItem, _Mapping]] = ..., ActorNpc: _Optional[_Union[_proto_common_pb2.PB_ActorMob, _Mapping]] = ..., ActorAquaticMob: _Optional[_Union[_proto_common_pb2.PB_ActorAquaticMob, _Mapping]] = ..., ActorFlyBlock: _Optional[_Union[_proto_common_pb2.PB_ActorFlyBlock, _Mapping]] = ..., ActorProjectile: _Optional[_Union[_proto_common_pb2.PB_ActorProjectile, _Mapping]] = ..., ActorFlyMob: _Optional[_Union[_proto_common_pb2.PB_ActorFlyMob, _Mapping]] = ..., ActorGhost: _Optional[_Union[_proto_common_pb2.PB_ActorGhost, _Mapping]] = ..., ActorThornBall: _Optional[_Union[_proto_common_pb2.PB_ActorThornBall, _Mapping]] = ..., ActorFishhook: _Optional[_Union[_proto_common_pb2.PB_ActorFishhook, _Mapping]] = ..., ActorPipeline: _Optional[_Union[_proto_common_pb2.PB_ActorPipeline, _Mapping]] = ..., ActorSnowHare: _Optional[_Union[_proto_common_pb2.PB_ActorSnowHare, _Mapping]] = ..., ActorObj: _Optional[_Union[_proto_common_pb2.PB_ActorObj, _Mapping]] = ..., ActorCompData: _Optional[_Union[_proto_common_pb2.PB_ActorCompData, _Mapping]] = ..., ActorBlockStruct: _Optional[_Union[_proto_common_pb2.PB_ActorBlockStruct, _Mapping]] = ..., ActorBlockStructWormTab: _Optional[_Union[_proto_common_pb2.PB_ActorBlockStructWormTab, _Mapping]] = ..., ActorBlockAwaken: _Optional[_Union[_proto_common_pb2.PB_ActorBlockAwaken, _Mapping]] = ...) -> None: ...

class PB_BlockStructUpdateHC(_message.Message):
    __slots__ = ("objid", "blockstructdata")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKSTRUCTDATA_FIELD_NUMBER: _ClassVar[int]
    objid: int
    blockstructdata: _proto_common_pb2.PB_BlockStructData
    def __init__(self, objid: _Optional[int] = ..., blockstructdata: _Optional[_Union[_proto_common_pb2.PB_BlockStructData, _Mapping]] = ...) -> None: ...

class AssembleBlockInfo(_message.Message):
    __slots__ = ("Block", "data", "Info", "BlockEx")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    BLOCKEX_FIELD_NUMBER: _ClassVar[int]
    Block: int
    data: int
    Info: int
    BlockEx: int
    def __init__(self, Block: _Optional[int] = ..., data: _Optional[int] = ..., Info: _Optional[int] = ..., BlockEx: _Optional[int] = ...) -> None: ...

class PB_VehicleAssembleBlockUpdateHC(_message.Message):
    __slots__ = ("ObjID", "BlockInfo", "ContainerBuf", "ChassisPos", "WheelPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKINFO_FIELD_NUMBER: _ClassVar[int]
    CONTAINERBUF_FIELD_NUMBER: _ClassVar[int]
    CHASSISPOS_FIELD_NUMBER: _ClassVar[int]
    WHEELPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    BlockInfo: _containers.RepeatedCompositeFieldContainer[AssembleBlockInfo]
    ContainerBuf: str
    ChassisPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    WheelPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    def __init__(self, ObjID: _Optional[int] = ..., BlockInfo: _Optional[_Iterable[_Union[AssembleBlockInfo, _Mapping]]] = ..., ContainerBuf: _Optional[str] = ..., ChassisPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ..., WheelPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ...) -> None: ...

class PB_VehicleAssembleBlockAllHC(_message.Message):
    __slots__ = ("ObjID", "UnzipLen", "BlobLen", "BlobDetail", "BlockVersion", "ChassisPos", "WheelPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBDETAIL_FIELD_NUMBER: _ClassVar[int]
    BLOCKVERSION_FIELD_NUMBER: _ClassVar[int]
    CHASSISPOS_FIELD_NUMBER: _ClassVar[int]
    WHEELPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    UnzipLen: int
    BlobLen: int
    BlobDetail: str
    BlockVersion: int
    ChassisPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    WheelPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    def __init__(self, ObjID: _Optional[int] = ..., UnzipLen: _Optional[int] = ..., BlobLen: _Optional[int] = ..., BlobDetail: _Optional[str] = ..., BlockVersion: _Optional[int] = ..., ChassisPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ..., WheelPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ...) -> None: ...

class PB_ActorLeaveAOIHC(_message.Message):
    __slots__ = ("ObjID",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    def __init__(self, ObjID: _Optional[int] = ...) -> None: ...

class PB_ActorModelChange(_message.Message):
    __slots__ = ("ObjID", "modelcomponent")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MODELCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    modelcomponent: str
    def __init__(self, ObjID: _Optional[int] = ..., modelcomponent: _Optional[str] = ...) -> None: ...

class PB_ActorMoveV2HC(_message.Message):
    __slots__ = ("ObjID", "Position", "Yaw_Pitch", "ChangeFlags")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    YAW_PITCH_FIELD_NUMBER: _ClassVar[int]
    CHANGEFLAGS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Position: _containers.RepeatedScalarFieldContainer[int]
    Yaw_Pitch: int
    ChangeFlags: int
    def __init__(self, ObjID: _Optional[int] = ..., Position: _Optional[_Iterable[int]] = ..., Yaw_Pitch: _Optional[int] = ..., ChangeFlags: _Optional[int] = ...) -> None: ...

class PB_ActorMoveV3HC_Batch(_message.Message):
    __slots__ = ("MoveBatch", "AniBatch")
    MOVEBATCH_FIELD_NUMBER: _ClassVar[int]
    ANIBATCH_FIELD_NUMBER: _ClassVar[int]
    MoveBatch: _containers.RepeatedCompositeFieldContainer[PB_ActorMoveV2HC]
    AniBatch: _containers.RepeatedCompositeFieldContainer[PB_ActorAnimHC]
    def __init__(self, MoveBatch: _Optional[_Iterable[_Union[PB_ActorMoveV2HC, _Mapping]]] = ..., AniBatch: _Optional[_Iterable[_Union[PB_ActorAnimHC, _Mapping]]] = ...) -> None: ...

class PB_ActorMoveHC(_message.Message):
    __slots__ = ("ObjID", "MoveMotion")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MOVEMOTION_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    MoveMotion: _proto_common_pb2.PB_MoveMotion
    def __init__(self, ObjID: _Optional[int] = ..., MoveMotion: _Optional[_Union[_proto_common_pb2.PB_MoveMotion, _Mapping]] = ...) -> None: ...

class PB_FullrotActorMoveHC(_message.Message):
    __slots__ = ("ObjID", "Position", "Yaw", "ChangeFlags")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    CHANGEFLAGS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Position: _proto_common_pb2.PB_Vector3
    Yaw: int
    ChangeFlags: int
    def __init__(self, ObjID: _Optional[int] = ..., Position: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Yaw: _Optional[int] = ..., ChangeFlags: _Optional[int] = ...) -> None: ...

class PB_TrainMoveHC(_message.Message):
    __slots__ = ("ObjID", "MapID", "CurveT", "CarReverse", "HeadCar", "TailCar", "OutIndex", "RailKnot")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CURVET_FIELD_NUMBER: _ClassVar[int]
    CARREVERSE_FIELD_NUMBER: _ClassVar[int]
    HEADCAR_FIELD_NUMBER: _ClassVar[int]
    TAILCAR_FIELD_NUMBER: _ClassVar[int]
    OUTINDEX_FIELD_NUMBER: _ClassVar[int]
    RAILKNOT_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    MapID: int
    CurveT: float
    CarReverse: int
    HeadCar: int
    TailCar: int
    OutIndex: int
    RailKnot: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., MapID: _Optional[int] = ..., CurveT: _Optional[float] = ..., CarReverse: _Optional[int] = ..., HeadCar: _Optional[int] = ..., TailCar: _Optional[int] = ..., OutIndex: _Optional[int] = ..., RailKnot: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorTeleportHC(_message.Message):
    __slots__ = ("ObjID", "TargetMap", "TargetPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TARGETMAP_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    TargetMap: int
    TargetPos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., TargetMap: _Optional[int] = ..., TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorMotionHC(_message.Message):
    __slots__ = ("ObjID", "x", "y", "z", "isChangePos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    ISCHANGEPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    x: float
    y: float
    z: float
    isChangePos: bool
    def __init__(self, ObjID: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., isChangePos: _Optional[bool] = ...) -> None: ...

class PB_ActorMotionV2HC(_message.Message):
    __slots__ = ("ObjID", "x", "y", "z", "isChangePos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    ISCHANGEPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    x: int
    y: int
    z: int
    isChangePos: bool
    def __init__(self, ObjID: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., isChangePos: _Optional[bool] = ...) -> None: ...

class PB_MechaMotionHC(_message.Message):
    __slots__ = ("ObjId", "MotionType", "MotionParam")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MOTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    MOTIONPARAM_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    MotionType: int
    MotionParam: float
    def __init__(self, ObjId: _Optional[int] = ..., MotionType: _Optional[int] = ..., MotionParam: _Optional[float] = ...) -> None: ...

class PB_SyncTriggerBlock(_message.Message):
    __slots__ = ("Uin", "BlockPos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    BlockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, Uin: _Optional[int] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BlockInteractHC(_message.Message):
    __slots__ = ("ObjID", "face", "blockpos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    face: int
    blockpos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., face: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_BlockPunchHC(_message.Message):
    __slots__ = ("ObjID", "status", "face", "digmethod", "blockpos", "vehicleObjID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    DIGMETHOD_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    status: int
    face: int
    digmethod: int
    blockpos: _proto_common_pb2.PB_Vector3
    vehicleObjID: int
    def __init__(self, ObjID: _Optional[int] = ..., status: _Optional[int] = ..., face: _Optional[int] = ..., digmethod: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., vehicleObjID: _Optional[int] = ...) -> None: ...

class PB_ItemUseHC(_message.Message):
    __slots__ = ("ObjID", "itemid", "status", "shift")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    itemid: int
    status: int
    shift: int
    def __init__(self, ObjID: _Optional[int] = ..., itemid: _Optional[int] = ..., status: _Optional[int] = ..., shift: _Optional[int] = ...) -> None: ...

class PB_SetHookHC(_message.Message):
    __slots__ = ("ObjID", "hookID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HOOKID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    hookID: int
    def __init__(self, ObjID: _Optional[int] = ..., hookID: _Optional[int] = ...) -> None: ...

class PB_ItemSkillUseHC(_message.Message):
    __slots__ = ("ObjID", "itemid", "status", "skillid")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SKILLID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    itemid: int
    status: int
    skillid: int
    def __init__(self, ObjID: _Optional[int] = ..., itemid: _Optional[int] = ..., status: _Optional[int] = ..., skillid: _Optional[int] = ...) -> None: ...

class PB_ActorInteractHC(_message.Message):
    __slots__ = ("ObjID", "target", "itype", "iplot")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ITYPE_FIELD_NUMBER: _ClassVar[int]
    IPLOT_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    target: int
    itype: int
    iplot: int
    def __init__(self, ObjID: _Optional[int] = ..., target: _Optional[int] = ..., itype: _Optional[int] = ..., iplot: _Optional[int] = ...) -> None: ...

class PB_RClickUpInteractHC(_message.Message):
    __slots__ = ("ObjID", "target")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    target: int
    def __init__(self, ObjID: _Optional[int] = ..., target: _Optional[int] = ...) -> None: ...

class PB_TrainFollowOpHC(_message.Message):
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

class PB_ActorAnimHC(_message.Message):
    __slots__ = ("actorid", "anim", "anim1", "actid", "bodyscale_invalid", "customscale", "actidTrigger", "sideAct", "animSeq", "isLoop", "animweapon", "isSeqId")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ANIM_FIELD_NUMBER: _ClassVar[int]
    ANIM1_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    BODYSCALE_INVALID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSCALE_FIELD_NUMBER: _ClassVar[int]
    ACTIDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    SIDEACT_FIELD_NUMBER: _ClassVar[int]
    ANIMSEQ_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    ANIMWEAPON_FIELD_NUMBER: _ClassVar[int]
    ISSEQID_FIELD_NUMBER: _ClassVar[int]
    actorid: int
    anim: int
    anim1: int
    actid: int
    bodyscale_invalid: float
    customscale: float
    actidTrigger: int
    sideAct: bool
    animSeq: int
    isLoop: int
    animweapon: int
    isSeqId: bool
    def __init__(self, actorid: _Optional[int] = ..., anim: _Optional[int] = ..., anim1: _Optional[int] = ..., actid: _Optional[int] = ..., bodyscale_invalid: _Optional[float] = ..., customscale: _Optional[float] = ..., actidTrigger: _Optional[int] = ..., sideAct: _Optional[bool] = ..., animSeq: _Optional[int] = ..., isLoop: _Optional[int] = ..., animweapon: _Optional[int] = ..., isSeqId: _Optional[bool] = ...) -> None: ...

class PB_BackPackGridUpdateHC(_message.Message):
    __slots__ = ("ItemInfo",)
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    ItemInfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ItemData]
    def __init__(self, ItemInfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ItemData, _Mapping]]] = ...) -> None: ...

class PB_BackPackEquipWeaponHC(_message.Message):
    __slots__ = ("GridId",)
    GRIDID_FIELD_NUMBER: _ClassVar[int]
    GridId: int
    def __init__(self, GridId: _Optional[int] = ...) -> None: ...

class PB_EquipWeaponHC(_message.Message):
    __slots__ = ("itemId", "uin")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    uin: int
    def __init__(self, itemId: _Optional[int] = ..., uin: _Optional[int] = ...) -> None: ...

class PB_CloseContainerHC(_message.Message):
    __slots__ = ("BaseIndex",)
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    def __init__(self, BaseIndex: _Optional[int] = ...) -> None: ...

class PB_OpenContainerHC(_message.Message):
    __slots__ = ("BaseIndex", "TotalItemGrids", "AttribInfo", "Text", "NpcID", "Pos", "ItemInfo", "VehicleObjID", "MechaStructObjID", "BlockID")
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    TOTALITEMGRIDS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBINFO_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NPCID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    MECHASTRUCTOBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    TotalItemGrids: int
    AttribInfo: _containers.RepeatedScalarFieldContainer[float]
    Text: str
    NpcID: int
    Pos: _proto_common_pb2.PB_Vector3
    ItemInfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ItemData]
    VehicleObjID: int
    MechaStructObjID: int
    BlockID: int
    def __init__(self, BaseIndex: _Optional[int] = ..., TotalItemGrids: _Optional[int] = ..., AttribInfo: _Optional[_Iterable[float]] = ..., Text: _Optional[str] = ..., NpcID: _Optional[int] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., ItemInfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ItemData, _Mapping]]] = ..., VehicleObjID: _Optional[int] = ..., MechaStructObjID: _Optional[int] = ..., BlockID: _Optional[int] = ...) -> None: ...

class PB_NeedContainerPasswordHC(_message.Message):
    __slots__ = ("Pos", "state", "VehicleObjID")
    POS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    state: int
    VehicleObjID: int
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., state: _Optional[int] = ..., VehicleObjID: _Optional[int] = ...) -> None: ...

class PB_UpdateContainerHC(_message.Message):
    __slots__ = ("BaseIndex", "AttribInfo", "Text", "Pos", "ItemInfo")
    BASEINDEX_FIELD_NUMBER: _ClassVar[int]
    ATTRIBINFO_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    BaseIndex: int
    AttribInfo: _containers.RepeatedScalarFieldContainer[float]
    Text: str
    Pos: _proto_common_pb2.PB_Vector3
    ItemInfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ItemData]
    def __init__(self, BaseIndex: _Optional[int] = ..., AttribInfo: _Optional[_Iterable[float]] = ..., Text: _Optional[str] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., ItemInfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ItemData, _Mapping]]] = ...) -> None: ...

class PB_ActorEquipItemHC(_message.Message):
    __slots__ = ("ObjId", "SlotType", "ItemInfo")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SLOTTYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    SlotType: int
    ItemInfo: _proto_common_pb2.PB_ItemData
    def __init__(self, ObjId: _Optional[int] = ..., SlotType: _Optional[int] = ..., ItemInfo: _Optional[_Union[_proto_common_pb2.PB_ItemData, _Mapping]] = ...) -> None: ...

class PB_EnchantItemSuccessHC(_message.Message):
    __slots__ = ("GridIndex",)
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    def __init__(self, GridIndex: _Optional[int] = ...) -> None: ...

class PB_RuneOperateSuccessHC(_message.Message):
    __slots__ = ("OpType", "GridIndex", "Result")
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    OpType: int
    GridIndex: int
    Result: int
    def __init__(self, OpType: _Optional[int] = ..., GridIndex: _Optional[int] = ..., Result: _Optional[int] = ...) -> None: ...

class PB_RepairItemSuccessHC(_message.Message):
    __slots__ = ("GridIndex",)
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    GridIndex: int
    def __init__(self, GridIndex: _Optional[int] = ...) -> None: ...

class PB_GunDoReloadHC(_message.Message):
    __slots__ = ("BulletID", "Num", "Total", "isCustomGun", "curShortcut")
    BULLETID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ISCUSTOMGUN_FIELD_NUMBER: _ClassVar[int]
    CURSHORTCUT_FIELD_NUMBER: _ClassVar[int]
    BulletID: int
    Num: int
    Total: int
    isCustomGun: bool
    curShortcut: int
    def __init__(self, BulletID: _Optional[int] = ..., Num: _Optional[int] = ..., Total: _Optional[int] = ..., isCustomGun: _Optional[bool] = ..., curShortcut: _Optional[int] = ...) -> None: ...

class PB_AccountHorseHC(_message.Message):
    __slots__ = ("HorseID", "SyncType", "SyncData")
    HORSEID_FIELD_NUMBER: _ClassVar[int]
    SYNCTYPE_FIELD_NUMBER: _ClassVar[int]
    SYNCDATA_FIELD_NUMBER: _ClassVar[int]
    HorseID: int
    SyncType: int
    SyncData: int
    def __init__(self, HorseID: _Optional[int] = ..., SyncType: _Optional[int] = ..., SyncData: _Optional[int] = ...) -> None: ...

class PB_UIDisplayHorseHC(_message.Message):
    __slots__ = ("HorseObjID", "PlayerObjID")
    HORSEOBJID_FIELD_NUMBER: _ClassVar[int]
    PLAYEROBJID_FIELD_NUMBER: _ClassVar[int]
    HorseObjID: int
    PlayerObjID: int
    def __init__(self, HorseObjID: _Optional[int] = ..., PlayerObjID: _Optional[int] = ...) -> None: ...

class PB_ActorAttrChangeHC(_message.Message):
    __slots__ = ("ObjID", "HP", "BeHurtTarget", "Armor", "ExtarHP", "MaxHP", "Scale", "WalkAction", "RunAction", "JumpAction", "FlyAction", "SwimAction", "SneakAction", "FightAction", "CriticalHP", "IronHP")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    BEHURTTARGET_FIELD_NUMBER: _ClassVar[int]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    EXTARHP_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    WALKACTION_FIELD_NUMBER: _ClassVar[int]
    RUNACTION_FIELD_NUMBER: _ClassVar[int]
    JUMPACTION_FIELD_NUMBER: _ClassVar[int]
    FLYACTION_FIELD_NUMBER: _ClassVar[int]
    SWIMACTION_FIELD_NUMBER: _ClassVar[int]
    SNEAKACTION_FIELD_NUMBER: _ClassVar[int]
    FIGHTACTION_FIELD_NUMBER: _ClassVar[int]
    CRITICALHP_FIELD_NUMBER: _ClassVar[int]
    IRONHP_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    HP: float
    BeHurtTarget: int
    Armor: float
    ExtarHP: float
    MaxHP: float
    Scale: _proto_common_pb2.PB_Vector3f
    WalkAction: int
    RunAction: int
    JumpAction: int
    FlyAction: int
    SwimAction: int
    SneakAction: int
    FightAction: int
    CriticalHP: bool
    IronHP: float
    def __init__(self, ObjID: _Optional[int] = ..., HP: _Optional[float] = ..., BeHurtTarget: _Optional[int] = ..., Armor: _Optional[float] = ..., ExtarHP: _Optional[float] = ..., MaxHP: _Optional[float] = ..., Scale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., WalkAction: _Optional[int] = ..., RunAction: _Optional[int] = ..., JumpAction: _Optional[int] = ..., FlyAction: _Optional[int] = ..., SwimAction: _Optional[int] = ..., SneakAction: _Optional[int] = ..., FightAction: _Optional[int] = ..., CriticalHP: _Optional[bool] = ..., IronHP: _Optional[float] = ...) -> None: ...

class PB_ActorAttrSpeedChangeHC(_message.Message):
    __slots__ = ("WalkSpeed", "RunSpeed", "JumpSpeed", "FlySpeed", "SwimSpeed", "SneakSpeed", "SprintRatio", "SwimmingRatio")
    WALKSPEED_FIELD_NUMBER: _ClassVar[int]
    RUNSPEED_FIELD_NUMBER: _ClassVar[int]
    JUMPSPEED_FIELD_NUMBER: _ClassVar[int]
    FLYSPEED_FIELD_NUMBER: _ClassVar[int]
    SWIMSPEED_FIELD_NUMBER: _ClassVar[int]
    SNEAKSPEED_FIELD_NUMBER: _ClassVar[int]
    SPRINTRATIO_FIELD_NUMBER: _ClassVar[int]
    SWIMMINGRATIO_FIELD_NUMBER: _ClassVar[int]
    WalkSpeed: float
    RunSpeed: float
    JumpSpeed: float
    FlySpeed: float
    SwimSpeed: float
    SneakSpeed: float
    SprintRatio: float
    SwimmingRatio: float
    def __init__(self, WalkSpeed: _Optional[float] = ..., RunSpeed: _Optional[float] = ..., JumpSpeed: _Optional[float] = ..., FlySpeed: _Optional[float] = ..., SwimSpeed: _Optional[float] = ..., SneakSpeed: _Optional[float] = ..., SprintRatio: _Optional[float] = ..., SwimmingRatio: _Optional[float] = ...) -> None: ...

class PB_ActorBuffChangeHC(_message.Message):
    __slots__ = ("ObjID", "Buffs")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Buffs: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ActorBuff]
    def __init__(self, ObjID: _Optional[int] = ..., Buffs: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ActorBuff, _Mapping]]] = ...) -> None: ...

class PB_ActorReviveHC(_message.Message):
    __slots__ = ("ObjID", "MapID", "ReviveType", "ReviveYaw", "RevivePitch", "RevivePosition")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    REVIVETYPE_FIELD_NUMBER: _ClassVar[int]
    REVIVEYAW_FIELD_NUMBER: _ClassVar[int]
    REVIVEPITCH_FIELD_NUMBER: _ClassVar[int]
    REVIVEPOSITION_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    MapID: int
    ReviveType: int
    ReviveYaw: float
    RevivePitch: float
    RevivePosition: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., MapID: _Optional[int] = ..., ReviveType: _Optional[int] = ..., ReviveYaw: _Optional[float] = ..., RevivePitch: _Optional[float] = ..., RevivePosition: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_OxygenComp(_message.Message):
    __slots__ = ("bopen", "maxval", "userate", "recoverval")
    BOPEN_FIELD_NUMBER: _ClassVar[int]
    MAXVAL_FIELD_NUMBER: _ClassVar[int]
    USERATE_FIELD_NUMBER: _ClassVar[int]
    RECOVERVAL_FIELD_NUMBER: _ClassVar[int]
    bopen: bool
    maxval: float
    userate: float
    recoverval: float
    def __init__(self, bopen: _Optional[bool] = ..., maxval: _Optional[float] = ..., userate: _Optional[float] = ..., recoverval: _Optional[float] = ...) -> None: ...

class PB_PlayerAttrChangeHC(_message.Message):
    __slots__ = ("HP", "Oxygen", "Exp", "FoodLevel", "Strength", "MaxHP", "OverflowHP", "MaxStrength", "OverflowStrength", "Armor", "Perseverance", "StarDebuffTime", "StarDebuffStage", "Scale", "IronHp", "oxygenComp")
    HP_FIELD_NUMBER: _ClassVar[int]
    OXYGEN_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    FOODLEVEL_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWHP_FIELD_NUMBER: _ClassVar[int]
    MAXSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    PERSEVERANCE_FIELD_NUMBER: _ClassVar[int]
    STARDEBUFFTIME_FIELD_NUMBER: _ClassVar[int]
    STARDEBUFFSTAGE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    IRONHP_FIELD_NUMBER: _ClassVar[int]
    OXYGENCOMP_FIELD_NUMBER: _ClassVar[int]
    HP: float
    Oxygen: float
    Exp: int
    FoodLevel: int
    Strength: float
    MaxHP: float
    OverflowHP: float
    MaxStrength: float
    OverflowStrength: float
    Armor: float
    Perseverance: float
    StarDebuffTime: int
    StarDebuffStage: int
    Scale: _proto_common_pb2.PB_Vector3f
    IronHp: float
    oxygenComp: PB_OxygenComp
    def __init__(self, HP: _Optional[float] = ..., Oxygen: _Optional[float] = ..., Exp: _Optional[int] = ..., FoodLevel: _Optional[int] = ..., Strength: _Optional[float] = ..., MaxHP: _Optional[float] = ..., OverflowHP: _Optional[float] = ..., MaxStrength: _Optional[float] = ..., OverflowStrength: _Optional[float] = ..., Armor: _Optional[float] = ..., Perseverance: _Optional[float] = ..., StarDebuffTime: _Optional[int] = ..., StarDebuffStage: _Optional[int] = ..., Scale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., IronHp: _Optional[float] = ..., oxygenComp: _Optional[_Union[PB_OxygenComp, _Mapping]] = ...) -> None: ...

class PB_MobBodyChangeHC(_message.Message):
    __slots__ = ("ObjId", "BodyColor", "Sheared")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BODYCOLOR_FIELD_NUMBER: _ClassVar[int]
    SHEARED_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    BodyColor: int
    Sheared: int
    def __init__(self, ObjId: _Optional[int] = ..., BodyColor: _Optional[int] = ..., Sheared: _Optional[int] = ...) -> None: ...

class PB_JruisdicTionHC(_message.Message):
    __slots__ = ("Ret",)
    RET_FIELD_NUMBER: _ClassVar[int]
    Ret: int
    def __init__(self, Ret: _Optional[int] = ...) -> None: ...

class PB_ChatHC(_message.Message):
    __slots__ = ("ChatType", "Uin", "Speaker", "Content", "Language", "Extend", "Translate")
    CHATTYPE_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EXTEND_FIELD_NUMBER: _ClassVar[int]
    TRANSLATE_FIELD_NUMBER: _ClassVar[int]
    ChatType: int
    Uin: int
    Speaker: str
    Content: str
    Language: int
    Extend: str
    Translate: str
    def __init__(self, ChatType: _Optional[int] = ..., Uin: _Optional[int] = ..., Speaker: _Optional[str] = ..., Content: _Optional[str] = ..., Language: _Optional[int] = ..., Extend: _Optional[str] = ..., Translate: _Optional[str] = ...) -> None: ...

class PB_ActorInviteHC(_message.Message):
    __slots__ = ("InviteType", "Targetuin", "ActID", "inviterPosX", "inviterPosZ")
    INVITETYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    INVITERPOSX_FIELD_NUMBER: _ClassVar[int]
    INVITERPOSZ_FIELD_NUMBER: _ClassVar[int]
    InviteType: int
    Targetuin: int
    ActID: int
    inviterPosX: int
    inviterPosZ: int
    def __init__(self, InviteType: _Optional[int] = ..., Targetuin: _Optional[int] = ..., ActID: _Optional[int] = ..., inviterPosX: _Optional[int] = ..., inviterPosZ: _Optional[int] = ...) -> None: ...

class PB_WGlobalUpdateHC(_message.Message):
    __slots__ = ("WorldTime", "ViewRange", "MapID", "Raining", "DayNightTime", "Darking", "CurWeather")
    WORLDTIME_FIELD_NUMBER: _ClassVar[int]
    VIEWRANGE_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    RAINING_FIELD_NUMBER: _ClassVar[int]
    DAYNIGHTTIME_FIELD_NUMBER: _ClassVar[int]
    DARKING_FIELD_NUMBER: _ClassVar[int]
    CURWEATHER_FIELD_NUMBER: _ClassVar[int]
    WorldTime: int
    ViewRange: int
    MapID: int
    Raining: int
    DayNightTime: int
    Darking: int
    CurWeather: int
    def __init__(self, WorldTime: _Optional[int] = ..., ViewRange: _Optional[int] = ..., MapID: _Optional[int] = ..., Raining: _Optional[int] = ..., DayNightTime: _Optional[int] = ..., Darking: _Optional[int] = ..., CurWeather: _Optional[int] = ...) -> None: ...

class PB_PlayersUpdateInfoHC(_message.Message):
    __slots__ = ("TeamScores", "TeamFlags", "Players")
    TEAMSCORES_FIELD_NUMBER: _ClassVar[int]
    TEAMFLAGS_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    TeamScores: _containers.RepeatedScalarFieldContainer[int]
    TeamFlags: _containers.RepeatedScalarFieldContainer[int]
    Players: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_PlayerBriefInfo]
    def __init__(self, TeamScores: _Optional[_Iterable[int]] = ..., TeamFlags: _Optional[_Iterable[int]] = ..., Players: _Optional[_Iterable[_Union[_proto_common_pb2.PB_PlayerBriefInfo, _Mapping]]] = ...) -> None: ...

class PB_PlayerLeaveHC(_message.Message):
    __slots__ = ("Uins",)
    UINS_FIELD_NUMBER: _ClassVar[int]
    Uins: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Uins: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_TeamScoreHC(_message.Message):
    __slots__ = ("Teams",)
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    Teams: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_TeamScore]
    def __init__(self, Teams: _Optional[_Iterable[_Union[_proto_common_pb2.PB_TeamScore, _Mapping]]] = ...) -> None: ...

class PB_SetTeamIDHC(_message.Message):
    __slots__ = ("TeamID", "ObjID", "ResetAttr")
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    RESETATTR_FIELD_NUMBER: _ClassVar[int]
    TeamID: int
    ObjID: int
    ResetAttr: bool
    def __init__(self, TeamID: _Optional[int] = ..., ObjID: _Optional[int] = ..., ResetAttr: _Optional[bool] = ...) -> None: ...

class PB_SetPlayerGameInfoHC(_message.Message):
    __slots__ = ("Score", "Result", "Ranking", "PlayerResult")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RANKING_FIELD_NUMBER: _ClassVar[int]
    PLAYERRESULT_FIELD_NUMBER: _ClassVar[int]
    Score: int
    Result: int
    Ranking: int
    PlayerResult: int
    def __init__(self, Score: _Optional[int] = ..., Result: _Optional[int] = ..., Ranking: _Optional[int] = ..., PlayerResult: _Optional[int] = ...) -> None: ...

class PB_GameTipsHC(_message.Message):
    __slots__ = ("TipsType", "Id", "Num", "OtherName", "TranslateName")
    TIPSTYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    OTHERNAME_FIELD_NUMBER: _ClassVar[int]
    TRANSLATENAME_FIELD_NUMBER: _ClassVar[int]
    TipsType: int
    Id: int
    Num: int
    OtherName: str
    TranslateName: str
    def __init__(self, TipsType: _Optional[int] = ..., Id: _Optional[int] = ..., Num: _Optional[int] = ..., OtherName: _Optional[str] = ..., TranslateName: _Optional[str] = ...) -> None: ...

class PB_PlayEffectHC(_message.Message):
    __slots__ = ("EffectType", "Particle", "PickItem", "Sound", "ActorBody", "DestroyBlock", "PlayMusicGrid", "StopMusicGrid", "StringActorBody", "CrackBlock", "effectScale", "effectClass", "TriggerSound", "EffectVehicle", "SoundNew", "SoundID", "ParticleID", "v3fScale", "rot", "offset")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_FIELD_NUMBER: _ClassVar[int]
    PICKITEM_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    ACTORBODY_FIELD_NUMBER: _ClassVar[int]
    DESTROYBLOCK_FIELD_NUMBER: _ClassVar[int]
    PLAYMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STOPMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STRINGACTORBODY_FIELD_NUMBER: _ClassVar[int]
    CRACKBLOCK_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTCLASS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERSOUND_FIELD_NUMBER: _ClassVar[int]
    EFFECTVEHICLE_FIELD_NUMBER: _ClassVar[int]
    SOUNDNEW_FIELD_NUMBER: _ClassVar[int]
    SOUNDID_FIELD_NUMBER: _ClassVar[int]
    PARTICLEID_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EffectType: int
    Particle: _proto_common_pb2.PB_EffectParticle
    PickItem: _proto_common_pb2.PB_EffectPickItem
    Sound: _proto_common_pb2.PB_EffectSound
    ActorBody: _proto_common_pb2.PB_EffectActorBody
    DestroyBlock: _proto_common_pb2.PB_EffectDestroyBlock
    PlayMusicGrid: _proto_common_pb2.PB_EffectPlayMusicGrid
    StopMusicGrid: _proto_common_pb2.PB_EffectStopMusicGrid
    StringActorBody: _proto_common_pb2.PB_EffectStringActorBody
    CrackBlock: _proto_common_pb2.PB_EffectCrackBlock
    effectScale: int
    effectClass: int
    TriggerSound: _proto_common_pb2.PB_EffectTriggerSound
    EffectVehicle: _proto_common_pb2.PB_EffectVehicle
    SoundNew: _proto_common_pb2.PB_EffectSoundNew
    SoundID: _proto_common_pb2.PB_EffectSoundID
    ParticleID: _proto_common_pb2.PB_EffectParticleID
    v3fScale: _proto_common_pb2.PB_Vector3f
    rot: _proto_common_pb2.PB_Vector3f
    offset: _proto_common_pb2.PB_Vector3f
    def __init__(self, EffectType: _Optional[int] = ..., Particle: _Optional[_Union[_proto_common_pb2.PB_EffectParticle, _Mapping]] = ..., PickItem: _Optional[_Union[_proto_common_pb2.PB_EffectPickItem, _Mapping]] = ..., Sound: _Optional[_Union[_proto_common_pb2.PB_EffectSound, _Mapping]] = ..., ActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectActorBody, _Mapping]] = ..., DestroyBlock: _Optional[_Union[_proto_common_pb2.PB_EffectDestroyBlock, _Mapping]] = ..., PlayMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectPlayMusicGrid, _Mapping]] = ..., StopMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectStopMusicGrid, _Mapping]] = ..., StringActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectStringActorBody, _Mapping]] = ..., CrackBlock: _Optional[_Union[_proto_common_pb2.PB_EffectCrackBlock, _Mapping]] = ..., effectScale: _Optional[int] = ..., effectClass: _Optional[int] = ..., TriggerSound: _Optional[_Union[_proto_common_pb2.PB_EffectTriggerSound, _Mapping]] = ..., EffectVehicle: _Optional[_Union[_proto_common_pb2.PB_EffectVehicle, _Mapping]] = ..., SoundNew: _Optional[_Union[_proto_common_pb2.PB_EffectSoundNew, _Mapping]] = ..., SoundID: _Optional[_Union[_proto_common_pb2.PB_EffectSoundID, _Mapping]] = ..., ParticleID: _Optional[_Union[_proto_common_pb2.PB_EffectParticleID, _Mapping]] = ..., v3fScale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_PlayEffectHC_V2(_message.Message):
    __slots__ = ("EffectType", "Particle", "PickItem", "Sound", "ActorBody", "DestroyBlock", "PlayMusicGrid", "StopMusicGrid", "StringActorBody", "CrackBlock", "effectScale", "effectClass", "TriggerSound", "EffectVehicle", "SoundNew", "SoundID", "ParticleID", "usePlayerViewRange", "v3fScale", "rot", "offset")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_FIELD_NUMBER: _ClassVar[int]
    PICKITEM_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    ACTORBODY_FIELD_NUMBER: _ClassVar[int]
    DESTROYBLOCK_FIELD_NUMBER: _ClassVar[int]
    PLAYMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STOPMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STRINGACTORBODY_FIELD_NUMBER: _ClassVar[int]
    CRACKBLOCK_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTCLASS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERSOUND_FIELD_NUMBER: _ClassVar[int]
    EFFECTVEHICLE_FIELD_NUMBER: _ClassVar[int]
    SOUNDNEW_FIELD_NUMBER: _ClassVar[int]
    SOUNDID_FIELD_NUMBER: _ClassVar[int]
    PARTICLEID_FIELD_NUMBER: _ClassVar[int]
    USEPLAYERVIEWRANGE_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EffectType: int
    Particle: _proto_common_pb2.PB_EffectParticle
    PickItem: _proto_common_pb2.PB_EffectPickItem
    Sound: _proto_common_pb2.PB_EffectSound_V2
    ActorBody: _proto_common_pb2.PB_EffectActorBody
    DestroyBlock: _proto_common_pb2.PB_EffectDestroyBlock
    PlayMusicGrid: _proto_common_pb2.PB_EffectPlayMusicGrid
    StopMusicGrid: _proto_common_pb2.PB_EffectStopMusicGrid
    StringActorBody: _proto_common_pb2.PB_EffectStringActorBody
    CrackBlock: _proto_common_pb2.PB_EffectCrackBlock
    effectScale: int
    effectClass: int
    TriggerSound: _proto_common_pb2.PB_EffectTriggerSound
    EffectVehicle: _proto_common_pb2.PB_EffectVehicle
    SoundNew: _proto_common_pb2.PB_EffectSoundNew
    SoundID: _proto_common_pb2.PB_EffectSoundID_V2
    ParticleID: _proto_common_pb2.PB_EffectParticleID_V2
    usePlayerViewRange: bool
    v3fScale: _proto_common_pb2.PB_Vector3f
    rot: _proto_common_pb2.PB_Vector3f
    offset: _proto_common_pb2.PB_Vector3f
    def __init__(self, EffectType: _Optional[int] = ..., Particle: _Optional[_Union[_proto_common_pb2.PB_EffectParticle, _Mapping]] = ..., PickItem: _Optional[_Union[_proto_common_pb2.PB_EffectPickItem, _Mapping]] = ..., Sound: _Optional[_Union[_proto_common_pb2.PB_EffectSound_V2, _Mapping]] = ..., ActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectActorBody, _Mapping]] = ..., DestroyBlock: _Optional[_Union[_proto_common_pb2.PB_EffectDestroyBlock, _Mapping]] = ..., PlayMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectPlayMusicGrid, _Mapping]] = ..., StopMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectStopMusicGrid, _Mapping]] = ..., StringActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectStringActorBody, _Mapping]] = ..., CrackBlock: _Optional[_Union[_proto_common_pb2.PB_EffectCrackBlock, _Mapping]] = ..., effectScale: _Optional[int] = ..., effectClass: _Optional[int] = ..., TriggerSound: _Optional[_Union[_proto_common_pb2.PB_EffectTriggerSound, _Mapping]] = ..., EffectVehicle: _Optional[_Union[_proto_common_pb2.PB_EffectVehicle, _Mapping]] = ..., SoundNew: _Optional[_Union[_proto_common_pb2.PB_EffectSoundNew, _Mapping]] = ..., SoundID: _Optional[_Union[_proto_common_pb2.PB_EffectSoundID_V2, _Mapping]] = ..., ParticleID: _Optional[_Union[_proto_common_pb2.PB_EffectParticleID_V2, _Mapping]] = ..., usePlayerViewRange: _Optional[bool] = ..., v3fScale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_PlayEffectHC_V3(_message.Message):
    __slots__ = ("EffectType", "effectScale", "effectClass", "usePlayerViewRange", "Particle", "PickItem", "Sound", "ActorBody", "DestroyBlock", "PlayMusicGrid", "StopMusicGrid", "StringActorBody", "CrackBlock", "TriggerSound", "EffectVehicle", "SoundNew")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTCLASS_FIELD_NUMBER: _ClassVar[int]
    USEPLAYERVIEWRANGE_FIELD_NUMBER: _ClassVar[int]
    PARTICLE_FIELD_NUMBER: _ClassVar[int]
    PICKITEM_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    ACTORBODY_FIELD_NUMBER: _ClassVar[int]
    DESTROYBLOCK_FIELD_NUMBER: _ClassVar[int]
    PLAYMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STOPMUSICGRID_FIELD_NUMBER: _ClassVar[int]
    STRINGACTORBODY_FIELD_NUMBER: _ClassVar[int]
    CRACKBLOCK_FIELD_NUMBER: _ClassVar[int]
    TRIGGERSOUND_FIELD_NUMBER: _ClassVar[int]
    EFFECTVEHICLE_FIELD_NUMBER: _ClassVar[int]
    SOUNDNEW_FIELD_NUMBER: _ClassVar[int]
    EffectType: _proto_common_pb2.ePBEffectType
    effectScale: int
    effectClass: int
    usePlayerViewRange: bool
    Particle: _proto_common_pb2.PB_EffectParticle_V2
    PickItem: _proto_common_pb2.PB_EffectPickItem
    Sound: _proto_common_pb2.PB_EffectSound_V2
    ActorBody: _proto_common_pb2.PB_EffectActorBody
    DestroyBlock: _proto_common_pb2.PB_EffectDestroyBlock_V2
    PlayMusicGrid: _proto_common_pb2.PB_EffectPlayMusicGrid_V2
    StopMusicGrid: _proto_common_pb2.PB_EffectStopMusicGrid
    StringActorBody: _proto_common_pb2.PB_EffectStringActorBody
    CrackBlock: _proto_common_pb2.PB_EffectCrackBlock
    TriggerSound: _proto_common_pb2.PB_EffectTriggerSound
    EffectVehicle: _proto_common_pb2.PB_EffectVehicle
    SoundNew: _proto_common_pb2.PB_EffectSoundNew_V2
    def __init__(self, EffectType: _Optional[_Union[_proto_common_pb2.ePBEffectType, str]] = ..., effectScale: _Optional[int] = ..., effectClass: _Optional[int] = ..., usePlayerViewRange: _Optional[bool] = ..., Particle: _Optional[_Union[_proto_common_pb2.PB_EffectParticle_V2, _Mapping]] = ..., PickItem: _Optional[_Union[_proto_common_pb2.PB_EffectPickItem, _Mapping]] = ..., Sound: _Optional[_Union[_proto_common_pb2.PB_EffectSound_V2, _Mapping]] = ..., ActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectActorBody, _Mapping]] = ..., DestroyBlock: _Optional[_Union[_proto_common_pb2.PB_EffectDestroyBlock_V2, _Mapping]] = ..., PlayMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectPlayMusicGrid_V2, _Mapping]] = ..., StopMusicGrid: _Optional[_Union[_proto_common_pb2.PB_EffectStopMusicGrid, _Mapping]] = ..., StringActorBody: _Optional[_Union[_proto_common_pb2.PB_EffectStringActorBody, _Mapping]] = ..., CrackBlock: _Optional[_Union[_proto_common_pb2.PB_EffectCrackBlock, _Mapping]] = ..., TriggerSound: _Optional[_Union[_proto_common_pb2.PB_EffectTriggerSound, _Mapping]] = ..., EffectVehicle: _Optional[_Union[_proto_common_pb2.PB_EffectVehicle, _Mapping]] = ..., SoundNew: _Optional[_Union[_proto_common_pb2.PB_EffectSoundNew_V2, _Mapping]] = ...) -> None: ...

class PB_EffectScaleHC(_message.Message):
    __slots__ = ("EffectType", "effectScale", "objID", "effectName", "Pos", "rot", "v3fScale", "offset")
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EffectType: int
    effectScale: float
    objID: int
    effectName: str
    Pos: _proto_common_pb2.PB_Vector3
    rot: _proto_common_pb2.PB_Vector3f
    v3fScale: _proto_common_pb2.PB_Vector3f
    offset: _proto_common_pb2.PB_Vector3f
    def __init__(self, EffectType: _Optional[int] = ..., effectScale: _Optional[float] = ..., objID: _Optional[int] = ..., effectName: _Optional[str] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., rot: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., v3fScale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_PlayerMountActorHC(_message.Message):
    __slots__ = ("PlayerUIN", "RidePosIndex", "ActorID", "force", "InteractBlockId", "iscontrl")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    RIDEPOSINDEX_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    INTERACTBLOCKID_FIELD_NUMBER: _ClassVar[int]
    ISCONTRL_FIELD_NUMBER: _ClassVar[int]
    PlayerUIN: int
    RidePosIndex: int
    ActorID: int
    force: int
    InteractBlockId: int
    iscontrl: bool
    def __init__(self, PlayerUIN: _Optional[int] = ..., RidePosIndex: _Optional[int] = ..., ActorID: _Optional[int] = ..., force: _Optional[int] = ..., InteractBlockId: _Optional[int] = ..., iscontrl: _Optional[bool] = ...) -> None: ...

class PB_PlayerSleepHC(_message.Message):
    __slots__ = ("Flags", "Pos", "Uin", "targetPos", "AnimID")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    Flags: int
    Pos: _proto_common_pb2.PB_Vector3
    Uin: int
    targetPos: _proto_common_pb2.PB_Vector3
    AnimID: int
    def __init__(self, Flags: _Optional[int] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Uin: _Optional[int] = ..., targetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., AnimID: _Optional[int] = ...) -> None: ...

class PB_OpenWindowHC(_message.Message):
    __slots__ = ("id", "x", "y", "z")
    ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    id: int
    x: int
    y: int
    z: int
    def __init__(self, id: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class PB_LastPingHC(_message.Message):
    __slots__ = ("MPLastPingOne",)
    MPLASTPINGONE_FIELD_NUMBER: _ClassVar[int]
    MPLastPingOne: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, MPLastPingOne: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_CGameStageHC(_message.Message):
    __slots__ = ("Stage", "GameTime")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    GAMETIME_FIELD_NUMBER: _ClassVar[int]
    Stage: int
    GameTime: int
    def __init__(self, Stage: _Optional[int] = ..., GameTime: _Optional[int] = ...) -> None: ...

class PB_PlayerPermitHC(_message.Message):
    __slots__ = ("RoomFlags", "PlayerFlags", "SpamPreventionMinutes", "BanItems", "MutePlayerlist", "PlayerSpeakingWhitelist")
    ROOMFLAGS_FIELD_NUMBER: _ClassVar[int]
    PLAYERFLAGS_FIELD_NUMBER: _ClassVar[int]
    SPAMPREVENTIONMINUTES_FIELD_NUMBER: _ClassVar[int]
    BANITEMS_FIELD_NUMBER: _ClassVar[int]
    MUTEPLAYERLIST_FIELD_NUMBER: _ClassVar[int]
    PLAYERSPEAKINGWHITELIST_FIELD_NUMBER: _ClassVar[int]
    RoomFlags: int
    PlayerFlags: int
    SpamPreventionMinutes: int
    BanItems: _containers.RepeatedScalarFieldContainer[int]
    MutePlayerlist: _containers.RepeatedScalarFieldContainer[int]
    PlayerSpeakingWhitelist: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, RoomFlags: _Optional[int] = ..., PlayerFlags: _Optional[int] = ..., SpamPreventionMinutes: _Optional[int] = ..., BanItems: _Optional[_Iterable[int]] = ..., MutePlayerlist: _Optional[_Iterable[int]] = ..., PlayerSpeakingWhitelist: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_YMVoiceHC(_message.Message):
    __slots__ = ("Uin", "YMMemberID", "SpeakerSwitch", "MicSwitch", "YMMemberRole")
    UIN_FIELD_NUMBER: _ClassVar[int]
    YMMEMBERID_FIELD_NUMBER: _ClassVar[int]
    SPEAKERSWITCH_FIELD_NUMBER: _ClassVar[int]
    MICSWITCH_FIELD_NUMBER: _ClassVar[int]
    YMMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    YMMemberID: int
    SpeakerSwitch: int
    MicSwitch: int
    YMMemberRole: int
    def __init__(self, Uin: _Optional[int] = ..., YMMemberID: _Optional[int] = ..., SpeakerSwitch: _Optional[int] = ..., MicSwitch: _Optional[int] = ..., YMMemberRole: _Optional[int] = ...) -> None: ...

class PB_SkillCDHC(_message.Message):
    __slots__ = ("ItemID", "CD")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    ItemID: int
    CD: float
    def __init__(self, ItemID: _Optional[int] = ..., CD: _Optional[float] = ...) -> None: ...

class PB_Horse_SkillCDHC(_message.Message):
    __slots__ = ("ActorID", "Index", "CD")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    Index: int
    CD: float
    def __init__(self, ActorID: _Optional[int] = ..., Index: _Optional[int] = ..., CD: _Optional[float] = ...) -> None: ...

class PB_ActorMountActorHC(_message.Message):
    __slots__ = ("ActorIDOwner", "ActorID", "RidePosIndex")
    ACTORIDOWNER_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    RIDEPOSINDEX_FIELD_NUMBER: _ClassVar[int]
    ActorIDOwner: int
    ActorID: int
    RidePosIndex: int
    def __init__(self, ActorIDOwner: _Optional[int] = ..., ActorID: _Optional[int] = ..., RidePosIndex: _Optional[int] = ...) -> None: ...

class PB_ActorReverseHC(_message.Message):
    __slots__ = ("ActorID", "Reverse")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    Reverse: int
    def __init__(self, ActorID: _Optional[int] = ..., Reverse: _Optional[int] = ...) -> None: ...

class PB_ActorBindHC(_message.Message):
    __slots__ = ("ActorID", "ActorIDBind", "OffetBind")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ACTORIDBIND_FIELD_NUMBER: _ClassVar[int]
    OFFETBIND_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    ActorIDBind: int
    OffetBind: _proto_common_pb2.PB_Vector3
    def __init__(self, ActorID: _Optional[int] = ..., ActorIDBind: _Optional[int] = ..., OffetBind: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayWeaponEffectHC(_message.Message):
    __slots__ = ("EffectName", "EffectID", "EffectStatus", "EffectScale", "ObjId")
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    EFFECTSTATUS_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EffectName: str
    EffectID: int
    EffectStatus: int
    EffectScale: int
    ObjId: int
    def __init__(self, EffectName: _Optional[str] = ..., EffectID: _Optional[int] = ..., EffectStatus: _Optional[int] = ..., EffectScale: _Optional[int] = ..., ObjId: _Optional[int] = ...) -> None: ...

class PB_ScriptVarHC(_message.Message):
    __slots__ = ("ScriptVars",)
    SCRIPTVARS_FIELD_NUMBER: _ClassVar[int]
    ScriptVars: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, ScriptVars: _Optional[_Iterable[float]] = ...) -> None: ...

class PB_GVChangeRoleHC(_message.Message):
    __slots__ = ("GVMemberRole",)
    GVMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    GVMemberRole: int
    def __init__(self, GVMemberRole: _Optional[int] = ...) -> None: ...

class PB_YMChangeRoleHC(_message.Message):
    __slots__ = ("YMMemberRole",)
    YMMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    YMMemberRole: int
    def __init__(self, YMMemberRole: _Optional[int] = ...) -> None: ...

class PB_SpecialItemUseHC(_message.Message):
    __slots__ = ("ItemId", "ItemNum")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    ItemId: int
    ItemNum: int
    def __init__(self, ItemId: _Optional[int] = ..., ItemNum: _Optional[int] = ...) -> None: ...

class PB_LeaveRoomInfoHC(_message.Message):
    __slots__ = ("Cause", "KickerType")
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    KICKERTYPE_FIELD_NUMBER: _ClassVar[int]
    Cause: int
    KickerType: int
    def __init__(self, Cause: _Optional[int] = ..., KickerType: _Optional[int] = ...) -> None: ...

class PB_InviteJoinRoomHC(_message.Message):
    __slots__ = ("Uin", "RoomState", "PassWorld")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ROOMSTATE_FIELD_NUMBER: _ClassVar[int]
    PASSWORLD_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    RoomState: str
    PassWorld: str
    def __init__(self, Uin: _Optional[int] = ..., RoomState: _Optional[str] = ..., PassWorld: _Optional[str] = ...) -> None: ...

class PB_SetSpectatorModeHC(_message.Message):
    __slots__ = ("Uin", "SpectatorMode")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SPECTATORMODE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    SpectatorMode: int
    def __init__(self, Uin: _Optional[int] = ..., SpectatorMode: _Optional[int] = ...) -> None: ...

class PB_SetSpectatorTypeHC(_message.Message):
    __slots__ = ("Uin", "SpectatorType")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SPECTATORTYPE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    SpectatorType: int
    def __init__(self, Uin: _Optional[int] = ..., SpectatorType: _Optional[int] = ...) -> None: ...

class PB_SetSpectatorPlayerHC(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ...) -> None: ...

class PB_SetPlayerModelAniHC(_message.Message):
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

class PB_SendMyViewmodeToSpectatorHC(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin", "MyViewmode")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    MYVIEWMODE_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    MyViewmode: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ..., MyViewmode: _Optional[int] = ...) -> None: ...

class PB_SetBobbingToSpectatorHC(_message.Message):
    __slots__ = ("SpectatorUin", "ToSpectatorUin", "Bobbing")
    SPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    TOSPECTATORUIN_FIELD_NUMBER: _ClassVar[int]
    BOBBING_FIELD_NUMBER: _ClassVar[int]
    SpectatorUin: int
    ToSpectatorUin: int
    Bobbing: int
    def __init__(self, SpectatorUin: _Optional[int] = ..., ToSpectatorUin: _Optional[int] = ..., Bobbing: _Optional[int] = ...) -> None: ...

class PB_BallOperateHC(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData", "Uin")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    Uin: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_BasketBallOperateHC(_message.Message):
    __slots__ = ("Type", "ActorID", "IsSelectedTarget", "FallResult", "ExtendData", "Uin")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSELECTEDTARGET_FIELD_NUMBER: _ClassVar[int]
    FALLRESULT_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    IsSelectedTarget: bool
    FallResult: int
    ExtendData: int
    Uin: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., IsSelectedTarget: _Optional[bool] = ..., FallResult: _Optional[int] = ..., ExtendData: _Optional[int] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_ResetRoundHC(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_RocketAttribChangeHC(_message.Message):
    __slots__ = ("ObjID", "State", "Fuel")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FUEL_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    State: int
    Fuel: int
    def __init__(self, ObjID: _Optional[int] = ..., State: _Optional[int] = ..., Fuel: _Optional[int] = ...) -> None: ...

class PB_ActorBodyTextureHC(_message.Message):
    __slots__ = ("ObjID", "TexName", "MeshName")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TEXNAME_FIELD_NUMBER: _ClassVar[int]
    MESHNAME_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    TexName: str
    MeshName: str
    def __init__(self, ObjID: _Optional[int] = ..., TexName: _Optional[str] = ..., MeshName: _Optional[str] = ...) -> None: ...

class PB_AttractAttribChangeHC(_message.Message):
    __slots__ = ("ObjID", "State", "blockID", "blockExID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKEXID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    State: int
    blockID: int
    blockExID: int
    def __init__(self, ObjID: _Optional[int] = ..., State: _Optional[int] = ..., blockID: _Optional[int] = ..., blockExID: _Optional[int] = ...) -> None: ...

class PB_WorldTimesHC(_message.Message):
    __slots__ = ("Times",)
    TIMES_FIELD_NUMBER: _ClassVar[int]
    Times: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Times: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_StatisticHC(_message.Message):
    __slots__ = ("EventID", "WorldType", "FristName", "Param1", "Param2", "Param3", "Param4", "Param5", "Param6", "Param7")
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    WORLDTYPE_FIELD_NUMBER: _ClassVar[int]
    FRISTNAME_FIELD_NUMBER: _ClassVar[int]
    PARAM1_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    PARAM3_FIELD_NUMBER: _ClassVar[int]
    PARAM4_FIELD_NUMBER: _ClassVar[int]
    PARAM5_FIELD_NUMBER: _ClassVar[int]
    PARAM6_FIELD_NUMBER: _ClassVar[int]
    PARAM7_FIELD_NUMBER: _ClassVar[int]
    EventID: int
    WorldType: int
    FristName: str
    Param1: str
    Param2: str
    Param3: str
    Param4: str
    Param5: str
    Param6: str
    Param7: str
    def __init__(self, EventID: _Optional[int] = ..., WorldType: _Optional[int] = ..., FristName: _Optional[str] = ..., Param1: _Optional[str] = ..., Param2: _Optional[str] = ..., Param3: _Optional[str] = ..., Param4: _Optional[str] = ..., Param5: _Optional[str] = ..., Param6: _Optional[str] = ..., Param7: _Optional[str] = ...) -> None: ...

class PB_TotemPointHC(_message.Message):
    __slots__ = ("Op", "Point", "MapID")
    OP_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    Op: int
    Point: _proto_common_pb2.PB_Vector3
    MapID: int
    def __init__(self, Op: _Optional[int] = ..., Point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MapID: _Optional[int] = ...) -> None: ...

class PB_HorseFlyStateHC(_message.Message):
    __slots__ = ("m_fEnergy", "m_bTired")
    M_FENERGY_FIELD_NUMBER: _ClassVar[int]
    M_BTIRED_FIELD_NUMBER: _ClassVar[int]
    m_fEnergy: float
    m_bTired: int
    def __init__(self, m_fEnergy: _Optional[float] = ..., m_bTired: _Optional[int] = ...) -> None: ...

class PB_OpenDialogueHC(_message.Message):
    __slots__ = ("ObjID", "InteractData", "ItemID", "PlotType", "Openpos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    INTERACTDATA_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PLOTTYPE_FIELD_NUMBER: _ClassVar[int]
    OPENPOS_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    InteractData: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_IntertactData]
    ItemID: int
    PlotType: int
    Openpos: _proto_common_pb2.PB_Vector3
    def __init__(self, ObjID: _Optional[int] = ..., InteractData: _Optional[_Iterable[_Union[_proto_common_pb2.PB_IntertactData, _Mapping]]] = ..., ItemID: _Optional[int] = ..., PlotType: _Optional[int] = ..., Openpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_CloseDialogueHC(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_UpdateTaskHC(_message.Message):
    __slots__ = ("Type", "ID", "Num")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ID: int
    Num: int
    def __init__(self, Type: _Optional[int] = ..., ID: _Optional[int] = ..., Num: _Optional[int] = ...) -> None: ...

class PB_SyncTaskEnterWorldHC(_message.Message):
    __slots__ = ("TaskInfoData",)
    TASKINFODATA_FIELD_NUMBER: _ClassVar[int]
    TaskInfoData: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_TaskInfoData]
    def __init__(self, TaskInfoData: _Optional[_Iterable[_Union[_proto_common_pb2.PB_TaskInfoData, _Mapping]]] = ...) -> None: ...

class PB_CompleteTaskHC(_message.Message):
    __slots__ = ("TaskID",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TaskID: int
    def __init__(self, TaskID: _Optional[int] = ...) -> None: ...

class PB_PlayerAddAvartarHC(_message.Message):
    __slots__ = ("Uin", "avatarmodel", "index")
    UIN_FIELD_NUMBER: _ClassVar[int]
    AVATARMODEL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    avatarmodel: int
    index: int
    def __init__(self, Uin: _Optional[int] = ..., avatarmodel: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class PB_PlayerChangeModelHC(_message.Message):
    __slots__ = ("Uin", "playerindex", "customskins", "Reason")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSKINS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    playerindex: int
    customskins: str
    Reason: int
    def __init__(self, Uin: _Optional[int] = ..., playerindex: _Optional[int] = ..., customskins: _Optional[str] = ..., Reason: _Optional[int] = ...) -> None: ...

class PB_PlayerAvartarColorHC(_message.Message):
    __slots__ = ("Uin", "r", "g", "b", "partID", "modelID", "block")
    UIN_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    r: float
    g: float
    b: float
    partID: float
    modelID: float
    block: float
    def __init__(self, Uin: _Optional[int] = ..., r: _Optional[float] = ..., g: _Optional[float] = ..., b: _Optional[float] = ..., partID: _Optional[float] = ..., modelID: _Optional[float] = ..., block: _Optional[float] = ...) -> None: ...

class PB_PlayActHC(_message.Message):
    __slots__ = ("Uin", "ActID", "ActIDTrigger")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ACTID_FIELD_NUMBER: _ClassVar[int]
    ACTIDTRIGGER_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    ActID: int
    ActIDTrigger: int
    def __init__(self, Uin: _Optional[int] = ..., ActID: _Optional[int] = ..., ActIDTrigger: _Optional[int] = ...) -> None: ...

class PB_CreateBlueprintHC(_message.Message):
    __slots__ = ("Point", "sheetname", "authorname")
    POINT_FIELD_NUMBER: _ClassVar[int]
    SHEETNAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORNAME_FIELD_NUMBER: _ClassVar[int]
    Point: _proto_common_pb2.PB_Vector3
    sheetname: str
    authorname: str
    def __init__(self, Point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., sheetname: _Optional[str] = ..., authorname: _Optional[str] = ...) -> None: ...

class PB_MeasureDistanceHC(_message.Message):
    __slots__ = ("Uin", "MapID", "blockpos", "findpos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    FINDPOS_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    MapID: int
    blockpos: _proto_common_pb2.PB_Vector3
    findpos: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_Vector3]
    def __init__(self, Uin: _Optional[int] = ..., MapID: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., findpos: _Optional[_Iterable[_Union[_proto_common_pb2.PB_Vector3, _Mapping]]] = ...) -> None: ...

class PB_BluePrintPreBlockHC(_message.Message):
    __slots__ = ("BlockPos", "MapID", "PreBlocks")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    PREBLOCKS_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    MapID: int
    PreBlocks: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_PreBlockData]
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MapID: _Optional[int] = ..., PreBlocks: _Optional[_Iterable[_Union[_proto_common_pb2.PB_PreBlockData, _Mapping]]] = ...) -> None: ...

class PB_GravityOperateHC(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData", "Uin")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    Uin: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_PlayerBodyColorHC(_message.Message):
    __slots__ = ("DestColor", "CurColor", "Uin")
    DESTCOLOR_FIELD_NUMBER: _ClassVar[int]
    CURCOLOR_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    DestColor: int
    CurColor: int
    Uin: int
    def __init__(self, DestColor: _Optional[int] = ..., CurColor: _Optional[int] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_AvatarPartInfoHC(_message.Message):
    __slots__ = ("AnchorId", "ModelStr")
    ANCHORID_FIELD_NUMBER: _ClassVar[int]
    MODELSTR_FIELD_NUMBER: _ClassVar[int]
    AnchorId: int
    ModelStr: str
    def __init__(self, AnchorId: _Optional[int] = ..., ModelStr: _Optional[str] = ...) -> None: ...

class PB_AvatarPartsPrioritySyncHC(_message.Message):
    __slots__ = ("ObjId", "PriorityData")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    PRIORITYDATA_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    PriorityData: _containers.RepeatedCompositeFieldContainer[PB_AvatarPartsPriorityData]
    def __init__(self, ObjId: _Optional[int] = ..., PriorityData: _Optional[_Iterable[_Union[PB_AvatarPartsPriorityData, _Mapping]]] = ...) -> None: ...

class PB_AvatarPartsPriorityData(_message.Message):
    __slots__ = ("Priority", "Parts")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    Priority: int
    Parts: _containers.RepeatedCompositeFieldContainer[PB_AvatarPartInfoHC]
    def __init__(self, Priority: _Optional[int] = ..., Parts: _Optional[_Iterable[_Union[PB_AvatarPartInfoHC, _Mapping]]] = ...) -> None: ...

class PB_AvatarPartsPrioritySyncAllHC(_message.Message):
    __slots__ = ("AllObjects",)
    ALLOBJECTS_FIELD_NUMBER: _ClassVar[int]
    AllObjects: _containers.RepeatedCompositeFieldContainer[PB_AvatarPartsPrioritySyncHC]
    def __init__(self, AllObjects: _Optional[_Iterable[_Union[PB_AvatarPartsPrioritySyncHC, _Mapping]]] = ...) -> None: ...

class PB_CustomModelHC(_message.Message):
    __slots__ = ("UnzipLen", "BlobLen", "BlobDetail", "FileName", "ItemID", "ModelName", "ModelDesc", "ClassName", "Type", "Box", "folderIndex", "IsDownload", "AuthUin", "BlockIdVersion")
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBDETAIL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    MODELDESC_FIELD_NUMBER: _ClassVar[int]
    CLASSNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BOX_FIELD_NUMBER: _ClassVar[int]
    FOLDERINDEX_FIELD_NUMBER: _ClassVar[int]
    ISDOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    AUTHUIN_FIELD_NUMBER: _ClassVar[int]
    BLOCKIDVERSION_FIELD_NUMBER: _ClassVar[int]
    UnzipLen: int
    BlobLen: int
    BlobDetail: str
    FileName: str
    ItemID: int
    ModelName: str
    ModelDesc: str
    ClassName: str
    Type: int
    Box: _proto_common_pb2.PB_Vector3
    folderIndex: int
    IsDownload: bool
    AuthUin: int
    BlockIdVersion: int
    def __init__(self, UnzipLen: _Optional[int] = ..., BlobLen: _Optional[int] = ..., BlobDetail: _Optional[str] = ..., FileName: _Optional[str] = ..., ItemID: _Optional[int] = ..., ModelName: _Optional[str] = ..., ModelDesc: _Optional[str] = ..., ClassName: _Optional[str] = ..., Type: _Optional[int] = ..., Box: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., folderIndex: _Optional[int] = ..., IsDownload: _Optional[bool] = ..., AuthUin: _Optional[int] = ..., BlockIdVersion: _Optional[int] = ...) -> None: ...

class PB_CustomModelPrepareHC(_message.Message):
    __slots__ = ("FileName", "Index")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FileName: str
    Index: int
    def __init__(self, FileName: _Optional[str] = ..., Index: _Optional[int] = ...) -> None: ...

class PB_CustomItemIDsHC(_message.Message):
    __slots__ = ("CustomItemIDs", "CustomModelFileNames", "CustomModelClassNames", "CustomTypes", "InvolvedIds", "CustomModelFolderIndexs")
    CUSTOMITEMIDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMODELFILENAMES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMODELCLASSNAMES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMTYPES_FIELD_NUMBER: _ClassVar[int]
    INVOLVEDIDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMODELFOLDERINDEXS_FIELD_NUMBER: _ClassVar[int]
    CustomItemIDs: _containers.RepeatedScalarFieldContainer[int]
    CustomModelFileNames: _containers.RepeatedScalarFieldContainer[str]
    CustomModelClassNames: _containers.RepeatedScalarFieldContainer[str]
    CustomTypes: _containers.RepeatedScalarFieldContainer[int]
    InvolvedIds: _containers.RepeatedScalarFieldContainer[int]
    CustomModelFolderIndexs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, CustomItemIDs: _Optional[_Iterable[int]] = ..., CustomModelFileNames: _Optional[_Iterable[str]] = ..., CustomModelClassNames: _Optional[_Iterable[str]] = ..., CustomTypes: _Optional[_Iterable[int]] = ..., InvolvedIds: _Optional[_Iterable[int]] = ..., CustomModelFolderIndexs: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_PlayerSpawnPointHC(_message.Message):
    __slots__ = ("x", "y", "z", "Uin", "mapid")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    z: int
    Uin: int
    mapid: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., Uin: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class PB_CustomModelClassHC(_message.Message):
    __slots__ = ("Data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    Data: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_CustomModelClassData]
    def __init__(self, Data: _Optional[_Iterable[_Union[_proto_common_pb2.PB_CustomModelClassData, _Mapping]]] = ...) -> None: ...

class PB_TransferOneRecordHC(_message.Message):
    __slots__ = ("DesID", "TeamColor", "PassItemID", "PassItemNum", "ForbidItemID", "IsExpendable")
    DESID_FIELD_NUMBER: _ClassVar[int]
    TEAMCOLOR_FIELD_NUMBER: _ClassVar[int]
    PASSITEMID_FIELD_NUMBER: _ClassVar[int]
    PASSITEMNUM_FIELD_NUMBER: _ClassVar[int]
    FORBIDITEMID_FIELD_NUMBER: _ClassVar[int]
    ISEXPENDABLE_FIELD_NUMBER: _ClassVar[int]
    DesID: int
    TeamColor: int
    PassItemID: int
    PassItemNum: int
    ForbidItemID: int
    IsExpendable: bool
    def __init__(self, DesID: _Optional[int] = ..., TeamColor: _Optional[int] = ..., PassItemID: _Optional[int] = ..., PassItemNum: _Optional[int] = ..., ForbidItemID: _Optional[int] = ..., IsExpendable: _Optional[bool] = ...) -> None: ...

class PB_TransferRecordHC(_message.Message):
    __slots__ = ("SrcID", "IsEdit", "OneRecord")
    SRCID_FIELD_NUMBER: _ClassVar[int]
    ISEDIT_FIELD_NUMBER: _ClassVar[int]
    ONERECORD_FIELD_NUMBER: _ClassVar[int]
    SrcID: int
    IsEdit: bool
    OneRecord: PB_TransferOneRecordHC
    def __init__(self, SrcID: _Optional[int] = ..., IsEdit: _Optional[bool] = ..., OneRecord: _Optional[_Union[PB_TransferOneRecordHC, _Mapping]] = ...) -> None: ...

class PB_TransferNameTipHC(_message.Message):
    __slots__ = ("SrcID", "TransferName", "TransferTip", "ShowName", "Status")
    SRCID_FIELD_NUMBER: _ClassVar[int]
    TRANSFERNAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFERTIP_FIELD_NUMBER: _ClassVar[int]
    SHOWNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SrcID: int
    TransferName: str
    TransferTip: str
    ShowName: bool
    Status: int
    def __init__(self, SrcID: _Optional[int] = ..., TransferName: _Optional[str] = ..., TransferTip: _Optional[str] = ..., ShowName: _Optional[bool] = ..., Status: _Optional[int] = ...) -> None: ...

class PB_TransferAddDelHC(_message.Message):
    __slots__ = ("AddDel", "MapID", "postion", "Status", "TransferID", "vehicleObj", "postion_v")
    ADDDEL_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    POSTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSFERID_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJ_FIELD_NUMBER: _ClassVar[int]
    POSTION_V_FIELD_NUMBER: _ClassVar[int]
    AddDel: bool
    MapID: int
    postion: _proto_common_pb2.PB_Vector3
    Status: int
    TransferID: int
    vehicleObj: int
    postion_v: _proto_common_pb2.PB_Vector3
    def __init__(self, AddDel: _Optional[bool] = ..., MapID: _Optional[int] = ..., postion: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Status: _Optional[int] = ..., TransferID: _Optional[int] = ..., vehicleObj: _Optional[int] = ..., postion_v: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_TransferDataHC(_message.Message):
    __slots__ = ("ID", "TransferName", "TransferTip", "ShowName", "MapID", "postion", "Status", "OneRecord", "vehicleObj", "postion_v")
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFERNAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFERTIP_FIELD_NUMBER: _ClassVar[int]
    SHOWNAME_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    POSTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ONERECORD_FIELD_NUMBER: _ClassVar[int]
    VEHICLEOBJ_FIELD_NUMBER: _ClassVar[int]
    POSTION_V_FIELD_NUMBER: _ClassVar[int]
    ID: int
    TransferName: str
    TransferTip: str
    ShowName: bool
    MapID: int
    postion: _proto_common_pb2.PB_Vector3
    Status: int
    OneRecord: _containers.RepeatedCompositeFieldContainer[PB_TransferOneRecordHC]
    vehicleObj: int
    postion_v: _proto_common_pb2.PB_Vector3
    def __init__(self, ID: _Optional[int] = ..., TransferName: _Optional[str] = ..., TransferTip: _Optional[str] = ..., ShowName: _Optional[bool] = ..., MapID: _Optional[int] = ..., postion: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Status: _Optional[int] = ..., OneRecord: _Optional[_Iterable[_Union[PB_TransferOneRecordHC, _Mapping]]] = ..., vehicleObj: _Optional[int] = ..., postion_v: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_TransferTargetHC(_message.Message):
    __slots__ = ("Uin", "DesID", "SrcID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    DESID_FIELD_NUMBER: _ClassVar[int]
    SRCID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    DesID: int
    SrcID: int
    def __init__(self, Uin: _Optional[int] = ..., DesID: _Optional[int] = ..., SrcID: _Optional[int] = ...) -> None: ...

class PB_OpenUIHC(_message.Message):
    __slots__ = ("Uin", "Type", "ID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Type: int
    ID: int
    def __init__(self, Uin: _Optional[int] = ..., Type: _Optional[int] = ..., ID: _Optional[int] = ...) -> None: ...

class PB_RespNpcShopInfoHC(_message.Message):
    __slots__ = ("NpcShopInfo",)
    NPCSHOPINFO_FIELD_NUMBER: _ClassVar[int]
    NpcShopInfo: _proto_common_pb2.PB_NpcShopData
    def __init__(self, NpcShopInfo: _Optional[_Union[_proto_common_pb2.PB_NpcShopData, _Mapping]] = ...) -> None: ...

class PB_NotifyNpcShopBuySkuHC(_message.Message):
    __slots__ = ("Ret", "ShopID", "SkuID", "LeftNum", "EndTime", "Uin", "BuyCount")
    RET_FIELD_NUMBER: _ClassVar[int]
    SHOPID_FIELD_NUMBER: _ClassVar[int]
    SKUID_FIELD_NUMBER: _ClassVar[int]
    LEFTNUM_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    BUYCOUNT_FIELD_NUMBER: _ClassVar[int]
    Ret: int
    ShopID: int
    SkuID: int
    LeftNum: int
    EndTime: int
    Uin: int
    BuyCount: int
    def __init__(self, Ret: _Optional[int] = ..., ShopID: _Optional[int] = ..., SkuID: _Optional[int] = ..., LeftNum: _Optional[int] = ..., EndTime: _Optional[int] = ..., Uin: _Optional[int] = ..., BuyCount: _Optional[int] = ...) -> None: ...

class PB_SyncPlayerPositionHC(_message.Message):
    __slots__ = ("Position", "Motion")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    Position: _proto_common_pb2.PB_Vector3
    Motion: _proto_common_pb2.PB_Vector3f
    def __init__(self, Position: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Motion: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_VehiclePosDesc(_message.Message):
    __slots__ = ("Position", "RotateQuat")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATEQUAT_FIELD_NUMBER: _ClassVar[int]
    Position: _proto_common_pb2.PB_Vector3
    RotateQuat: _proto_common_pb2.PB_Quaternion
    def __init__(self, Position: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., RotateQuat: _Optional[_Union[_proto_common_pb2.PB_Quaternion, _Mapping]] = ...) -> None: ...

class PB_VehicleSTrustersPowerLevel(_message.Message):
    __slots__ = ("Position", "PowerLevel", "CurPower")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    POWERLEVEL_FIELD_NUMBER: _ClassVar[int]
    CURPOWER_FIELD_NUMBER: _ClassVar[int]
    Position: _proto_common_pb2.PB_Vector3
    PowerLevel: int
    CurPower: int
    def __init__(self, Position: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., PowerLevel: _Optional[int] = ..., CurPower: _Optional[int] = ...) -> None: ...

class PB_VehicleMoveHC(_message.Message):
    __slots__ = ("ObjID", "ChassisPos", "WheelPos", "STrustersPower")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    CHASSISPOS_FIELD_NUMBER: _ClassVar[int]
    WHEELPOS_FIELD_NUMBER: _ClassVar[int]
    STRUSTERSPOWER_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    ChassisPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    WheelPos: _containers.RepeatedCompositeFieldContainer[PB_VehiclePosDesc]
    STrustersPower: _containers.RepeatedCompositeFieldContainer[PB_VehicleSTrustersPowerLevel]
    def __init__(self, ObjID: _Optional[int] = ..., ChassisPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ..., WheelPos: _Optional[_Iterable[_Union[PB_VehiclePosDesc, _Mapping]]] = ..., STrustersPower: _Optional[_Iterable[_Union[PB_VehicleSTrustersPowerLevel, _Mapping]]] = ...) -> None: ...

class PB_OpenEditActorModelHC(_message.Message):
    __slots__ = ("ContainerPos", "MapID")
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ContainerPos: _proto_common_pb2.PB_Vector3
    MapID: int
    def __init__(self, ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MapID: _Optional[int] = ...) -> None: ...

class PB_CloseEditActorModelHC(_message.Message):
    __slots__ = ("BoneModels", "MapID", "ContainerPos", "ModelType", "ModelMark", "ModelName", "SkinDisplay")
    BONEMODELS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    MODELTYPE_FIELD_NUMBER: _ClassVar[int]
    MODELMARK_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    SKINDISPLAY_FIELD_NUMBER: _ClassVar[int]
    BoneModels: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ActorOneBoneModelData]
    MapID: int
    ContainerPos: _proto_common_pb2.PB_Vector3
    ModelType: int
    ModelMark: str
    ModelName: str
    SkinDisplay: bool
    def __init__(self, BoneModels: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ActorOneBoneModelData, _Mapping]]] = ..., MapID: _Optional[int] = ..., ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., ModelType: _Optional[int] = ..., ModelMark: _Optional[str] = ..., ModelName: _Optional[str] = ..., SkinDisplay: _Optional[bool] = ...) -> None: ...

class PB_OneCustomActorModelDataHC(_message.Message):
    __slots__ = ("BoneModels", "ModelMark", "Type", "ModelName", "SkinDisplay", "AuthUin")
    BONEMODELS_FIELD_NUMBER: _ClassVar[int]
    MODELMARK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    SKINDISPLAY_FIELD_NUMBER: _ClassVar[int]
    AUTHUIN_FIELD_NUMBER: _ClassVar[int]
    BoneModels: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ActorOneBoneModelData]
    ModelMark: str
    Type: int
    ModelName: str
    SkinDisplay: bool
    AuthUin: int
    def __init__(self, BoneModels: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ActorOneBoneModelData, _Mapping]]] = ..., ModelMark: _Optional[str] = ..., Type: _Optional[int] = ..., ModelName: _Optional[str] = ..., SkinDisplay: _Optional[bool] = ..., AuthUin: _Optional[int] = ...) -> None: ...

class PB_CustomActorModelDataHC(_message.Message):
    __slots__ = ("ModelDatas",)
    MODELDATAS_FIELD_NUMBER: _ClassVar[int]
    ModelDatas: _containers.RepeatedCompositeFieldContainer[PB_OneCustomActorModelDataHC]
    def __init__(self, ModelDatas: _Optional[_Iterable[_Union[PB_OneCustomActorModelDataHC, _Mapping]]] = ...) -> None: ...

class PB_VehiclePreBlockHC(_message.Message):
    __slots__ = ("BlockPos", "MapID", "AttrInfo", "PreBlocks")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ATTRINFO_FIELD_NUMBER: _ClassVar[int]
    PREBLOCKS_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    MapID: int
    AttrInfo: str
    PreBlocks: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_PreBlockData]
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MapID: _Optional[int] = ..., AttrInfo: _Optional[str] = ..., PreBlocks: _Optional[_Iterable[_Union[_proto_common_pb2.PB_PreBlockData, _Mapping]]] = ...) -> None: ...

class PB_VehicleItemIdHC(_message.Message):
    __slots__ = ("ItemID",)
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ItemID: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ItemID: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_VehicleAttribChangeHC(_message.Message):
    __slots__ = ("ObjID", "Fuel", "PartIndex", "ActualSpeed", "ShowSpeed", "EngineRotationSpeed", "EngineState", "STrustersPower", "NitroLevel", "NitroEnable")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    FUEL_FIELD_NUMBER: _ClassVar[int]
    PARTINDEX_FIELD_NUMBER: _ClassVar[int]
    ACTUALSPEED_FIELD_NUMBER: _ClassVar[int]
    SHOWSPEED_FIELD_NUMBER: _ClassVar[int]
    ENGINEROTATIONSPEED_FIELD_NUMBER: _ClassVar[int]
    ENGINESTATE_FIELD_NUMBER: _ClassVar[int]
    STRUSTERSPOWER_FIELD_NUMBER: _ClassVar[int]
    NITROLEVEL_FIELD_NUMBER: _ClassVar[int]
    NITROENABLE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    Fuel: int
    PartIndex: int
    ActualSpeed: int
    ShowSpeed: int
    EngineRotationSpeed: float
    EngineState: int
    STrustersPower: _containers.RepeatedCompositeFieldContainer[PB_VehicleSTrustersPowerLevel]
    NitroLevel: int
    NitroEnable: int
    def __init__(self, ObjID: _Optional[int] = ..., Fuel: _Optional[int] = ..., PartIndex: _Optional[int] = ..., ActualSpeed: _Optional[int] = ..., ShowSpeed: _Optional[int] = ..., EngineRotationSpeed: _Optional[float] = ..., EngineState: _Optional[int] = ..., STrustersPower: _Optional[_Iterable[_Union[PB_VehicleSTrustersPowerLevel, _Mapping]]] = ..., NitroLevel: _Optional[int] = ..., NitroEnable: _Optional[int] = ...) -> None: ...

class PB_WorkshopItemInfoHC(_message.Message):
    __slots__ = ("ItemID", "ItemName", "ItemDesc", "IsStart")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    ITEMDESC_FIELD_NUMBER: _ClassVar[int]
    ISSTART_FIELD_NUMBER: _ClassVar[int]
    ItemID: int
    ItemName: str
    ItemDesc: str
    IsStart: bool
    def __init__(self, ItemID: _Optional[int] = ..., ItemName: _Optional[str] = ..., ItemDesc: _Optional[str] = ..., IsStart: _Optional[bool] = ...) -> None: ...

class PB_PlayerCameraRotateHC(_message.Message):
    __slots__ = ("Pitch", "Yaw")
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    Pitch: float
    Yaw: float
    def __init__(self, Pitch: _Optional[float] = ..., Yaw: _Optional[float] = ...) -> None: ...

class PB_PlayerChangeViewModeHC(_message.Message):
    __slots__ = ("ViewMode", "Lock", "ClientMode")
    VIEWMODE_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    CLIENTMODE_FIELD_NUMBER: _ClassVar[int]
    ViewMode: int
    Lock: bool
    ClientMode: bool
    def __init__(self, ViewMode: _Optional[int] = ..., Lock: _Optional[bool] = ..., ClientMode: _Optional[bool] = ...) -> None: ...

class PB_PlayerCanMoveHC(_message.Message):
    __slots__ = ("CanMove",)
    CANMOVE_FIELD_NUMBER: _ClassVar[int]
    CanMove: bool
    def __init__(self, CanMove: _Optional[bool] = ...) -> None: ...

class PB_PlayerCanControlHC(_message.Message):
    __slots__ = ("CanControl",)
    CANCONTROL_FIELD_NUMBER: _ClassVar[int]
    CanControl: bool
    def __init__(self, CanControl: _Optional[bool] = ...) -> None: ...

class PB_PlayerSetAttrHC(_message.Message):
    __slots__ = ("AttrType", "Val")
    ATTRTYPE_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    AttrType: int
    Val: float
    def __init__(self, AttrType: _Optional[int] = ..., Val: _Optional[float] = ...) -> None: ...

class PB_TriggerTimerDataHC(_message.Message):
    __slots__ = ("TimerID", "Time", "Type", "Title")
    TIMERID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TimerID: int
    Time: int
    Type: int
    Title: str
    def __init__(self, TimerID: _Optional[int] = ..., Time: _Optional[int] = ..., Type: _Optional[int] = ..., Title: _Optional[str] = ...) -> None: ...

class PB_PlayerFreezingHC(_message.Message):
    __slots__ = ("freezingflag",)
    FREEZINGFLAG_FIELD_NUMBER: _ClassVar[int]
    freezingflag: int
    def __init__(self, freezingflag: _Optional[int] = ...) -> None: ...

class PB_WorkshopBuildHC(_message.Message):
    __slots__ = ("Isbuild", "Mapid", "ContainerPos")
    ISBUILD_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    Isbuild: bool
    Mapid: int
    ContainerPos: _proto_common_pb2.PB_Vector3
    def __init__(self, Isbuild: _Optional[bool] = ..., Mapid: _Optional[int] = ..., ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_GameRuleHC(_message.Message):
    __slots__ = ("ruleid", "optionid", "value")
    RULEID_FIELD_NUMBER: _ClassVar[int]
    OPTIONID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ruleid: int
    optionid: int
    value: float
    def __init__(self, ruleid: _Optional[int] = ..., optionid: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class PB_PlayerScaleHC(_message.Message):
    __slots__ = ("Uin", "Scale", "ObjID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Scale: float
    ObjID: int
    def __init__(self, Uin: _Optional[int] = ..., Scale: _Optional[float] = ..., ObjID: _Optional[int] = ...) -> None: ...

class PB_PlayerNavigateHC(_message.Message):
    __slots__ = ("TargetPos", "Speed", "CanControl", "showTip")
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    CANCONTROL_FIELD_NUMBER: _ClassVar[int]
    SHOWTIP_FIELD_NUMBER: _ClassVar[int]
    TargetPos: _proto_common_pb2.PB_Vector3
    Speed: float
    CanControl: bool
    showTip: bool
    def __init__(self, TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Speed: _Optional[float] = ..., CanControl: _Optional[bool] = ..., showTip: _Optional[bool] = ...) -> None: ...

class PB_PlayerCommonSetHC(_message.Message):
    __slots__ = ("Uin", "Value")
    UIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Value: float
    def __init__(self, Uin: _Optional[int] = ..., Value: _Optional[float] = ...) -> None: ...

class PB_OpenEditFullyCustomModelHC(_message.Message):
    __slots__ = ("ContainerPos", "MapID", "Edited", "url", "version", "result")
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ContainerPos: _proto_common_pb2.PB_Vector3
    MapID: int
    Edited: bool
    url: str
    version: int
    result: int
    def __init__(self, ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MapID: _Optional[int] = ..., Edited: _Optional[bool] = ..., url: _Optional[str] = ..., version: _Optional[int] = ..., result: _Optional[int] = ...) -> None: ...

class PB_CloseFullyCustomModelUIHC(_message.Message):
    __slots__ = ("Result", "MapID", "ContainerPos", "Skey")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CONTAINERPOS_FIELD_NUMBER: _ClassVar[int]
    SKEY_FIELD_NUMBER: _ClassVar[int]
    Result: int
    MapID: int
    ContainerPos: _proto_common_pb2.PB_Vector3
    Skey: str
    def __init__(self, Result: _Optional[int] = ..., MapID: _Optional[int] = ..., ContainerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Skey: _Optional[str] = ...) -> None: ...

class PB_RespDownLoadResUrlHC(_message.Message):
    __slots__ = ("Type", "ExternData", "DownloadUrl")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNDATA_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ExternData: str
    DownloadUrl: str
    def __init__(self, Type: _Optional[int] = ..., ExternData: _Optional[str] = ..., DownloadUrl: _Optional[str] = ...) -> None: ...

class PB_PreOpenEditFCMUIHC(_message.Message):
    __slots__ = ("State",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    State: int
    def __init__(self, State: _Optional[int] = ...) -> None: ...

class PB_VehicleAssembleLineHC(_message.Message):
    __slots__ = ("ObjID", "to")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    to: int
    def __init__(self, ObjID: _Optional[int] = ..., to: _Optional[int] = ..., **kwargs) -> None: ...

class PB_VehicleAssembleLineOperateHC(_message.Message):
    __slots__ = ("ObjID", "State", "BlockPos", "isfire")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ISFIRE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    State: bool
    BlockPos: _proto_common_pb2.PB_Vector3
    isfire: bool
    def __init__(self, ObjID: _Optional[int] = ..., State: _Optional[bool] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., isfire: _Optional[bool] = ...) -> None: ...

class PB_VehicleBindActorHC(_message.Message):
    __slots__ = ("vehicleObjID", "bindObjID", "BlockPos")
    VEHICLEOBJID_FIELD_NUMBER: _ClassVar[int]
    BINDOBJID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    vehicleObjID: int
    bindObjID: int
    BlockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, vehicleObjID: _Optional[int] = ..., bindObjID: _Optional[int] = ..., BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_TriggerMusicHC(_message.Message):
    __slots__ = ("objid", "Name", "Volume", "Pitch", "IsLoop", "PlayState", "SoundID", "VolumeV2", "PitchV2")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    PLAYSTATE_FIELD_NUMBER: _ClassVar[int]
    SOUNDID_FIELD_NUMBER: _ClassVar[int]
    VOLUMEV2_FIELD_NUMBER: _ClassVar[int]
    PITCHV2_FIELD_NUMBER: _ClassVar[int]
    objid: int
    Name: str
    Volume: float
    Pitch: float
    IsLoop: bool
    PlayState: int
    SoundID: int
    VolumeV2: int
    PitchV2: int
    def __init__(self, objid: _Optional[int] = ..., Name: _Optional[str] = ..., Volume: _Optional[float] = ..., Pitch: _Optional[float] = ..., IsLoop: _Optional[bool] = ..., PlayState: _Optional[int] = ..., SoundID: _Optional[int] = ..., VolumeV2: _Optional[int] = ..., PitchV2: _Optional[int] = ...) -> None: ...

class PB_CSPlayerPermitHC(_message.Message):
    __slots__ = ("TargetUin", "Flags", "BanItems", "DataType", "Permits")
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    BANITEMS_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    PERMITS_FIELD_NUMBER: _ClassVar[int]
    TargetUin: int
    Flags: int
    BanItems: _containers.RepeatedScalarFieldContainer[int]
    DataType: int
    Permits: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_CSPermitData]
    def __init__(self, TargetUin: _Optional[int] = ..., Flags: _Optional[int] = ..., BanItems: _Optional[_Iterable[int]] = ..., DataType: _Optional[int] = ..., Permits: _Optional[_Iterable[_Union[_proto_common_pb2.PB_CSPermitData, _Mapping]]] = ...) -> None: ...

class PB_CSAuthorityHC(_message.Message):
    __slots__ = ("DataType", "Authorities")
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHORITIES_FIELD_NUMBER: _ClassVar[int]
    DataType: int
    Authorities: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_CSAuthorityData]
    def __init__(self, DataType: _Optional[int] = ..., Authorities: _Optional[_Iterable[_Union[_proto_common_pb2.PB_CSAuthorityData, _Mapping]]] = ...) -> None: ...

class PB_SSTaskHC(_message.Message):
    __slots__ = ("TargetUin", "TaskId", "ParamJson", "UnzipLen", "ZipLen")
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    PARAMJSON_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    ZIPLEN_FIELD_NUMBER: _ClassVar[int]
    TargetUin: int
    TaskId: int
    ParamJson: str
    UnzipLen: int
    ZipLen: int
    def __init__(self, TargetUin: _Optional[int] = ..., TaskId: _Optional[int] = ..., ParamJson: _Optional[str] = ..., UnzipLen: _Optional[int] = ..., ZipLen: _Optional[int] = ...) -> None: ...

class PB_CloudServerChangeHC(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class PB_TriggerOpenStoreHC(_message.Message):
    __slots__ = ("ObjID",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    def __init__(self, ObjID: _Optional[int] = ...) -> None: ...

class PB_UsePackingFcmItemHC(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class PB_CreatePackingCMHC(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class PB_OnePackingCMDataHC(_message.Message):
    __slots__ = ("PackingPos", "Quat", "Name", "Model", "Dir")
    PACKINGPOS_FIELD_NUMBER: _ClassVar[int]
    QUAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    PackingPos: _proto_common_pb2.PB_Vector3
    Quat: _proto_common_pb2.PB_Quaternion
    Name: str
    Model: str
    Dir: int
    def __init__(self, PackingPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Quat: _Optional[_Union[_proto_common_pb2.PB_Quaternion, _Mapping]] = ..., Name: _Optional[str] = ..., Model: _Optional[str] = ..., Dir: _Optional[int] = ...) -> None: ...

class PB_OnePackingFCMDataHC(_message.Message):
    __slots__ = ("Name", "Desc", "SKey", "PackingCMs", "Dir", "MinPos", "MaxPos", "AuthUin")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    SKEY_FIELD_NUMBER: _ClassVar[int]
    PACKINGCMS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    MINPOS_FIELD_NUMBER: _ClassVar[int]
    MAXPOS_FIELD_NUMBER: _ClassVar[int]
    AUTHUIN_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Desc: str
    SKey: str
    PackingCMs: _containers.RepeatedCompositeFieldContainer[PB_OnePackingCMDataHC]
    Dir: int
    MinPos: _proto_common_pb2.PB_Vector3
    MaxPos: _proto_common_pb2.PB_Vector3
    AuthUin: int
    def __init__(self, Name: _Optional[str] = ..., Desc: _Optional[str] = ..., SKey: _Optional[str] = ..., PackingCMs: _Optional[_Iterable[_Union[PB_OnePackingCMDataHC, _Mapping]]] = ..., Dir: _Optional[int] = ..., MinPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., MaxPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., AuthUin: _Optional[int] = ...) -> None: ...

class PB_PackingFCMDataHC(_message.Message):
    __slots__ = ("PackingFCMs",)
    PACKINGFCMS_FIELD_NUMBER: _ClassVar[int]
    PackingFCMs: _containers.RepeatedCompositeFieldContainer[PB_OnePackingFCMDataHC]
    def __init__(self, PackingFCMs: _Optional[_Iterable[_Union[PB_OnePackingFCMDataHC, _Mapping]]] = ...) -> None: ...

class PB_CloudRoomStatusTimeHC(_message.Message):
    __slots__ = ("Status", "Time")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    Status: int
    Time: int
    def __init__(self, Status: _Optional[int] = ..., Time: _Optional[int] = ...) -> None: ...

class PB_SensorContainerDataHC(_message.Message):
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

class PB_DoorDataHC(_message.Message):
    __slots__ = ("BlockPos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    BlockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, BlockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_PlayerCarryActorHC(_message.Message):
    __slots__ = ("ActorID", "PlayerUIN")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    PlayerUIN: int
    def __init__(self, ActorID: _Optional[int] = ..., PlayerUIN: _Optional[int] = ...) -> None: ...

class PB_ActorPickupActorHC(_message.Message):
    __slots__ = ("AtkObjid", "DefObjid", "IsChangeDefActor", "AtkHitBoundH", "AnimA", "AnimB", "offset", "rote", "playspeed", "playmodel", "anchorId")
    ATKOBJID_FIELD_NUMBER: _ClassVar[int]
    DEFOBJID_FIELD_NUMBER: _ClassVar[int]
    ISCHANGEDEFACTOR_FIELD_NUMBER: _ClassVar[int]
    ATKHITBOUNDH_FIELD_NUMBER: _ClassVar[int]
    ANIMA_FIELD_NUMBER: _ClassVar[int]
    ANIMB_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROTE_FIELD_NUMBER: _ClassVar[int]
    PLAYSPEED_FIELD_NUMBER: _ClassVar[int]
    PLAYMODEL_FIELD_NUMBER: _ClassVar[int]
    ANCHORID_FIELD_NUMBER: _ClassVar[int]
    AtkObjid: int
    DefObjid: int
    IsChangeDefActor: bool
    AtkHitBoundH: int
    AnimA: int
    AnimB: int
    offset: _proto_common_pb2.PB_Vector3f
    rote: _proto_common_pb2.PB_Vector3f
    playspeed: int
    playmodel: int
    anchorId: int
    def __init__(self, AtkObjid: _Optional[int] = ..., DefObjid: _Optional[int] = ..., IsChangeDefActor: _Optional[bool] = ..., AtkHitBoundH: _Optional[int] = ..., AnimA: _Optional[int] = ..., AnimB: _Optional[int] = ..., offset: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., rote: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., playspeed: _Optional[int] = ..., playmodel: _Optional[int] = ..., anchorId: _Optional[int] = ...) -> None: ...

class PB_ActorDropPickupActorHC(_message.Message):
    __slots__ = ("AtkObjid", "speed", "dir", "hasInertance", "isThrow", "CarriedMov")
    ATKOBJID_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    HASINERTANCE_FIELD_NUMBER: _ClassVar[int]
    ISTHROW_FIELD_NUMBER: _ClassVar[int]
    CARRIEDMOV_FIELD_NUMBER: _ClassVar[int]
    AtkObjid: int
    speed: float
    dir: _proto_common_pb2.PB_Vector3f
    hasInertance: bool
    isThrow: bool
    CarriedMov: _proto_common_pb2.PB_Vector3f
    def __init__(self, AtkObjid: _Optional[int] = ..., speed: _Optional[float] = ..., dir: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., hasInertance: _Optional[bool] = ..., isThrow: _Optional[bool] = ..., CarriedMov: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_VillagerBodyChangeHC(_message.Message):
    __slots__ = ("ObjId", "ChangeType", "ChangeValue", "OtherValue")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    CHANGETYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGEVALUE_FIELD_NUMBER: _ClassVar[int]
    OTHERVALUE_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    ChangeType: int
    ChangeValue: int
    OtherValue: str
    def __init__(self, ObjId: _Optional[int] = ..., ChangeType: _Optional[int] = ..., ChangeValue: _Optional[int] = ..., OtherValue: _Optional[str] = ...) -> None: ...

class PB_PlayerTameActorHC(_message.Message):
    __slots__ = ("ActorID", "PlayerUIN")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    PlayerUIN: int
    def __init__(self, ActorID: _Optional[int] = ..., PlayerUIN: _Optional[int] = ...) -> None: ...

class PB_VillagerCloth(_message.Message):
    __slots__ = ("ActorID", "bshow", "modlename")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    BSHOW_FIELD_NUMBER: _ClassVar[int]
    MODLENAME_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    bshow: bool
    modlename: str
    def __init__(self, ActorID: _Optional[int] = ..., bshow: _Optional[bool] = ..., modlename: _Optional[str] = ...) -> None: ...

class PB_ActorHeadDisplayIconHC(_message.Message):
    __slots__ = ("ActorID", "ItemID", "Tick")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    TICK_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    ItemID: int
    Tick: int
    def __init__(self, ActorID: _Optional[int] = ..., ItemID: _Optional[int] = ..., Tick: _Optional[int] = ...) -> None: ...

class PB_ActorChatBubbleHC(_message.Message):
    __slots__ = ("ActorID", "JsonRichText")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    JSONRICHTEXT_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    JsonRichText: str
    def __init__(self, ActorID: _Optional[int] = ..., JsonRichText: _Optional[str] = ...) -> None: ...

class PB_ActorPlayAnimByIdHC(_message.Message):
    __slots__ = ("ActorID", "AnimID", "Loopmode", "Layer", "crossfade", "AnimName", "Speed")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    LOOPMODE_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    ANIMNAME_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    AnimID: int
    Loopmode: int
    Layer: int
    crossfade: float
    AnimName: str
    Speed: float
    def __init__(self, ActorID: _Optional[int] = ..., AnimID: _Optional[int] = ..., Loopmode: _Optional[int] = ..., Layer: _Optional[int] = ..., crossfade: _Optional[float] = ..., AnimName: _Optional[str] = ..., Speed: _Optional[float] = ...) -> None: ...

class PB_ActorPlayHandAnimHC(_message.Message):
    __slots__ = ("ActorID", "AnimID", "Loopmode", "Layer", "crossfade", "AnimName", "Speed")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    LOOPMODE_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    ANIMNAME_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    AnimID: int
    Loopmode: int
    Layer: int
    crossfade: float
    AnimName: str
    Speed: float
    def __init__(self, ActorID: _Optional[int] = ..., AnimID: _Optional[int] = ..., Loopmode: _Optional[int] = ..., Layer: _Optional[int] = ..., crossfade: _Optional[float] = ..., AnimName: _Optional[str] = ..., Speed: _Optional[float] = ...) -> None: ...

class PB_BlockPlayAnimHC(_message.Message):
    __slots__ = ("Pos", "AnimID", "Loopmode", "Layer", "crossfade", "AnimName", "Speed")
    POS_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    LOOPMODE_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    ANIMNAME_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    AnimID: int
    Loopmode: int
    Layer: int
    crossfade: float
    AnimName: str
    Speed: float
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., AnimID: _Optional[int] = ..., Loopmode: _Optional[int] = ..., Layer: _Optional[int] = ..., crossfade: _Optional[float] = ..., AnimName: _Optional[str] = ..., Speed: _Optional[float] = ...) -> None: ...

class PB_VillageTotemTipHC(_message.Message):
    __slots__ = ("villagerNum", "blockPos")
    VILLAGERNUM_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    villagerNum: int
    blockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, villagerNum: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_VillageTotemActiveHC(_message.Message):
    __slots__ = ("uin", "blockPos", "mapID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    blockPos: _proto_common_pb2.PB_Vector3
    mapID: int
    def __init__(self, uin: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., mapID: _Optional[int] = ...) -> None: ...

class PB_SaveTombStoneHC(_message.Message):
    __slots__ = ("Point", "title")
    POINT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    Point: _proto_common_pb2.PB_Vector3
    title: str
    def __init__(self, Point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class PB_PlayerLevelModeHC(_message.Message):
    __slots__ = ("SumExp", "CurLevel", "CurExp")
    SUMEXP_FIELD_NUMBER: _ClassVar[int]
    CURLEVEL_FIELD_NUMBER: _ClassVar[int]
    CUREXP_FIELD_NUMBER: _ClassVar[int]
    SumExp: int
    CurLevel: int
    CurExp: int
    def __init__(self, SumExp: _Optional[int] = ..., CurLevel: _Optional[int] = ..., CurExp: _Optional[int] = ...) -> None: ...

class PB_ActionAttrStateHC(_message.Message):
    __slots__ = ("Attr",)
    ATTR_FIELD_NUMBER: _ClassVar[int]
    Attr: int
    def __init__(self, Attr: _Optional[int] = ...) -> None: ...

class PB_Edu_RolesInfoHC(_message.Message):
    __slots__ = ("rolesInfo",)
    ROLESINFO_FIELD_NUMBER: _ClassVar[int]
    rolesInfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_Edu_RoleInfo]
    def __init__(self, rolesInfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_Edu_RoleInfo, _Mapping]]] = ...) -> None: ...

class PB_ImportModelHC(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ImportModelData]
    def __init__(self, models: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ImportModelData, _Mapping]]] = ...) -> None: ...

class PB_LightningHC(_message.Message):
    __slots__ = ("targetpos",)
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    targetpos: _proto_common_pb2.PB_Vector3
    def __init__(self, targetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_InteractMobPackHC(_message.Message):
    __slots__ = ("uiName", "param", "mobID")
    UINAME_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    MOBID_FIELD_NUMBER: _ClassVar[int]
    uiName: str
    param: str
    mobID: int
    def __init__(self, uiName: _Optional[str] = ..., param: _Optional[str] = ..., mobID: _Optional[int] = ...) -> None: ...

class PB_UpdateMobBackpackHC(_message.Message):
    __slots__ = ("mobID", "ItemInfo")
    MOBID_FIELD_NUMBER: _ClassVar[int]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    mobID: int
    ItemInfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_ItemData]
    def __init__(self, mobID: _Optional[int] = ..., ItemInfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_ItemData, _Mapping]]] = ...) -> None: ...

class PB_PlayerTransformSkinHC(_message.Message):
    __slots__ = ("Uin", "playerindex", "customskins", "Reason", "MainPlayerId")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSKINS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MAINPLAYERID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    playerindex: int
    customskins: str
    Reason: int
    MainPlayerId: int
    def __init__(self, Uin: _Optional[int] = ..., playerindex: _Optional[int] = ..., customskins: _Optional[str] = ..., Reason: _Optional[int] = ..., MainPlayerId: _Optional[int] = ...) -> None: ...

class PB_PlayerSaveArchHC(_message.Message):
    __slots__ = ("Uin", "playTime", "showTip", "userdata")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_FIELD_NUMBER: _ClassVar[int]
    SHOWTIP_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    playTime: int
    showTip: bool
    userdata: str
    def __init__(self, Uin: _Optional[int] = ..., playTime: _Optional[int] = ..., showTip: _Optional[bool] = ..., userdata: _Optional[str] = ...) -> None: ...

class PB_PrayTreeStageHC(_message.Message):
    __slots__ = ("stage",)
    STAGE_FIELD_NUMBER: _ClassVar[int]
    stage: int
    def __init__(self, stage: _Optional[int] = ...) -> None: ...

class PB_PrayTreeReqHC(_message.Message):
    __slots__ = ("Uin", "stage", "treeId")
    UIN_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    TREEID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    stage: int
    treeId: str
    def __init__(self, Uin: _Optional[int] = ..., stage: _Optional[int] = ..., treeId: _Optional[str] = ...) -> None: ...

class PB_PrayTreeInfoHC(_message.Message):
    __slots__ = ("stage", "treeId", "hostuin")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    TREEID_FIELD_NUMBER: _ClassVar[int]
    HOSTUIN_FIELD_NUMBER: _ClassVar[int]
    stage: int
    treeId: str
    hostuin: int
    def __init__(self, stage: _Optional[int] = ..., treeId: _Optional[str] = ..., hostuin: _Optional[int] = ...) -> None: ...

class PB_PrayTreeTimeUpdateHC(_message.Message):
    __slots__ = ("stage", "treeTime")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    TREETIME_FIELD_NUMBER: _ClassVar[int]
    stage: int
    treeTime: str
    def __init__(self, stage: _Optional[int] = ..., treeTime: _Optional[str] = ...) -> None: ...

class PB_HomeNpcOpenHC(_message.Message):
    __slots__ = ("Uin", "npcType", "npcId", "activeNpcDialogue")
    UIN_FIELD_NUMBER: _ClassVar[int]
    NPCTYPE_FIELD_NUMBER: _ClassVar[int]
    NPCID_FIELD_NUMBER: _ClassVar[int]
    ACTIVENPCDIALOGUE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    npcType: int
    npcId: int
    activeNpcDialogue: bool
    def __init__(self, Uin: _Optional[int] = ..., npcType: _Optional[int] = ..., npcId: _Optional[int] = ..., activeNpcDialogue: _Optional[bool] = ...) -> None: ...

class PB_PrayErrorHC(_message.Message):
    __slots__ = ("Uin", "errorType")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ERRORTYPE_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    errorType: int
    def __init__(self, Uin: _Optional[int] = ..., errorType: _Optional[int] = ...) -> None: ...

class PB_Open_HomeCloset_HC(_message.Message):
    __slots__ = ("Uin", "skinIDs", "skinPartIDs")
    UIN_FIELD_NUMBER: _ClassVar[int]
    SKINIDS_FIELD_NUMBER: _ClassVar[int]
    SKINPARTIDS_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    skinIDs: str
    skinPartIDs: str
    def __init__(self, Uin: _Optional[int] = ..., skinIDs: _Optional[str] = ..., skinPartIDs: _Optional[str] = ...) -> None: ...

class PB_OpenDevGoodsBuyDialogHC(_message.Message):
    __slots__ = ("itemid", "desc")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    itemid: int
    desc: str
    def __init__(self, itemid: _Optional[int] = ..., desc: _Optional[str] = ...) -> None: ...

class PB_PlayGraphicsHC(_message.Message):
    __slots__ = ("Operateid", "graphicsinfo")
    OPERATEID_FIELD_NUMBER: _ClassVar[int]
    GRAPHICSINFO_FIELD_NUMBER: _ClassVar[int]
    Operateid: int
    graphicsinfo: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_GraphicsAttr]
    def __init__(self, Operateid: _Optional[int] = ..., graphicsinfo: _Optional[_Iterable[_Union[_proto_common_pb2.PB_GraphicsAttr, _Mapping]]] = ...) -> None: ...

class PB_GodTempleCreateHC(_message.Message):
    __slots__ = ("onoff", "worldid")
    ONOFF_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    onoff: bool
    worldid: int
    def __init__(self, onoff: _Optional[bool] = ..., worldid: _Optional[int] = ...) -> None: ...

class PB_SFActivity_HC(_message.Message):
    __slots__ = ("type", "taskId", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    taskId: int
    value: int
    def __init__(self, type: _Optional[int] = ..., taskId: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class PB_ShapeAdditionAnimHC(_message.Message):
    __slots__ = ("Uin", "status")
    UIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    status: bool
    def __init__(self, Uin: _Optional[int] = ..., status: _Optional[bool] = ...) -> None: ...

class PB_OneHomelandRanchAnimal(_message.Message):
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

class PB_HomelandRanchInfoHC(_message.Message):
    __slots__ = ("full", "Animals")
    FULL_FIELD_NUMBER: _ClassVar[int]
    ANIMALS_FIELD_NUMBER: _ClassVar[int]
    full: bool
    Animals: _containers.RepeatedCompositeFieldContainer[PB_OneHomelandRanchAnimal]
    def __init__(self, full: _Optional[bool] = ..., Animals: _Optional[_Iterable[_Union[PB_OneHomelandRanchAnimal, _Mapping]]] = ...) -> None: ...

class PB_UseItemByHomelandHC(_message.Message):
    __slots__ = ("ItemID", "ItemNum")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNUM_FIELD_NUMBER: _ClassVar[int]
    ItemID: int
    ItemNum: int
    def __init__(self, ItemID: _Optional[int] = ..., ItemNum: _Optional[int] = ...) -> None: ...

class PB_CustomBaseModelHC(_message.Message):
    __slots__ = ("Uin", "TeamId", "ModelData")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    MODELDATA_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    TeamId: int
    ModelData: str
    def __init__(self, Uin: _Optional[int] = ..., TeamId: _Optional[int] = ..., ModelData: _Optional[str] = ...) -> None: ...

class PB_ChangeActorModelHC(_message.Message):
    __slots__ = ("ObjID", "modelID")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MODELID_FIELD_NUMBER: _ClassVar[int]
    ObjID: _containers.RepeatedScalarFieldContainer[int]
    modelID: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ObjID: _Optional[_Iterable[int]] = ..., modelID: _Optional[_Iterable[str]] = ...) -> None: ...

class PB_NotifiyActorModelHC(_message.Message):
    __slots__ = ("modelID", "modelData")
    MODELID_FIELD_NUMBER: _ClassVar[int]
    MODELDATA_FIELD_NUMBER: _ClassVar[int]
    modelID: _containers.RepeatedScalarFieldContainer[str]
    modelData: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, modelID: _Optional[_Iterable[str]] = ..., modelData: _Optional[_Iterable[str]] = ...) -> None: ...

class PB_VoiceInformHC(_message.Message):
    __slots__ = ("Uin", "type", "voiceId", "reportUin", "node", "dir")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VOICEID_FIELD_NUMBER: _ClassVar[int]
    REPORTUIN_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    type: int
    voiceId: str
    reportUin: int
    node: str
    dir: str
    def __init__(self, Uin: _Optional[int] = ..., type: _Optional[int] = ..., voiceId: _Optional[str] = ..., reportUin: _Optional[int] = ..., node: _Optional[str] = ..., dir: _Optional[str] = ...) -> None: ...

class PB_UpdatePotContainerHC(_message.Message):
    __slots__ = ("uin", "x", "y", "z", "isMaking", "progress", "craftID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    ISMAKING_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CRAFTID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    x: int
    y: int
    z: int
    isMaking: bool
    progress: int
    craftID: int
    def __init__(self, uin: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., isMaking: _Optional[bool] = ..., progress: _Optional[int] = ..., craftID: _Optional[int] = ...) -> None: ...

class PB_StarStationDataHC(_message.Message):
    __slots__ = ("starStationID", "starStationName", "mapID", "isConsoleActive", "isSign", "consolePos", "starStationCabinDef", "unfinishedTransferRecord", "stationType", "stationExtraData")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONNAME_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ISCONSOLEACTIVE_FIELD_NUMBER: _ClassVar[int]
    ISSIGN_FIELD_NUMBER: _ClassVar[int]
    CONSOLEPOS_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONCABINDEF_FIELD_NUMBER: _ClassVar[int]
    UNFINISHEDTRANSFERRECORD_FIELD_NUMBER: _ClassVar[int]
    STATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    STATIONEXTRADATA_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    starStationName: str
    mapID: int
    isConsoleActive: bool
    isSign: bool
    consolePos: _proto_common_pb2.PB_Vector3
    starStationCabinDef: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_StarStationCabinDef]
    unfinishedTransferRecord: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_UnfinishedStarStationTransferRecord]
    stationType: int
    stationExtraData: int
    def __init__(self, starStationID: _Optional[int] = ..., starStationName: _Optional[str] = ..., mapID: _Optional[int] = ..., isConsoleActive: _Optional[bool] = ..., isSign: _Optional[bool] = ..., consolePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., starStationCabinDef: _Optional[_Iterable[_Union[_proto_common_pb2.PB_StarStationCabinDef, _Mapping]]] = ..., unfinishedTransferRecord: _Optional[_Iterable[_Union[_proto_common_pb2.PB_UnfinishedStarStationTransferRecord, _Mapping]]] = ..., stationType: _Optional[int] = ..., stationExtraData: _Optional[int] = ...) -> None: ...

class PB_BlockExploitHC(_message.Message):
    __slots__ = ("ObjID", "status", "face", "blockpos", "picktype")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    PICKTYPE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    status: int
    face: int
    blockpos: _proto_common_pb2.PB_Vector3
    picktype: int
    def __init__(self, ObjID: _Optional[int] = ..., status: _Optional[int] = ..., face: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., picktype: _Optional[int] = ...) -> None: ...

class PB_PlayerTransferByStarStationHC(_message.Message):
    __slots__ = ("uin", "destMapID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    destMapID: int
    def __init__(self, uin: _Optional[int] = ..., destMapID: _Optional[int] = ...) -> None: ...

class PB_VacantBossStateHC(_message.Message):
    __slots__ = ("objid", "type", "fval0", "fval1", "ival0", "ival1", "TargetPos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FVAL0_FIELD_NUMBER: _ClassVar[int]
    FVAL1_FIELD_NUMBER: _ClassVar[int]
    IVAL0_FIELD_NUMBER: _ClassVar[int]
    IVAL1_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    objid: int
    type: int
    fval0: float
    fval1: float
    ival0: int
    ival1: int
    TargetPos: _proto_common_pb2.PB_Vector3
    def __init__(self, objid: _Optional[int] = ..., type: _Optional[int] = ..., fval0: _Optional[float] = ..., fval1: _Optional[float] = ..., ival0: _Optional[int] = ..., ival1: _Optional[int] = ..., TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActivateStarStationHC(_message.Message):
    __slots__ = ("starStationID", "starStationName", "mapID", "consolePos", "result", "playerUin")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONNAME_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CONSOLEPOS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    starStationName: str
    mapID: int
    consolePos: _proto_common_pb2.PB_Vector3
    result: bool
    playerUin: int
    def __init__(self, starStationID: _Optional[int] = ..., starStationName: _Optional[str] = ..., mapID: _Optional[int] = ..., consolePos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., result: _Optional[bool] = ..., playerUin: _Optional[int] = ...) -> None: ...

class PB_UpgradeStarStationCabinHC(_message.Message):
    __slots__ = ("starStationID", "cabinPos", "playerUin", "result")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: _proto_common_pb2.PB_Vector3
    playerUin: int
    result: bool
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., playerUin: _Optional[int] = ..., result: _Optional[bool] = ...) -> None: ...

class PB_UpdateStarStationSignInfoHC(_message.Message):
    __slots__ = ("starStationID", "isSign")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    ISSIGN_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    isSign: bool
    def __init__(self, starStationID: _Optional[int] = ..., isSign: _Optional[bool] = ...) -> None: ...

class PB_PlayerRevivePointHC(_message.Message):
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

class PB_StarStationTransferDeductFeeHC(_message.Message):
    __slots__ = ("transferType", "result")
    TRANSFERTYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    transferType: int
    result: int
    def __init__(self, transferType: _Optional[int] = ..., result: _Optional[int] = ...) -> None: ...

class PB_PlayAltmanMusicHC(_message.Message):
    __slots__ = ("blockID",)
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    blockID: int
    def __init__(self, blockID: _Optional[int] = ...) -> None: ...

class PB_AchievementSyncHC(_message.Message):
    __slots__ = ("achievementList",)
    ACHIEVEMENTLIST_FIELD_NUMBER: _ClassVar[int]
    achievementList: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_AchievementInfo]
    def __init__(self, achievementList: _Optional[_Iterable[_Union[_proto_common_pb2.PB_AchievementInfo, _Mapping]]] = ...) -> None: ...

class PB_NotifyUpdateToolModelTextureHC(_message.Message):
    __slots__ = ("Uin", "textureIndex", "objid")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TEXTUREINDEX_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    textureIndex: int
    objid: int
    def __init__(self, Uin: _Optional[int] = ..., textureIndex: _Optional[int] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_AddExpResultHC(_message.Message):
    __slots__ = ("op", "result", "Uin")
    OP_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    op: int
    result: int
    Uin: int
    def __init__(self, op: _Optional[int] = ..., result: _Optional[int] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_BPEventHC(_message.Message):
    __slots__ = ("sType", "val", "extenddata")
    STYPE_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    sType: str
    val: int
    extenddata: str
    def __init__(self, sType: _Optional[str] = ..., val: _Optional[int] = ..., extenddata: _Optional[str] = ...) -> None: ...

class PB_HorseFlagHC(_message.Message):
    __slots__ = ("flag", "objid")
    FLAG_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    flag: int
    objid: int
    def __init__(self, flag: _Optional[int] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_HomeLandRanchFooderStateHC(_message.Message):
    __slots__ = ("objid", "enterstate", "serverid")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ENTERSTATE_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    enterstate: int
    serverid: str
    def __init__(self, objid: _Optional[int] = ..., enterstate: _Optional[int] = ..., serverid: _Optional[str] = ...) -> None: ...

class PB_ActorStopAnimHC(_message.Message):
    __slots__ = ("anim", "actorid", "isSeq")
    ANIM_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSEQ_FIELD_NUMBER: _ClassVar[int]
    anim: int
    actorid: int
    isSeq: bool
    def __init__(self, anim: _Optional[int] = ..., actorid: _Optional[int] = ..., isSeq: _Optional[bool] = ...) -> None: ...

class PB_HomeLandMenuBuyHC(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_HomeLandSpecialFurnitureBuyHC(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PB_HomeLandShopCellHC(_message.Message):
    __slots__ = ("uin", "itemid", "num")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    uin: int
    itemid: int
    num: int
    def __init__(self, uin: _Optional[int] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class PB_Custom_Msg(_message.Message):
    __slots__ = ("msgname", "content", "ziplen", "unziplen")
    MSGNAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ZIPLEN_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    msgname: str
    content: str
    ziplen: int
    unziplen: int
    def __init__(self, msgname: _Optional[str] = ..., content: _Optional[str] = ..., ziplen: _Optional[int] = ..., unziplen: _Optional[int] = ...) -> None: ...

class PB_ExchangeItemsToBackPackResultHC(_message.Message):
    __slots__ = ("result", "opertype")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    OPERTYPE_FIELD_NUMBER: _ClassVar[int]
    result: int
    opertype: int
    def __init__(self, result: _Optional[int] = ..., opertype: _Optional[int] = ...) -> None: ...

class PB_InteractLanternBirdHC(_message.Message):
    __slots__ = ("uin", "guessid")
    UIN_FIELD_NUMBER: _ClassVar[int]
    GUESSID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    guessid: int
    def __init__(self, uin: _Optional[int] = ..., guessid: _Optional[int] = ...) -> None: ...

class PB_ChangeQQMusicPlayerHC(_message.Message):
    __slots__ = ("type", "musicId", "state", "volume", "uin", "musicList", "uinList", "startPos", "duration", "playMode", "isPaused", "isOpen", "nameList")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUSICID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    MUSICLIST_FIELD_NUMBER: _ClassVar[int]
    UINLIST_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PLAYMODE_FIELD_NUMBER: _ClassVar[int]
    ISPAUSED_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    NAMELIST_FIELD_NUMBER: _ClassVar[int]
    type: int
    musicId: int
    state: bool
    volume: int
    uin: int
    musicList: _containers.RepeatedScalarFieldContainer[int]
    uinList: _containers.RepeatedScalarFieldContainer[int]
    startPos: int
    duration: int
    playMode: int
    isPaused: bool
    isOpen: bool
    nameList: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[int] = ..., musicId: _Optional[int] = ..., state: _Optional[bool] = ..., volume: _Optional[int] = ..., uin: _Optional[int] = ..., musicList: _Optional[_Iterable[int]] = ..., uinList: _Optional[_Iterable[int]] = ..., startPos: _Optional[int] = ..., duration: _Optional[int] = ..., playMode: _Optional[int] = ..., isPaused: _Optional[bool] = ..., isOpen: _Optional[bool] = ..., nameList: _Optional[_Iterable[str]] = ...) -> None: ...

class PB_SetTiangouHC(_message.Message):
    __slots__ = ("strID", "moonPhase", "moonRes", "defaultControlMoon", "tiangouStart")
    STRID_FIELD_NUMBER: _ClassVar[int]
    MOONPHASE_FIELD_NUMBER: _ClassVar[int]
    MOONRES_FIELD_NUMBER: _ClassVar[int]
    DEFAULTCONTROLMOON_FIELD_NUMBER: _ClassVar[int]
    TIANGOUSTART_FIELD_NUMBER: _ClassVar[int]
    strID: int
    moonPhase: int
    moonRes: str
    defaultControlMoon: bool
    tiangouStart: bool
    def __init__(self, strID: _Optional[int] = ..., moonPhase: _Optional[int] = ..., moonRes: _Optional[str] = ..., defaultControlMoon: _Optional[bool] = ..., tiangouStart: _Optional[bool] = ...) -> None: ...

class PB_PlayerOpenUIHC(_message.Message):
    __slots__ = ("uiName", "uiParam")
    UINAME_FIELD_NUMBER: _ClassVar[int]
    UIPARAM_FIELD_NUMBER: _ClassVar[int]
    uiName: str
    uiParam: str
    def __init__(self, uiName: _Optional[str] = ..., uiParam: _Optional[str] = ...) -> None: ...

class PB_RideInvisibleHC(_message.Message):
    __slots__ = ("invisible", "ObjIDList")
    INVISIBLE_FIELD_NUMBER: _ClassVar[int]
    OBJIDLIST_FIELD_NUMBER: _ClassVar[int]
    invisible: bool
    ObjIDList: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, invisible: _Optional[bool] = ..., ObjIDList: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_PlaySkinActHC(_message.Message):
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

class PB_ActorStopSkinActHC(_message.Message):
    __slots__ = ("ActorID1", "ActorID2")
    ACTORID1_FIELD_NUMBER: _ClassVar[int]
    ACTORID2_FIELD_NUMBER: _ClassVar[int]
    ActorID1: int
    ActorID2: int
    def __init__(self, ActorID1: _Optional[int] = ..., ActorID2: _Optional[int] = ...) -> None: ...

class PB_ChangeQQMusicClubHC(_message.Message):
    __slots__ = ("type", "pointIndex", "actinIndex", "actionId", "time", "beginPos", "endPos", "uin", "enterArea", "playingMusic", "fractions", "uins", "dataset")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTINDEX_FIELD_NUMBER: _ClassVar[int]
    ACTININDEX_FIELD_NUMBER: _ClassVar[int]
    ACTIONID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    BEGINPOS_FIELD_NUMBER: _ClassVar[int]
    ENDPOS_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    ENTERAREA_FIELD_NUMBER: _ClassVar[int]
    PLAYINGMUSIC_FIELD_NUMBER: _ClassVar[int]
    FRACTIONS_FIELD_NUMBER: _ClassVar[int]
    UINS_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    type: int
    pointIndex: int
    actinIndex: int
    actionId: int
    time: int
    beginPos: _containers.RepeatedScalarFieldContainer[int]
    endPos: _containers.RepeatedScalarFieldContainer[int]
    uin: int
    enterArea: bool
    playingMusic: bool
    fractions: str
    uins: str
    dataset: str
    def __init__(self, type: _Optional[int] = ..., pointIndex: _Optional[int] = ..., actinIndex: _Optional[int] = ..., actionId: _Optional[int] = ..., time: _Optional[int] = ..., beginPos: _Optional[_Iterable[int]] = ..., endPos: _Optional[_Iterable[int]] = ..., uin: _Optional[int] = ..., enterArea: _Optional[bool] = ..., playingMusic: _Optional[bool] = ..., fractions: _Optional[str] = ..., uins: _Optional[str] = ..., dataset: _Optional[str] = ...) -> None: ...

class PB_MiniClubMusicPlayerHC(_message.Message):
    __slots__ = ("type", "musicId", "state", "volume", "uin", "musicList", "uinList", "startPos", "duration", "playMode", "isPaused", "isOpen", "nameList")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUSICID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    MUSICLIST_FIELD_NUMBER: _ClassVar[int]
    UINLIST_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PLAYMODE_FIELD_NUMBER: _ClassVar[int]
    ISPAUSED_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    NAMELIST_FIELD_NUMBER: _ClassVar[int]
    type: int
    musicId: int
    state: bool
    volume: int
    uin: int
    musicList: _containers.RepeatedScalarFieldContainer[int]
    uinList: _containers.RepeatedScalarFieldContainer[int]
    startPos: int
    duration: int
    playMode: int
    isPaused: bool
    isOpen: bool
    nameList: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[int] = ..., musicId: _Optional[int] = ..., state: _Optional[bool] = ..., volume: _Optional[int] = ..., uin: _Optional[int] = ..., musicList: _Optional[_Iterable[int]] = ..., uinList: _Optional[_Iterable[int]] = ..., startPos: _Optional[int] = ..., duration: _Optional[int] = ..., playMode: _Optional[int] = ..., isPaused: _Optional[bool] = ..., isOpen: _Optional[bool] = ..., nameList: _Optional[_Iterable[str]] = ...) -> None: ...

class PaintedInfo(_message.Message):
    __slots__ = ("key", "paintid", "pos", "texname", "showtime", "dir", "mapid")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PAINTID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    TEXNAME_FIELD_NUMBER: _ClassVar[int]
    SHOWTIME_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    key: str
    paintid: int
    pos: _proto_common_pb2.PB_Vector3
    texname: str
    showtime: int
    dir: int
    mapid: int
    def __init__(self, key: _Optional[str] = ..., paintid: _Optional[int] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., texname: _Optional[str] = ..., showtime: _Optional[int] = ..., dir: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class PB_AddPaintedInfoHC(_message.Message):
    __slots__ = ("paintedinfos",)
    PAINTEDINFOS_FIELD_NUMBER: _ClassVar[int]
    paintedinfos: _containers.RepeatedCompositeFieldContainer[PaintedInfo]
    def __init__(self, paintedinfos: _Optional[_Iterable[_Union[PaintedInfo, _Mapping]]] = ...) -> None: ...

class BulletholeInfo(_message.Message):
    __slots__ = ("pos", "blockPos", "texname", "showtime", "dir", "secondDir", "mapid", "isBlock", "objId", "normal")
    POS_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    TEXNAME_FIELD_NUMBER: _ClassVar[int]
    SHOWTIME_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    SECONDDIR_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ISBLOCK_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    pos: _proto_common_pb2.PB_Vector3f
    blockPos: _proto_common_pb2.PB_Vector3
    texname: str
    showtime: int
    dir: int
    secondDir: int
    mapid: int
    isBlock: bool
    objId: int
    normal: _proto_common_pb2.PB_Vector3f
    def __init__(self, pos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., texname: _Optional[str] = ..., showtime: _Optional[int] = ..., dir: _Optional[int] = ..., secondDir: _Optional[int] = ..., mapid: _Optional[int] = ..., isBlock: _Optional[bool] = ..., objId: _Optional[int] = ..., normal: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class BulletEffect(_message.Message):
    __slots__ = ("particleId", "duration", "start", "dir", "worldid", "size", "range", "particleStrId")
    PARTICLEID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    PARTICLESTRID_FIELD_NUMBER: _ClassVar[int]
    particleId: int
    duration: float
    start: _proto_common_pb2.PB_Vector3f
    dir: _proto_common_pb2.PB_Vector3f
    worldid: int
    size: float
    range: float
    particleStrId: str
    def __init__(self, particleId: _Optional[int] = ..., duration: _Optional[float] = ..., start: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., dir: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., worldid: _Optional[int] = ..., size: _Optional[float] = ..., range: _Optional[float] = ..., particleStrId: _Optional[str] = ...) -> None: ...

class BulletHit(_message.Message):
    __slots__ = ("particleId", "size", "point", "yaw", "pitch", "worldid", "particleStrId")
    PARTICLEID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    PARTICLESTRID_FIELD_NUMBER: _ClassVar[int]
    particleId: int
    size: float
    point: _proto_common_pb2.PB_Vector3
    yaw: float
    pitch: float
    worldid: int
    particleStrId: str
    def __init__(self, particleId: _Optional[int] = ..., size: _Optional[float] = ..., point: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., worldid: _Optional[int] = ..., particleStrId: _Optional[str] = ...) -> None: ...

class PB_AddBulletholeInfoHC(_message.Message):
    __slots__ = ("infos", "effects", "hits")
    INFOS_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[BulletholeInfo]
    effects: _containers.RepeatedCompositeFieldContainer[BulletEffect]
    hits: _containers.RepeatedCompositeFieldContainer[BulletHit]
    def __init__(self, infos: _Optional[_Iterable[_Union[BulletholeInfo, _Mapping]]] = ..., effects: _Optional[_Iterable[_Union[BulletEffect, _Mapping]]] = ..., hits: _Optional[_Iterable[_Union[BulletHit, _Mapping]]] = ...) -> None: ...

class BulletholeInfoV2(_message.Message):
    __slots__ = ("data", "showtime", "objId", "mapid")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SHOWTIME_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[int]
    showtime: int
    objId: int
    mapid: int
    def __init__(self, data: _Optional[_Iterable[int]] = ..., showtime: _Optional[int] = ..., objId: _Optional[int] = ..., mapid: _Optional[int] = ...) -> None: ...

class BulletEffectV2(_message.Message):
    __slots__ = ("duration", "data", "worldid", "particleStrId")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    PARTICLESTRID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    data: _containers.RepeatedScalarFieldContainer[int]
    worldid: int
    particleStrId: str
    def __init__(self, duration: _Optional[int] = ..., data: _Optional[_Iterable[int]] = ..., worldid: _Optional[int] = ..., particleStrId: _Optional[str] = ...) -> None: ...

class BulletHitV2(_message.Message):
    __slots__ = ("data", "worldid", "particleStrId")
    DATA_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    PARTICLESTRID_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[int]
    worldid: int
    particleStrId: str
    def __init__(self, data: _Optional[_Iterable[int]] = ..., worldid: _Optional[int] = ..., particleStrId: _Optional[str] = ...) -> None: ...

class PB_AddBulletholeInfoV2HC(_message.Message):
    __slots__ = ("infos", "effects", "hits")
    INFOS_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[BulletholeInfoV2]
    effects: _containers.RepeatedCompositeFieldContainer[BulletEffectV2]
    hits: _containers.RepeatedCompositeFieldContainer[BulletHitV2]
    def __init__(self, infos: _Optional[_Iterable[_Union[BulletholeInfoV2, _Mapping]]] = ..., effects: _Optional[_Iterable[_Union[BulletEffectV2, _Mapping]]] = ..., hits: _Optional[_Iterable[_Union[BulletHitV2, _Mapping]]] = ...) -> None: ...

class PB_RemovePaintedInfoHC(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[_Iterable[str]] = ...) -> None: ...

class PB_TopBrandHC(_message.Message):
    __slots__ = ("targetUin", "brandName")
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    BRANDNAME_FIELD_NUMBER: _ClassVar[int]
    targetUin: int
    brandName: str
    def __init__(self, targetUin: _Optional[int] = ..., brandName: _Optional[str] = ...) -> None: ...

class PB_WeaponPointHC(_message.Message):
    __slots__ = ("targetUin", "pointType", "itemid")
    TARGETUIN_FIELD_NUMBER: _ClassVar[int]
    POINTTYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    targetUin: int
    pointType: int
    itemid: int
    def __init__(self, targetUin: _Optional[int] = ..., pointType: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...

class PB_AddLightningChainHC(_message.Message):
    __slots__ = ("targetWID", "chainID", "linkSrcWID", "chainType", "startPos")
    TARGETWID_FIELD_NUMBER: _ClassVar[int]
    CHAINID_FIELD_NUMBER: _ClassVar[int]
    LINKSRCWID_FIELD_NUMBER: _ClassVar[int]
    CHAINTYPE_FIELD_NUMBER: _ClassVar[int]
    STARTPOS_FIELD_NUMBER: _ClassVar[int]
    targetWID: int
    chainID: int
    linkSrcWID: int
    chainType: int
    startPos: _proto_common_pb2.PB_Vector3
    def __init__(self, targetWID: _Optional[int] = ..., chainID: _Optional[int] = ..., linkSrcWID: _Optional[int] = ..., chainType: _Optional[int] = ..., startPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_STARTFISHINGHC(_message.Message):
    __slots__ = ("playerID", "hookID", "targetpos")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    HOOKID_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    hookID: int
    targetpos: _proto_common_pb2.PB_Vector3
    def __init__(self, playerID: _Optional[int] = ..., hookID: _Optional[int] = ..., targetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ENDFISHINGHC(_message.Message):
    __slots__ = ("playerID", "resultID")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    RESULTID_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    resultID: int
    def __init__(self, playerID: _Optional[int] = ..., resultID: _Optional[int] = ...) -> None: ...

class PB_QUITFISHINGHC(_message.Message):
    __slots__ = ("playerID",)
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    def __init__(self, playerID: _Optional[int] = ...) -> None: ...

class PB_CHANGEFISHINGSTAGEHC(_message.Message):
    __slots__ = ("playerID", "state")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    state: int
    def __init__(self, playerID: _Optional[int] = ..., state: _Optional[int] = ...) -> None: ...

class PB_FishingBeginFlashHC(_message.Message):
    __slots__ = ("playerUin",)
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    def __init__(self, playerUin: _Optional[int] = ...) -> None: ...

class PB_PlayerVehicleMoveInputHC(_message.Message):
    __slots__ = ("vehicleID", "Accel", "Brake", "Left", "Right")
    VEHICLEID_FIELD_NUMBER: _ClassVar[int]
    ACCEL_FIELD_NUMBER: _ClassVar[int]
    BRAKE_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    vehicleID: int
    Accel: float
    Brake: float
    Left: float
    Right: float
    def __init__(self, vehicleID: _Optional[int] = ..., Accel: _Optional[float] = ..., Brake: _Optional[float] = ..., Left: _Optional[float] = ..., Right: _Optional[float] = ...) -> None: ...

class PB_BindItemToActorHC(_message.Message):
    __slots__ = ("playerID", "isBind", "bindId", "itemId", "anchorId")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    ISBIND_FIELD_NUMBER: _ClassVar[int]
    BINDID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ANCHORID_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    isBind: bool
    bindId: int
    itemId: int
    anchorId: int
    def __init__(self, playerID: _Optional[int] = ..., isBind: _Optional[bool] = ..., bindId: _Optional[int] = ..., itemId: _Optional[int] = ..., anchorId: _Optional[int] = ...) -> None: ...

class PB_ChangeShowEquipHC(_message.Message):
    __slots__ = ("playerUin", "itemId")
    PLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    playerUin: int
    itemId: int
    def __init__(self, playerUin: _Optional[int] = ..., itemId: _Optional[int] = ...) -> None: ...

class PB_GameModeChangeHC(_message.Message):
    __slots__ = ("oldGameMode", "newGameMode")
    OLDGAMEMODE_FIELD_NUMBER: _ClassVar[int]
    NEWGAMEMODE_FIELD_NUMBER: _ClassVar[int]
    oldGameMode: int
    newGameMode: int
    def __init__(self, oldGameMode: _Optional[int] = ..., newGameMode: _Optional[int] = ...) -> None: ...

class PB_PushSnowBallOperateHC(_message.Message):
    __slots__ = ("Type", "ActorID", "ExtendData", "TargetPos", "Uin")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    ExtendData: int
    TargetPos: _proto_common_pb2.PB_Vector3
    Uin: int
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., ExtendData: _Optional[int] = ..., TargetPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Uin: _Optional[int] = ...) -> None: ...

class PB_PushSnowBallSizeChangeHC(_message.Message):
    __slots__ = ("ActorID", "Size")
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ActorID: int
    Size: int
    def __init__(self, ActorID: _Optional[int] = ..., Size: _Optional[int] = ...) -> None: ...

class PB_ActorPlayAnimHC(_message.Message):
    __slots__ = ("objId", "seqId", "loop", "speed", "layer", "preSeqId", "preLayer", "crossfade")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SEQID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    PRESEQID_FIELD_NUMBER: _ClassVar[int]
    PRELAYER_FIELD_NUMBER: _ClassVar[int]
    CROSSFADE_FIELD_NUMBER: _ClassVar[int]
    objId: int
    seqId: int
    loop: int
    speed: float
    layer: int
    preSeqId: int
    preLayer: int
    crossfade: float
    def __init__(self, objId: _Optional[int] = ..., seqId: _Optional[int] = ..., loop: _Optional[int] = ..., speed: _Optional[float] = ..., layer: _Optional[int] = ..., preSeqId: _Optional[int] = ..., preLayer: _Optional[int] = ..., crossfade: _Optional[float] = ...) -> None: ...

class PB_MoveSyncHC(_message.Message):
    __slots__ = ("id", "accept", "pos", "motion")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    accept: bool
    pos: _proto_common_pb2.PB_Vector3
    motion: _proto_common_pb2.PB_Vector3f
    def __init__(self, id: _Optional[int] = ..., accept: _Optional[bool] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., motion: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ...) -> None: ...

class MoveAuthoritativeData(_message.Message):
    __slots__ = ("timestamp", "correctionKind", "pos", "acceleration", "motion", "endEuler", "movemode")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CORRECTIONKIND_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    ENDEULER_FIELD_NUMBER: _ClassVar[int]
    MOVEMODE_FIELD_NUMBER: _ClassVar[int]
    timestamp: float
    correctionKind: int
    pos: _proto_common_pb2.PB_Vector3f
    acceleration: _proto_common_pb2.PB_Vector3f
    motion: _proto_common_pb2.PB_Vector3f
    endEuler: _proto_common_pb2.PB_Vector3f
    movemode: int
    def __init__(self, timestamp: _Optional[float] = ..., correctionKind: _Optional[int] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., acceleration: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., motion: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., endEuler: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., movemode: _Optional[int] = ...) -> None: ...

class PB_ControlMoveV4HC(_message.Message):
    __slots__ = ("lastProcessedClientSeq", "authData")
    LASTPROCESSEDCLIENTSEQ_FIELD_NUMBER: _ClassVar[int]
    AUTHDATA_FIELD_NUMBER: _ClassVar[int]
    lastProcessedClientSeq: int
    authData: MoveAuthoritativeData
    def __init__(self, lastProcessedClientSeq: _Optional[int] = ..., authData: _Optional[_Union[MoveAuthoritativeData, _Mapping]] = ...) -> None: ...

class PB_MoveMoveHC(_message.Message):
    __slots__ = ("seq", "tm", "pos", "motion")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TM_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    seq: int
    tm: int
    pos: _proto_common_pb2.PB_Vector3
    motion: _proto_common_pb2.PB_Vector3
    def __init__(self, seq: _Optional[int] = ..., tm: _Optional[int] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., motion: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_MoveIntervalHC(_message.Message):
    __slots__ = ("sync_interval",)
    SYNC_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    sync_interval: int
    def __init__(self, sync_interval: _Optional[int] = ...) -> None: ...

class PB_ResetRoleFlagsHC(_message.Message):
    __slots__ = ("flags", "types")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    flags: int
    types: int
    def __init__(self, flags: _Optional[int] = ..., types: _Optional[int] = ...) -> None: ...

class PB_PlayerCanFireHC(_message.Message):
    __slots__ = ("fire",)
    FIRE_FIELD_NUMBER: _ClassVar[int]
    fire: bool
    def __init__(self, fire: _Optional[bool] = ...) -> None: ...

class PB_PlayerTransferHC(_message.Message):
    __slots__ = ("uin", "targetpos", "destMapID")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    targetpos: _proto_common_pb2.PB_Vector3
    destMapID: int
    def __init__(self, uin: _Optional[int] = ..., targetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., destMapID: _Optional[int] = ...) -> None: ...

class PB_ModBlockColorAnimHC(_message.Message):
    __slots__ = ("mapid", "targetpos", "interval", "color", "changetimes")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    TARGETPOS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CHANGETIMES_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    targetpos: _proto_common_pb2.PB_Vector3
    interval: float
    color: int
    changetimes: int
    def __init__(self, mapid: _Optional[int] = ..., targetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., interval: _Optional[float] = ..., color: _Optional[int] = ..., changetimes: _Optional[int] = ...) -> None: ...

class PB_WeatherHC(_message.Message):
    __slots__ = ("groupID", "weatherID", "isCome", "strength", "weatherTime", "duststorm", "tempest", "blizzard")
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    WEATHERID_FIELD_NUMBER: _ClassVar[int]
    ISCOME_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    WEATHERTIME_FIELD_NUMBER: _ClassVar[int]
    DUSTSTORM_FIELD_NUMBER: _ClassVar[int]
    TEMPEST_FIELD_NUMBER: _ClassVar[int]
    BLIZZARD_FIELD_NUMBER: _ClassVar[int]
    groupID: int
    weatherID: int
    isCome: bool
    strength: float
    weatherTime: int
    duststorm: PB_SandDuststormWeatherHC
    tempest: PB_TempestWeatherHC
    blizzard: PB_BlizzardWeatherHC
    def __init__(self, groupID: _Optional[int] = ..., weatherID: _Optional[int] = ..., isCome: _Optional[bool] = ..., strength: _Optional[float] = ..., weatherTime: _Optional[int] = ..., duststorm: _Optional[_Union[PB_SandDuststormWeatherHC, _Mapping]] = ..., tempest: _Optional[_Union[PB_TempestWeatherHC, _Mapping]] = ..., blizzard: _Optional[_Union[PB_BlizzardWeatherHC, _Mapping]] = ...) -> None: ...

class PB_SandDuststormWeatherHC(_message.Message):
    __slots__ = ("dir", "initPosX", "initPosZ", "movePosX", "movePosZ", "isUpEnd", "allTick")
    DIR_FIELD_NUMBER: _ClassVar[int]
    INITPOSX_FIELD_NUMBER: _ClassVar[int]
    INITPOSZ_FIELD_NUMBER: _ClassVar[int]
    MOVEPOSX_FIELD_NUMBER: _ClassVar[int]
    MOVEPOSZ_FIELD_NUMBER: _ClassVar[int]
    ISUPEND_FIELD_NUMBER: _ClassVar[int]
    ALLTICK_FIELD_NUMBER: _ClassVar[int]
    dir: int
    initPosX: int
    initPosZ: int
    movePosX: int
    movePosZ: int
    isUpEnd: bool
    allTick: int
    def __init__(self, dir: _Optional[int] = ..., initPosX: _Optional[int] = ..., initPosZ: _Optional[int] = ..., movePosX: _Optional[int] = ..., movePosZ: _Optional[int] = ..., isUpEnd: _Optional[bool] = ..., allTick: _Optional[int] = ...) -> None: ...

class PB_TempestWeatherHC(_message.Message):
    __slots__ = ("dir", "allTick")
    DIR_FIELD_NUMBER: _ClassVar[int]
    ALLTICK_FIELD_NUMBER: _ClassVar[int]
    dir: int
    allTick: int
    def __init__(self, dir: _Optional[int] = ..., allTick: _Optional[int] = ...) -> None: ...

class PB_BlizzardWeatherHC(_message.Message):
    __slots__ = ("dir", "allTick")
    DIR_FIELD_NUMBER: _ClassVar[int]
    ALLTICK_FIELD_NUMBER: _ClassVar[int]
    dir: int
    allTick: int
    def __init__(self, dir: _Optional[int] = ..., allTick: _Optional[int] = ...) -> None: ...

class TaskInitData(_message.Message):
    __slots__ = ("ObjID", "taskId", "taskState", "rewardState", "arryNum", "completeYear", "completeMonth", "completeDay")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TASKSTATE_FIELD_NUMBER: _ClassVar[int]
    REWARDSTATE_FIELD_NUMBER: _ClassVar[int]
    ARRYNUM_FIELD_NUMBER: _ClassVar[int]
    COMPLETEYEAR_FIELD_NUMBER: _ClassVar[int]
    COMPLETEMONTH_FIELD_NUMBER: _ClassVar[int]
    COMPLETEDAY_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    taskId: int
    taskState: int
    rewardState: int
    arryNum: _containers.RepeatedScalarFieldContainer[int]
    completeYear: int
    completeMonth: int
    completeDay: int
    def __init__(self, ObjID: _Optional[int] = ..., taskId: _Optional[int] = ..., taskState: _Optional[int] = ..., rewardState: _Optional[int] = ..., arryNum: _Optional[_Iterable[int]] = ..., completeYear: _Optional[int] = ..., completeMonth: _Optional[int] = ..., completeDay: _Optional[int] = ...) -> None: ...

class PB_TaskInitDataHC(_message.Message):
    __slots__ = ("iniData", "objID")
    INIDATA_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    iniData: _containers.RepeatedCompositeFieldContainer[TaskInitData]
    objID: int
    def __init__(self, iniData: _Optional[_Iterable[_Union[TaskInitData, _Mapping]]] = ..., objID: _Optional[int] = ...) -> None: ...

class PB_ByMountHC(_message.Message):
    __slots__ = ("objID", "rideID", "boneId", "rideHp", "ride", "offsetpos", "scale", "rote", "sendbone", "ablefly", "rideindex", "isRote", "triggerAdd", "ridingConditions", "usingItem")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    RIDEID_FIELD_NUMBER: _ClassVar[int]
    BONEID_FIELD_NUMBER: _ClassVar[int]
    RIDEHP_FIELD_NUMBER: _ClassVar[int]
    RIDE_FIELD_NUMBER: _ClassVar[int]
    OFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ROTE_FIELD_NUMBER: _ClassVar[int]
    SENDBONE_FIELD_NUMBER: _ClassVar[int]
    ABLEFLY_FIELD_NUMBER: _ClassVar[int]
    RIDEINDEX_FIELD_NUMBER: _ClassVar[int]
    ISROTE_FIELD_NUMBER: _ClassVar[int]
    TRIGGERADD_FIELD_NUMBER: _ClassVar[int]
    RIDINGCONDITIONS_FIELD_NUMBER: _ClassVar[int]
    USINGITEM_FIELD_NUMBER: _ClassVar[int]
    objID: int
    rideID: int
    boneId: int
    rideHp: int
    ride: int
    offsetpos: _proto_common_pb2.PB_Vector3f
    scale: _proto_common_pb2.PB_Vector3f
    rote: _proto_common_pb2.PB_Vector3f
    sendbone: bool
    ablefly: bool
    rideindex: int
    isRote: bool
    triggerAdd: bool
    ridingConditions: int
    usingItem: int
    def __init__(self, objID: _Optional[int] = ..., rideID: _Optional[int] = ..., boneId: _Optional[int] = ..., rideHp: _Optional[int] = ..., ride: _Optional[int] = ..., offsetpos: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., scale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., rote: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., sendbone: _Optional[bool] = ..., ablefly: _Optional[bool] = ..., rideindex: _Optional[int] = ..., isRote: _Optional[bool] = ..., triggerAdd: _Optional[bool] = ..., ridingConditions: _Optional[int] = ..., usingItem: _Optional[int] = ...) -> None: ...

class PB_ActorSetAttrHC(_message.Message):
    __slots__ = ("objID", "attrType", "value")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ATTRTYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objID: int
    attrType: int
    value: int
    def __init__(self, objID: _Optional[int] = ..., attrType: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class TaskObjectInitData(_message.Message):
    __slots__ = ("Objectiveid", "RewardState")
    OBJECTIVEID_FIELD_NUMBER: _ClassVar[int]
    REWARDSTATE_FIELD_NUMBER: _ClassVar[int]
    Objectiveid: int
    RewardState: int
    def __init__(self, Objectiveid: _Optional[int] = ..., RewardState: _Optional[int] = ...) -> None: ...

class PB_TaskObjectInitDataHC(_message.Message):
    __slots__ = ("Playerid", "iniData")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    INIDATA_FIELD_NUMBER: _ClassVar[int]
    Playerid: int
    iniData: _containers.RepeatedCompositeFieldContainer[TaskObjectInitData]
    def __init__(self, Playerid: _Optional[int] = ..., iniData: _Optional[_Iterable[_Union[TaskObjectInitData, _Mapping]]] = ...) -> None: ...

class PB_ActorJumpHC(_message.Message):
    __slots__ = ("objid", "state")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    objid: int
    state: bool
    def __init__(self, objid: _Optional[int] = ..., state: _Optional[bool] = ...) -> None: ...

class TechTreesTaskNode(_message.Message):
    __slots__ = ("type", "val", "arryNum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    ARRYNUM_FIELD_NUMBER: _ClassVar[int]
    type: int
    val: int
    arryNum: int
    def __init__(self, type: _Optional[int] = ..., val: _Optional[int] = ..., arryNum: _Optional[int] = ...) -> None: ...

class PB_TechTreeInfoChange_HC(_message.Message):
    __slots__ = ("taskId", "taskstate", "year", "month", "day", "node", "transitionstate")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TASKSTATE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    TRANSITIONSTATE_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    taskstate: int
    year: int
    month: int
    day: int
    node: _containers.RepeatedCompositeFieldContainer[TechTreesTaskNode]
    transitionstate: int
    def __init__(self, taskId: _Optional[int] = ..., taskstate: _Optional[int] = ..., year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ..., node: _Optional[_Iterable[_Union[TechTreesTaskNode, _Mapping]]] = ..., transitionstate: _Optional[int] = ...) -> None: ...

class PB_SetGravityFailure_HC(_message.Message):
    __slots__ = ("objid", "state")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    objid: int
    state: bool
    def __init__(self, objid: _Optional[int] = ..., state: _Optional[bool] = ...) -> None: ...

class KineticNode(_message.Message):
    __slots__ = ("speed", "Pos", "Children")
    SPEED_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    speed: int
    Pos: _proto_common_pb2.PB_Vector3
    Children: _containers.RepeatedCompositeFieldContainer[KineticNode]
    def __init__(self, speed: _Optional[int] = ..., Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., Children: _Optional[_Iterable[_Union[KineticNode, _Mapping]]] = ...) -> None: ...

class PB_MechaKineticUint_HC(_message.Message):
    __slots__ = ("SourcePos", "KineticNode", "objid")
    SOURCEPOS_FIELD_NUMBER: _ClassVar[int]
    KINETICNODE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SourcePos: _containers.RepeatedCompositeFieldContainer[_proto_common_pb2.PB_Vector3]
    KineticNode: _containers.RepeatedCompositeFieldContainer[KineticNode]
    objid: int
    def __init__(self, SourcePos: _Optional[_Iterable[_Union[_proto_common_pb2.PB_Vector3, _Mapping]]] = ..., KineticNode: _Optional[_Iterable[_Union[KineticNode, _Mapping]]] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_SetInteractActorMecha_HC(_message.Message):
    __slots__ = ("objid",)
    OBJID_FIELD_NUMBER: _ClassVar[int]
    objid: int
    def __init__(self, objid: _Optional[int] = ...) -> None: ...

class PB_UnlockItems_HC(_message.Message):
    __slots__ = ("UnlockItems",)
    UNLOCKITEMS_FIELD_NUMBER: _ClassVar[int]
    UnlockItems: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, UnlockItems: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_PlayCameraShake_HC(_message.Message):
    __slots__ = ("shaking", "power", "duration")
    SHAKING_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    shaking: bool
    power: int
    duration: int
    def __init__(self, shaking: _Optional[bool] = ..., power: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class PB_MechaFuelEngineLogicData_HC(_message.Message):
    __slots__ = ("Pos", "outputSpeed", "outputTPES", "engineCurFC", "isWorking", "isOverHeat", "objid")
    POS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTSPEED_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTPES_FIELD_NUMBER: _ClassVar[int]
    ENGINECURFC_FIELD_NUMBER: _ClassVar[int]
    ISWORKING_FIELD_NUMBER: _ClassVar[int]
    ISOVERHEAT_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    outputSpeed: int
    outputTPES: float
    engineCurFC: float
    isWorking: int
    isOverHeat: int
    objid: int
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., outputSpeed: _Optional[int] = ..., outputTPES: _Optional[float] = ..., engineCurFC: _Optional[float] = ..., isWorking: _Optional[int] = ..., isOverHeat: _Optional[int] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_AddMechaFuelEngineLogic_HC(_message.Message):
    __slots__ = ("Pos", "blockId", "dir", "outputSpeed", "outputTPES", "engineCurFC", "isWorking", "isOverHeat", "objid")
    POS_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    OUTPUTSPEED_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTPES_FIELD_NUMBER: _ClassVar[int]
    ENGINECURFC_FIELD_NUMBER: _ClassVar[int]
    ISWORKING_FIELD_NUMBER: _ClassVar[int]
    ISOVERHEAT_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    Pos: _proto_common_pb2.PB_Vector3
    blockId: int
    dir: int
    outputSpeed: int
    outputTPES: float
    engineCurFC: float
    isWorking: bool
    isOverHeat: bool
    objid: int
    def __init__(self, Pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., blockId: _Optional[int] = ..., dir: _Optional[int] = ..., outputSpeed: _Optional[int] = ..., outputTPES: _Optional[float] = ..., engineCurFC: _Optional[float] = ..., isWorking: _Optional[bool] = ..., isOverHeat: _Optional[bool] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_KineticNodeData_HC(_message.Message):
    __slots__ = ("state", "speed", "Pos", "ParentPos", "SourcePos", "objid")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    PARENTPOS_FIELD_NUMBER: _ClassVar[int]
    SOURCEPOS_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    state: bool
    speed: int
    Pos: _containers.RepeatedScalarFieldContainer[int]
    ParentPos: _containers.RepeatedScalarFieldContainer[int]
    SourcePos: _containers.RepeatedScalarFieldContainer[int]
    objid: int
    def __init__(self, state: _Optional[bool] = ..., speed: _Optional[int] = ..., Pos: _Optional[_Iterable[int]] = ..., ParentPos: _Optional[_Iterable[int]] = ..., SourcePos: _Optional[_Iterable[int]] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_ContainerUIData_HC(_message.Message):
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

class PB_MechaRecoveryHeadHC(_message.Message):
    __slots__ = ("objid", "headpos")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HEADPOS_FIELD_NUMBER: _ClassVar[int]
    objid: int
    headpos: _proto_common_pb2.PB_Vector3
    def __init__(self, objid: _Optional[int] = ..., headpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_MechaTunnelAnimPlay_HC(_message.Message):
    __slots__ = ("mapid", "blockpos", "dir", "animID")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    blockpos: _proto_common_pb2.PB_Vector3
    dir: int
    animID: int
    def __init__(self, mapid: _Optional[int] = ..., blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., dir: _Optional[int] = ..., animID: _Optional[int] = ...) -> None: ...

class PB_MechaStructureSyncHC(_message.Message):
    __slots__ = ("mechaDataBlob", "unzipLen")
    MECHADATABLOB_FIELD_NUMBER: _ClassVar[int]
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    mechaDataBlob: bytes
    unzipLen: int
    def __init__(self, mechaDataBlob: _Optional[bytes] = ..., unzipLen: _Optional[int] = ...) -> None: ...

class PB_MechaStructureOperateCH(_message.Message):
    __slots__ = ("nodeA", "nodeB", "operation")
    NODEA_FIELD_NUMBER: _ClassVar[int]
    NODEB_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    nodeA: _proto_common_pb2.PB_Vector3
    nodeB: _proto_common_pb2.PB_Vector3
    operation: int
    def __init__(self, nodeA: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., nodeB: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., operation: _Optional[int] = ...) -> None: ...

class PB_MechaStructureOperateHC(_message.Message):
    __slots__ = ("nodeA", "nodeB", "success", "operation")
    NODEA_FIELD_NUMBER: _ClassVar[int]
    NODEB_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    nodeA: _proto_common_pb2.PB_Vector3
    nodeB: _proto_common_pb2.PB_Vector3
    success: bool
    operation: int
    def __init__(self, nodeA: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., nodeB: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., success: _Optional[bool] = ..., operation: _Optional[int] = ...) -> None: ...

class PB_TransferGoodsComp_HC(_message.Message):
    __slots__ = ("mapid", "itemobjid", "position", "speed", "showBaffle")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ITEMOBJID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    SHOWBAFFLE_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    itemobjid: int
    position: _containers.RepeatedScalarFieldContainer[int]
    speed: int
    showBaffle: bool
    def __init__(self, mapid: _Optional[int] = ..., itemobjid: _Optional[int] = ..., position: _Optional[_Iterable[int]] = ..., speed: _Optional[int] = ..., showBaffle: _Optional[bool] = ...) -> None: ...

class PB_EnterLivingwheelHC(_message.Message):
    __slots__ = ("uin", "playerPos", "mapid", "blockPos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    PLAYERPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    playerPos: _proto_common_pb2.PB_Vector3
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, uin: _Optional[int] = ..., playerPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_LeaveLivingwheelHC(_message.Message):
    __slots__ = ("uin", "mapid", "blockPos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    def __init__(self, uin: _Optional[int] = ..., mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_UpdateLivingwheelHC(_message.Message):
    __slots__ = ("mapid", "blockPos", "type", "objid", "work", "clockwise")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    WORK_FIELD_NUMBER: _ClassVar[int]
    CLOCKWISE_FIELD_NUMBER: _ClassVar[int]
    mapid: int
    blockPos: _proto_common_pb2.PB_Vector3
    type: int
    objid: int
    work: bool
    clockwise: bool
    def __init__(self, mapid: _Optional[int] = ..., blockPos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., type: _Optional[int] = ..., objid: _Optional[int] = ..., work: _Optional[bool] = ..., clockwise: _Optional[bool] = ...) -> None: ...

class PB_IronHC(_message.Message):
    __slots__ = ("objid", "host")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    objid: int
    host: int
    def __init__(self, objid: _Optional[int] = ..., host: _Optional[int] = ...) -> None: ...

class PB_IronDomeEssenceEquip_HC(_message.Message):
    __slots__ = ("obj", "state", "type", "hp")
    OBJ_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    obj: int
    state: int
    type: int
    hp: float
    def __init__(self, obj: _Optional[int] = ..., state: _Optional[int] = ..., type: _Optional[int] = ..., hp: _Optional[float] = ...) -> None: ...

class PB_Part_HC(_message.Message):
    __slots__ = ("obj",)
    OBJ_FIELD_NUMBER: _ClassVar[int]
    obj: int
    def __init__(self, obj: _Optional[int] = ...) -> None: ...

class PB_PartManager_HC(_message.Message):
    __slots__ = ("obj", "partid", "state")
    OBJ_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    obj: int
    partid: int
    state: int
    def __init__(self, obj: _Optional[int] = ..., partid: _Optional[int] = ..., state: _Optional[int] = ...) -> None: ...

class BlockTextureColor(_message.Message):
    __slots__ = ("blockid", "color", "slot")
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    blockid: int
    color: int
    slot: int
    def __init__(self, blockid: _Optional[int] = ..., color: _Optional[int] = ..., slot: _Optional[int] = ...) -> None: ...

class PB_BlockTextureColors_HC(_message.Message):
    __slots__ = ("blockcolor",)
    BLOCKCOLOR_FIELD_NUMBER: _ClassVar[int]
    blockcolor: _containers.RepeatedCompositeFieldContainer[BlockTextureColor]
    def __init__(self, blockcolor: _Optional[_Iterable[_Union[BlockTextureColor, _Mapping]]] = ...) -> None: ...

class PB_ModContainer_ModelPart(_message.Message):
    __slots__ = ("optype", "part", "anchor", "model", "pos", "rot", "scale", "meshstate")
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    MESHSTATE_FIELD_NUMBER: _ClassVar[int]
    optype: _proto_common_pb2.ePBModContainerModelPartOp
    part: str
    anchor: str
    model: str
    pos: _proto_common_pb2.PB_Vector3
    rot: _proto_common_pb2.PB_Vector3
    scale: _proto_common_pb2.PB_Vector3f
    meshstate: int
    def __init__(self, optype: _Optional[_Union[_proto_common_pb2.ePBModContainerModelPartOp, str]] = ..., part: _Optional[str] = ..., anchor: _Optional[str] = ..., model: _Optional[str] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., rot: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., scale: _Optional[_Union[_proto_common_pb2.PB_Vector3f, _Mapping]] = ..., meshstate: _Optional[int] = ...) -> None: ...

class PB_ModContainer_HC(_message.Message):
    __slots__ = ("blockpos", "mapid", "optype", "modelpart")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    MODELPART_FIELD_NUMBER: _ClassVar[int]
    blockpos: _proto_common_pb2.PB_Vector3
    mapid: int
    optype: _proto_common_pb2.ePBModContainerOp
    modelpart: PB_ModContainer_ModelPart
    def __init__(self, blockpos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., mapid: _Optional[int] = ..., optype: _Optional[_Union[_proto_common_pb2.ePBModContainerOp, str]] = ..., modelpart: _Optional[_Union[PB_ModContainer_ModelPart, _Mapping]] = ...) -> None: ...

class PB_PlayerGunActionStateHC(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: int
    def __init__(self, state: _Optional[int] = ...) -> None: ...

class PB_LookAtActorHC(_message.Message):
    __slots__ = ("obj", "targetobj")
    OBJ_FIELD_NUMBER: _ClassVar[int]
    TARGETOBJ_FIELD_NUMBER: _ClassVar[int]
    obj: int
    targetobj: int
    def __init__(self, obj: _Optional[int] = ..., targetobj: _Optional[int] = ...) -> None: ...

class PB_UpdateLaserPointerHC(_message.Message):
    __slots__ = ("enable", "pos", "uin")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    pos: _proto_common_pb2.PB_Vector3
    uin: int
    def __init__(self, enable: _Optional[bool] = ..., pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., uin: _Optional[int] = ...) -> None: ...

class PB_UpdateNewTameDataHC(_message.Message):
    __slots__ = ("targetId", "ownerUin", "follow")
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    OWNERUIN_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_FIELD_NUMBER: _ClassVar[int]
    targetId: int
    ownerUin: int
    follow: bool
    def __init__(self, targetId: _Optional[int] = ..., ownerUin: _Optional[int] = ..., follow: _Optional[bool] = ...) -> None: ...

class PB_UpdateReproductionDataHC(_message.Message):
    __slots__ = ("objId", "isForbidden", "state")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ISFORBIDDEN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    objId: int
    isForbidden: bool
    state: int
    def __init__(self, objId: _Optional[int] = ..., isForbidden: _Optional[bool] = ..., state: _Optional[int] = ...) -> None: ...

class PB_UpdateNewGrowDataHC(_message.Message):
    __slots__ = ("targetId", "state")
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    targetId: int
    state: int
    def __init__(self, targetId: _Optional[int] = ..., state: _Optional[int] = ...) -> None: ...

class PB_AI_TTS_AUDIO_HC_MSG(_message.Message):
    __slots__ = ("agent_id", "agent_name", "text_content", "audio_data")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
    agent_id: int
    agent_name: str
    text_content: str
    audio_data: bytes
    def __init__(self, agent_id: _Optional[int] = ..., agent_name: _Optional[str] = ..., text_content: _Optional[str] = ..., audio_data: _Optional[bytes] = ...) -> None: ...

class PB_FileData(_message.Message):
    __slots__ = ("page", "totalPage", "seq", "data")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTALPAGE_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    page: int
    totalPage: int
    seq: int
    data: str
    def __init__(self, page: _Optional[int] = ..., totalPage: _Optional[int] = ..., seq: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class PB_PlayerTouchEvtTargetGroup(_message.Message):
    __slots__ = ("objType", "ids")
    OBJTYPE_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    objType: int
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, objType: _Optional[int] = ..., ids: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_PlayerTouchEvtInfoPB(_message.Message):
    __slots__ = ("eventFuncId", "targets")
    EVENTFUNCID_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    eventFuncId: int
    targets: _containers.RepeatedCompositeFieldContainer[PB_PlayerTouchEvtTargetGroup]
    def __init__(self, eventFuncId: _Optional[int] = ..., targets: _Optional[_Iterable[_Union[PB_PlayerTouchEvtTargetGroup, _Mapping]]] = ...) -> None: ...

class PB_PlayerTouchEvtSyncHC(_message.Message):
    __slots__ = ("uin", "evts")
    UIN_FIELD_NUMBER: _ClassVar[int]
    EVTS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    evts: _containers.RepeatedCompositeFieldContainer[PB_PlayerTouchEvtInfoPB]
    def __init__(self, uin: _Optional[int] = ..., evts: _Optional[_Iterable[_Union[PB_PlayerTouchEvtInfoPB, _Mapping]]] = ...) -> None: ...

class PB_VecPlayerAllTouchEvtSyncHCs(_message.Message):
    __slots__ = ("playerAllEvts",)
    PLAYERALLEVTS_FIELD_NUMBER: _ClassVar[int]
    playerAllEvts: _containers.RepeatedCompositeFieldContainer[PB_PlayerTouchEvtSyncHC]
    def __init__(self, playerAllEvts: _Optional[_Iterable[_Union[PB_PlayerTouchEvtSyncHC, _Mapping]]] = ...) -> None: ...

class PB_WBPMsgHC(_message.Message):
    __slots__ = ("msgid", "regionmsg", "syncgridsmsg", "autoplacestatemsg")
    MSGID_FIELD_NUMBER: _ClassVar[int]
    REGIONMSG_FIELD_NUMBER: _ClassVar[int]
    SYNCGRIDSMSG_FIELD_NUMBER: _ClassVar[int]
    AUTOPLACESTATEMSG_FIELD_NUMBER: _ClassVar[int]
    msgid: int
    regionmsg: _proto_common_pb2.PB_WBPRegionMsg
    syncgridsmsg: _proto_common_pb2.PB_WBPSyncGridsMsg
    autoplacestatemsg: _proto_common_pb2.PB_WBPAutoPlaceStateMsg
    def __init__(self, msgid: _Optional[int] = ..., regionmsg: _Optional[_Union[_proto_common_pb2.PB_WBPRegionMsg, _Mapping]] = ..., syncgridsmsg: _Optional[_Union[_proto_common_pb2.PB_WBPSyncGridsMsg, _Mapping]] = ..., autoplacestatemsg: _Optional[_Union[_proto_common_pb2.PB_WBPAutoPlaceStateMsg, _Mapping]] = ...) -> None: ...

class PB_SleepMsgHC(_message.Message):
    __slots__ = ("objId", "sleep", "currentAnim")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    SLEEP_FIELD_NUMBER: _ClassVar[int]
    CURRENTANIM_FIELD_NUMBER: _ClassVar[int]
    objId: int
    sleep: bool
    currentAnim: int
    def __init__(self, objId: _Optional[int] = ..., sleep: _Optional[bool] = ..., currentAnim: _Optional[int] = ...) -> None: ...

class PB_DropItemStateData_HC(_message.Message):
    __slots__ = ("iTimedDropTime", "iTimedDropTickCount", "iInteractionDropTime", "iInteractionDropTickCount", "iInteractionDropCounter", "bNeedCheckRecover", "itemsList", "bInteractionDropLock", "fInteractionTime", "mobID", "playerID", "iconName", "touchState")
    ITIMEDDROPTIME_FIELD_NUMBER: _ClassVar[int]
    ITIMEDDROPTICKCOUNT_FIELD_NUMBER: _ClassVar[int]
    IINTERACTIONDROPTIME_FIELD_NUMBER: _ClassVar[int]
    IINTERACTIONDROPTICKCOUNT_FIELD_NUMBER: _ClassVar[int]
    IINTERACTIONDROPCOUNTER_FIELD_NUMBER: _ClassVar[int]
    BNEEDCHECKRECOVER_FIELD_NUMBER: _ClassVar[int]
    ITEMSLIST_FIELD_NUMBER: _ClassVar[int]
    BINTERACTIONDROPLOCK_FIELD_NUMBER: _ClassVar[int]
    FINTERACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    MOBID_FIELD_NUMBER: _ClassVar[int]
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    ICONNAME_FIELD_NUMBER: _ClassVar[int]
    TOUCHSTATE_FIELD_NUMBER: _ClassVar[int]
    iTimedDropTime: int
    iTimedDropTickCount: int
    iInteractionDropTime: int
    iInteractionDropTickCount: int
    iInteractionDropCounter: int
    bNeedCheckRecover: bool
    itemsList: _containers.RepeatedScalarFieldContainer[int]
    bInteractionDropLock: bool
    fInteractionTime: float
    mobID: int
    playerID: int
    iconName: str
    touchState: int
    def __init__(self, iTimedDropTime: _Optional[int] = ..., iTimedDropTickCount: _Optional[int] = ..., iInteractionDropTime: _Optional[int] = ..., iInteractionDropTickCount: _Optional[int] = ..., iInteractionDropCounter: _Optional[int] = ..., bNeedCheckRecover: _Optional[bool] = ..., itemsList: _Optional[_Iterable[int]] = ..., bInteractionDropLock: _Optional[bool] = ..., fInteractionTime: _Optional[float] = ..., mobID: _Optional[int] = ..., playerID: _Optional[int] = ..., iconName: _Optional[str] = ..., touchState: _Optional[int] = ...) -> None: ...

class PB_PlayerPlayHandAnim_HC(_message.Message):
    __slots__ = ("uin", "animId")
    UIN_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    uin: int
    animId: int
    def __init__(self, uin: _Optional[int] = ..., animId: _Optional[int] = ...) -> None: ...

class PB_PlayerPlayDigBlockEffect_HC(_message.Message):
    __slots__ = ("uin", "blockId", "x", "y", "z")
    UIN_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    uin: int
    blockId: int
    x: int
    y: int
    z: int
    def __init__(self, uin: _Optional[int] = ..., blockId: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class PB_LivingTimedXrayEffect_HC(_message.Message):
    __slots__ = ("objid", "duration")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    objid: _containers.RepeatedScalarFieldContainer[int]
    duration: int
    def __init__(self, objid: _Optional[_Iterable[int]] = ..., duration: _Optional[int] = ...) -> None: ...

class PB_MineralProspectBlockInfo(_message.Message):
    __slots__ = ("pos", "blockId")
    POS_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    pos: _proto_common_pb2.PB_Vector3
    blockId: int
    def __init__(self, pos: _Optional[_Union[_proto_common_pb2.PB_Vector3, _Mapping]] = ..., blockId: _Optional[int] = ...) -> None: ...

class PB_MineralProspectBlock_HC(_message.Message):
    __slots__ = ("blockInfos", "duration", "radius")
    BLOCKINFOS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    blockInfos: _containers.RepeatedCompositeFieldContainer[PB_MineralProspectBlockInfo]
    duration: int
    radius: int
    def __init__(self, blockInfos: _Optional[_Iterable[_Union[PB_MineralProspectBlockInfo, _Mapping]]] = ..., duration: _Optional[int] = ..., radius: _Optional[int] = ...) -> None: ...
