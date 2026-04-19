#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动解析 PCAP 文件中 RakNet 协议内的 Protobuf 数据。

用法：
    python raknet_proto_parser.py -p capture.pcap -d proto_dir/

依赖：
    - Python 3.6+
    - protobuf 库: pip install protobuf
    - tshark (Wireshark) 或 scapy (备用): pip install scapy
    - protoc (Protobuf 编译器) 用于动态编译 .proto 文件
"""

from loguru import logger

import argparse
import sys
import subprocess
import tempfile
import importlib.util
import struct
import json
import re
import blackboxprotobuf
from pathlib import Path

ignored_msg_code = [6501, 4047, 11]

msg_code_to_name = {
    11: "PB_HeartBeatCH",
    12: "PB_HeartBeatHC",
    101: "PB_SyncChunkDataCH",
    102: "PB_SyncChunkDataHC",
    103: "PB_BlockUpdateCH",  # PB_BLOCK_DATA_UPDATE_CH
    104: "PB_BlockUpdateHC",  # PB_BLOCK_DATA_UPDATE_HC
    105: "PB_SyncSectionLightDataHC",
    106: "PB_OverrideLightDataHC",
    1001: "PB_RoleEnterWorldCH",
    1002: "PB_RoleEnterWorldHC",
    1003: "PB_RoleLeaveWorldCH",
    1004: "PB_RoleLeaveWorldHC",
    1006: "PB_ActorEnterAOIHC",
    1008: "PB_ActorLeaveAOIHC",
    1010: "PB_GameLeaderSwitchHC",
    1011: "PB_GeneralEnterAOIHC",
    1012: "PB_PvpActivityConfigCH",
    1013: "PB_RoleCheckJoinFromSrcCH",
    2001: "PB_RoleMoveCH",
    2002: "PB_TrainMoveCH",
    2004: "PB_ActorMoveHC",
    2005: "PB_TrainMoveHC",
    2006: "PB_ActorMoveV2HC",
    2007: "PB_ActorTeleportCH",
    2008: "PB_ActorTeleportHC",
    2009: "PB_ActorMotionHC",
    2010: "PB_MechaMotionHC",
    2011: "PB_GunInfoCH",
    2012: "PB_SetInfoCH",
    2013: "PB_SyncGridUserDataCH",  # PB_SYNC_GRIDUSERDATA_CH
    2014: "PB_SyncGridUserDataHC",  # PB_SYNC_GRIDUSERDATA_HC
    2015: "PB_SyncTriggerBlockHC",
    2016: "PB_FullrotActorMoveHC",
    2017: "PB_ActorMotionV2HC",
    2018: "PB_ActorMoveV3HC",
    2019: "PB_ActorModelChangeHC",
    2997: "PB_BlockInteractHC",
    2998: "PB_BlockPunchHC",
    2999: "PB_ItemUseHC",
    3000: "PB_ActorInteractHC",
    3001: "PB_BlockInteractEndCH",
    3002: "PB_BlockInteractCH",
    3003: "PB_BlockPunchCH",
    3004: "PB_ItemUseCH",
    3005: "PB_ActorInteractCH",
    3006: "PB_ActorAnimCH",
    3007: "PB_ActorAnimHC",
    3008: "PB_BackPackGridUpdateHC",
    3009: "PB_BackPackGridSwapCH",
    3010: "PB_BackPackMoveItemCH",
    3011: "PB_BackPackGridDiscardCH",
    3015: "PB_BackPackEquipWeaponCH",
    3016: "PB_BackPackEquipWeaponHC",
    3017: "PB_CloseContainerCH",
    3018: "PB_CloseContainerHC",
    3020: "PB_OpenContainerHC",
    3022: "PB_UpdateContainerHC",
    3023: "PB_SetContainerTextCH",
    3026: "PB_ActorEquipItemHC",
    3029: "PB_BackPackStoreCH",
    3031: "PB_BackPackLootCH",
    3033: "PB_BackPackSortCH",
    3034: "PB_BackPackSetItemCH",
    3035: "PB_StorageBoxSortCH",
    3036: "PB_BackPackShortcutOpCH",
    3037: "PB_CraftItemCH",
    3039: "PB_EnchantItemCH",
    3041: "PB_EnchantItemRandomCH",
    3042: "PB_EnchantItemSuccessHC",
    3043: "PB_RepairItemCH",
    3044: "PB_RepairItemSuccessHC",
    3045: "PB_GunDoReloadCH",
    3046: "PB_GunDoReloadHC",
    3047: "PB_GunRecoveryCH",
    3050: "PB_AccountHorseCH",
    3051: "PB_AccountHorseHC",
    3052: "PB_ActorSetCustomCH",  # PB_ACTOT_SET_CUSTOM_CH
    3053: "PB_ActorSetCustomHC",  # PB_ACTOT_SET_CUSTOM_HC
    3054: "PB_ActorPlayAnimCH",
    3055: "PB_ActorPlayAnimHC",
    3056: "PB_ActorAttackCH",
    3057: "PB_ActorDefanceStateCH",
    3058: "PB_RClickUpInteractCH",
    3059: "PB_RClickUpInteractHC",
    3060: "PB_PCMouseEventCH",
    3061: "PB_PlayerGunActionCH",
    3062: "PB_PlayerGunActionStateHC",
    3063: "PB_LivingInteractNewCH",
    3064: "PB_LivingInteractNewNewTameHC",  # PB_LIVING_INTERACT_NEW_NEWTAME_HC
    3065: "PB_LivingReproductionHC",  # PB_LIVING_REPRODUCTION_HC
    3066: "PB_LivingInteractNewNewGrowHC",  # PB_LIVING_INTERACT_NEW_NEWGROW_HC
    3067: "PB_TrainFollowOpCH",
    3068: "PB_TrainFollowOpHC",
    4000: "PB_ActorAttrChangeHC",
    4001: "PB_ActorBuffChangeHC",
    4002: "PB_ActorReviveCH",
    4003: "PB_ActorReviveHC",
    4004: "PB_PlayerAttrChangeHC",
    4005: "PB_MobBodyChangeHC",
    4006: "PB_JruisdicTionCH",
    4007: "PB_JruisdicTionHC",
    4010: "PB_ChatCH",
    4011: "PB_ChatHC",
    4012: "PB_WGlobalUpdateHC",
    4013: "PB_PlayersUpdateInfoHC",
    4014: "PB_GameTipsHC",
    4015: "PB_PlayEffectHC",
    4016: "PB_PlayerMountActorCH",
    4017: "PB_PlayerMountActorHC",
    4018: "PB_PlayerMoveInputCH",
    4019: "PB_PlayerRevivePointCH",
    4020: "PB_PlayerSleepHC",
    4021: "PB_PlayerSleepCH",
    4022: "PB_OpenWindowHC",
    4023: "PB_NpcTradeCH",
    4024: "PB_LastPingHC",
    4025: "PB_CGameStageHC",
    4026: "PB_PlayerPermitHC",
    4027: "PB_PlayerRevivePointHC",
    4028: "PB_PlayEffectHC_V2",
    4029: "PB_SkillCDHC",
    4030: "PB_ActorMountActorHC",
    4031: "PB_ActorReverseHC",
    4032: "PB_ActorBindHC",
    4033: "PB_PlayWeaponEffectHC",
    4034: "PB_ScriptVarHC",
    4035: "PB_PlayWeaponEffectCH",
    4037: "PB_SetSpectatorModeCH",
    4038: "PB_SetSpectatorModeHC",
    4039: "PB_SetSpectatorTypeCH",
    4040: "PB_SetSpectatorTypeHC",
    4041: "PB_SetSpectatorPlayerCH",
    4042: "PB_OtherPlayerAttrChangeHC",  # PB_OTHER_PLAYER_ATTR_CHANGE_HC
    4043: "PB_PlayerLeaveHC",
    4044: "PB_TeamScoreHC",
    4045: "PB_SetTeamHC",  # PB_SET_TEAM_HC
    4046: "PB_SetPlayerGameInfoHC",
    4047: "PB_MoveSyncCH",
    4048: "PB_MoveSyncHC",
    4049: "PB_UIDisplayHorseHC",
    4050: "PB_SyncMoveV2CH",
    4051: "PB_SyncMoveV2HC",
    4052: "PB_UpdateMoveIntervalHC",  # PB_UPDATE_MOVE_INTERVAL_HC
    4053: "PB_MoveDiffCH",  # PB_MOVE_DIFF_CH
    4054: "PB_PlayEffectHC_V3",
    4055: "PB_SyncMoveV4CH",
    4056: "PB_SyncMoveV4HC",
    5001: "PB_ActorGetAccountItem",  # PB_ACTOR_GET_ACCOUNT_ITEM
    5002: "PB_SpecialItemUseCH",
    5003: "PB_SpecialItemUseHC",
    5004: "PB_LeaveRoomInfoHC",
    5005: "PB_InviteJoinRoomHC",
    5006: "PB_SetSpectatorPlayerHC",
    5007: "PB_SetPlayerModelAniCH",
    5008: "PB_SetPlayerModelAniHC",
    5009: "PB_SendViewmodeSpectatorCH",  # PB_SEND_VIEWMODE_SPECTATOR_CH
    5010: "PB_SendViewmodeSpectatorHC",  # PB_SEND_VIEWMODE_SPECTATOR_HC
    5011: "PB_SetBobbingSpectatorCH",  # PB_SET_BOBBING_SPECTATOR_CH
    5012: "PB_SetBobbingSpectatorHC",  # PB_SET_BOBBING_SPECTATOR_HC
    5013: "PB_ItemSkillUseCH",
    5014: "PB_ItemSkillUseHC",
    5015: "PB_BallOperateCH",
    5016: "PB_BallOperateHC",
    5017: "PB_ResetRoundHC",
    5018: "PB_RocketAttribChangeHC",
    5019: "PB_RocketTeleportCH",
    5020: "PB_SetHookHC",
    5021: "PB_SetHookCH",
    5022: "PB_WorldTimesHC",
    5023: "PB_StatisticHC",
    5024: "PB_TotemPointHC",
    5025: "PB_NeedContainerPasswordHC",
    5026: "PB_NeedContainerPasswordCH",
    5027: "PB_HorseFlyStateHC",
    5028: "PB_OpenDialogueHC",
    5029: "PB_CloseDialogueHC",
    5030: "PB_CloseDialogueCH",
    5031: "PB_AnswerTaskCH",
    5032: "PB_UpdateTaskHC",  # PB_UPDATETASK_HC
    5033: "PB_SyncTaskEnterWorldHC",
    5034: "PB_CompleteTaskHC",
    5035: "PB_CompleteTaskCH",
    5036: "PB_AttractAttribChangeHC",
    5037: "PB_ActorBodyTextureHC",
    5038: "PB_PlayerAddAvartarHC",
    5039: "PB_PlayerChangeModelHC",
    5040: "PB_PlayerAvartarColorHC",
    5041: "PB_PlayActCH",
    5042: "PB_PlayActHC",
    5043: "PB_CreateBlueprintHC",
    5044: "PB_MeasureDistanceHC",
    5045: "PB_BluePrintPreBlockCH",
    5046: "PB_BluePrintPreBlockHC",
    5047: "PB_GravityOperateCH",
    5048: "PB_GravityOperateHC",
    5049: "PB_PlayerBodyColorHC",
    5050: "PB_CustomModelHC",
    5051: "PB_CustomItemIDsHC",
    5052: "PB_PlayerSpawnPointHC",
    5053: "PB_MakeCustomModelCH",
    5054: "PB_SelectMobSpawnerCH",
    5055: "PB_CustomModelClassHC",
    5056: "PB_TransferRecordHC",
    5057: "PB_TransferRecordCH",
    5058: "PB_TransferAddDelHC",
    5059: "PB_TransferStatusCH",  # PB_TRANSFER_STATUS_CH
    5060: "PB_TransferStatusHC",  # PB_TRANSFER_STATUS_HC
    5061: "PB_SyncLoveAmbassadorIconIdHC",  # PB_SYNC_LOVEAMBASSADOR_ICONID_HC
    5062: "PB_SyncLoveAmbassadorIconIdCH",  # PB_SYNC_LOVEAMBASSADOR_ICONID_CH
    5063: "PB_TransferDataHC",
    5064: "PB_ActorTransferCH",
    5065: "PB_ActorTransferHC",
    5066: "PB_BackPackSetItemWithoutLimitCH",
    5067: "PB_GetNpcShopInfoCH",
    5068: "PB_RespNpcShopInfoHC",
    5069: "PB_BuyNpcShopItemCH",
    5070: "PB_NotifyNpcShopBuySkuHC",
    5071: "PB_VehicleMoveHC",
    5072: "PB_OpenEditActorModelHC",
    5073: "PB_CloseEditActorModelCH",
    5074: "PB_CloseEditActorModelHC",
    5075: "PB_CustomActorModelDataHC",
    5076: "PB_PackGiftNotifyItemChgHC",
    5077: "PB_VehiclePreBlockCH",
    5078: "PB_VehiclePreBlockHC",
    5079: "PB_VehicleItemUseCH",
    5080: "PB_VehicleStartBlockCH",
    5081: "PB_VehicleAllItemIdHC",  # PB_VEHICLE_ALL_ITEMID_HC
    5082: "PB_VehicleOneItemIdHC",  # PB_VEHICLE_ONE_ITEMID_HC
    5083: "PB_VehicleAttribChangeHC",
    5084: "PB_VehicleAttribChangeCH",
    5085: "PB_WorkshopItemInfoCH",
    5086: "PB_WorkshopItemInfoHC",
    5087: "PB_VehicleAssembleBlockUpdateHC",
    5088: "PB_PlayerVehicleMoveInputCH",
    5089: "PB_PlayerResetVehicleCH",
    5090: "PB_PlayerMotionStateChangeCH",
    5091: "PB_PlayerClickCH",
    5092: "PB_PlayerCameraRotateHC",
    5093: "PB_PlayerChangeViewModeHC",
    5094: "PB_PlayerCanMoveHC",
    5095: "PB_PlayerCanControlHC",
    5096: "PB_PlayerSetAttrHC",
    5097: "PB_PlayerFreezingHC",
    5098: "PB_PlayerSelectShortcutCH",
    5099: "PB_GameRuleHC",
    5100: "PB_BasketballOperateHC",  # PB_BASKETBALL_OPERATE_HC
    5101: "PB_BasketballOperateCH",  # PB_BASKETBALL_OPERATE_CH
    5102: "PB_PlayerVehicleMoveInputHC",
    5103: "PB_PlayerCanFireHC",
    5104: "PB_PlayerTouchEvtSyncHC",
    5105: "PB_PlayerTouchEvtCH",
    5200: "PB_BuyAdShopGoods",
    5201: "PB_BuyAdShopGoodsHC",  # PB_BUY_AD_SHOP_GOOD_HC
    5202: "PB_SyncPlayerPosHC",  # PB_SYNC_PLAYER_POS_HC
    5203: "PB_AchievementAwardCH",  # PB_ACHIEVEMENT_AWARD_CH
    5204: "PB_SyncClientActionLogCH",
    5205: "PB_SyncRoomExtraHC",  # PB_SYNC_ROOM_EXTRA_HC
    5206: "PB_UploadCheckInfoCH",
    5207: "PB_GetAdShopExtraAwardCH",
    5208: "PB_ExtractStoreItemCH",
    5209: "PB_UploadClientInfoCH",
    5210: "PB_SyncPlayerPosCH",  # PB_SYNC_PLAYER_POS_CH
    6000: "PB_TriggerTimerHC",  # PB_TRIGGER_TIMER_HC
    6001: "PB_WorkshopBuildHC",
    6002: "PB_TriggerPlayerAttriCH",  # PB_TRIGGER_PLAYER_ATTRI_CH
    6003: "PB_PlayerAttrScaleHC",  # PB_PLAYER_ATTR_SCALE_HC
    6004: "PB_PlayerAttrScaleCH",  # PB_PLAYER_ATTR_SCALE_CH
    6005: "PB_PlayerNavigateHC",  # PB_PLAYER_NAVIGATE_HC
    6006: "PB_PlayerFaceYawHC",  # PB_PLAYER_FACE_YAW_HC
    6007: "PB_OpenEditFullyCustomModelHC",
    6008: "PB_ReqDownLoadResUrlCH",
    6009: "PB_CloseFullyCustomModelUI_CH",
    6010: "PB_CloseFullyCustomModelUI_HC",
    6011: "PB_RespDownLoadResUrlHC",
    6012: "PB_PreOpenEditFCMUI",  # PB_PRE_OPEN_EDIT_FCM_UI
    6013: "PB_EffectScaleHC",
    6014: "PB_PlayerNavFinishedCH",
    6015: "PB_TriggerMusicHC",
    6016: "PB_TriggerSoundCH",  # PB_TRIGGER_SOUND_CH
    6017: "PB_PlayerJumpHC",  # PB_PLAYER_JUMP_HC
    6018: "PB_PlayerJumpCH",  # PB_PLAYER_JUMP_CH
    6019: "PB_PlayerSpecialSkillCH",  # PB_PLAYER_SPECIAL_SKILL_CH
    6020: "PB_HorseSkillCDHC",  # PB_HORSE_SKILLCD_HC
    6021: "PB_CloudServerPermitCH",  # PB_CLOUDSERVER_PERMIT_CH
    6022: "PB_CloudServerPermitHC",  # PB_CLOUDSERVER_PERMIT_HC
    6023: "PB_CloudServerAuthorityHC",  # PB_CLOUDSERVER_AUTHORITY_HC
    6024: "PB_CloudServerAuthorityCH",  # PB_CLOUDSERVER_AUTHORITY_CH
    6025: "PB_SsSyncTaskHC",  # PB_SS_SYNC_TASK_HC
    6026: "PB_SsSyncTaskCH",  # PB_SS_SYNC_TASK_CH
    6027: "PB_VehicleAssembleBlockAllHC",
    6028: "PB_VehicleAssembleLineCH",
    6029: "PB_VehicleAssembleLineHC",
    6030: "PB_VehicleAssembleLineOperateCH",
    6031: "PB_VehicleAssembleLineOperateHC",
    6032: "PB_UpdateActionerDataCH",
    6033: "PB_VehicleWorkshopLineCH",
    6034: "PB_CloudServerChangeTeamCH",  # PB_CLOUDSERVER_CHANGE_TEAM_CH
    6035: "PB_CloudServerChangeStateHC",  # PB_CLOUDSERVER_CHANGE_STATE_HC
    6036: "PB_YMChangeRoleHC",
    6037: "PB_YMChangeRoleCH",
    6038: "PB_YMVoiceCH",
    6039: "PB_YMVoiceHC",
    6040: "PB_CSRentRoomAutoMuteCH",
    6041: "PB_VehicleWorkshopLineUpdateCH",
    6042: "PB_MapEditHandleCH",
    6043: "PB_MapEditRevokeCH",
    6044: "PB_CloudRoomOwnerStartGameCH",
    6045: "PB_CSKickOffDataCH",
    6046: "PB_TriggerOpenStoreHC",
    6047: "PB_UsePackingFCMItemCH",
    6048: "PB_UsePackingFcmItemHC",
    6049: "PB_CreatePackingCMCH",
    6050: "PB_CreatePackingCMHC",
    6051: "PB_PackingFCMDataHC",
    6052: "PB_InputContentCH",
    6053: "PB_InputKeyCH",
    6054: "PB_CloudRoomStatusTimeHC",
    6055: "PB_PlayerVehicleSleepHC",  # PB_PLAYER_VEHICLE_SLEEP_HC
    6056: "PB_SensorContainerDataCH",
    6057: "PB_SensorContainerDataHC",
    6058: "PB_VehicleBindActorHC",
    6059: "PB_DoorDataHC",
    6060: "PB_PlayerCarryActorCH",
    6061: "PB_PlayerCarryActorHC",
    6062: "PB_VillagerBodyChangeHC",
    6063: "PB_PlayerTameActorHC",
    6064: "PB_VillagerModifyNameCH",
    6065: "PB_VillagerClothHC",
    6066: "PB_ActorHeadDisplayIconHC",
    6067: "PB_ActorPlayAnimByIdHC",
    6068: "PB_VillageTotemTipHC",
    6069: "PB_VillageTotemActiveHC",
    6070: "PB_SaveTombStoneHC",
    6071: "PB_PlayerLevelModeHC",
    6072: "PB_ActionAttrStateHC",
    6073: "PB_EduRoleInfoHC",  # PB_EDU_ROLEINFO_HC
    6074: "PB_PlayerGotoPosCH",
    6075: "PB_ImportModelHC",
    6076: "PB_CustomModelPreHC",  # PB_CUSTOM_MODEL_PRE_HC
    6077: "PB_CustomModelPreCH",  # PB_CUSTOM_MODEL_PRE_CH
    6078: "PB_PlayerResetDeformationCH",  # PB_RESETDEFORMATION_CH
    6079: "PB_PlayerDeformationSkinCH",  # PB_DEFORMATION_SKIN_CH
    6080: "PB_PlayerTransformSkinHC",  # PB_PLAYERTRANSFORMSKIN_HC
    6081: "PB_PlayerRestoreTransformSkinCH",  # PB_RESTORE_DEFORMATION_CH
    6082: "PB_PlayerSaveArchHC",
    6083: "PB_PlayerPushArchCH",  # PB_PLAYER_PUSH_ARCH_CH
    6084: "PB_LightningHC",
    6085: "PB_InteractMobPackHC",
    6086: "PB_UpdateMobBackpackHC",
    6087: "PB_MoveMobBackpackItemCH",
    6088: "PB_InteractMobBackpackItemCH",
    6089: "PB_AltarLuckyDrawCH",
    6090: "PB_SFActivityHC",  # PB_SFACTIVITY_HC
    6091: "PB_OpenDevGoodsBuyDialogHC",
    6092: "PB_HomePrayInfoHC",  # PB_HOME_PRAY_INFO_HC
    6093: "PB_HomePrayTreeStateHC",  # PB_HOME_PRAY_TREE_STATE_HC
    6094: "PB_HomePrayReqHC",  # PB_HOME_PRAY_REQ_HC
    6095: "PB_PrayTreeTimeCH",
    6096: "PB_PrayTreeTimeUpdateHC",
    6097: "PB_PrayErrorHC",
    6098: "PB_HomeNpcOpenHC",
    6099: "PB_OpenHomeClosetHC",  # PB_OPEN_HOMECLOSET_HC
    6100: "PB_GodTempleCreateHC",
    6101: "PB_ShapeAdditionAnimHC",
    6102: "PB_SummonPetCH",  # PB_HOME_SUMMONPET_CH
    6103: "PB_HomelandRanchInfoHC",  # PB_HOMELAND_RANCH_HC
    6104: "PB_HomeLandRanchUpdateAnimalStateCH",
    6105: "PB_PlayGraphicsHC",  # PB_TRIGGER_GRAPHICS_HC
    6106: "PB_UseItemByHomelandHC",
    6107: "PB_CustomBaseModelHC",
    6108: "PB_ChangeActorModelHC",
    6109: "PB_RequestModelName",  # PB_REQUEST_MODEL_CH
    6110: "PB_NotifiyActorModelHC",  # PB_NOTIFIY_MODEL_HC
    6111: "PB_VoiceInformCH",
    6112: "PB_VoiceInformHC",
    6113: "PB_RuneOperateCH",
    6114: "PB_RuneOperateSuccessHC",
    6115: "PB_FurnaceTemperatureCH",
    6116: "PB_PlayerTakeContainerGridItemCH",  # PB_TAKE_CONTAINER_ITEM_CH
    6117: "PB_PlayerPotSetMakeCH",
    6118: "PB_UpdatePotContainerHC",
    6119: "PB_NotifyStarStationAddedHC",  # PB_NOTIFY_STARSTATION_ADDED_HC
    6120: "PB_NotifyStarStationRemovedHC",  # PB_NOTIFY_STARSTATION_REMOVED_HC
    6121: "PB_NotifyStarStationChangeNameStatusHC",  # PB_NOTIFY_STARSTATION_CHANGENAMESTATUS_HC
    6122: "PB_StarStationChangeNameStatusCH",  # PB_STARSTATION_CHANGENAMESTATUS_CH
    6123: "PB_NotifyEnterStarStationCabinHC",  # PB_NOTIFY_ENTER_STARSTATION_CABIN_HC
    6124: "PB_LeaveStarStationCabinCH",  # PB_LEAVE_STARSTATION_CABIN_CH
    6125: "PB_NotifyLeaveStarStationCabinHC",  # PB_NOTIFY_LEAVE_STARSTATION_CABIN_HC
    6126: "PB_UpdateStarStationCabinLevelCH",  # PB_UPDATE_STARSTATION_CABIN_LEVEL_CH
    6127: "PB_NotifyUpdateStarStationCabinLevelHC",  # PB_NOTIFY_UPDATE_STARSTATION_CABIN_LEVEL_HC
    6128: "PB_UpdateStarStationCabinStatusCH",  # PB_UPDATE_STARSTATION_CABIN_STATUS_CH
    6129: "PB_NotifyUpdateStarStationCabinStatusHC",  # PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUS_HC
    6130: "PB_NotifyUpdateStarStationCabinAddedHC",  # PB_NOTIFY_UPDATE_STARSTATION_CABIN_ADDED_HC
    6131: "PB_NotifyUpdateStarStationCabinRemovedHC",  # PB_NOTIFY_UPDATE_STARSTATION_CABIN_REMOVED_HC
    6132: "PB_AddUnfinishedTransferRecordCH",  # PB_ADD_UNFINISHED_TRANSFER_RECORD_CH
    6133: "PB_NotifyAddUnfinishedTransferRecordHC",  # PB_NOTIFY_ADD_UNFINISHED_TRANSFER_RECORD_HC
    6134: "PB_NotifyUpdateUnfinishedTransferRecordStatusHC",  # PB_NOTIFY_UPDATE_UNFINISHED_TRANSFER_RECORD_STATUS_HC
    6135: "PB_RemoveUnfinishedTransferRecordCH",  # PB_REMOVE_UNFINISHED_TRANSFER_RECORD_CH
    6136: "PB_NotifyRemoveUnfinishedTransferRecordHC",  # PB_NOTIFY_REMOVE_UNFINISHED_TRANSFER_RECORD_HC
    6137: "PB_StarStationDataHC",
    6138: "PB_PlayerTransferByStarStationCH",
    6139: "PB_NotifyPlayerTransferByStarStationHC",  # PB_NOTIFY_PLAYER_TRANSFER_BY_STRSTATION_HC
    6140: "PB_NotifyActivateStarStationHC",  # PB_NOTIFY_ACTIVATE_STARSTATION_HC
    6141: "PB_NotifyUpgradeStarStationCabinHC",  # PB_NOTIFY_UPGRADE_STARSTATION_CABIN_HC
    6142: "PB_NotifyUpdateStarStationSignInfoHC",  # PB_NOTIFY_UPDATE_STARSTATION_SIGN_INFO_HC
    6143: "PB_RequireStarStationTransferCH",  # PB_REQUIRE_STARSTATION_TRANSFER_CH
    6144: "PB_NotifyStarStationTransferResultHC",  # PB_NOTIFY_STARSTATION_TRANSFER_RESULT_HC
    6145: "PB_BlockExploitCH",
    6146: "PB_BlockExploitHC",
    6147: "PB_VacantBossStateHC",
    6148: "PB_BackPackRemoveItemItemCH",  # PB_BACKPACK_REMOVEITEM_CH
    6149: "PB_PlayAltmanMusicHC",  # PB_NOTIFY_PLAYALTMANMUSIC_HC
    6150: "PB_NotifyUpdateToolModelTextureHC",  # PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_HC
    6151: "PB_GainItemsToBackPackCH",
    6152: "PB_UpdateStarStationCabinStatusEndCH",  # PB_UPDATE_STARSTATION_CABIN_STATUSEND_CH
    6153: "PB_NotifyUpdateStarStationCabinStatusEndHC",  # PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUSEND_HC
    6154: "PB_AddStarStationTransferDescCH",  # PB_ADD_STARSTATION_TRANSFER_DESC_CH
    6155: "PB_AddExpCH",
    6156: "PB_AddExpResultHC",
    6157: "PB_CoustomUIEvent",
    6158: "PB_AchievementSyncHC",
    6159: "PB_AchievementUpdateCH",
    6160: "PB_BPEventHC",  # PB_BATTLEPASS_EVENT_HC
    6161: "PB_AddStarCH",
    6162: "PB_UseHearthCH",
    6163: "PB_ActorStopAnimHC",
    6164: "PB_ActorStopAnimCH",
    6167: "PB_HomeLandRanchFooderCH",  # PB_HOMELAND_RANCH_FOODER_CH
    6168: "PB_HorseFlagHC",
    6169: "PB_HomeLandRanchFooderStateHC",
    6170: "PB_AchievementInitDataHC",  # PB_ACHIEVEMENT_INITDATA_HC
    6171: "PB_HomeLandMenuBuyHC",
    6172: "PB_HomeLandMenuBuyCH",
    6173: "PB_HomeLandFarmShopHC",  # PB_HOMELAND_FARM_SHOP_HC
    6174: "PB_HomeLandFarmShopCH",  # PB_HOMELAND_FARM_SHOP_CH
    6177: "PB_HomeLandSpecialFurnitureBuyHC",
    6178: "PB_HomeLandSpecialFurnitureBuyCH",
    6179: "PB_PlayerOpenUIHC",
    6180: "PB_AnswerLanternBird_CH",
    6181: "PB_ExchangeItemsToBackPackCH",
    6182: "PB_ExchangeItemsToBackPackResultHC",
    6183: "PB_ChangeQQMusicPlayerHC",
    6184: "PB_ChangeQQMusicPlayerCH",
    6185: "PB_SetTiangouHC",
    6186: "PB_PlayeCloseUICH",
    6187: "PB_RideInvisibleHC",
    6188: "PB_ActorPlaySoundCH",
    6189: "PB_ActorInviteCH",
    6190: "PB_ActorInviteHC",
    6191: "PB_PlaySkinActHC",
    6192: "PB_PlaySkinActCH",
    6193: "PB_ChangeQQMusicClubHC",
    6194: "PB_ChangeQQMusicClubCH",
    6195: "PB_ActorStopSkinActHC",
    6196: "PB_MiniClubMusicPlayerHC",
    6197: "PB_MiniClubMusicPlayerCH",
    6198: "PB_ActorStopSkinActCH",
    6199: "PB_SprayPaintInfoCH",
    6200: "PB_AddPaintedInfoHC",
    6201: "PB_RemovePaintedInfoHC",
    6202: "PB_EquipWeaponHC",
    6203: "PB_EquipWeaponCH",
    6204: "PB_PlayEffectCH",
    6205: "PB_GainItemsUserDatastrToBackPackCH",
    6206: "PB_UseMusicYuPuCH",
    6207: "PB_DanceByPlayingCH",
    6208: "PB_StopDanceByPlayingCH",
    6209: "PB_StartActCH",
    6210: "PB_StopActCH",
    6211: "PB_TopBrandCH",
    6212: "PB_TopBrandHC",
    6213: "PB_HostCheckCheat",  # PB_CHEAT_CHECK_CH
    6214: "PB_WeaponPointHC",
    6215: "PB_GameModeChangeHC",
    6216: "PB_AddLightningChainHC",
    6217: "PB_STARTFISHINGCH",
    6218: "PB_STARTFISHINGHC",
    6219: "PB_ENDFISHINGCH",
    6220: "PB_ENDFISHINGHC",
    6221: "PB_QUITFISHINGCH",
    6222: "PB_QUITFISHINGHC",
    6223: "PB_CHANGEFISHINGSTAGEHC",
    6224: "PB_ExposePosChangeCH",
    6225: "PB_NotifyUpdateToolModelTextureCH",  # PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_CH
    6226: "PB_BindItemToActorHC",
    6227: "PB_FishingBeginFlashHC",
    6228: "PB_EndPlayFishCH",
    6229: "PB_ChangeShowEquipHC",
    6240: "PB_ResetRoleFlagsHC",  # PB_RESET_ROLE_FLAGS
    6241: "PB_BindPlayerToPhysicsPlatHC",
    6242: "PB_UnbindPlayerToPhysicsPlatHC",
    6243: "PB_PhysicsComUpdate",  # PB_PHYSICS_COM_UPDATE
    6244: "PB_PhysicsComPlatLocalPos",  # PB_PHYSICS_COM_PLAT_LOCAL_POS
    6245: "PB_EffectComParticleUpdate",  # PB_EFFECT_COM_PARTICLE_UPDATE
    6246: "PB_SoundComUpdate",  # PB_SOUND_COM_UPDATE
    6247: "PB_BindPlayerToPhysicsPlatCH",
    6248: "PB_UnbindPlayerToPhysicsPlatCH",
    6249: "PB_MeteorShowerHC",  # PB_METEOR_SHOWER_HC
    6250: "PB_PlayerTransferHC",
    6251: "PB_NotifyPlayerBlockChangeColorAnimHC",  # PB_NOTIFY_PLAYER_BLOCK_CHANGE_COLOR_ANIM_HC
    6252: "PB_ActorPlayHandAnimHC",
    6253: "PB_BlockPlayAnimHC",
    6254: "PB_BlockStructUpdateHC",
    6255: "PB_PlayerEnterLivingwheelHC",  # PB_PLAYER_ENTER_LIVINGWHEEL_HC
    6256: "PB_PlayerLeaveLivingwheelHC",  # PB_PLAYER_LEAVE_LIVINGWHEEL_HC
    6257: "PB_PlayerWorkingLivingwheelCH",  # PB_PLAYER_WORKING_LIVINGWHEEL_CH
    6258: "PB_UpdateLivingwheelHC",
    6259: "PB_RequestLivingwheelCH",
    6260: "PB_CreateBlockCH",  # PB_CREATE_BLOCK_CH
    6261: "PB_ActorVillagerInfoHC",  # PB_ACTOR_VILLAGER_INFO_HC
    6262: "PB_ActorSandwormShowHC",  # PB_ACTOR_SANDWORM_SHOW_HC
    6263: "PB_ActorSandwormCanMoveHC",  # PB_ACTOR_SANDWORM_CAN_MOVE_HC
    6264: "PB_ActorScaleHC",  # PB_ACTOR_SCASLE_HC
    6265: "PB_ActorSandwormNibblePlayerHC",  # PB_ACTOR_SANDWORM_NIBBLE_PLAYER_HC
    6266: "PB_ActorCreateThornballHC",  # PB_ACTOR_CREATE_THORNBALL_HC
    6267: "PB_ActorReboundsAttackUpHC",  # PB_ACTOR_REBOUNDS_ATTACK_UP_HC
    6268: "PB_ActorReboundsAttackRoundHC",  # PB_ACTOR_REBOUNDS_ATTACK_ROUND_HC
    6269: "PB_RemoveSawtoothThornbHC",  # PB_REMOVE_SAWTOOTH_THORNB_HC
    6270: "PB_ChNoticeAttackedUpCH",  # PB_CH_NOTICE_ATTACKED_UP_CH
    6271: "PB_ChNoticeAttackedRoundCH",  # PB_CH_NOTICE_ATTACKED_ROUND_CH
    6272: "PB_ChNoticeRemoveSawtoothThornbaCH",  # PB_CH_NOTICE_REMOVE_SAWTOOTH_THORNBA_CH
    6273: "PB_AttrShapeShiftRightClickCH",  # PB_ATTR_SHAPE_SHIFT_RIGHT_CLICK_CH
    6274: "PB_DestoryBlockCH",  # PB_DESTORY_BLOCK_CH
    6275: "PB_WaterPressureCH",  # PB_WATER_PRESSURE_CH
    6276: "PB_AttrShapeShiftSyncHC",  # PB_ATTR_SHAPE_SHIFT_SYNC_HC
    6277: "PB_CoconutHitHC",  # PB_COCONUT_HIT_HC
    6278: "PB_CoconutSkipNightHC",  # PB_COCONUT_SKIP_NIGHT_HC
    6279: "PB_ActorSharkBitePlayerMoveHC",  # PB_ACTOR_SHARK_BITE_PLAYER_MOVE_HC
    6280: "PB_CrabInfoSyncHC",  # PB_CRAB_INFO_SYNC_HC
    6281: "PB_CrabClickCountResetCH",  # PB_CRAB_CLICKCOUNT_RESET_CH
    6282: "PB_HippocampusRefreshModelHC",  # PB_HIPPOCAMPUS_REFRESHMODEL_HC
    6283: "PB_HippocampusChangeColorHC",  # PB_HIPPOCAMPUS_CHANGECOLOR_HC
    6284: "PB_BackpackGridDurationHC",  # PB_BACKPACKGRID_DRUATION_HC
    6285: "PB_GunLogicUseWaterCanoonSkillCH",  # PB_GUNLOGIC_USE_WaterCanoonSkill_CH
    6286: "PB_ActorSnowmanPartShowHC",  # PB_ACTOR_SNOWMAN_PART_SHOW_HC
    6287: "PB_MobPartShowHC",  # PB_MOB_PART_SHOW_HC
    6288: "PB_PlayerShakeCH",  # PB_PLAYER_SHAKE_CH
    6289: "PB_ActorDissolveComponentOpenHC",  # PB_ACTOR_DISSOLVE_COMPONENT_OPEN_HC
    6290: "PB_CookBookInfoHC",  # PB_COOKBOOKINFO_HC
    6291: "PB_StoveTakeCH",
    6292: "PB_SetHpVisibleHC",  # PB_SETHPVISIBLE_HC
    6293: "PB_SkillplayanimHC",
    6294: "PB_SkillstopanimHC",
    6295: "PB_SkillplaybodyeffectHC",
    6296: "PB_SkillstopbodyeffectHC",
    6297: "PB_SkillworldplaybodyeffectHC",
    6298: "PB_AccumulatorHC",
    6299: "PB_SkillplaytoolanimHC",
    6300: "PB_SkillstoptoolanimHC",
    6301: "PB_SkillsetchargemoveHC",
    6302: "PB_SkillmoveHC",
    6303: "PB_SkillcameraHC",
    6304: "PB_StopweaponanimHC",
    6305: "PB_StopweaponanimCH",
    6306: "PB_StopweaponmotionHC",
    6307: "PB_StopweaponmotionCH",
    6308: "PB_SetlocotypeHC",
    6309: "PB_BasestateHC",
    6310: "PB_SetmovementModeHC",
    6311: "PB_HorseflystateHC",
    6312: "PB_PlayerCameraconfigHC",
    6313: "PB_BackpackNumChangeHC",
    6314: "PB_PlaySkinVoiceCH",
    6315: "PB_PlaySkinVoiceHC",
    6316: "PB_BoxPlayAniCH",
    6317: "PB_NewYearBossStageHC",
    6318: "PB_NewYearHpHC",
    6320: "PB_NewYearMonsterPosHC",
    6321: "PB_StorageBoxPutAllCH",
    6322: "PB_TeleportShowPanelHC",  # PB_TELEPORT_SHOWPANEL_HC
    6323: "PB_DynamicProtoHC",  # PB_DYNAMIC_PROTO_HC
    6324: "PB_DynamicProtoCH",  # PB_DYNAMIC_PROTO_CH
    6330: "PB_StorageBoxTakeOutAllCH",  # PB_STORAGE_BOX_TAKE_OUT_ALL_CH
    6331: "PB_SyncDyeableItemCH",
    6332: "PB_CustomPbcCH",
    6333: "PB_CustomPbcHC",
    6334: "PB_UpdateLaserPointerHC",
    6335: "PB_UpdateLaserPointerCH",
    6500: "PB_PhysicsInputFrame",  # PB_PHYSICS_INPUT_FRAME
    6501: "PB_PhysicsTimestamp",  # PB_PHYSICS_ASYNC_TIMESTAMP
    6502: "PB_PhysicsSetupTimestamp",  # PB_PHYSICS_SETUP_TIMESTAMP
    6503: "PB_PhysicsTimeDilation",  # PB_PHYSICS_TIME_DILATION
    6504: "PB_PhysicsReplicatedInputCH",
    6505: "PB_PhysicsReplicatedInputHC",
    6506: "PB_PhysicsReplicatedStateCH",
    6507: "PB_PhysicsReplicatedStateHC",
    6508: "PB_PhysicsCommonReplicated",  # PB_PHYSICS_COMMON_REPLICATED
    7000: "PB_CustomMsg",  # PB_CUSTOM_MSG
    7001: "PB_BlockDataCH",
    7002: "PB_PushSnowBallOperateCH",
    7003: "PB_PushSnowBallOperateHC",
    7004: "PB_PushSnowBallSizeChangeHC",
    7005: "PB_PlayEffectShaderHC",  # PB_PLAY_EFFECT_SHADER_HC
    7006: "PB_NewRepairItemCH",
    7007: "PB_SendObjActorMsg",  # PB_SEND_OBJACTOR_MSG
    7008: "PB_AddBulletholeHC",  # PB_ADD_BULLETHOLE_HC
    7009: "PB_ActorShootCH",
    7010: "PB_ActorFireworkCH",
    7011: "PB_ActorPlayAnimNewCH",  # PB_ACTOR_PLAYANIM_NEW_CH
    7012: "PB_ActorSpeedChangeHC",  # PB_ACTOR_SPEED_CHANGE_HC
    7013: "PB_TaskInitDataHC",
    7014: "PB_ByMountHC",
    7016: "PB_ActorPickupActorHC",
    7018: "PB_ActorDropActorHC",  # PB_ACTOR_DROP_ACTOR_HC
    7019: "PB_WeatherHC",  # PB_GROUP_WEATHER_HC
    7020: "PB_ByMountCH",
    7021: "PB_AddBulletholeV2HC",  # PB_ADD_BULLETHOLEV2_HC
    7024: "PB_ActorSetAttrToTrackingPlayersHC",  # PB_ACTOR_SET_ATTR_TOTRACKINGPLAYERS_HC
    7025: "PB_TaskObjectiveInitDataHC",  # PB_TASK_OBJECTIVE_INITDATA_HC
    7026: "PB_PlayWeaponMotionHC",
    7027: "PB_PlayWeaponMotionCH",
    7028: "PB_PlayWeaponAnimHC",
    7029: "PB_PlayWeaponAnimCH",
    7030: "PB_ActorJumpHC",
    7031: "PB_TechTreeInfoChangeHC",  # PB_TECHTREEINFOCHANGE_HC
    7032: "PB_SetGravityFailureHC",  # PB_ACTORSETGRAVITYFAILURE_HC
    7033: "PB_SetInteractActorMechaHC",
    7034: "PB_UnlockItemsHC",  # PB_UNLOCKITEMS_HC
    7035: "PB_CheckNewUnlockItem_CH",
    7036: "PB_PlayCameraShakeHC",  # PB_PLAY_CAMERA_SHAKE_HC
    7037: "PB_RecentlyMakeCraft_CH",
    7038: "PB_MechaKineticUintHC",  # PB_MECHAKINETICUINT_HC
    7039: "PB_KineticNodeDataHC",  # PB_MECHAKINETICNODEDATA_HC
    7040: "PB_ContainerUIData_HC",
    7041: "PB_ContainerUIData_CH",
    7042: "PB_MechaRecoveryHeadHC",
    7043: "PB_MechaTunnelAnimPlayHC",  # PB_MECHA_TUNNEL_ANIM_PLAY_HC
    7044: "PB_MechaStructureSyncHC",
    7045: "PB_MechaStructureOperateCH",
    7046: "PB_MechaStructureOperateHC",
    7047: "PB_TransferGoodsCompHC",  # PB_TRANSFER_GOOD_COMP_HC
    7048: "PB_PickTransferGoodItem_CH",
    7049: "PB_MechaKineticNodeLogicDataHC",  # PB_MECHA_KINETNODELOGIC_DATA_HC
    7050: "PB_MechaAddKineticNodeLogicHC",  # PB_MECHA_ADDKINETNODELOGIC_HC
    7051: "PB_IronDomeEssenceDisEquip_CH",
    7052: "PB_IronHC",
    7053: "PB_IronDomeEssenceEquip_HC",
    7054: "PB_Part_HC",
    7055: "PB_PartManager_HC",
    7056: "PB_BlockTextureColors_HC",
    7057: "PB_LookAtActorHC",
    7058: "PB_SandboxLuaLogDataCH",  # PB_SANDBOX_LUA_LOG_DATA_CH
    7059: "PB_SandboxLuaLogDataHC",  # PB_SANDBOX_LUA_LOG_DATA_HC
    7101: "PB_AI_TTS_AUDIO_HC_MSG",
    7102: "PB_AI_ASR_AUDIO_CH_MSG",
    7103: "PB_ModContainer_HC",
    7104: "PB_WBPMsgHC",
    7105: "PB_WBPMsgCH",
    7106: "PB_RakePlantItemId_CH",
    7107: "PB_AvatarPartsPrioritySyncHC",
    7108: "PB_AvatarPartsPrioritySyncAllHC",
    7109: "PB_ActorChatBubbleHC",
    7110: "PB_SleepMsgHC",
    7111: "PB_DropItemStateData_HC",
    7112: "PB_DropItemInteractResult_CH",
    7113: "PB_ActorSwitchPhysicTypeHC",  # PB_ACTOR_SWITCH_PHYSICTYPE_HC
    7114: "PB_PlayerUseItem_CH",
    7115: "PB_PlayerPlayHandAnim_HC",
    7116: "PB_PlayerPlayDigBlockEffect_HC",
    7117: "PB_ActorPlayAnimFinishCH",
    10002: "PB_WorldSyncSaveHC",  # PB_WORLD_SYNC_SAVE_HC
}

# 尝试导入 protobuf 相关库
try:
    from google.protobuf.json_format import MessageToDict
    from google.protobuf.message import Message
except ImportError:
    print("请安装 protobuf: pip install protobuf", file=sys.stderr)
    sys.exit(1)

# 尝试导入 pcap 解析库
try:
    import scapy.all as scapy

    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    subprocess.run(["tshark", "--version"], capture_output=True, check=True)
    TSHARK_AVAILABLE = True
except (subprocess.CalledProcessError, FileNotFoundError):
    TSHARK_AVAILABLE = False


def compile_proto_files(proto_dir):
    """
    编译指定目录下的所有 .proto 文件，返回生成的模块路径列表。
    使用临时目录存放编译结果，并导入所有模块。
    返回: 字典，键为消息全名，值为消息类。
    """
    proto_dir = Path(proto_dir)
    if not proto_dir.is_dir():
        raise NotADirectoryError(f"Proto 目录不存在: {proto_dir}")

    # 检查 protoc 是否可用
    try:
        subprocess.run(["protoc", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("未找到 protoc，请安装 protobuf 编译器。", file=sys.stderr)
        sys.exit(1)

    # 收集所有 .proto 文件
    proto_files = list(proto_dir.glob("*.proto"))
    if not proto_files:
        print(f"在 {proto_dir} 中未找到 .proto 文件", file=sys.stderr)
        sys.exit(1)

    # 创建临时目录用于编译
    with tempfile.TemporaryDirectory() as tmpdir:
        # 编译所有 proto 文件，输出到临时目录
        cmd = ["protoc", f"--python_out={tmpdir}", f"-I={proto_dir}/"] + [
            str(f) for f in proto_files
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"编译 proto 文件失败: {e.stderr}", file=sys.stderr)
            sys.exit(1)

        # 导入所有生成的模块
        sys.path.insert(0, tmpdir)
        modules = {}
        for proto_file in proto_files:
            module_name = proto_file.stem + "_pb2"
            try:
                module = importlib.import_module(module_name)
                modules[module_name] = module
            except ImportError as e:
                print(f"导入模块 {module_name} 失败: {e}", file=sys.stderr)

        # 遍历所有模块，收集消息类
        message_classes = {}
        for module in modules.values():
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Message):
                    # 消息全名格式: package.MessageName
                    full_name = attr.DESCRIPTOR.full_name
                    message_classes[full_name] = attr
        return message_classes


def extract_udp_payloads_tshark(pcap_file):
    """
    使用 tshark 提取所有 UDP 负载的原始数据（十六进制字符串），返回字节列表。
    """
    cmd = [
        "tshark",
        "-r",
        pcap_file,
        "-Y",
        "raknet",
        "-T",
        "fields",
        "-e",
        "udp.payload",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"tshark 执行失败: {e.stderr}", file=sys.stderr)
        return []

    payloads = []
    for line in result.stdout.strip().splitlines():
        if not line:
            continue
        # 每个包可能包含多个字段，以逗号分隔
        parts = line.split(",")
        for part in parts:
            part = part.strip()
            if part:
                try:
                    data = bytes.fromhex(part)
                    payloads.append(data)
                except ValueError:
                    print(f"警告: 无法解析十六进制数据: {part}", file=sys.stderr)
    return payloads


def extract_udp_payloads_scapy(pcap_file):
    """
    使用 Scapy 提取 UDP 负载。
    """
    if not SCAPY_AVAILABLE:
        print("scapy 未安装，无法使用 scapy 解析器。", file=sys.stderr)
        return []

    packets = scapy.rdpcap(pcap_file)
    payloads = []
    for pkt in packets:
        if pkt.haslayer(scapy.UDP):
            udp_payload = (
                bytes(pkt[scapy.UDP].payload) if pkt[scapy.UDP].payload else b""
            )
            if udp_payload:
                payloads.append(udp_payload)
    return payloads


split_packet = b""
c = 0


def parse_raknet_messages(udp_data):
    """
    从 UDP 负载中解析 RakNet 消息，提取所有用户消息的数据部分（即 Protobuf 数据）。
    采用简化解析：消息格式为 [消息ID(1字节)] [消息长度(2字节小端)] [数据]。
    如果消息 ID >= 0x80，则认为是用户消息，返回其数据部分（不含 ID 和长度）。
    返回列表：每个元素为一条用户消息的数据（字节串）。
    """
    global c, split_packet
    messages = []
    i = 0
    c += 1
    data_len = len(udp_data)
    try:
        msg_id = udp_data[i]
        i += 1
        # 用户消息 ID 通常 >= 0x80
        if 0x80 <= msg_id <= 0x8F:  # frame_set_0-f
            i += 3  # packet number
            while i < data_len:
                # 至少需要 1 字节 ID
                if i >= data_len:
                    break

                msg_flag = udp_data[i]
                i += 1
                payload_length = struct.unpack(">H", udp_data[i : i + 2])[0] // 8
                i += 2
                if msg_flag in (0b01100000, 0b00100000, 0b00000000):  # no split packet
                    i += 8
                    payload = udp_data[i : i + payload_length]
                    i += payload_length - 1
                    messages.append(payload)
                elif msg_flag in (0b01110000, 0b00110000, 0b00010000):  # split packet
                    i += 7
                    split_count, split_id, split_index = struct.unpack(
                        ">IHI", udp_data[i : i + 10]
                    )
                    # print('split', split_count, split_id, split_index)
                    i += 10
                    if len(split_packet) == 0:
                        #    split_packets.insert(split_id + 1, udp_data[i:i+payload_length])
                        #    print(udp_data[i:i+payload_length])
                        split_packet += udp_data[i + 1 : i + payload_length]
                    else:
                        #    split_packets[split_id] += udp_data[i:i+payload_length]
                        split_packet += udp_data[i : i + payload_length]
                    i += payload_length
                    if split_count == split_index + 1:
                        messages.append(split_packet)
                        # print(len(split_packet))
                        split_packet = b""
                        # print(messages)
                else:
                    i += 1
        else:
            # 系统消息，可能也有长度，但这里简单跳过，处理下一个字节
            # 或者尝试解析长度，但为了简单，我们假设系统消息是单字节且无数据
            # 如果后续还有消息，继续循环
            pass
    except (IndexError, struct.error):
        pass
    return messages


def parse_message_header(data):
    """
    解析消息头，返回 (msg_id, msg_data, is_client_to_server) 或 None。
    根据长度判断方向：如果长度 >=12 则尝试解析为客户端->服务端头，否则尝试服务端->客户端头。
    返回：
        msg_id: 消息 ID (int)
        msg_data: 消息体字节串
        direction: 'c2s' 或 's2c'
    """
    if len(data) < 4:
        return None

    # 先尝试解析为服务端->客户端头（4字节）
    msg_id_s2c, msg_len_s2c = struct.unpack("<HH", data[:4])
    if msg_len_s2c <= len(data) - 4:
        return msg_id_s2c, data[4 : 4 + msg_len_s2c], "s2c"

    # 如果数据足够 12 字节，尝试解析为客户端->服务端头
    if len(data) >= 12:
        # 跳过玩家 ID 和占位符
        _, _, msg_id_c2s, msg_len_c2s = struct.unpack("<IIHH", data[:12])
        if msg_len_c2s <= len(data) - 12:
            return msg_id_c2s, data[12 : 12 + msg_len_c2s], "c2s"

    # 无法识别
    return None


def to_camel_case(text):
    # 使用正则匹配下划线+字母，替换为大写字母
    s = re.sub(r"(_)([a-zA-z])", lambda m: m.group(2).upper(), text.lower())
    # 首字母大写（大驼峰）
    return s[0].upper() + s[1:]


def build_msgid_to_class_map(message_classes):
    """
    从 proto 文件中解析 ePBMsgCode 枚举，构建消息 ID 到消息类的映射。
    由于枚举定义在某个 proto 文件中，我们通过遍历所有消息类的 descriptor 来关联。
    消息类名可能与枚举值有对应关系，但需要实际映射。通常枚举值名称与消息类名有对应关系。
    这里我们采用简单方法：对于每个消息类，尝试根据其名称从枚举中查找对应的 ID。
    因为 ePBMsgCode 的枚举值通常命名为 PB_XXXX_HC 或 PB_XXXX_CH，而消息类名类似。
    我们需要加载所有 proto 文件后，从模块中获取枚举值。
    """
    # 首先，加载所有模块，获取 ePBMsgCode 枚举
    # 遍历所有已导入模块，查找名为 'ePBMsgCode' 的枚举
    msg_code_enum = None
    for module_name, module in sys.modules.items():
        if module_name.endswith("_pb2"):
            if hasattr(module, "ePBMsgCode"):
                msg_code_enum = getattr(module, "ePBMsgCode")
                break
    if not msg_code_enum:
        # 如果没找到，尝试遍历所有模块
        for module in list(sys.modules.values()):
            if hasattr(module, "ePBMsgCode"):
                msg_code_enum = getattr(module, "ePBMsgCode")
                break
    if not msg_code_enum:
        print(
            "未找到 ePBMsgCode 枚举定义，请确保 proto 文件中包含该枚举。",
            file=sys.stderr,
        )
        sys.exit(1)

    # 构建映射：消息 ID -> 消息类
    id_to_class = {}
    # 枚举的 descriptor 包含值到名称的映射
    for value in msg_code_enum.items():
        msg_id = value[1]
        enum_name = value[0]
        # 尝试根据枚举名猜测消息类名
        # 常见模式：枚举名如 PB_HEARTBEAT_CH 对应消息类 PB_HeartBeatCH
        # 需要去掉前缀 'PB_'，然后转换为驼峰（但 proto 中消息类通常就是这样的名称）
        # 我们直接尝试用枚举名去掉 'PB_' 作为消息类名，再查找
        # 注意：有些消息类可能没有直接对应，但大部分是
        class_candidate: str = enum_name[3:]  # 去掉 'PB_'
        if class_candidate.endswith("_CH"):
            class_candidate = "PB_" + to_camel_case(class_candidate[:-3]) + "CH"
        elif class_candidate.endswith("_HC"):
            class_candidate = "PB_" + to_camel_case(class_candidate[:-3]) + "HC"
        # 在消息类字典中查找完整名称（包括包名）
        # 包名通常是 'game.ch' 或 'game.hc'，我们需要尝试匹配
        for full_name, cls in message_classes.items():
            # 提取类名（最后一个点之后）
            short_name = full_name.split(".")[-1]
            if (
                short_name == class_candidate
                or short_name.lower() == class_candidate.lower()
                or short_name.upper() == class_candidate.upper()
            ):
                id_to_class[msg_id] = cls
                break
        else:
            if msg_id in msg_code_to_name:
                class_candidate: str = msg_code_to_name[msg_id]
                for full_name, cls in message_classes.items():
                    # 提取类名（最后一个点之后）
                    short_name = full_name.split(".")[-1]
                    if short_name == class_candidate:
                        id_to_class[msg_id] = cls
                        break
                else:
                    # print('找不到对应消息: ' + enum_name)
                    pass
            else:
                # print('未知类型: ' + enum_name)
                pass
            # 未找到，可能类名与枚举名不一致，尝试其他匹配（如全部大写转驼峰）
            # 例如 PB_HEARTBEAT_CH -> HeartBeatCH
            # 简单处理：忽略
    return id_to_class


message_classes = {}
id_to_class = {}


def init():
    global message_classes, id_to_class
    # message_classes = compile_proto_files('../pb/')
    import mn2mc.mini.proto

    # 遍历所有模块，收集消息类
    message_classes = {}
    for module_name in mn2mc.mini.proto.__all__:
        module = getattr(mn2mc.mini.proto, module_name)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, Message):
                # 消息全名格式: package.MessageName
                full_name = attr.DESCRIPTOR.full_name
                message_classes[full_name] = attr
    id_to_class = build_msgid_to_class_map(message_classes)
    logger.info(f"Mapped {len(id_to_class)} protobuf messages!")


def parse(msg_id, msg_body):
    global message_classes, id_to_class
    if msg_id in ignored_msg_code:
        return
    if msg_id not in id_to_class:
        logger.debug(f"未知消息 ID {msg_id}")
        # print(f"原始数据: {msg_body.hex()}")
        try:
            json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
            if json_msg != "{}":
                logger.debug(json_msg)
        except Exception:
            pass
        return

    msg_class = id_to_class[msg_id]
    try:
        proto_msg = msg_class()
        logger.debug(msg_class)
        proto_msg.ParseFromString(msg_body)
        json_msg = MessageToDict(proto_msg, preserving_proto_field_name=True)
        logger.debug(json.dumps(json_msg, indent=2, ensure_ascii=False))
    except Exception as e:
        logger.debug(f"解析失败: {e}")
        # print(f"数据 (前64字节): {msg_body[:64].hex()}")
        try:
            json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
            if json_msg != "{}":
                logger.debug(json_msg)
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser(
        description="解析 PCAP 中 RakNet 协议内的 Protobuf 数据"
    )
    parser.add_argument("-p", "--pcap", required=True, help="PCAP 文件路径")
    parser.add_argument(
        "-d", "--proto-dir", required=True, help="包含所有 .proto 文件的目录"
    )
    parser.add_argument("--tshark", action="store_true", help="强制使用 tshark 解析")
    parser.add_argument("--scapy", action="store_true", help="强制使用 scapy 解析")
    args = parser.parse_args()

    # 1. 编译 proto 文件并加载消息类
    print("正在编译 Proto 文件...")
    message_classes = compile_proto_files(args.proto_dir)
    print(f"共加载 {len(message_classes)} 个消息类")

    # 2. 构建消息 ID 到消息类的映射
    print("构建消息 ID 映射...")
    id_to_class = build_msgid_to_class_map(message_classes)
    print(f"成功映射 {len(id_to_class)} 个消息 ID")

    # 3. 提取 UDP 负载
    if args.tshark:
        if not TSHARK_AVAILABLE:
            print("tshark 不可用，请安装 Wireshark", file=sys.stderr)
            sys.exit(1)
        udp_payloads = extract_udp_payloads_tshark(args.pcap)
    elif args.scapy:
        if not SCAPY_AVAILABLE:
            print("scapy 不可用，请安装 scapy", file=sys.stderr)
            sys.exit(1)
        udp_payloads = extract_udp_payloads_scapy(args.pcap)
    else:
        if TSHARK_AVAILABLE:
            udp_payloads = extract_udp_payloads_tshark(args.pcap)
        elif SCAPY_AVAILABLE:
            print(
                "警告: tshark 未找到，使用 scapy 解析器（可能不准确）", file=sys.stderr
            )
            udp_payloads = extract_udp_payloads_scapy(args.pcap)
        else:
            print("错误: 未找到 tshark 或 scapy，无法解析 PCAP", file=sys.stderr)
            sys.exit(1)

    print(f"从 {args.pcap} 提取到 {len(udp_payloads)} 个 UDP 负载")

    # 4. 解析每个 UDP 负载中的 RakNet 消息，提取用户数据
    all_user_data = []
    for idx, udp_data in enumerate(udp_payloads):
        raknet_msgs = parse_raknet_messages(udp_data)
        if raknet_msgs:
            print(f"UDP 负载 {idx + 1}: 解析出 {len(raknet_msgs)} 条 RakNet 用户消息")
            all_user_data.extend(raknet_msgs)
        else:
            print(f"UDP 负载 {idx + 1}: 未找到用户消息")

    print(f"总共提取 {len(all_user_data)} 条用户消息数据")

    # 5. 解析每条用户消息
    success_count = 0
    fallback_success_count = 0
    for idx, user_data in enumerate(all_user_data):
        parsed = parse_message_header(user_data)
        if parsed is None:
            print(
                f"\n--- 消息 {idx + 1} 无法解析头，原始数据 (前32字节): {user_data[:32].hex()} ---"
            )
            continue

        msg_id, msg_body, direction = parsed
        print(f"\n--- 消息 {idx + 1} (方向: {direction}, ID: {msg_id}) ---")

        if msg_id not in id_to_class:
            print(f"未知消息 ID {msg_id}")
            print(f"原始数据: {msg_body.hex()}")
            try:
                json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
                if json_msg != "{}":
                    print(json_msg)
                    fallback_success_count += 1
            except Exception:
                pass
            continue

        msg_class = id_to_class[msg_id]
        try:
            proto_msg = msg_class()
            print(msg_class)
            proto_msg.ParseFromString(msg_body)
            json_msg = MessageToDict(proto_msg, preserving_proto_field_name=True)
            print(json.dumps(json_msg, indent=2, ensure_ascii=False))
            success_count += 1
        except Exception as e:
            print(f"解析失败: {e}")
            print(f"数据 (前64字节): {msg_body[:64].hex()}")
            try:
                json_msg = blackboxprotobuf.protobuf_to_json(msg_body)[0]
                if json_msg != "{}":
                    print(json_msg)
                    fallback_success_count += 1
            except Exception:
                pass

    print()
    print(f"解析成功消息数: {success_count}")
    print(f"原始解析消息数: {fallback_success_count}")


if __name__ == "__main__":
    main()
