from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ePBErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_UNKNOWN: _ClassVar[ePBErrorCode]
    PB_ERROR_WRONG_MSG_CODE: _ClassVar[ePBErrorCode]
    PB_ERROR_WRONG_REQUESTER: _ClassVar[ePBErrorCode]
    PB_ERROR_WRONG_ARGS: _ClassVar[ePBErrorCode]
    PB_ERROR_PLAYER_NOT_LOGIN: _ClassVar[ePBErrorCode]
    PB_ERROR_ILLEGAL_ARGS: _ClassVar[ePBErrorCode]
    PB_ERROR_OP_NOT_FOUND: _ClassVar[ePBErrorCode]
    PB_ERROR_BACKPACK_FULL: _ClassVar[ePBErrorCode]
    PB_ERROR_STORAGE_FULL: _ClassVar[ePBErrorCode]
    PB_ERROR_ENCHANT_NOT_ENOUGH: _ClassVar[ePBErrorCode]
    PB_ERROR_ENCHANT_FAILED: _ClassVar[ePBErrorCode]
    PB_ERROR_ENCHANT_NOT_CHANGED: _ClassVar[ePBErrorCode]
    PB_ERROR_CRAFT_NOT_ENOUGH: _ClassVar[ePBErrorCode]
    PB_ERROR_STAR_NOT_ENOUGH: _ClassVar[ePBErrorCode]
    PB_ERROR_REPAIR_NOT_ENOUGH: _ClassVar[ePBErrorCode]
    PB_ERROR_REPAIR_NOT_DAMAGED: _ClassVar[ePBErrorCode]
    PB_ERROR_ROLE_ENTER_BANNED: _ClassVar[ePBErrorCode]
    PB_ERROR_ROLE_ENTER_TOO_OFTEN: _ClassVar[ePBErrorCode]
    PB_ERROR_ROLE_ENTER_SERVER_FULL: _ClassVar[ePBErrorCode]
    PB_ERROR_ROLE_ENTER_SERVER_CLOSING: _ClassVar[ePBErrorCode]
    PB_ERROR_ROLE_MOVE_ILLEGAL_POS: _ClassVar[ePBErrorCode]
    PB_MAX_ERROR_CODE: _ClassVar[ePBErrorCode]

class ePBMsgCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_REQ_ERROR_HC: _ClassVar[ePBMsgCode]
    PB_HEARTBEAT_CH: _ClassVar[ePBMsgCode]
    PB_HEARTBEAT_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_CHUNK_DATA_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_CHUNK_DATA_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_DATA_UPDATE_CH: _ClassVar[ePBMsgCode]
    PB_BLOCK_DATA_UPDATE_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_SECTION_LIGHT_DATA_HC: _ClassVar[ePBMsgCode]
    PB_OVERRIDE_LIGHT_DATA_HC: _ClassVar[ePBMsgCode]
    PB_ROLE_ENTER_WORLD_CH: _ClassVar[ePBMsgCode]
    PB_ROLE_ENTER_WORLD_HC: _ClassVar[ePBMsgCode]
    PB_ROLE_LEAVE_WORLD_CH: _ClassVar[ePBMsgCode]
    PB_ROLE_LEAVE_WORLD_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_ENTER_AOI_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_LEAVE_AOI_HC: _ClassVar[ePBMsgCode]
    PB_GAME_LEADER_SWITCH_HC: _ClassVar[ePBMsgCode]
    PB_GENERAL_ENTER_AOI_HC: _ClassVar[ePBMsgCode]
    PB_PVP_ACTIVITY_CONFIG_CH: _ClassVar[ePBMsgCode]
    PB_ROLE_CHECK_JOINFROMSRC_CH: _ClassVar[ePBMsgCode]
    PB_ROLE_MOVE_CH: _ClassVar[ePBMsgCode]
    PB_TRAIN_MOVE_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_TRAIN_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOVEV2_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_TELEPORT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_TELEPORT_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOTION_HC: _ClassVar[ePBMsgCode]
    PB_MECHA_MOTION_HC: _ClassVar[ePBMsgCode]
    PB_GUN_INFO_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_SETINFO_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_GRIDUSERDATA_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_GRIDUSERDATA_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_TRIGGERBLOCK_HC: _ClassVar[ePBMsgCode]
    PB_FULLROT_ACTOR_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOTIONV2_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOVEV3_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MODELCHG_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_INTERACT_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_PUNCH_HC: _ClassVar[ePBMsgCode]
    PB_ITEM_USE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_INTERACT_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_INTERACT_END_CH: _ClassVar[ePBMsgCode]
    PB_BLOCK_INTERACT_CH: _ClassVar[ePBMsgCode]
    PB_BLOCK_PUNCH_CH: _ClassVar[ePBMsgCode]
    PB_ITEM_USE_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_INTERACT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_ANIM_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_GRID_UPDATE_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_GRID_SWAP_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_MOVEITEM_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_GRID_DISCARD_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_EQUIP_WEAPON_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_EQUIP_WEAPON_HC: _ClassVar[ePBMsgCode]
    PB_CLOSE_CONTAINER_CH: _ClassVar[ePBMsgCode]
    PB_CLOSE_CONTAINER_HC: _ClassVar[ePBMsgCode]
    PB_OPEN_CONTAINER_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_CONTAINER_HC: _ClassVar[ePBMsgCode]
    PB_SET_CONTAINERTEXT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_EQUIP_ITEM_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_STORE_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_LOOT_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_SORT_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_SETITEM_CH: _ClassVar[ePBMsgCode]
    PB_BACKPACK_SHORTCUT_OP_CH: _ClassVar[ePBMsgCode]
    PB_STORAGEBOX_SORT_CH: _ClassVar[ePBMsgCode]
    PB_CRAFT_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_ENCHANT_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_ENCHANT_ITEM_RANDOM_CH: _ClassVar[ePBMsgCode]
    PB_ENCHANT_ITEM_SUCCESS_HC: _ClassVar[ePBMsgCode]
    PB_REPAIR_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_REPAIR_ITEM_SUCCESS_HC: _ClassVar[ePBMsgCode]
    PB_GUN_DORELOAD_CH: _ClassVar[ePBMsgCode]
    PB_GUN_DORELOAD_HC: _ClassVar[ePBMsgCode]
    PB_GUN_RECOVERY_CH: _ClassVar[ePBMsgCode]
    PB_ACCOUNT_HORSE_CH: _ClassVar[ePBMsgCode]
    PB_ACCOUNT_HORSE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOT_SET_CUSTOM_CH: _ClassVar[ePBMsgCode]
    PB_ACTOT_SET_CUSTOM_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAY_ANIM_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAY_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_ATTACK_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_DEFANCESTATE_CH: _ClassVar[ePBMsgCode]
    PB_RCLICKUP_INTERACT_CH: _ClassVar[ePBMsgCode]
    PB_RCLICKUP_INTERACT_HC: _ClassVar[ePBMsgCode]
    PB_MOUSE_EVENT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_GUNACTION_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_GUNACTION_STATE_HC: _ClassVar[ePBMsgCode]
    PB_LIVING_INTERACT_NEW_CH: _ClassVar[ePBMsgCode]
    PB_LIVING_INTERACT_NEW_NEWTAME_HC: _ClassVar[ePBMsgCode]
    PB_LIVING_REPRODUCTION_HC: _ClassVar[ePBMsgCode]
    PB_LIVING_INTERACT_NEW_NEWGROW_HC: _ClassVar[ePBMsgCode]
    PB_TRAIN_FOLLOW_OP_CH: _ClassVar[ePBMsgCode]
    PB_TRAIN_FOLLOW_OP_HC: _ClassVar[ePBMsgCode]
    PB_TRAIN_REFINABLE_TAKE_RESULT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_ATTR_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_BUFF_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_REVIVE_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_REVIVE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_ATTR_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_MOB_BODY_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ROOM_JRUISDICTION_CH: _ClassVar[ePBMsgCode]
    PB_ROOM_JRUISDICTION_HC: _ClassVar[ePBMsgCode]
    PB_CHAT_CH: _ClassVar[ePBMsgCode]
    PB_CHAT_HC: _ClassVar[ePBMsgCode]
    PB_WGLOBAL_UPDATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYERS_UPDATEINFO_HC: _ClassVar[ePBMsgCode]
    PB_GAME_TIPS_HC: _ClassVar[ePBMsgCode]
    PB_PLAYEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_MOUNTACTOR_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_MOUNTACTOR_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_MOVEINPUT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_REVIVEPOINT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_REVIVEPOINT_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SLEEP_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SLEEP_CH: _ClassVar[ePBMsgCode]
    PB_OPENWINDOW_HC: _ClassVar[ePBMsgCode]
    PB_NPCTRADE_CH: _ClassVar[ePBMsgCode]
    PB_LASTPING_HC: _ClassVar[ePBMsgCode]
    PB_CGAMESTAGE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYERPERMIT_HC: _ClassVar[ePBMsgCode]
    PB_PLAYEFFECT_HC_V2: _ClassVar[ePBMsgCode]
    PB_SKILLCD_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_MOUNTACTOR_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_REVERSE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_BIND_HC: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_SCRIPTVAR_HC: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONEFFECT_CH: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATORMODE_CH: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATORMODE_HC: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATORTYPE_CH: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATORTYPE_HC: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATOR_PLAYER_CH: _ClassVar[ePBMsgCode]
    PB_OTHER_PLAYER_ATTR_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_LEAVE_HC: _ClassVar[ePBMsgCode]
    PB_TEAM_SCORE_HC: _ClassVar[ePBMsgCode]
    PB_SET_TEAM_HC: _ClassVar[ePBMsgCode]
    PB_SET_PLAYER_GAME_INFO_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVE_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_UIDISPLAYHORSE_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVEV2_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVEV2_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_MOVE_INTERVAL_HC: _ClassVar[ePBMsgCode]
    PB_MOVE_DIFF_CH: _ClassVar[ePBMsgCode]
    PB_PLAYEFFECT_HC_V3: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVEV4_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_MOVEV4_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_GET_ACCOUNT_ITEM: _ClassVar[ePBMsgCode]
    PB_SPECIALITEM_USE_CH: _ClassVar[ePBMsgCode]
    PB_SPECIALITEM_USE_HC: _ClassVar[ePBMsgCode]
    PB_LEAVE_ROOM_INFO_HC: _ClassVar[ePBMsgCode]
    PB_INVITEJOINROOM_HC: _ClassVar[ePBMsgCode]
    PB_SET_SPECTATOR_PLAYER_HC: _ClassVar[ePBMsgCode]
    PB_SET_PLAYER_MODEL_ANI_CH: _ClassVar[ePBMsgCode]
    PB_SET_PLAYER_MODEL_ANI_HC: _ClassVar[ePBMsgCode]
    PB_SEND_VIEWMODE_SPECTATOR_CH: _ClassVar[ePBMsgCode]
    PB_SEND_VIEWMODE_SPECTATOR_HC: _ClassVar[ePBMsgCode]
    PB_SET_BOBBING_SPECTATOR_CH: _ClassVar[ePBMsgCode]
    PB_SET_BOBBING_SPECTATOR_HC: _ClassVar[ePBMsgCode]
    PB_ITEM_SKILL_USE_CH: _ClassVar[ePBMsgCode]
    PB_ITEM_SKILL_USE_HC: _ClassVar[ePBMsgCode]
    PB_BALL_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_BALL_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_RESET_ROUND_HC: _ClassVar[ePBMsgCode]
    PB_ROCKET_ATTRIB_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ROCKET_TELEPORT_CH: _ClassVar[ePBMsgCode]
    PB_SET_HOOK_HC: _ClassVar[ePBMsgCode]
    PB_SET_HOOK_CH: _ClassVar[ePBMsgCode]
    PB_WORLD_TIMES_HC: _ClassVar[ePBMsgCode]
    PB_STATISTIC_HC: _ClassVar[ePBMsgCode]
    PB_TOTEMPOINT_HC: _ClassVar[ePBMsgCode]
    PB_NEED_CONTAINER_PASSWORD_HC: _ClassVar[ePBMsgCode]
    PB_NEED_CONTAINER_PASSWORD_CH: _ClassVar[ePBMsgCode]
    PB_HORSEFLYSTATE_HC: _ClassVar[ePBMsgCode]
    PB_OPENDIALOGUE_HC: _ClassVar[ePBMsgCode]
    PB_CLOSEDIALOGUE_HC: _ClassVar[ePBMsgCode]
    PB_CLOSEDIALOGUE_CH: _ClassVar[ePBMsgCode]
    PB_ANSWERTASK_CH: _ClassVar[ePBMsgCode]
    PB_UPDATETASK_HC: _ClassVar[ePBMsgCode]
    PB_SYNCTASK_ENTERWORLD_HC: _ClassVar[ePBMsgCode]
    PB_COMPLETE_TASK_HC: _ClassVar[ePBMsgCode]
    PB_COMPLETE_TASK_CH: _ClassVar[ePBMsgCode]
    PB_ATTRACT_ATTRIB_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_BODY_TEXTURE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_ADDAVARTAR_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CHANGEMODEL_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_AVARTARCOLOR_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_ACT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_ACT_HC: _ClassVar[ePBMsgCode]
    PB_CREATE_BLUEPRINT_HC: _ClassVar[ePBMsgCode]
    PB_MEASURE_DISTANCE_HC: _ClassVar[ePBMsgCode]
    PB_BLUEPRINT_PREBLOCK_CH: _ClassVar[ePBMsgCode]
    PB_BLUEPRINT_PREBLOCK_HC: _ClassVar[ePBMsgCode]
    PB_GRAVITY_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_GRAVITY_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_BODY_COLOR_HC: _ClassVar[ePBMsgCode]
    PB_CUSTOM_MODEL_HC: _ClassVar[ePBMsgCode]
    PB_CUSTOM_ITEMIDS_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SPAWN_POINT_HC: _ClassVar[ePBMsgCode]
    PB_MAKE_CUSTOM_MODEL_CH: _ClassVar[ePBMsgCode]
    PB_SELECT_MOB_SPAWN_CH: _ClassVar[ePBMsgCode]
    PB_CUSTOM_MODELCLASS_HC: _ClassVar[ePBMsgCode]
    PB_TRANSFER_RECORD_HC: _ClassVar[ePBMsgCode]
    PB_TRANSFER_RECORD_CH: _ClassVar[ePBMsgCode]
    PB_TRANSFER_ADD_DEL_HC: _ClassVar[ePBMsgCode]
    PB_TRANSFER_STATUS_CH: _ClassVar[ePBMsgCode]
    PB_TRANSFER_STATUS_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_LOVEAMBASSADOR_ICONID_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_LOVEAMBASSADOR_ICONID_CH: _ClassVar[ePBMsgCode]
    PB_TRANSFER_DATA_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_TRANSFER_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_TRANSFER_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_SETITEMWITHOUTLIMIT_CH: _ClassVar[ePBMsgCode]
    PB_NPCSHOP_GETSHOPINFO_CH: _ClassVar[ePBMsgCode]
    PB_NPCSHOP_RESPGETSHOPINFO_HC: _ClassVar[ePBMsgCode]
    PB_NPCSHOP_BUYSKU_CH: _ClassVar[ePBMsgCode]
    PB_NPCSHOP_NOTIFYBUY_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_OPEN_EDIT_ACTORMODEL_HC: _ClassVar[ePBMsgCode]
    PB_CLOSE_EDIT_ACTORMODEL_CH: _ClassVar[ePBMsgCode]
    PB_CLOSE_EDIT_ACTORMODEL_HC: _ClassVar[ePBMsgCode]
    PB_CUSTOMACTOR_MODELDATA_HC: _ClassVar[ePBMsgCode]
    PB_PACKGIFT_NOTIFYITEMCHANGE_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_PREBLOCK_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_PREBLOCK_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ITEMUSE_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_STARTBLOCK_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ALL_ITEMID_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ONE_ITEMID_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ATTRIB_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ATTRIB_CHANGE_CH: _ClassVar[ePBMsgCode]
    PB_WORKSHOP_ITEMINFO_CH: _ClassVar[ePBMsgCode]
    PB_WORKSHOP_ITEMINFO_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLEASSEMBLEBLOCK_UPDATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_VEHICLE_MOVEINPUT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_RESETVEHICLE_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_MOTIONSTATECHANGE_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_CLICK_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_CAMERAROTATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CHANGEVIEWMODE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CANMOVE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CANCONTROL_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SETATTR_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_FREEZING_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SELECTSHORTCUT_CH: _ClassVar[ePBMsgCode]
    PB_GAMERULE_HC: _ClassVar[ePBMsgCode]
    PB_BASKETBALL_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_BASKETBALL_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_VEHICLE_MOVEINPUT_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CANFIRE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_TOUCH_EVT_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_TOUCH_EVT_CH: _ClassVar[ePBMsgCode]
    PB_BUY_AD_SHOP_GOOD_CH: _ClassVar[ePBMsgCode]
    PB_BUY_AD_SHOP_GOOD_HC: _ClassVar[ePBMsgCode]
    PB_SYNC_PLAYER_POS_HC: _ClassVar[ePBMsgCode]
    PB_ACHIEVEMENT_AWARD_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_CLIENT_ACTIONLOG_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_ROOM_EXTRA_HC: _ClassVar[ePBMsgCode]
    PB_UPLOAD_CHECK_INFO_CH: _ClassVar[ePBMsgCode]
    PB_GET_ADSHOP_EXTRA_AWARD_CH: _ClassVar[ePBMsgCode]
    PB_EXTRACT_STORE_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_UPLOAD_CLIENT_INFO_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_PLAYER_POS_CH: _ClassVar[ePBMsgCode]
    PB_TRIGGER_TIMER_HC: _ClassVar[ePBMsgCode]
    PB_WORKSHOP_BUILD_HC: _ClassVar[ePBMsgCode]
    PB_TRIGGER_PLAYER_ATTRI_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_ATTR_SCALE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_ATTR_SCALE_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_NAVIGATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_FACE_YAW_HC: _ClassVar[ePBMsgCode]
    PB_OPENEDIT_FULLYCUSTOMMODEL_HC: _ClassVar[ePBMsgCode]
    PB_REQ_DOWNLOADRES_URL_CH: _ClassVar[ePBMsgCode]
    PB_CLOSE_FULLYCUSTOMMODEL_UI_CH: _ClassVar[ePBMsgCode]
    PB_CLOSE_FULLYCUSTOMMODEL_UI_HC: _ClassVar[ePBMsgCode]
    PB_RESP_DOWNLOADRES_URL_HC: _ClassVar[ePBMsgCode]
    PB_PRE_OPEN_EDIT_FCM_UI: _ClassVar[ePBMsgCode]
    PB_EFFECTSCALE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_NAVFINISHED_CH: _ClassVar[ePBMsgCode]
    PB_TRIGGER_MUSIC_HC: _ClassVar[ePBMsgCode]
    PB_TRIGGER_SOUND_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_JUMP_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_JUMP_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_SPECIAL_SKILL_CH: _ClassVar[ePBMsgCode]
    PB_HORSE_SKILLCD_HC: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_PERMIT_CH: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_PERMIT_HC: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_AUTHORITY_HC: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_AUTHORITY_CH: _ClassVar[ePBMsgCode]
    PB_SS_SYNC_TASK_HC: _ClassVar[ePBMsgCode]
    PB_SS_SYNC_TASK_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLEASSEMBLEBLOCK_ALL_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ASSEMBLE_LINE_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ASSEMBLE_LINE_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ASSEMBLE_LINE_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_ASSEMBLE_LINE_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_ACTIONEDATA_UPDATE_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_WORKSHOP_LINE_CH: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_CHANGE_TEAM_CH: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_CHANGE_STATE_HC: _ClassVar[ePBMsgCode]
    PB_YM_CHANGEROLE_HC: _ClassVar[ePBMsgCode]
    PB_YM_CHANGEROLE_CH: _ClassVar[ePBMsgCode]
    PB_YM_VOICE_CH: _ClassVar[ePBMsgCode]
    PB_YM_VOICE_HC: _ClassVar[ePBMsgCode]
    PB_CLOUDSERVER_ROOM_AUTOMUTE_CH: _ClassVar[ePBMsgCode]
    PB_VEHICLE_WORKSHOP_LINE_UPDATE_CH: _ClassVar[ePBMsgCode]
    PB_MAP_EDIT_HANDLE_CH: _ClassVar[ePBMsgCode]
    PB_MAP_EDIT_REVOKE_CH: _ClassVar[ePBMsgCode]
    PB_CLOUD_ROOM_OWNER_START_GAME_CH: _ClassVar[ePBMsgCode]
    PB_CLOUD_ROOM_KICK_OFF_CH: _ClassVar[ePBMsgCode]
    PB_TRIGGER_OPENSTORE_HC: _ClassVar[ePBMsgCode]
    PB_USE_PACKINGFCMITEM_CH: _ClassVar[ePBMsgCode]
    PB_USE_PACKINGFCMITEM_HC: _ClassVar[ePBMsgCode]
    PB_CREATE_PACKINGCM_CH: _ClassVar[ePBMsgCode]
    PB_CREATE_PACKINGCM_HC: _ClassVar[ePBMsgCode]
    PB_PACKING_FCMDATA_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_INPUTCONTENT_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_INPUTKEYS_CH: _ClassVar[ePBMsgCode]
    PB_CLOUD_ROOM_STATUSTIME_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_VEHICLE_SLEEP_HC: _ClassVar[ePBMsgCode]
    PB_SENSOR_CONTAINER_DATA_CH: _ClassVar[ePBMsgCode]
    PB_SENSOR_CONTAINER_DATA_HC: _ClassVar[ePBMsgCode]
    PB_VEHICLE_BIND_ACTOR_HC: _ClassVar[ePBMsgCode]
    PB_DOOR_DATA_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CARRYACTOR_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_CARRYACTOR_HC: _ClassVar[ePBMsgCode]
    PB_VILLAGER_BODY_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_TAME_ACTOR_HC: _ClassVar[ePBMsgCode]
    PB_VILLAGER_MODIFY_NAME_CH: _ClassVar[ePBMsgCode]
    PB_VILLAGER_CLOTH_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_HEAD_DISPLAY_ICON_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAY_ANIM_BY_ID_HC: _ClassVar[ePBMsgCode]
    PB_VILLAGE_TOTEM_TIP_HC: _ClassVar[ePBMsgCode]
    PB_VILLAGE_TOTEM_ACTIVE_HC: _ClassVar[ePBMsgCode]
    PB_SAVE_TOMB_STONE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_LEVELMODE_HC: _ClassVar[ePBMsgCode]
    PB_ACTION_ATTR_STATE_HC: _ClassVar[ePBMsgCode]
    PB_EDU_ROLEINFO_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_GOTOPOS_CH: _ClassVar[ePBMsgCode]
    PB_IMPORT_MODEL_HC: _ClassVar[ePBMsgCode]
    PB_CUSTOM_MODEL_PRE_HC: _ClassVar[ePBMsgCode]
    PB_CUSTOM_MODEL_PRE_CH: _ClassVar[ePBMsgCode]
    PB_RESETDEFORMATION_CH: _ClassVar[ePBMsgCode]
    PB_DEFORMATION_SKIN_CH: _ClassVar[ePBMsgCode]
    PB_PLAYERTRANSFORMSKIN_HC: _ClassVar[ePBMsgCode]
    PB_RESTORE_DEFORMATION_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_SAVE_ARCH_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_PUSH_ARCH_CH: _ClassVar[ePBMsgCode]
    PB_LIGHTNING_HC: _ClassVar[ePBMsgCode]
    PB_INTERACT_MOBPACK_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_MOB_BACKPACK_HC: _ClassVar[ePBMsgCode]
    PB_MOVE_MOBBACKPACKITEM_CH: _ClassVar[ePBMsgCode]
    PB_INTERACT_MOBBACKPACKITEM_CH: _ClassVar[ePBMsgCode]
    PB_ALTAR_LUCKY_DRAW_CH: _ClassVar[ePBMsgCode]
    PB_SFACTIVITY_HC: _ClassVar[ePBMsgCode]
    PB_OPEN_DEVGOODSBUY_DIALOGHC: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_INFO_HC: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_TREE_STATE_HC: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_REQ_HC: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_TIME_CH: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_TIMEUPDATE_HC: _ClassVar[ePBMsgCode]
    PB_HOME_PRAY_ERROR_HC: _ClassVar[ePBMsgCode]
    PB_OPEN_HOMENPC_HC: _ClassVar[ePBMsgCode]
    PB_OPEN_HOMECLOSET_HC: _ClassVar[ePBMsgCode]
    PB_GODTEMPLE_CREATE_HC: _ClassVar[ePBMsgCode]
    PB_SHAPE_ADDITION_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_HOME_SUMMONPET_CH: _ClassVar[ePBMsgCode]
    PB_HOMELAND_RANCH_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_RANCH_ANIMAL_UPDATE_CH: _ClassVar[ePBMsgCode]
    PB_TRIGGER_GRAPHICS_HC: _ClassVar[ePBMsgCode]
    PB_USEITEM_BY_HOMELAND_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CUSTOM_BASEMODEL_HC: _ClassVar[ePBMsgCode]
    PB_CHANGE_ACTOR_MODEL_HC: _ClassVar[ePBMsgCode]
    PB_REQUEST_MODEL_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFIY_MODEL_HC: _ClassVar[ePBMsgCode]
    PB_VOICE_INFORM_CH: _ClassVar[ePBMsgCode]
    PB_VOICE_INFORM_HC: _ClassVar[ePBMsgCode]
    PB_RUNE_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_RUNE_OPERATE_SUCCESS_HC: _ClassVar[ePBMsgCode]
    PB_FURNACE_TEMPERATURE_CH: _ClassVar[ePBMsgCode]
    PB_TAKE_CONTAINER_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_POT_CONTAINER_SET_MAKE_CH: _ClassVar[ePBMsgCode]
    PB_UPDATE_POT_CONTAINER_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_STARSTATION_ADDED_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_STARSTATION_REMOVED_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_STARSTATION_CHANGENAMESTATUS_HC: _ClassVar[ePBMsgCode]
    PB_STARSTATION_CHANGENAMESTATUS_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_ENTER_STARSTATION_CABIN_HC: _ClassVar[ePBMsgCode]
    PB_LEAVE_STARSTATION_CABIN_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_LEAVE_STARSTATION_CABIN_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_STARSTATION_CABIN_LEVEL_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_CABIN_LEVEL_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_STARSTATION_CABIN_STATUS_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUS_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_CABIN_ADDED_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_CABIN_REMOVED_HC: _ClassVar[ePBMsgCode]
    PB_ADD_UNFINISHED_TRANSFER_RECORD_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_ADD_UNFINISHED_TRANSFER_RECORD_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_UNFINISHED_TRANSFER_RECORD_STATUS_HC: _ClassVar[ePBMsgCode]
    PB_REMOVE_UNFINISHED_TRANSFER_RECORD_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_REMOVE_UNFINISHED_TRANSFER_RECORD_HC: _ClassVar[ePBMsgCode]
    PB_STARSTATION_DATA_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_TRANSFER_BY_STRSTATION_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_PLAYER_TRANSFER_BY_STRSTATION_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_ACTIVATE_STARSTATION_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPGRADE_STARSTATION_CABIN_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_SIGN_INFO_HC: _ClassVar[ePBMsgCode]
    PB_REQUIRE_STARSTATION_TRANSFER_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_STARSTATION_TRANSFER_RESULT_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_EXPLOIT_CH: _ClassVar[ePBMsgCode]
    PB_BLOCK_EXPLOIT_HC: _ClassVar[ePBMsgCode]
    PB_VACANT_BOSS_STATE_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_REMOVEITEM_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_PLAYALTMANMUSIC_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_HC: _ClassVar[ePBMsgCode]
    PB_GAINITEMSTOBACKPACK_CH: _ClassVar[ePBMsgCode]
    PB_UPDATE_STARSTATION_CABIN_STATUSEND_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUSEND_HC: _ClassVar[ePBMsgCode]
    PB_ADD_STARSTATION_TRANSFER_DESC_CH: _ClassVar[ePBMsgCode]
    PB_ADDEXP_CH: _ClassVar[ePBMsgCode]
    PB_ADDEXPRESULT_HC: _ClassVar[ePBMsgCode]
    PB_COUSTOMUI_EVENT_CH: _ClassVar[ePBMsgCode]
    PB_ACHIEVEMENT_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_ACHIEVEMENT_UPDATE_CH: _ClassVar[ePBMsgCode]
    PB_BATTLEPASS_EVENT_HC: _ClassVar[ePBMsgCode]
    PB_ADDSTAR_CH: _ClassVar[ePBMsgCode]
    PB_USEHEARTH_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_STOP_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_STOP_ANIM_CH: _ClassVar[ePBMsgCode]
    PB_HOMELAND_RANCH_FOODER_CH: _ClassVar[ePBMsgCode]
    PB_HORSE_FLAG_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_RANCH_FOODERSTATE_HC: _ClassVar[ePBMsgCode]
    PB_ACHIEVEMENT_INITDATA_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_COOK_MENUBUY_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_COOK_MENUBUY_CH: _ClassVar[ePBMsgCode]
    PB_HOMELAND_FARM_SHOP_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_FARM_SHOP_CH: _ClassVar[ePBMsgCode]
    PB_HOMELAND_COOK_SPFURNITUREBUY_HC: _ClassVar[ePBMsgCode]
    PB_HOMELAND_COOK_SPFURNITUREBUY_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_OPENUI_HC: _ClassVar[ePBMsgCode]
    PB_ANSWER_LANTERNBIRD_CH: _ClassVar[ePBMsgCode]
    PB_EXCHANGEITEMSTOBACKPACK_CH: _ClassVar[ePBMsgCode]
    PB_EXCHANGEITEMSTOBACKPACKRESULT_HC: _ClassVar[ePBMsgCode]
    PB_CHANGE_QQMUSIC_PLAYER_HC: _ClassVar[ePBMsgCode]
    PB_CHANGE_QQMUSIC_PLAYER_CH: _ClassVar[ePBMsgCode]
    PB_SET_TIANGOU_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CLOSEUI_CH: _ClassVar[ePBMsgCode]
    PB_RIDE_INVISIBLE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAY_SOUND_CH: _ClassVar[ePBMsgCode]
    PB_ACTORINVITE_CH: _ClassVar[ePBMsgCode]
    PB_ACTORINVITE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SKIN_ACT_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SKIN_ACT_CH: _ClassVar[ePBMsgCode]
    PB_CHANGE_QQMUSIC_CLUB_HC: _ClassVar[ePBMsgCode]
    PB_CHANGE_QQMUSIC_CLUB_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_STOP_SKIN_ACT_HC: _ClassVar[ePBMsgCode]
    PB_MINICLUB_PLAYER_HC: _ClassVar[ePBMsgCode]
    PB_MINICLUB_PLAYER_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_STOP_SKIN_ACT_CH: _ClassVar[ePBMsgCode]
    PB_SPRAY_PAINT_INFO_CH: _ClassVar[ePBMsgCode]
    PB_ADD_PAINTED_INFO_HC: _ClassVar[ePBMsgCode]
    PB_REMOVE_PAINTED_INFO_HC: _ClassVar[ePBMsgCode]
    PB_Equip_Weapon_HC: _ClassVar[ePBMsgCode]
    PB_Equip_Weapon_CH: _ClassVar[ePBMsgCode]
    PB_PLAYEFFECT_CH: _ClassVar[ePBMsgCode]
    PB_GainItemsUserDatastrToBackPack_CH: _ClassVar[ePBMsgCode]
    PB_UseMusicYuPu_CH: _ClassVar[ePBMsgCode]
    PB_DanceByPlaying_CH: _ClassVar[ePBMsgCode]
    PB_StopDanceByPlaying_CH: _ClassVar[ePBMsgCode]
    PB_StartAct_CH: _ClassVar[ePBMsgCode]
    PB_StopAct_CH: _ClassVar[ePBMsgCode]
    PB_TOP_BRAND_CH: _ClassVar[ePBMsgCode]
    PB_TOP_BRAND_HC: _ClassVar[ePBMsgCode]
    PB_CHEAT_CHECK_CH: _ClassVar[ePBMsgCode]
    PB_WEAPON_POINT_HC: _ClassVar[ePBMsgCode]
    PB_GAME_MODE_CHANGE: _ClassVar[ePBMsgCode]
    PB_ADDLIGHTCHAIN_HC: _ClassVar[ePBMsgCode]
    PB_STARTFISHING_CH: _ClassVar[ePBMsgCode]
    PB_STARTFISHING_HC: _ClassVar[ePBMsgCode]
    PB_ENDFISHING_CH: _ClassVar[ePBMsgCode]
    PB_ENDFISHING_HC: _ClassVar[ePBMsgCode]
    PB_QUITFISHING_CH: _ClassVar[ePBMsgCode]
    PB_QUITFISHING_HC: _ClassVar[ePBMsgCode]
    PB_CHANGEFISHINGSTAGE_HC: _ClassVar[ePBMsgCode]
    PB_CHANGEEXPOSEPOS_CH: _ClassVar[ePBMsgCode]
    PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_CH: _ClassVar[ePBMsgCode]
    PB_BIND_ITEM_TO_ACTOR_HC: _ClassVar[ePBMsgCode]
    PB_FISHING_BEGIN_FLASH_HC: _ClassVar[ePBMsgCode]
    PB_END_PLAY_FISH_CH: _ClassVar[ePBMsgCode]
    PB_CHANGE_SHOW_EQUIP_HC: _ClassVar[ePBMsgCode]
    PB_RESET_ROLE_FLAGS: _ClassVar[ePBMsgCode]
    PB_BIND_PLAYER_TO_PHYSICS_PLAT_HC: _ClassVar[ePBMsgCode]
    PB_UNBIND_PLAYER_TO_PHYSICS_PLAT_HC: _ClassVar[ePBMsgCode]
    PB_PHYSICS_COM_UPDATE: _ClassVar[ePBMsgCode]
    PB_PHYSICS_COM_PLAT_LOCAL_POS: _ClassVar[ePBMsgCode]
    PB_EFFECT_COM_PARTICLE_UPDATE: _ClassVar[ePBMsgCode]
    PB_SOUND_COM_UPDATE: _ClassVar[ePBMsgCode]
    PB_BIND_PLAYER_TO_PHYSICS_PLAT_CH: _ClassVar[ePBMsgCode]
    PB_UNBIND_PLAYER_TO_PHYSICS_PLAT_CH: _ClassVar[ePBMsgCode]
    PB_METEOR_SHOWER_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_TRANSFER_HC: _ClassVar[ePBMsgCode]
    PB_NOTIFY_PLAYER_BLOCK_CHANGE_COLOR_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAY_HAND_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_PLAY_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_BLOCKSTRUCT_UPDATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_ENTER_LIVINGWHEEL_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_LEAVE_LIVINGWHEEL_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_WORKING_LIVINGWHEEL_CH: _ClassVar[ePBMsgCode]
    PB_UPDATE_LIVINGWHEEL_HC: _ClassVar[ePBMsgCode]
    PB_REQUEST_LIVINGWHEEL_CH: _ClassVar[ePBMsgCode]
    PB_CREATE_BLOCK_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_VILLAGER_INFO_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SANDWORM_SHOW_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SANDWORM_CAN_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SCASLE_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SANDWORM_NIBBLE_PLAYER_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_CREATE_THORNBALL_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_REBOUNDS_ATTACK_UP_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_REBOUNDS_ATTACK_ROUND_HC: _ClassVar[ePBMsgCode]
    PB_REMOVE_SAWTOOTH_THORNB_HC: _ClassVar[ePBMsgCode]
    PB_CH_NOTICE_ATTACKED_UP_CH: _ClassVar[ePBMsgCode]
    PB_CH_NOTICE_ATTACKED_ROUND_CH: _ClassVar[ePBMsgCode]
    PB_CH_NOTICE_REMOVE_SAWTOOTH_THORNBA_CH: _ClassVar[ePBMsgCode]
    PB_ATTR_SHAPE_SHIFT_RIGHT_CLICK_CH: _ClassVar[ePBMsgCode]
    PB_DESTORY_BLOCK_CH: _ClassVar[ePBMsgCode]
    PB_WATER_PRESSURE_CH: _ClassVar[ePBMsgCode]
    PB_ATTR_SHAPE_SHIFT_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_COCONUT_HIT_HC: _ClassVar[ePBMsgCode]
    PB_COCONUT_SKIP_NIGHT_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SHARK_BITE_PLAYER_MOVE_HC: _ClassVar[ePBMsgCode]
    PB_CRAB_INFO_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_CRAB_CLICKCOUNT_RESET_CH: _ClassVar[ePBMsgCode]
    PB_HIPPOCAMPUS_REFRESHMODEL_HC: _ClassVar[ePBMsgCode]
    PB_HIPPOCAMPUS_CHANGECOLOR_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACKGRID_DRUATION_HC: _ClassVar[ePBMsgCode]
    PB_GUNLOGIC_USE_WaterCanoonSkill_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_SNOWMAN_PART_SHOW_HC: _ClassVar[ePBMsgCode]
    PB_MOB_PART_SHOW_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_SHAKE_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_DISSOLVE_COMPONENT_OPEN_HC: _ClassVar[ePBMsgCode]
    PB_COOKBOOKINFO_HC: _ClassVar[ePBMsgCode]
    PB_STOVETAKE_CH: _ClassVar[ePBMsgCode]
    PB_SETHPVISIBLE_HC: _ClassVar[ePBMsgCode]
    PB_SKILLPLAYANIM_HC: _ClassVar[ePBMsgCode]
    PB_SKILLSTOPANIM_HC: _ClassVar[ePBMsgCode]
    PB_SKILLPLAYBODYEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_SKILLSTOPBODYEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_SKILLWORLDPLAYBODYEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_ACCUMULATOR_HC: _ClassVar[ePBMsgCode]
    PB_SKILLPLAYTOOLANIM_HC: _ClassVar[ePBMsgCode]
    PB_SKILLSTOPTOOLANIM_HC: _ClassVar[ePBMsgCode]
    PB_SKILLSETCHARGEMOVE_HC: _ClassVar[ePBMsgCode]
    PB_SKILLMOVE_HC: _ClassVar[ePBMsgCode]
    PB_SKILLCAMERA_HC: _ClassVar[ePBMsgCode]
    PB_STOPWEAPONANIM_HC: _ClassVar[ePBMsgCode]
    PB_STOPWEAPONANIM_CH: _ClassVar[ePBMsgCode]
    PB_STOPWEAPONMOTION_HC: _ClassVar[ePBMsgCode]
    PB_STOPWEAPONMOTION_CH: _ClassVar[ePBMsgCode]
    PB_SETLOCOTYPE_HC: _ClassVar[ePBMsgCode]
    PB_BASESTATE_HC: _ClassVar[ePBMsgCode]
    PB_SETMOVEMENT_MODE_HC: _ClassVar[ePBMsgCode]
    PB_7000_HORSEFLYSTATE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_CAMERACONFIG_HC: _ClassVar[ePBMsgCode]
    PB_BACKPACK_NUM_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_PLAY_SKIN_VOICE_CH: _ClassVar[ePBMsgCode]
    PB_PLAY_SKIN_VOICE_HC: _ClassVar[ePBMsgCode]
    PB_BOX_PLAY_ANI_CH: _ClassVar[ePBMsgCode]
    PB_NEW_YEAR_BOSS_STAGE_HC: _ClassVar[ePBMsgCode]
    PB_NEW_YEAR_HP_HC: _ClassVar[ePBMsgCode]
    PB_NEW_YEAR_MONSTER_POS_HC: _ClassVar[ePBMsgCode]
    PB_STORAGE_BOX_PUT_IN_ALL_CH: _ClassVar[ePBMsgCode]
    PB_TELEPORT_SHOWPANEL_HC: _ClassVar[ePBMsgCode]
    PB_DYNAMIC_PROTO_HC: _ClassVar[ePBMsgCode]
    PB_DYNAMIC_PROTO_CH: _ClassVar[ePBMsgCode]
    PB_STORAGE_BOX_TAKE_OUT_ALL_CH: _ClassVar[ePBMsgCode]
    PB_SYNC_DYEABLE_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_CUSTOM_PBC_CH: _ClassVar[ePBMsgCode]
    PB_CUSTOM_PBC_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_LASER_POINTER_HC: _ClassVar[ePBMsgCode]
    PB_UPDATE_LASER_POINTER_CH: _ClassVar[ePBMsgCode]
    PB_PHYSICS_INPUT_FRAME: _ClassVar[ePBMsgCode]
    PB_PHYSICS_ASYNC_TIMESTAMP: _ClassVar[ePBMsgCode]
    PB_PHYSICS_SETUP_TIMESTAMP: _ClassVar[ePBMsgCode]
    PB_PHYSICS_TIME_DILATION: _ClassVar[ePBMsgCode]
    PB_PHYSICS_REPLICATED_INPUT_CH: _ClassVar[ePBMsgCode]
    PB_PHYSICS_REPLICATED_INPUT_HC: _ClassVar[ePBMsgCode]
    PB_PHYSICS_REPLICATED_STATE_CH: _ClassVar[ePBMsgCode]
    PB_PHYSICS_REPLICATED_STATE_HC: _ClassVar[ePBMsgCode]
    PB_PHYSICS_COMMON_REPLICATED: _ClassVar[ePBMsgCode]
    PB_CUSTOM_MSG: _ClassVar[ePBMsgCode]
    PB_BlockData_CH: _ClassVar[ePBMsgCode]
    PB_PUSHSNOWBALL_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_PUSHSNOWBALL_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_PUSHSNOWBALL_SIZECHANGE_HC: _ClassVar[ePBMsgCode]
    PB_PLAY_EFFECT_SHADER_HC: _ClassVar[ePBMsgCode]
    PB_NEW_REPAIR_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_SEND_OBJACTOR_MSG: _ClassVar[ePBMsgCode]
    PB_ADD_BULLETHOLE_HC: _ClassVar[ePBMsgCode]
    PB_ACTORSHOOT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_FIREWORK_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAYANIM_NEW_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_SPEED_CHANGE_HC: _ClassVar[ePBMsgCode]
    PB_TASK_INITDATA_HC: _ClassVar[ePBMsgCode]
    PB_BYMOUNT_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PICKUP_ACTOR_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_DROP_ACTOR_HC: _ClassVar[ePBMsgCode]
    PB_GROUP_WEATHER_HC: _ClassVar[ePBMsgCode]
    PB_BYMOUNT_CH: _ClassVar[ePBMsgCode]
    PB_ADD_BULLETHOLEV2_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_SET_ATTR_TOTRACKINGPLAYERS_HC: _ClassVar[ePBMsgCode]
    PB_TASK_OBJECTIVE_INITDATA_HC: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONMOTION_HC: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONMOTION_CH: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONANIM_HC: _ClassVar[ePBMsgCode]
    PB_PLAYWEAPONANIM_CH: _ClassVar[ePBMsgCode]
    PB_ACTORJUMP_HC: _ClassVar[ePBMsgCode]
    PB_TECHTREEINFOCHANGE_HC: _ClassVar[ePBMsgCode]
    PB_ACTORSETGRAVITYFAILURE_HC: _ClassVar[ePBMsgCode]
    PB_SETINTERACTACTORMECHA_HC: _ClassVar[ePBMsgCode]
    PB_UNLOCKITEMS_HC: _ClassVar[ePBMsgCode]
    PB_CHECKNEWUNLOCKITEM_CH: _ClassVar[ePBMsgCode]
    PB_PLAY_CAMERA_SHAKE_HC: _ClassVar[ePBMsgCode]
    PB_RECENTLYMAKECRAFT_CH: _ClassVar[ePBMsgCode]
    PB_MECHAKINETICUINT_HC: _ClassVar[ePBMsgCode]
    PB_MECHAKINETICNODEDATA_HC: _ClassVar[ePBMsgCode]
    PB_CONTAINER_UI_DATA_HC: _ClassVar[ePBMsgCode]
    PB_CONTAINER_UI_DATA_CH: _ClassVar[ePBMsgCode]
    PB_MECHARECOVERYHEAD_HC: _ClassVar[ePBMsgCode]
    PB_MECHA_TUNNEL_ANIM_PLAY_HC: _ClassVar[ePBMsgCode]
    PB_MECHA_STRUCTURE_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_MECHA_STRUCTURE_OPERATE_CH: _ClassVar[ePBMsgCode]
    PB_MECHA_STRUCTURE_OPERATE_HC: _ClassVar[ePBMsgCode]
    PB_TRANSFER_GOOD_COMP_HC: _ClassVar[ePBMsgCode]
    PB_PICK_TRANSFER_GOOD_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_MECHA_KINETNODELOGIC_DATA_HC: _ClassVar[ePBMsgCode]
    PB_MECHA_ADDKINETNODELOGIC_HC: _ClassVar[ePBMsgCode]
    PB_IRONDOMEESSENCE_DISEQUIP_CH: _ClassVar[ePBMsgCode]
    PB_IRON_HC: _ClassVar[ePBMsgCode]
    PB_IRONDOMEESSENCE_EQUIP_HC: _ClassVar[ePBMsgCode]
    PB_PART_HC: _ClassVar[ePBMsgCode]
    PB_PARTMANAGER_HC: _ClassVar[ePBMsgCode]
    PB_BLOCKTEXTURECOLORS_HC: _ClassVar[ePBMsgCode]
    PB_LOOKATACTOR_HC: _ClassVar[ePBMsgCode]
    PB_SANDBOX_LUA_LOG_DATA_CH: _ClassVar[ePBMsgCode]
    PB_SANDBOX_LUA_LOG_DATA_HC: _ClassVar[ePBMsgCode]
    PB_AI_TTS_AUDIO_HC: _ClassVar[ePBMsgCode]
    PB_AI_ASR_AUDIO_CH: _ClassVar[ePBMsgCode]
    PB_MODCONTAINER_HC: _ClassVar[ePBMsgCode]
    PB_WBP_MSG_HC: _ClassVar[ePBMsgCode]
    PB_WBP_MSG_CH: _ClassVar[ePBMsgCode]
    PB_RAKEPLANTITEMID_CH: _ClassVar[ePBMsgCode]
    PB_AVATAR_PARTS_PRIORITY_SYNC_HC: _ClassVar[ePBMsgCode]
    PB_AVATAR_PARTS_PRIORITY_SYNC_ALL_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_CHAT_BUBBLE_HC: _ClassVar[ePBMsgCode]
    PB_SLEEP_MSG_HC: _ClassVar[ePBMsgCode]
    PB_DROPITEM_STATE_HC: _ClassVar[ePBMsgCode]
    PB_DROPITEM_INTERACT_RESULT_CH: _ClassVar[ePBMsgCode]
    PB_ACTOR_SWITCH_PHYSICTYPE_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_USE_ITEM_CH: _ClassVar[ePBMsgCode]
    PB_PLAYER_PLAY_HAND_ANIM_HC: _ClassVar[ePBMsgCode]
    PB_PLAYER_PLAY_DIG_BLOCK_EFFECT_HC: _ClassVar[ePBMsgCode]
    PB_ACTOR_PLAYANIM_FINISH_CH: _ClassVar[ePBMsgCode]
    PB_LIVING_TIMERXRAYEFFECT_HC: _ClassVar[ePBMsgCode]
    PB_BLOCK_MINERALPROSPECT_HC: _ClassVar[ePBMsgCode]
    PB_WORLD_SYNC_SAVE_HC: _ClassVar[ePBMsgCode]
    PB_MAX_MSG_CODE: _ClassVar[ePBMsgCode]

class ePBModContainerOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_MODCONTAINER_MODELPART: _ClassVar[ePBModContainerOp]

class ePBModContainerModelPartOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_MODCONTAINER_MODELPART_ADD: _ClassVar[ePBModContainerModelPartOp]
    PB_MODCONTAINER_MODELPART_DELETE: _ClassVar[ePBModContainerModelPartOp]
    PB_MODCONTAINER_MODELPART_MESHSTATE: _ClassVar[ePBModContainerModelPartOp]

class ePBActorTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ACTORTYPEGENERAL: _ClassVar[ePBActorTypes]
    PB_ACTORTYPEROLE: _ClassVar[ePBActorTypes]
    PB_ACTORTYPEMONSTER: _ClassVar[ePBActorTypes]
    PB_ACTORTYPEBOSS: _ClassVar[ePBActorTypes]
    PB_ACTORTYPEBLOCK: _ClassVar[ePBActorTypes]
    PB_ACTORTYPEITEM: _ClassVar[ePBActorTypes]

class ePBStanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_STANCESTAND: _ClassVar[ePBStanceType]
    PB_STANCEWALK: _ClassVar[ePBStanceType]
    PB_STANCERUN: _ClassVar[ePBStanceType]
    PB_STANCEJUMP: _ClassVar[ePBStanceType]
    PB_STANCELAY: _ClassVar[ePBStanceType]
    PB_STANCESWIM: _ClassVar[ePBStanceType]
    PB_STANCEFLY: _ClassVar[ePBStanceType]

class ePBEffectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_EFFECT_PARTICLE: _ClassVar[ePBEffectType]
    PB_EFFECT_PICKITEM: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND: _ClassVar[ePBEffectType]
    PB_EFFECT_ACTORBODY: _ClassVar[ePBEffectType]
    PB_EFFECT_DESTROYBLOCK: _ClassVar[ePBEffectType]
    PB_EFFECT_PLAYMUSICGRID: _ClassVar[ePBEffectType]
    PB_EFFECT_STOPMUSICGRID: _ClassVar[ePBEffectType]
    PB_EFFECT_STRINGACTORBODY: _ClassVar[ePBEffectType]
    PB_EFFECT_CRACKBLOCK: _ClassVar[ePBEffectType]
    PB_EFFECT_TIRGGERSOUND: _ClassVar[ePBEffectType]
    PB_EFFECT_VEHICLE: _ClassVar[ePBEffectType]
    PB_EFFECT_STOPPARTICLE: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NEW: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NEW_FOR_TRACK: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NEW_STOP: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NOTE: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NOTE_STOP: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUNDID: _ClassVar[ePBEffectType]
    PB_EFFECT_PARTICLEID: _ClassVar[ePBEffectType]
    PB_EFFECT_SOUND_NEW_PAUSE: _ClassVar[ePBEffectType]

class eEffectIDX(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Volume: _ClassVar[eEffectIDX]
    Pitch: _ClassVar[eEffectIDX]
    Flags: _ClassVar[eEffectIDX]
    Segment: _ClassVar[eEffectIDX]
    PosX: _ClassVar[eEffectIDX]
    PosY: _ClassVar[eEffectIDX]
    PosZ: _ClassVar[eEffectIDX]
PB_ERROR_UNKNOWN: ePBErrorCode
PB_ERROR_WRONG_MSG_CODE: ePBErrorCode
PB_ERROR_WRONG_REQUESTER: ePBErrorCode
PB_ERROR_WRONG_ARGS: ePBErrorCode
PB_ERROR_PLAYER_NOT_LOGIN: ePBErrorCode
PB_ERROR_ILLEGAL_ARGS: ePBErrorCode
PB_ERROR_OP_NOT_FOUND: ePBErrorCode
PB_ERROR_BACKPACK_FULL: ePBErrorCode
PB_ERROR_STORAGE_FULL: ePBErrorCode
PB_ERROR_ENCHANT_NOT_ENOUGH: ePBErrorCode
PB_ERROR_ENCHANT_FAILED: ePBErrorCode
PB_ERROR_ENCHANT_NOT_CHANGED: ePBErrorCode
PB_ERROR_CRAFT_NOT_ENOUGH: ePBErrorCode
PB_ERROR_STAR_NOT_ENOUGH: ePBErrorCode
PB_ERROR_REPAIR_NOT_ENOUGH: ePBErrorCode
PB_ERROR_REPAIR_NOT_DAMAGED: ePBErrorCode
PB_ERROR_ROLE_ENTER_BANNED: ePBErrorCode
PB_ERROR_ROLE_ENTER_TOO_OFTEN: ePBErrorCode
PB_ERROR_ROLE_ENTER_SERVER_FULL: ePBErrorCode
PB_ERROR_ROLE_ENTER_SERVER_CLOSING: ePBErrorCode
PB_ERROR_ROLE_MOVE_ILLEGAL_POS: ePBErrorCode
PB_MAX_ERROR_CODE: ePBErrorCode
PB_REQ_ERROR_HC: ePBMsgCode
PB_HEARTBEAT_CH: ePBMsgCode
PB_HEARTBEAT_HC: ePBMsgCode
PB_SYNC_CHUNK_DATA_CH: ePBMsgCode
PB_SYNC_CHUNK_DATA_HC: ePBMsgCode
PB_BLOCK_DATA_UPDATE_CH: ePBMsgCode
PB_BLOCK_DATA_UPDATE_HC: ePBMsgCode
PB_SYNC_SECTION_LIGHT_DATA_HC: ePBMsgCode
PB_OVERRIDE_LIGHT_DATA_HC: ePBMsgCode
PB_ROLE_ENTER_WORLD_CH: ePBMsgCode
PB_ROLE_ENTER_WORLD_HC: ePBMsgCode
PB_ROLE_LEAVE_WORLD_CH: ePBMsgCode
PB_ROLE_LEAVE_WORLD_HC: ePBMsgCode
PB_ACTOR_ENTER_AOI_HC: ePBMsgCode
PB_ACTOR_LEAVE_AOI_HC: ePBMsgCode
PB_GAME_LEADER_SWITCH_HC: ePBMsgCode
PB_GENERAL_ENTER_AOI_HC: ePBMsgCode
PB_PVP_ACTIVITY_CONFIG_CH: ePBMsgCode
PB_ROLE_CHECK_JOINFROMSRC_CH: ePBMsgCode
PB_ROLE_MOVE_CH: ePBMsgCode
PB_TRAIN_MOVE_CH: ePBMsgCode
PB_ACTOR_MOVE_HC: ePBMsgCode
PB_TRAIN_MOVE_HC: ePBMsgCode
PB_ACTOR_MOVEV2_HC: ePBMsgCode
PB_ACTOR_TELEPORT_CH: ePBMsgCode
PB_ACTOR_TELEPORT_HC: ePBMsgCode
PB_ACTOR_MOTION_HC: ePBMsgCode
PB_MECHA_MOTION_HC: ePBMsgCode
PB_GUN_INFO_CH: ePBMsgCode
PB_SYNC_SETINFO_CH: ePBMsgCode
PB_SYNC_GRIDUSERDATA_CH: ePBMsgCode
PB_SYNC_GRIDUSERDATA_HC: ePBMsgCode
PB_SYNC_TRIGGERBLOCK_HC: ePBMsgCode
PB_FULLROT_ACTOR_MOVE_HC: ePBMsgCode
PB_ACTOR_MOTIONV2_HC: ePBMsgCode
PB_ACTOR_MOVEV3_HC: ePBMsgCode
PB_ACTOR_MODELCHG_HC: ePBMsgCode
PB_BLOCK_INTERACT_HC: ePBMsgCode
PB_BLOCK_PUNCH_HC: ePBMsgCode
PB_ITEM_USE_HC: ePBMsgCode
PB_ACTOR_INTERACT_HC: ePBMsgCode
PB_BLOCK_INTERACT_END_CH: ePBMsgCode
PB_BLOCK_INTERACT_CH: ePBMsgCode
PB_BLOCK_PUNCH_CH: ePBMsgCode
PB_ITEM_USE_CH: ePBMsgCode
PB_ACTOR_INTERACT_CH: ePBMsgCode
PB_ACTOR_ANIM_CH: ePBMsgCode
PB_ACTOR_ANIM_HC: ePBMsgCode
PB_BACKPACK_GRID_UPDATE_HC: ePBMsgCode
PB_BACKPACK_GRID_SWAP_CH: ePBMsgCode
PB_BACKPACK_MOVEITEM_CH: ePBMsgCode
PB_BACKPACK_GRID_DISCARD_CH: ePBMsgCode
PB_BACKPACK_EQUIP_WEAPON_CH: ePBMsgCode
PB_BACKPACK_EQUIP_WEAPON_HC: ePBMsgCode
PB_CLOSE_CONTAINER_CH: ePBMsgCode
PB_CLOSE_CONTAINER_HC: ePBMsgCode
PB_OPEN_CONTAINER_HC: ePBMsgCode
PB_UPDATE_CONTAINER_HC: ePBMsgCode
PB_SET_CONTAINERTEXT_CH: ePBMsgCode
PB_ACTOR_EQUIP_ITEM_HC: ePBMsgCode
PB_BACKPACK_STORE_CH: ePBMsgCode
PB_BACKPACK_LOOT_CH: ePBMsgCode
PB_BACKPACK_SORT_CH: ePBMsgCode
PB_BACKPACK_SETITEM_CH: ePBMsgCode
PB_BACKPACK_SHORTCUT_OP_CH: ePBMsgCode
PB_STORAGEBOX_SORT_CH: ePBMsgCode
PB_CRAFT_ITEM_CH: ePBMsgCode
PB_ENCHANT_ITEM_CH: ePBMsgCode
PB_ENCHANT_ITEM_RANDOM_CH: ePBMsgCode
PB_ENCHANT_ITEM_SUCCESS_HC: ePBMsgCode
PB_REPAIR_ITEM_CH: ePBMsgCode
PB_REPAIR_ITEM_SUCCESS_HC: ePBMsgCode
PB_GUN_DORELOAD_CH: ePBMsgCode
PB_GUN_DORELOAD_HC: ePBMsgCode
PB_GUN_RECOVERY_CH: ePBMsgCode
PB_ACCOUNT_HORSE_CH: ePBMsgCode
PB_ACCOUNT_HORSE_HC: ePBMsgCode
PB_ACTOT_SET_CUSTOM_CH: ePBMsgCode
PB_ACTOT_SET_CUSTOM_HC: ePBMsgCode
PB_ACTOR_PLAY_ANIM_CH: ePBMsgCode
PB_ACTOR_PLAY_ANIM_HC: ePBMsgCode
PB_ACTOR_ATTACK_CH: ePBMsgCode
PB_ACTOR_DEFANCESTATE_CH: ePBMsgCode
PB_RCLICKUP_INTERACT_CH: ePBMsgCode
PB_RCLICKUP_INTERACT_HC: ePBMsgCode
PB_MOUSE_EVENT_CH: ePBMsgCode
PB_PLAYER_GUNACTION_CH: ePBMsgCode
PB_PLAYER_GUNACTION_STATE_HC: ePBMsgCode
PB_LIVING_INTERACT_NEW_CH: ePBMsgCode
PB_LIVING_INTERACT_NEW_NEWTAME_HC: ePBMsgCode
PB_LIVING_REPRODUCTION_HC: ePBMsgCode
PB_LIVING_INTERACT_NEW_NEWGROW_HC: ePBMsgCode
PB_TRAIN_FOLLOW_OP_CH: ePBMsgCode
PB_TRAIN_FOLLOW_OP_HC: ePBMsgCode
PB_TRAIN_REFINABLE_TAKE_RESULT_CH: ePBMsgCode
PB_ACTOR_ATTR_CHANGE_HC: ePBMsgCode
PB_ACTOR_BUFF_CHANGE_HC: ePBMsgCode
PB_ACTOR_REVIVE_CH: ePBMsgCode
PB_ACTOR_REVIVE_HC: ePBMsgCode
PB_PLAYER_ATTR_CHANGE_HC: ePBMsgCode
PB_MOB_BODY_CHANGE_HC: ePBMsgCode
PB_ROOM_JRUISDICTION_CH: ePBMsgCode
PB_ROOM_JRUISDICTION_HC: ePBMsgCode
PB_CHAT_CH: ePBMsgCode
PB_CHAT_HC: ePBMsgCode
PB_WGLOBAL_UPDATE_HC: ePBMsgCode
PB_PLAYERS_UPDATEINFO_HC: ePBMsgCode
PB_GAME_TIPS_HC: ePBMsgCode
PB_PLAYEFFECT_HC: ePBMsgCode
PB_PLAYER_MOUNTACTOR_CH: ePBMsgCode
PB_PLAYER_MOUNTACTOR_HC: ePBMsgCode
PB_PLAYER_MOVEINPUT_CH: ePBMsgCode
PB_PLAYER_REVIVEPOINT_CH: ePBMsgCode
PB_PLAYER_REVIVEPOINT_HC: ePBMsgCode
PB_PLAYER_SLEEP_HC: ePBMsgCode
PB_PLAYER_SLEEP_CH: ePBMsgCode
PB_OPENWINDOW_HC: ePBMsgCode
PB_NPCTRADE_CH: ePBMsgCode
PB_LASTPING_HC: ePBMsgCode
PB_CGAMESTAGE_HC: ePBMsgCode
PB_PLAYERPERMIT_HC: ePBMsgCode
PB_PLAYEFFECT_HC_V2: ePBMsgCode
PB_SKILLCD_HC: ePBMsgCode
PB_ACTOR_MOUNTACTOR_HC: ePBMsgCode
PB_ACTOR_REVERSE_HC: ePBMsgCode
PB_ACTOR_BIND_HC: ePBMsgCode
PB_PLAYWEAPONEFFECT_HC: ePBMsgCode
PB_SCRIPTVAR_HC: ePBMsgCode
PB_PLAYWEAPONEFFECT_CH: ePBMsgCode
PB_SET_SPECTATORMODE_CH: ePBMsgCode
PB_SET_SPECTATORMODE_HC: ePBMsgCode
PB_SET_SPECTATORTYPE_CH: ePBMsgCode
PB_SET_SPECTATORTYPE_HC: ePBMsgCode
PB_SET_SPECTATOR_PLAYER_CH: ePBMsgCode
PB_OTHER_PLAYER_ATTR_CHANGE_HC: ePBMsgCode
PB_PLAYER_LEAVE_HC: ePBMsgCode
PB_TEAM_SCORE_HC: ePBMsgCode
PB_SET_TEAM_HC: ePBMsgCode
PB_SET_PLAYER_GAME_INFO_HC: ePBMsgCode
PB_SYNC_MOVE_CH: ePBMsgCode
PB_SYNC_MOVE_HC: ePBMsgCode
PB_UIDISPLAYHORSE_HC: ePBMsgCode
PB_SYNC_MOVEV2_CH: ePBMsgCode
PB_SYNC_MOVEV2_HC: ePBMsgCode
PB_UPDATE_MOVE_INTERVAL_HC: ePBMsgCode
PB_MOVE_DIFF_CH: ePBMsgCode
PB_PLAYEFFECT_HC_V3: ePBMsgCode
PB_SYNC_MOVEV4_CH: ePBMsgCode
PB_SYNC_MOVEV4_HC: ePBMsgCode
PB_ACTOR_GET_ACCOUNT_ITEM: ePBMsgCode
PB_SPECIALITEM_USE_CH: ePBMsgCode
PB_SPECIALITEM_USE_HC: ePBMsgCode
PB_LEAVE_ROOM_INFO_HC: ePBMsgCode
PB_INVITEJOINROOM_HC: ePBMsgCode
PB_SET_SPECTATOR_PLAYER_HC: ePBMsgCode
PB_SET_PLAYER_MODEL_ANI_CH: ePBMsgCode
PB_SET_PLAYER_MODEL_ANI_HC: ePBMsgCode
PB_SEND_VIEWMODE_SPECTATOR_CH: ePBMsgCode
PB_SEND_VIEWMODE_SPECTATOR_HC: ePBMsgCode
PB_SET_BOBBING_SPECTATOR_CH: ePBMsgCode
PB_SET_BOBBING_SPECTATOR_HC: ePBMsgCode
PB_ITEM_SKILL_USE_CH: ePBMsgCode
PB_ITEM_SKILL_USE_HC: ePBMsgCode
PB_BALL_OPERATE_CH: ePBMsgCode
PB_BALL_OPERATE_HC: ePBMsgCode
PB_RESET_ROUND_HC: ePBMsgCode
PB_ROCKET_ATTRIB_CHANGE_HC: ePBMsgCode
PB_ROCKET_TELEPORT_CH: ePBMsgCode
PB_SET_HOOK_HC: ePBMsgCode
PB_SET_HOOK_CH: ePBMsgCode
PB_WORLD_TIMES_HC: ePBMsgCode
PB_STATISTIC_HC: ePBMsgCode
PB_TOTEMPOINT_HC: ePBMsgCode
PB_NEED_CONTAINER_PASSWORD_HC: ePBMsgCode
PB_NEED_CONTAINER_PASSWORD_CH: ePBMsgCode
PB_HORSEFLYSTATE_HC: ePBMsgCode
PB_OPENDIALOGUE_HC: ePBMsgCode
PB_CLOSEDIALOGUE_HC: ePBMsgCode
PB_CLOSEDIALOGUE_CH: ePBMsgCode
PB_ANSWERTASK_CH: ePBMsgCode
PB_UPDATETASK_HC: ePBMsgCode
PB_SYNCTASK_ENTERWORLD_HC: ePBMsgCode
PB_COMPLETE_TASK_HC: ePBMsgCode
PB_COMPLETE_TASK_CH: ePBMsgCode
PB_ATTRACT_ATTRIB_CHANGE_HC: ePBMsgCode
PB_ACTOR_BODY_TEXTURE_HC: ePBMsgCode
PB_PLAYER_ADDAVARTAR_HC: ePBMsgCode
PB_PLAYER_CHANGEMODEL_HC: ePBMsgCode
PB_PLAYER_AVARTARCOLOR_HC: ePBMsgCode
PB_PLAYER_ACT_CH: ePBMsgCode
PB_PLAYER_ACT_HC: ePBMsgCode
PB_CREATE_BLUEPRINT_HC: ePBMsgCode
PB_MEASURE_DISTANCE_HC: ePBMsgCode
PB_BLUEPRINT_PREBLOCK_CH: ePBMsgCode
PB_BLUEPRINT_PREBLOCK_HC: ePBMsgCode
PB_GRAVITY_OPERATE_CH: ePBMsgCode
PB_GRAVITY_OPERATE_HC: ePBMsgCode
PB_PLAYER_BODY_COLOR_HC: ePBMsgCode
PB_CUSTOM_MODEL_HC: ePBMsgCode
PB_CUSTOM_ITEMIDS_HC: ePBMsgCode
PB_PLAYER_SPAWN_POINT_HC: ePBMsgCode
PB_MAKE_CUSTOM_MODEL_CH: ePBMsgCode
PB_SELECT_MOB_SPAWN_CH: ePBMsgCode
PB_CUSTOM_MODELCLASS_HC: ePBMsgCode
PB_TRANSFER_RECORD_HC: ePBMsgCode
PB_TRANSFER_RECORD_CH: ePBMsgCode
PB_TRANSFER_ADD_DEL_HC: ePBMsgCode
PB_TRANSFER_STATUS_CH: ePBMsgCode
PB_TRANSFER_STATUS_HC: ePBMsgCode
PB_SYNC_LOVEAMBASSADOR_ICONID_HC: ePBMsgCode
PB_SYNC_LOVEAMBASSADOR_ICONID_CH: ePBMsgCode
PB_TRANSFER_DATA_HC: ePBMsgCode
PB_ACTOR_TRANSFER_CH: ePBMsgCode
PB_ACTOR_TRANSFER_HC: ePBMsgCode
PB_BACKPACK_SETITEMWITHOUTLIMIT_CH: ePBMsgCode
PB_NPCSHOP_GETSHOPINFO_CH: ePBMsgCode
PB_NPCSHOP_RESPGETSHOPINFO_HC: ePBMsgCode
PB_NPCSHOP_BUYSKU_CH: ePBMsgCode
PB_NPCSHOP_NOTIFYBUY_HC: ePBMsgCode
PB_VEHICLE_MOVE_HC: ePBMsgCode
PB_OPEN_EDIT_ACTORMODEL_HC: ePBMsgCode
PB_CLOSE_EDIT_ACTORMODEL_CH: ePBMsgCode
PB_CLOSE_EDIT_ACTORMODEL_HC: ePBMsgCode
PB_CUSTOMACTOR_MODELDATA_HC: ePBMsgCode
PB_PACKGIFT_NOTIFYITEMCHANGE_HC: ePBMsgCode
PB_VEHICLE_PREBLOCK_CH: ePBMsgCode
PB_VEHICLE_PREBLOCK_HC: ePBMsgCode
PB_VEHICLE_ITEMUSE_CH: ePBMsgCode
PB_VEHICLE_STARTBLOCK_CH: ePBMsgCode
PB_VEHICLE_ALL_ITEMID_HC: ePBMsgCode
PB_VEHICLE_ONE_ITEMID_HC: ePBMsgCode
PB_VEHICLE_ATTRIB_CHANGE_HC: ePBMsgCode
PB_VEHICLE_ATTRIB_CHANGE_CH: ePBMsgCode
PB_WORKSHOP_ITEMINFO_CH: ePBMsgCode
PB_WORKSHOP_ITEMINFO_HC: ePBMsgCode
PB_VEHICLEASSEMBLEBLOCK_UPDATE_HC: ePBMsgCode
PB_PLAYER_VEHICLE_MOVEINPUT_CH: ePBMsgCode
PB_PLAYER_RESETVEHICLE_CH: ePBMsgCode
PB_PLAYER_MOTIONSTATECHANGE_CH: ePBMsgCode
PB_PLAYER_CLICK_CH: ePBMsgCode
PB_PLAYER_CAMERAROTATE_HC: ePBMsgCode
PB_PLAYER_CHANGEVIEWMODE_HC: ePBMsgCode
PB_PLAYER_CANMOVE_HC: ePBMsgCode
PB_PLAYER_CANCONTROL_HC: ePBMsgCode
PB_PLAYER_SETATTR_HC: ePBMsgCode
PB_PLAYER_FREEZING_HC: ePBMsgCode
PB_PLAYER_SELECTSHORTCUT_CH: ePBMsgCode
PB_GAMERULE_HC: ePBMsgCode
PB_BASKETBALL_OPERATE_HC: ePBMsgCode
PB_BASKETBALL_OPERATE_CH: ePBMsgCode
PB_PLAYER_VEHICLE_MOVEINPUT_HC: ePBMsgCode
PB_PLAYER_CANFIRE_HC: ePBMsgCode
PB_PLAYER_TOUCH_EVT_SYNC_HC: ePBMsgCode
PB_PLAYER_TOUCH_EVT_CH: ePBMsgCode
PB_BUY_AD_SHOP_GOOD_CH: ePBMsgCode
PB_BUY_AD_SHOP_GOOD_HC: ePBMsgCode
PB_SYNC_PLAYER_POS_HC: ePBMsgCode
PB_ACHIEVEMENT_AWARD_CH: ePBMsgCode
PB_SYNC_CLIENT_ACTIONLOG_CH: ePBMsgCode
PB_SYNC_ROOM_EXTRA_HC: ePBMsgCode
PB_UPLOAD_CHECK_INFO_CH: ePBMsgCode
PB_GET_ADSHOP_EXTRA_AWARD_CH: ePBMsgCode
PB_EXTRACT_STORE_ITEM_CH: ePBMsgCode
PB_UPLOAD_CLIENT_INFO_CH: ePBMsgCode
PB_SYNC_PLAYER_POS_CH: ePBMsgCode
PB_TRIGGER_TIMER_HC: ePBMsgCode
PB_WORKSHOP_BUILD_HC: ePBMsgCode
PB_TRIGGER_PLAYER_ATTRI_CH: ePBMsgCode
PB_PLAYER_ATTR_SCALE_HC: ePBMsgCode
PB_PLAYER_ATTR_SCALE_CH: ePBMsgCode
PB_PLAYER_NAVIGATE_HC: ePBMsgCode
PB_PLAYER_FACE_YAW_HC: ePBMsgCode
PB_OPENEDIT_FULLYCUSTOMMODEL_HC: ePBMsgCode
PB_REQ_DOWNLOADRES_URL_CH: ePBMsgCode
PB_CLOSE_FULLYCUSTOMMODEL_UI_CH: ePBMsgCode
PB_CLOSE_FULLYCUSTOMMODEL_UI_HC: ePBMsgCode
PB_RESP_DOWNLOADRES_URL_HC: ePBMsgCode
PB_PRE_OPEN_EDIT_FCM_UI: ePBMsgCode
PB_EFFECTSCALE_HC: ePBMsgCode
PB_PLAYER_NAVFINISHED_CH: ePBMsgCode
PB_TRIGGER_MUSIC_HC: ePBMsgCode
PB_TRIGGER_SOUND_CH: ePBMsgCode
PB_PLAYER_JUMP_HC: ePBMsgCode
PB_PLAYER_JUMP_CH: ePBMsgCode
PB_PLAYER_SPECIAL_SKILL_CH: ePBMsgCode
PB_HORSE_SKILLCD_HC: ePBMsgCode
PB_CLOUDSERVER_PERMIT_CH: ePBMsgCode
PB_CLOUDSERVER_PERMIT_HC: ePBMsgCode
PB_CLOUDSERVER_AUTHORITY_HC: ePBMsgCode
PB_CLOUDSERVER_AUTHORITY_CH: ePBMsgCode
PB_SS_SYNC_TASK_HC: ePBMsgCode
PB_SS_SYNC_TASK_CH: ePBMsgCode
PB_VEHICLEASSEMBLEBLOCK_ALL_HC: ePBMsgCode
PB_VEHICLE_ASSEMBLE_LINE_CH: ePBMsgCode
PB_VEHICLE_ASSEMBLE_LINE_HC: ePBMsgCode
PB_VEHICLE_ASSEMBLE_LINE_OPERATE_CH: ePBMsgCode
PB_VEHICLE_ASSEMBLE_LINE_OPERATE_HC: ePBMsgCode
PB_ACTIONEDATA_UPDATE_CH: ePBMsgCode
PB_VEHICLE_WORKSHOP_LINE_CH: ePBMsgCode
PB_CLOUDSERVER_CHANGE_TEAM_CH: ePBMsgCode
PB_CLOUDSERVER_CHANGE_STATE_HC: ePBMsgCode
PB_YM_CHANGEROLE_HC: ePBMsgCode
PB_YM_CHANGEROLE_CH: ePBMsgCode
PB_YM_VOICE_CH: ePBMsgCode
PB_YM_VOICE_HC: ePBMsgCode
PB_CLOUDSERVER_ROOM_AUTOMUTE_CH: ePBMsgCode
PB_VEHICLE_WORKSHOP_LINE_UPDATE_CH: ePBMsgCode
PB_MAP_EDIT_HANDLE_CH: ePBMsgCode
PB_MAP_EDIT_REVOKE_CH: ePBMsgCode
PB_CLOUD_ROOM_OWNER_START_GAME_CH: ePBMsgCode
PB_CLOUD_ROOM_KICK_OFF_CH: ePBMsgCode
PB_TRIGGER_OPENSTORE_HC: ePBMsgCode
PB_USE_PACKINGFCMITEM_CH: ePBMsgCode
PB_USE_PACKINGFCMITEM_HC: ePBMsgCode
PB_CREATE_PACKINGCM_CH: ePBMsgCode
PB_CREATE_PACKINGCM_HC: ePBMsgCode
PB_PACKING_FCMDATA_HC: ePBMsgCode
PB_PLAYER_INPUTCONTENT_CH: ePBMsgCode
PB_PLAYER_INPUTKEYS_CH: ePBMsgCode
PB_CLOUD_ROOM_STATUSTIME_HC: ePBMsgCode
PB_PLAYER_VEHICLE_SLEEP_HC: ePBMsgCode
PB_SENSOR_CONTAINER_DATA_CH: ePBMsgCode
PB_SENSOR_CONTAINER_DATA_HC: ePBMsgCode
PB_VEHICLE_BIND_ACTOR_HC: ePBMsgCode
PB_DOOR_DATA_HC: ePBMsgCode
PB_PLAYER_CARRYACTOR_CH: ePBMsgCode
PB_PLAYER_CARRYACTOR_HC: ePBMsgCode
PB_VILLAGER_BODY_CHANGE_HC: ePBMsgCode
PB_PLAYER_TAME_ACTOR_HC: ePBMsgCode
PB_VILLAGER_MODIFY_NAME_CH: ePBMsgCode
PB_VILLAGER_CLOTH_HC: ePBMsgCode
PB_ACTOR_HEAD_DISPLAY_ICON_HC: ePBMsgCode
PB_ACTOR_PLAY_ANIM_BY_ID_HC: ePBMsgCode
PB_VILLAGE_TOTEM_TIP_HC: ePBMsgCode
PB_VILLAGE_TOTEM_ACTIVE_HC: ePBMsgCode
PB_SAVE_TOMB_STONE_HC: ePBMsgCode
PB_PLAYER_LEVELMODE_HC: ePBMsgCode
PB_ACTION_ATTR_STATE_HC: ePBMsgCode
PB_EDU_ROLEINFO_HC: ePBMsgCode
PB_PLAYER_GOTOPOS_CH: ePBMsgCode
PB_IMPORT_MODEL_HC: ePBMsgCode
PB_CUSTOM_MODEL_PRE_HC: ePBMsgCode
PB_CUSTOM_MODEL_PRE_CH: ePBMsgCode
PB_RESETDEFORMATION_CH: ePBMsgCode
PB_DEFORMATION_SKIN_CH: ePBMsgCode
PB_PLAYERTRANSFORMSKIN_HC: ePBMsgCode
PB_RESTORE_DEFORMATION_CH: ePBMsgCode
PB_PLAYER_SAVE_ARCH_HC: ePBMsgCode
PB_PLAYER_PUSH_ARCH_CH: ePBMsgCode
PB_LIGHTNING_HC: ePBMsgCode
PB_INTERACT_MOBPACK_HC: ePBMsgCode
PB_UPDATE_MOB_BACKPACK_HC: ePBMsgCode
PB_MOVE_MOBBACKPACKITEM_CH: ePBMsgCode
PB_INTERACT_MOBBACKPACKITEM_CH: ePBMsgCode
PB_ALTAR_LUCKY_DRAW_CH: ePBMsgCode
PB_SFACTIVITY_HC: ePBMsgCode
PB_OPEN_DEVGOODSBUY_DIALOGHC: ePBMsgCode
PB_HOME_PRAY_INFO_HC: ePBMsgCode
PB_HOME_PRAY_TREE_STATE_HC: ePBMsgCode
PB_HOME_PRAY_REQ_HC: ePBMsgCode
PB_HOME_PRAY_TIME_CH: ePBMsgCode
PB_HOME_PRAY_TIMEUPDATE_HC: ePBMsgCode
PB_HOME_PRAY_ERROR_HC: ePBMsgCode
PB_OPEN_HOMENPC_HC: ePBMsgCode
PB_OPEN_HOMECLOSET_HC: ePBMsgCode
PB_GODTEMPLE_CREATE_HC: ePBMsgCode
PB_SHAPE_ADDITION_ANIM_HC: ePBMsgCode
PB_HOME_SUMMONPET_CH: ePBMsgCode
PB_HOMELAND_RANCH_HC: ePBMsgCode
PB_HOMELAND_RANCH_ANIMAL_UPDATE_CH: ePBMsgCode
PB_TRIGGER_GRAPHICS_HC: ePBMsgCode
PB_USEITEM_BY_HOMELAND_HC: ePBMsgCode
PB_PLAYER_CUSTOM_BASEMODEL_HC: ePBMsgCode
PB_CHANGE_ACTOR_MODEL_HC: ePBMsgCode
PB_REQUEST_MODEL_CH: ePBMsgCode
PB_NOTIFIY_MODEL_HC: ePBMsgCode
PB_VOICE_INFORM_CH: ePBMsgCode
PB_VOICE_INFORM_HC: ePBMsgCode
PB_RUNE_OPERATE_CH: ePBMsgCode
PB_RUNE_OPERATE_SUCCESS_HC: ePBMsgCode
PB_FURNACE_TEMPERATURE_CH: ePBMsgCode
PB_TAKE_CONTAINER_ITEM_CH: ePBMsgCode
PB_POT_CONTAINER_SET_MAKE_CH: ePBMsgCode
PB_UPDATE_POT_CONTAINER_HC: ePBMsgCode
PB_NOTIFY_STARSTATION_ADDED_HC: ePBMsgCode
PB_NOTIFY_STARSTATION_REMOVED_HC: ePBMsgCode
PB_NOTIFY_STARSTATION_CHANGENAMESTATUS_HC: ePBMsgCode
PB_STARSTATION_CHANGENAMESTATUS_CH: ePBMsgCode
PB_NOTIFY_ENTER_STARSTATION_CABIN_HC: ePBMsgCode
PB_LEAVE_STARSTATION_CABIN_CH: ePBMsgCode
PB_NOTIFY_LEAVE_STARSTATION_CABIN_HC: ePBMsgCode
PB_UPDATE_STARSTATION_CABIN_LEVEL_CH: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_CABIN_LEVEL_HC: ePBMsgCode
PB_UPDATE_STARSTATION_CABIN_STATUS_CH: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUS_HC: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_CABIN_ADDED_HC: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_CABIN_REMOVED_HC: ePBMsgCode
PB_ADD_UNFINISHED_TRANSFER_RECORD_CH: ePBMsgCode
PB_NOTIFY_ADD_UNFINISHED_TRANSFER_RECORD_HC: ePBMsgCode
PB_NOTIFY_UPDATE_UNFINISHED_TRANSFER_RECORD_STATUS_HC: ePBMsgCode
PB_REMOVE_UNFINISHED_TRANSFER_RECORD_CH: ePBMsgCode
PB_NOTIFY_REMOVE_UNFINISHED_TRANSFER_RECORD_HC: ePBMsgCode
PB_STARSTATION_DATA_HC: ePBMsgCode
PB_PLAYER_TRANSFER_BY_STRSTATION_CH: ePBMsgCode
PB_NOTIFY_PLAYER_TRANSFER_BY_STRSTATION_HC: ePBMsgCode
PB_NOTIFY_ACTIVATE_STARSTATION_HC: ePBMsgCode
PB_NOTIFY_UPGRADE_STARSTATION_CABIN_HC: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_SIGN_INFO_HC: ePBMsgCode
PB_REQUIRE_STARSTATION_TRANSFER_CH: ePBMsgCode
PB_NOTIFY_STARSTATION_TRANSFER_RESULT_HC: ePBMsgCode
PB_BLOCK_EXPLOIT_CH: ePBMsgCode
PB_BLOCK_EXPLOIT_HC: ePBMsgCode
PB_VACANT_BOSS_STATE_HC: ePBMsgCode
PB_BACKPACK_REMOVEITEM_CH: ePBMsgCode
PB_NOTIFY_PLAYALTMANMUSIC_HC: ePBMsgCode
PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_HC: ePBMsgCode
PB_GAINITEMSTOBACKPACK_CH: ePBMsgCode
PB_UPDATE_STARSTATION_CABIN_STATUSEND_CH: ePBMsgCode
PB_NOTIFY_UPDATE_STARSTATION_CABIN_STATUSEND_HC: ePBMsgCode
PB_ADD_STARSTATION_TRANSFER_DESC_CH: ePBMsgCode
PB_ADDEXP_CH: ePBMsgCode
PB_ADDEXPRESULT_HC: ePBMsgCode
PB_COUSTOMUI_EVENT_CH: ePBMsgCode
PB_ACHIEVEMENT_SYNC_HC: ePBMsgCode
PB_ACHIEVEMENT_UPDATE_CH: ePBMsgCode
PB_BATTLEPASS_EVENT_HC: ePBMsgCode
PB_ADDSTAR_CH: ePBMsgCode
PB_USEHEARTH_CH: ePBMsgCode
PB_ACTOR_STOP_ANIM_HC: ePBMsgCode
PB_ACTOR_STOP_ANIM_CH: ePBMsgCode
PB_HOMELAND_RANCH_FOODER_CH: ePBMsgCode
PB_HORSE_FLAG_HC: ePBMsgCode
PB_HOMELAND_RANCH_FOODERSTATE_HC: ePBMsgCode
PB_ACHIEVEMENT_INITDATA_HC: ePBMsgCode
PB_HOMELAND_COOK_MENUBUY_HC: ePBMsgCode
PB_HOMELAND_COOK_MENUBUY_CH: ePBMsgCode
PB_HOMELAND_FARM_SHOP_HC: ePBMsgCode
PB_HOMELAND_FARM_SHOP_CH: ePBMsgCode
PB_HOMELAND_COOK_SPFURNITUREBUY_HC: ePBMsgCode
PB_HOMELAND_COOK_SPFURNITUREBUY_CH: ePBMsgCode
PB_PLAYER_OPENUI_HC: ePBMsgCode
PB_ANSWER_LANTERNBIRD_CH: ePBMsgCode
PB_EXCHANGEITEMSTOBACKPACK_CH: ePBMsgCode
PB_EXCHANGEITEMSTOBACKPACKRESULT_HC: ePBMsgCode
PB_CHANGE_QQMUSIC_PLAYER_HC: ePBMsgCode
PB_CHANGE_QQMUSIC_PLAYER_CH: ePBMsgCode
PB_SET_TIANGOU_HC: ePBMsgCode
PB_PLAYER_CLOSEUI_CH: ePBMsgCode
PB_RIDE_INVISIBLE_HC: ePBMsgCode
PB_ACTOR_PLAY_SOUND_CH: ePBMsgCode
PB_ACTORINVITE_CH: ePBMsgCode
PB_ACTORINVITE_HC: ePBMsgCode
PB_PLAYER_SKIN_ACT_HC: ePBMsgCode
PB_PLAYER_SKIN_ACT_CH: ePBMsgCode
PB_CHANGE_QQMUSIC_CLUB_HC: ePBMsgCode
PB_CHANGE_QQMUSIC_CLUB_CH: ePBMsgCode
PB_ACTOR_STOP_SKIN_ACT_HC: ePBMsgCode
PB_MINICLUB_PLAYER_HC: ePBMsgCode
PB_MINICLUB_PLAYER_CH: ePBMsgCode
PB_ACTOR_STOP_SKIN_ACT_CH: ePBMsgCode
PB_SPRAY_PAINT_INFO_CH: ePBMsgCode
PB_ADD_PAINTED_INFO_HC: ePBMsgCode
PB_REMOVE_PAINTED_INFO_HC: ePBMsgCode
PB_Equip_Weapon_HC: ePBMsgCode
PB_Equip_Weapon_CH: ePBMsgCode
PB_PLAYEFFECT_CH: ePBMsgCode
PB_GainItemsUserDatastrToBackPack_CH: ePBMsgCode
PB_UseMusicYuPu_CH: ePBMsgCode
PB_DanceByPlaying_CH: ePBMsgCode
PB_StopDanceByPlaying_CH: ePBMsgCode
PB_StartAct_CH: ePBMsgCode
PB_StopAct_CH: ePBMsgCode
PB_TOP_BRAND_CH: ePBMsgCode
PB_TOP_BRAND_HC: ePBMsgCode
PB_CHEAT_CHECK_CH: ePBMsgCode
PB_WEAPON_POINT_HC: ePBMsgCode
PB_GAME_MODE_CHANGE: ePBMsgCode
PB_ADDLIGHTCHAIN_HC: ePBMsgCode
PB_STARTFISHING_CH: ePBMsgCode
PB_STARTFISHING_HC: ePBMsgCode
PB_ENDFISHING_CH: ePBMsgCode
PB_ENDFISHING_HC: ePBMsgCode
PB_QUITFISHING_CH: ePBMsgCode
PB_QUITFISHING_HC: ePBMsgCode
PB_CHANGEFISHINGSTAGE_HC: ePBMsgCode
PB_CHANGEEXPOSEPOS_CH: ePBMsgCode
PB_NOTIFY_UPDATE_TOOL_MODEL_TEXTURE_CH: ePBMsgCode
PB_BIND_ITEM_TO_ACTOR_HC: ePBMsgCode
PB_FISHING_BEGIN_FLASH_HC: ePBMsgCode
PB_END_PLAY_FISH_CH: ePBMsgCode
PB_CHANGE_SHOW_EQUIP_HC: ePBMsgCode
PB_RESET_ROLE_FLAGS: ePBMsgCode
PB_BIND_PLAYER_TO_PHYSICS_PLAT_HC: ePBMsgCode
PB_UNBIND_PLAYER_TO_PHYSICS_PLAT_HC: ePBMsgCode
PB_PHYSICS_COM_UPDATE: ePBMsgCode
PB_PHYSICS_COM_PLAT_LOCAL_POS: ePBMsgCode
PB_EFFECT_COM_PARTICLE_UPDATE: ePBMsgCode
PB_SOUND_COM_UPDATE: ePBMsgCode
PB_BIND_PLAYER_TO_PHYSICS_PLAT_CH: ePBMsgCode
PB_UNBIND_PLAYER_TO_PHYSICS_PLAT_CH: ePBMsgCode
PB_METEOR_SHOWER_HC: ePBMsgCode
PB_PLAYER_TRANSFER_HC: ePBMsgCode
PB_NOTIFY_PLAYER_BLOCK_CHANGE_COLOR_ANIM_HC: ePBMsgCode
PB_ACTOR_PLAY_HAND_ANIM_HC: ePBMsgCode
PB_BLOCK_PLAY_ANIM_HC: ePBMsgCode
PB_BLOCKSTRUCT_UPDATE_HC: ePBMsgCode
PB_PLAYER_ENTER_LIVINGWHEEL_HC: ePBMsgCode
PB_PLAYER_LEAVE_LIVINGWHEEL_HC: ePBMsgCode
PB_PLAYER_WORKING_LIVINGWHEEL_CH: ePBMsgCode
PB_UPDATE_LIVINGWHEEL_HC: ePBMsgCode
PB_REQUEST_LIVINGWHEEL_CH: ePBMsgCode
PB_CREATE_BLOCK_CH: ePBMsgCode
PB_ACTOR_VILLAGER_INFO_HC: ePBMsgCode
PB_ACTOR_SANDWORM_SHOW_HC: ePBMsgCode
PB_ACTOR_SANDWORM_CAN_MOVE_HC: ePBMsgCode
PB_ACTOR_SCASLE_HC: ePBMsgCode
PB_ACTOR_SANDWORM_NIBBLE_PLAYER_HC: ePBMsgCode
PB_ACTOR_CREATE_THORNBALL_HC: ePBMsgCode
PB_ACTOR_REBOUNDS_ATTACK_UP_HC: ePBMsgCode
PB_ACTOR_REBOUNDS_ATTACK_ROUND_HC: ePBMsgCode
PB_REMOVE_SAWTOOTH_THORNB_HC: ePBMsgCode
PB_CH_NOTICE_ATTACKED_UP_CH: ePBMsgCode
PB_CH_NOTICE_ATTACKED_ROUND_CH: ePBMsgCode
PB_CH_NOTICE_REMOVE_SAWTOOTH_THORNBA_CH: ePBMsgCode
PB_ATTR_SHAPE_SHIFT_RIGHT_CLICK_CH: ePBMsgCode
PB_DESTORY_BLOCK_CH: ePBMsgCode
PB_WATER_PRESSURE_CH: ePBMsgCode
PB_ATTR_SHAPE_SHIFT_SYNC_HC: ePBMsgCode
PB_COCONUT_HIT_HC: ePBMsgCode
PB_COCONUT_SKIP_NIGHT_HC: ePBMsgCode
PB_ACTOR_SHARK_BITE_PLAYER_MOVE_HC: ePBMsgCode
PB_CRAB_INFO_SYNC_HC: ePBMsgCode
PB_CRAB_CLICKCOUNT_RESET_CH: ePBMsgCode
PB_HIPPOCAMPUS_REFRESHMODEL_HC: ePBMsgCode
PB_HIPPOCAMPUS_CHANGECOLOR_HC: ePBMsgCode
PB_BACKPACKGRID_DRUATION_HC: ePBMsgCode
PB_GUNLOGIC_USE_WaterCanoonSkill_CH: ePBMsgCode
PB_ACTOR_SNOWMAN_PART_SHOW_HC: ePBMsgCode
PB_MOB_PART_SHOW_HC: ePBMsgCode
PB_PLAYER_SHAKE_CH: ePBMsgCode
PB_ACTOR_DISSOLVE_COMPONENT_OPEN_HC: ePBMsgCode
PB_COOKBOOKINFO_HC: ePBMsgCode
PB_STOVETAKE_CH: ePBMsgCode
PB_SETHPVISIBLE_HC: ePBMsgCode
PB_SKILLPLAYANIM_HC: ePBMsgCode
PB_SKILLSTOPANIM_HC: ePBMsgCode
PB_SKILLPLAYBODYEFFECT_HC: ePBMsgCode
PB_SKILLSTOPBODYEFFECT_HC: ePBMsgCode
PB_SKILLWORLDPLAYBODYEFFECT_HC: ePBMsgCode
PB_ACCUMULATOR_HC: ePBMsgCode
PB_SKILLPLAYTOOLANIM_HC: ePBMsgCode
PB_SKILLSTOPTOOLANIM_HC: ePBMsgCode
PB_SKILLSETCHARGEMOVE_HC: ePBMsgCode
PB_SKILLMOVE_HC: ePBMsgCode
PB_SKILLCAMERA_HC: ePBMsgCode
PB_STOPWEAPONANIM_HC: ePBMsgCode
PB_STOPWEAPONANIM_CH: ePBMsgCode
PB_STOPWEAPONMOTION_HC: ePBMsgCode
PB_STOPWEAPONMOTION_CH: ePBMsgCode
PB_SETLOCOTYPE_HC: ePBMsgCode
PB_BASESTATE_HC: ePBMsgCode
PB_SETMOVEMENT_MODE_HC: ePBMsgCode
PB_7000_HORSEFLYSTATE_HC: ePBMsgCode
PB_PLAYER_CAMERACONFIG_HC: ePBMsgCode
PB_BACKPACK_NUM_CHANGE_HC: ePBMsgCode
PB_PLAY_SKIN_VOICE_CH: ePBMsgCode
PB_PLAY_SKIN_VOICE_HC: ePBMsgCode
PB_BOX_PLAY_ANI_CH: ePBMsgCode
PB_NEW_YEAR_BOSS_STAGE_HC: ePBMsgCode
PB_NEW_YEAR_HP_HC: ePBMsgCode
PB_NEW_YEAR_MONSTER_POS_HC: ePBMsgCode
PB_STORAGE_BOX_PUT_IN_ALL_CH: ePBMsgCode
PB_TELEPORT_SHOWPANEL_HC: ePBMsgCode
PB_DYNAMIC_PROTO_HC: ePBMsgCode
PB_DYNAMIC_PROTO_CH: ePBMsgCode
PB_STORAGE_BOX_TAKE_OUT_ALL_CH: ePBMsgCode
PB_SYNC_DYEABLE_ITEM_CH: ePBMsgCode
PB_CUSTOM_PBC_CH: ePBMsgCode
PB_CUSTOM_PBC_HC: ePBMsgCode
PB_UPDATE_LASER_POINTER_HC: ePBMsgCode
PB_UPDATE_LASER_POINTER_CH: ePBMsgCode
PB_PHYSICS_INPUT_FRAME: ePBMsgCode
PB_PHYSICS_ASYNC_TIMESTAMP: ePBMsgCode
PB_PHYSICS_SETUP_TIMESTAMP: ePBMsgCode
PB_PHYSICS_TIME_DILATION: ePBMsgCode
PB_PHYSICS_REPLICATED_INPUT_CH: ePBMsgCode
PB_PHYSICS_REPLICATED_INPUT_HC: ePBMsgCode
PB_PHYSICS_REPLICATED_STATE_CH: ePBMsgCode
PB_PHYSICS_REPLICATED_STATE_HC: ePBMsgCode
PB_PHYSICS_COMMON_REPLICATED: ePBMsgCode
PB_CUSTOM_MSG: ePBMsgCode
PB_BlockData_CH: ePBMsgCode
PB_PUSHSNOWBALL_OPERATE_CH: ePBMsgCode
PB_PUSHSNOWBALL_OPERATE_HC: ePBMsgCode
PB_PUSHSNOWBALL_SIZECHANGE_HC: ePBMsgCode
PB_PLAY_EFFECT_SHADER_HC: ePBMsgCode
PB_NEW_REPAIR_ITEM_CH: ePBMsgCode
PB_SEND_OBJACTOR_MSG: ePBMsgCode
PB_ADD_BULLETHOLE_HC: ePBMsgCode
PB_ACTORSHOOT_CH: ePBMsgCode
PB_ACTOR_FIREWORK_CH: ePBMsgCode
PB_ACTOR_PLAYANIM_NEW_CH: ePBMsgCode
PB_ACTOR_SPEED_CHANGE_HC: ePBMsgCode
PB_TASK_INITDATA_HC: ePBMsgCode
PB_BYMOUNT_HC: ePBMsgCode
PB_ACTOR_PICKUP_ACTOR_HC: ePBMsgCode
PB_ACTOR_DROP_ACTOR_HC: ePBMsgCode
PB_GROUP_WEATHER_HC: ePBMsgCode
PB_BYMOUNT_CH: ePBMsgCode
PB_ADD_BULLETHOLEV2_HC: ePBMsgCode
PB_ACTOR_SET_ATTR_TOTRACKINGPLAYERS_HC: ePBMsgCode
PB_TASK_OBJECTIVE_INITDATA_HC: ePBMsgCode
PB_PLAYWEAPONMOTION_HC: ePBMsgCode
PB_PLAYWEAPONMOTION_CH: ePBMsgCode
PB_PLAYWEAPONANIM_HC: ePBMsgCode
PB_PLAYWEAPONANIM_CH: ePBMsgCode
PB_ACTORJUMP_HC: ePBMsgCode
PB_TECHTREEINFOCHANGE_HC: ePBMsgCode
PB_ACTORSETGRAVITYFAILURE_HC: ePBMsgCode
PB_SETINTERACTACTORMECHA_HC: ePBMsgCode
PB_UNLOCKITEMS_HC: ePBMsgCode
PB_CHECKNEWUNLOCKITEM_CH: ePBMsgCode
PB_PLAY_CAMERA_SHAKE_HC: ePBMsgCode
PB_RECENTLYMAKECRAFT_CH: ePBMsgCode
PB_MECHAKINETICUINT_HC: ePBMsgCode
PB_MECHAKINETICNODEDATA_HC: ePBMsgCode
PB_CONTAINER_UI_DATA_HC: ePBMsgCode
PB_CONTAINER_UI_DATA_CH: ePBMsgCode
PB_MECHARECOVERYHEAD_HC: ePBMsgCode
PB_MECHA_TUNNEL_ANIM_PLAY_HC: ePBMsgCode
PB_MECHA_STRUCTURE_SYNC_HC: ePBMsgCode
PB_MECHA_STRUCTURE_OPERATE_CH: ePBMsgCode
PB_MECHA_STRUCTURE_OPERATE_HC: ePBMsgCode
PB_TRANSFER_GOOD_COMP_HC: ePBMsgCode
PB_PICK_TRANSFER_GOOD_ITEM_CH: ePBMsgCode
PB_MECHA_KINETNODELOGIC_DATA_HC: ePBMsgCode
PB_MECHA_ADDKINETNODELOGIC_HC: ePBMsgCode
PB_IRONDOMEESSENCE_DISEQUIP_CH: ePBMsgCode
PB_IRON_HC: ePBMsgCode
PB_IRONDOMEESSENCE_EQUIP_HC: ePBMsgCode
PB_PART_HC: ePBMsgCode
PB_PARTMANAGER_HC: ePBMsgCode
PB_BLOCKTEXTURECOLORS_HC: ePBMsgCode
PB_LOOKATACTOR_HC: ePBMsgCode
PB_SANDBOX_LUA_LOG_DATA_CH: ePBMsgCode
PB_SANDBOX_LUA_LOG_DATA_HC: ePBMsgCode
PB_AI_TTS_AUDIO_HC: ePBMsgCode
PB_AI_ASR_AUDIO_CH: ePBMsgCode
PB_MODCONTAINER_HC: ePBMsgCode
PB_WBP_MSG_HC: ePBMsgCode
PB_WBP_MSG_CH: ePBMsgCode
PB_RAKEPLANTITEMID_CH: ePBMsgCode
PB_AVATAR_PARTS_PRIORITY_SYNC_HC: ePBMsgCode
PB_AVATAR_PARTS_PRIORITY_SYNC_ALL_HC: ePBMsgCode
PB_ACTOR_CHAT_BUBBLE_HC: ePBMsgCode
PB_SLEEP_MSG_HC: ePBMsgCode
PB_DROPITEM_STATE_HC: ePBMsgCode
PB_DROPITEM_INTERACT_RESULT_CH: ePBMsgCode
PB_ACTOR_SWITCH_PHYSICTYPE_HC: ePBMsgCode
PB_PLAYER_USE_ITEM_CH: ePBMsgCode
PB_PLAYER_PLAY_HAND_ANIM_HC: ePBMsgCode
PB_PLAYER_PLAY_DIG_BLOCK_EFFECT_HC: ePBMsgCode
PB_ACTOR_PLAYANIM_FINISH_CH: ePBMsgCode
PB_LIVING_TIMERXRAYEFFECT_HC: ePBMsgCode
PB_BLOCK_MINERALPROSPECT_HC: ePBMsgCode
PB_WORLD_SYNC_SAVE_HC: ePBMsgCode
PB_MAX_MSG_CODE: ePBMsgCode
PB_MODCONTAINER_MODELPART: ePBModContainerOp
PB_MODCONTAINER_MODELPART_ADD: ePBModContainerModelPartOp
PB_MODCONTAINER_MODELPART_DELETE: ePBModContainerModelPartOp
PB_MODCONTAINER_MODELPART_MESHSTATE: ePBModContainerModelPartOp
PB_ACTORTYPEGENERAL: ePBActorTypes
PB_ACTORTYPEROLE: ePBActorTypes
PB_ACTORTYPEMONSTER: ePBActorTypes
PB_ACTORTYPEBOSS: ePBActorTypes
PB_ACTORTYPEBLOCK: ePBActorTypes
PB_ACTORTYPEITEM: ePBActorTypes
PB_STANCESTAND: ePBStanceType
PB_STANCEWALK: ePBStanceType
PB_STANCERUN: ePBStanceType
PB_STANCEJUMP: ePBStanceType
PB_STANCELAY: ePBStanceType
PB_STANCESWIM: ePBStanceType
PB_STANCEFLY: ePBStanceType
PB_EFFECT_PARTICLE: ePBEffectType
PB_EFFECT_PICKITEM: ePBEffectType
PB_EFFECT_SOUND: ePBEffectType
PB_EFFECT_ACTORBODY: ePBEffectType
PB_EFFECT_DESTROYBLOCK: ePBEffectType
PB_EFFECT_PLAYMUSICGRID: ePBEffectType
PB_EFFECT_STOPMUSICGRID: ePBEffectType
PB_EFFECT_STRINGACTORBODY: ePBEffectType
PB_EFFECT_CRACKBLOCK: ePBEffectType
PB_EFFECT_TIRGGERSOUND: ePBEffectType
PB_EFFECT_VEHICLE: ePBEffectType
PB_EFFECT_STOPPARTICLE: ePBEffectType
PB_EFFECT_SOUND_NEW: ePBEffectType
PB_EFFECT_SOUND_NEW_FOR_TRACK: ePBEffectType
PB_EFFECT_SOUND_NEW_STOP: ePBEffectType
PB_EFFECT_SOUND_NOTE: ePBEffectType
PB_EFFECT_SOUND_NOTE_STOP: ePBEffectType
PB_EFFECT_SOUNDID: ePBEffectType
PB_EFFECT_PARTICLEID: ePBEffectType
PB_EFFECT_SOUND_NEW_PAUSE: ePBEffectType
Volume: eEffectIDX
Pitch: eEffectIDX
Flags: eEffectIDX
Segment: eEffectIDX
PosX: eEffectIDX
PosY: eEffectIDX
PosZ: eEffectIDX

class PB_ItemDataComponent(_message.Message):
    __slots__ = ("name", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class PB_Vector3(_message.Message):
    __slots__ = ("X", "Y", "Z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    X: int
    Y: int
    Z: int
    def __init__(self, X: _Optional[int] = ..., Y: _Optional[int] = ..., Z: _Optional[int] = ...) -> None: ...

class PB_Vector3f(_message.Message):
    __slots__ = ("X", "Y", "Z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    X: float
    Y: float
    Z: float
    def __init__(self, X: _Optional[float] = ..., Y: _Optional[float] = ..., Z: _Optional[float] = ...) -> None: ...

class PB_Quaternion(_message.Message):
    __slots__ = ("X", "Y", "Z", "W")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    X: float
    Y: float
    Z: float
    W: float
    def __init__(self, X: _Optional[float] = ..., Y: _Optional[float] = ..., Z: _Optional[float] = ..., W: _Optional[float] = ...) -> None: ...

class PB_Pos(_message.Message):
    __slots__ = ("X", "Y", "Z", "Map")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    X: int
    Y: int
    Z: int
    Map: int
    def __init__(self, X: _Optional[int] = ..., Y: _Optional[int] = ..., Z: _Optional[int] = ..., Map: _Optional[int] = ...) -> None: ...

class PB_BodyDir(_message.Message):
    __slots__ = ("RotationYaw", "RotationPitch", "Motion")
    ROTATIONYAW_FIELD_NUMBER: _ClassVar[int]
    ROTATIONPITCH_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    RotationYaw: float
    RotationPitch: float
    Motion: PB_Vector3
    def __init__(self, RotationYaw: _Optional[float] = ..., RotationPitch: _Optional[float] = ..., Motion: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_Item(_message.Message):
    __slots__ = ("DefID", "Idx", "Pile", "UserDataStr")
    DEFID_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    PILE_FIELD_NUMBER: _ClassVar[int]
    USERDATASTR_FIELD_NUMBER: _ClassVar[int]
    DefID: int
    Idx: int
    Pile: int
    UserDataStr: str
    def __init__(self, DefID: _Optional[int] = ..., Idx: _Optional[int] = ..., Pile: _Optional[int] = ..., UserDataStr: _Optional[str] = ...) -> None: ...

class PB_ItemRune(_message.Message):
    __slots__ = ("RuneID", "RuneVal0", "RuneVal1", "ItemID")
    RUNEID_FIELD_NUMBER: _ClassVar[int]
    RUNEVAL0_FIELD_NUMBER: _ClassVar[int]
    RUNEVAL1_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    RuneID: int
    RuneVal0: float
    RuneVal1: float
    ItemID: int
    def __init__(self, RuneID: _Optional[int] = ..., RuneVal0: _Optional[float] = ..., RuneVal1: _Optional[float] = ..., ItemID: _Optional[int] = ...) -> None: ...

class PB_ArmFumo(_message.Message):
    __slots__ = ("FumoIDs", "Runes")
    FUMOIDS_FIELD_NUMBER: _ClassVar[int]
    RUNES_FIELD_NUMBER: _ClassVar[int]
    FumoIDs: _containers.RepeatedScalarFieldContainer[int]
    Runes: _containers.RepeatedCompositeFieldContainer[PB_ItemRune]
    def __init__(self, FumoIDs: _Optional[_Iterable[int]] = ..., Runes: _Optional[_Iterable[_Union[PB_ItemRune, _Mapping]]] = ...) -> None: ...

class PB_Arm(_message.Message):
    __slots__ = ("DefID", "Idx", "Color", "Dur", "RepairNum", "Name", "Fumo", "UserDataInt", "datacomponents", "iteminsid")
    DEFID_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DUR_FIELD_NUMBER: _ClassVar[int]
    REPAIRNUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FUMO_FIELD_NUMBER: _ClassVar[int]
    USERDATAINT_FIELD_NUMBER: _ClassVar[int]
    DATACOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMINSID_FIELD_NUMBER: _ClassVar[int]
    DefID: int
    Idx: int
    Color: int
    Dur: int
    RepairNum: int
    Name: str
    Fumo: PB_ArmFumo
    UserDataInt: int
    datacomponents: _containers.RepeatedCompositeFieldContainer[PB_ItemDataComponent]
    iteminsid: int
    def __init__(self, DefID: _Optional[int] = ..., Idx: _Optional[int] = ..., Color: _Optional[int] = ..., Dur: _Optional[int] = ..., RepairNum: _Optional[int] = ..., Name: _Optional[str] = ..., Fumo: _Optional[_Union[PB_ArmFumo, _Mapping]] = ..., UserDataInt: _Optional[int] = ..., datacomponents: _Optional[_Iterable[_Union[PB_ItemDataComponent, _Mapping]]] = ..., iteminsid: _Optional[int] = ...) -> None: ...

class PB_ItemSpecial(_message.Message):
    __slots__ = ("SpecailTypeID", "Buff")
    SPECAILTYPEID_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    SpecailTypeID: int
    Buff: str
    def __init__(self, SpecailTypeID: _Optional[int] = ..., Buff: _Optional[str] = ...) -> None: ...

class PB_ItemGridEffects(_message.Message):
    __slots__ = ("effectname", "effecscale", "v3fScale", "rot", "offset")
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    EFFECSCALE_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    effectname: str
    effecscale: float
    v3fScale: PB_Vector3f
    rot: PB_Vector3f
    offset: PB_Vector3f
    def __init__(self, effectname: _Optional[str] = ..., effecscale: _Optional[float] = ..., v3fScale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_ItemGridData(_message.Message):
    __slots__ = ("Item", "Arm", "ItemSpecial")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    ITEMSPECIAL_FIELD_NUMBER: _ClassVar[int]
    Item: PB_Item
    Arm: PB_Arm
    ItemSpecial: PB_ItemSpecial
    def __init__(self, Item: _Optional[_Union[PB_Item, _Mapping]] = ..., Arm: _Optional[_Union[PB_Arm, _Mapping]] = ..., ItemSpecial: _Optional[_Union[PB_ItemSpecial, _Mapping]] = ...) -> None: ...

class PB_ItemGrid(_message.Message):
    __slots__ = ("Dir", "FallDistance", "SpecialFlag", "Type", "ItemGridData", "grideffects")
    DIR_FIELD_NUMBER: _ClassVar[int]
    FALLDISTANCE_FIELD_NUMBER: _ClassVar[int]
    SPECIALFLAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMGRIDDATA_FIELD_NUMBER: _ClassVar[int]
    GRIDEFFECTS_FIELD_NUMBER: _ClassVar[int]
    Dir: PB_BodyDir
    FallDistance: float
    SpecialFlag: int
    Type: int
    ItemGridData: PB_ItemGridData
    grideffects: _containers.RepeatedCompositeFieldContainer[PB_ItemGridEffects]
    def __init__(self, Dir: _Optional[_Union[PB_BodyDir, _Mapping]] = ..., FallDistance: _Optional[float] = ..., SpecialFlag: _Optional[int] = ..., Type: _Optional[int] = ..., ItemGridData: _Optional[_Union[PB_ItemGridData, _Mapping]] = ..., grideffects: _Optional[_Iterable[_Union[PB_ItemGridEffects, _Mapping]]] = ...) -> None: ...

class PB_RoleBackpack(_message.Message):
    __slots__ = ("PackTmp",)
    PACKTMP_FIELD_NUMBER: _ClassVar[int]
    PackTmp: int
    def __init__(self, PackTmp: _Optional[int] = ...) -> None: ...

class PB_PlayerVipInfo(_message.Message):
    __slots__ = ("VipType", "VipLevel", "VipExp")
    VIPTYPE_FIELD_NUMBER: _ClassVar[int]
    VIPLEVEL_FIELD_NUMBER: _ClassVar[int]
    VIPEXP_FIELD_NUMBER: _ClassVar[int]
    VipType: int
    VipLevel: int
    VipExp: int
    def __init__(self, VipType: _Optional[int] = ..., VipLevel: _Optional[int] = ..., VipExp: _Optional[int] = ...) -> None: ...

class PB_ChunkBlob(_message.Message):
    __slots__ = ("UnzipLen", "BlobLen", "BlobDetail")
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBDETAIL_FIELD_NUMBER: _ClassVar[int]
    UnzipLen: int
    BlobLen: int
    BlobDetail: bytes
    def __init__(self, UnzipLen: _Optional[int] = ..., BlobLen: _Optional[int] = ..., BlobDetail: _Optional[bytes] = ...) -> None: ...

class PB_ChunkSaveDB(_message.Message):
    __slots__ = ("OWID", "MapID", "x", "z", "Version", "ShareFlag", "ChunkBlob")
    OWID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SHAREFLAG_FIELD_NUMBER: _ClassVar[int]
    CHUNKBLOB_FIELD_NUMBER: _ClassVar[int]
    OWID: int
    MapID: int
    x: int
    z: int
    Version: int
    ShareFlag: int
    ChunkBlob: PB_ChunkBlob
    def __init__(self, OWID: _Optional[int] = ..., MapID: _Optional[int] = ..., x: _Optional[int] = ..., z: _Optional[int] = ..., Version: _Optional[int] = ..., ShareFlag: _Optional[int] = ..., ChunkBlob: _Optional[_Union[PB_ChunkBlob, _Mapping]] = ...) -> None: ...

class PB_SectionLightData(_message.Message):
    __slots__ = ("UnzipLen", "BlobLen", "LightDataDetail")
    UNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOBLEN_FIELD_NUMBER: _ClassVar[int]
    LIGHTDATADETAIL_FIELD_NUMBER: _ClassVar[int]
    UnzipLen: int
    BlobLen: int
    LightDataDetail: str
    def __init__(self, UnzipLen: _Optional[int] = ..., BlobLen: _Optional[int] = ..., LightDataDetail: _Optional[str] = ...) -> None: ...

class PB_SectionLightDB(_message.Message):
    __slots__ = ("OWID", "MapID", "x", "z", "y", "SectionLightData")
    OWID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    SECTIONLIGHTDATA_FIELD_NUMBER: _ClassVar[int]
    OWID: int
    MapID: int
    x: int
    z: int
    y: int
    SectionLightData: PB_SectionLightData
    def __init__(self, OWID: _Optional[int] = ..., MapID: _Optional[int] = ..., x: _Optional[int] = ..., z: _Optional[int] = ..., y: _Optional[int] = ..., SectionLightData: _Optional[_Union[PB_SectionLightData, _Mapping]] = ...) -> None: ...

class PB_OverrideLightData(_message.Message):
    __slots__ = ("x", "y", "z", "data")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    z: int
    data: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., z: _Optional[int] = ..., data: _Optional[int] = ...) -> None: ...

class PB_OverrideLightDB(_message.Message):
    __slots__ = ("OWID", "MapID", "x", "z", "LightDataArray")
    OWID_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    LIGHTDATAARRAY_FIELD_NUMBER: _ClassVar[int]
    OWID: int
    MapID: int
    x: int
    z: int
    LightDataArray: _containers.RepeatedCompositeFieldContainer[PB_OverrideLightData]
    def __init__(self, OWID: _Optional[int] = ..., MapID: _Optional[int] = ..., x: _Optional[int] = ..., z: _Optional[int] = ..., LightDataArray: _Optional[_Iterable[_Union[PB_OverrideLightData, _Mapping]]] = ...) -> None: ...

class PB_GridPak(_message.Message):
    __slots__ = ("Grids",)
    GRIDS_FIELD_NUMBER: _ClassVar[int]
    Grids: _containers.RepeatedCompositeFieldContainer[PB_ItemGrid]
    def __init__(self, Grids: _Optional[_Iterable[_Union[PB_ItemGrid, _Mapping]]] = ...) -> None: ...

class PB_ShortcutPak(_message.Message):
    __slots__ = ("HandIdx", "Grids")
    HANDIDX_FIELD_NUMBER: _ClassVar[int]
    GRIDS_FIELD_NUMBER: _ClassVar[int]
    HandIdx: int
    Grids: _containers.RepeatedCompositeFieldContainer[PB_ItemGrid]
    def __init__(self, HandIdx: _Optional[int] = ..., Grids: _Optional[_Iterable[_Union[PB_ItemGrid, _Mapping]]] = ...) -> None: ...

class PB_ArmPak(_message.Message):
    __slots__ = ("Grids",)
    GRIDS_FIELD_NUMBER: _ClassVar[int]
    Grids: _containers.RepeatedCompositeFieldContainer[PB_ItemGrid]
    def __init__(self, Grids: _Optional[_Iterable[_Union[PB_ItemGrid, _Mapping]]] = ...) -> None: ...

class PB_ActorBuff(_message.Message):
    __slots__ = ("BuffID", "BuffLV", "Ticks", "BuffInstanceId", "RandomValue")
    BUFFID_FIELD_NUMBER: _ClassVar[int]
    BUFFLV_FIELD_NUMBER: _ClassVar[int]
    TICKS_FIELD_NUMBER: _ClassVar[int]
    BUFFINSTANCEID_FIELD_NUMBER: _ClassVar[int]
    RANDOMVALUE_FIELD_NUMBER: _ClassVar[int]
    BuffID: int
    BuffLV: int
    Ticks: int
    BuffInstanceId: int
    RandomValue: int
    def __init__(self, BuffID: _Optional[int] = ..., BuffLV: _Optional[int] = ..., Ticks: _Optional[int] = ..., BuffInstanceId: _Optional[int] = ..., RandomValue: _Optional[int] = ...) -> None: ...

class PB_BuffAttr(_message.Message):
    __slots__ = ("AttrID", "Val")
    ATTRID_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    AttrID: int
    Val: float
    def __init__(self, AttrID: _Optional[int] = ..., Val: _Optional[float] = ...) -> None: ...

class PB_RolePackage(_message.Message):
    __slots__ = ("GridPak", "ShortcutPak", "ArmPak", "RevicePos", "ExtPak", "MouseCursorPak")
    GRIDPAK_FIELD_NUMBER: _ClassVar[int]
    SHORTCUTPAK_FIELD_NUMBER: _ClassVar[int]
    ARMPAK_FIELD_NUMBER: _ClassVar[int]
    REVICEPOS_FIELD_NUMBER: _ClassVar[int]
    EXTPAK_FIELD_NUMBER: _ClassVar[int]
    MOUSECURSORPAK_FIELD_NUMBER: _ClassVar[int]
    GridPak: PB_GridPak
    ShortcutPak: PB_ShortcutPak
    ArmPak: PB_ArmPak
    RevicePos: PB_Pos
    ExtPak: PB_GridPak
    MouseCursorPak: PB_GridPak
    def __init__(self, GridPak: _Optional[_Union[PB_GridPak, _Mapping]] = ..., ShortcutPak: _Optional[_Union[PB_ShortcutPak, _Mapping]] = ..., ArmPak: _Optional[_Union[PB_ArmPak, _Mapping]] = ..., RevicePos: _Optional[_Union[PB_Pos, _Mapping]] = ..., ExtPak: _Optional[_Union[PB_GridPak, _Mapping]] = ..., MouseCursorPak: _Optional[_Union[PB_GridPak, _Mapping]] = ...) -> None: ...

class PB_ActorBuffList(_message.Message):
    __slots__ = ("Buffs", "RelBuffAttrs", "AbsBuffAttrs")
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    RELBUFFATTRS_FIELD_NUMBER: _ClassVar[int]
    ABSBUFFATTRS_FIELD_NUMBER: _ClassVar[int]
    Buffs: _containers.RepeatedCompositeFieldContainer[PB_ActorBuff]
    RelBuffAttrs: _containers.RepeatedCompositeFieldContainer[PB_BuffAttr]
    AbsBuffAttrs: _containers.RepeatedCompositeFieldContainer[PB_BuffAttr]
    def __init__(self, Buffs: _Optional[_Iterable[_Union[PB_ActorBuff, _Mapping]]] = ..., RelBuffAttrs: _Optional[_Iterable[_Union[PB_BuffAttr, _Mapping]]] = ..., AbsBuffAttrs: _Optional[_Iterable[_Union[PB_BuffAttr, _Mapping]]] = ...) -> None: ...

class PB_RoleData(_message.Message):
    __slots__ = ("Uin", "OWID", "HP", "Oxygen", "FoodLevel", "FoodSatLevel", "UsedStamina", "Exp", "Level", "LastLoginTime", "LoginNum", "FallDist", "Flags", "LiveTicks", "RideActorID", "Pos", "Dir", "Package", "Buff", "CarringActorID", "STRENGTH", "ENABLE_STRENGTH", "max_strength", "Armor", "Perseverance", "MaxHP", "StrengthFoodShowState", "StarDebuffStage", "StarDebuffTime", "CanThrow")
    UIN_FIELD_NUMBER: _ClassVar[int]
    OWID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    OXYGEN_FIELD_NUMBER: _ClassVar[int]
    FOODLEVEL_FIELD_NUMBER: _ClassVar[int]
    FOODSATLEVEL_FIELD_NUMBER: _ClassVar[int]
    USEDSTAMINA_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LASTLOGINTIME_FIELD_NUMBER: _ClassVar[int]
    LOGINNUM_FIELD_NUMBER: _ClassVar[int]
    FALLDIST_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LIVETICKS_FIELD_NUMBER: _ClassVar[int]
    RIDEACTORID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    BUFF_FIELD_NUMBER: _ClassVar[int]
    CARRINGACTORID_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    PERSEVERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    STRENGTHFOODSHOWSTATE_FIELD_NUMBER: _ClassVar[int]
    STARDEBUFFSTAGE_FIELD_NUMBER: _ClassVar[int]
    STARDEBUFFTIME_FIELD_NUMBER: _ClassVar[int]
    CANTHROW_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    OWID: int
    HP: float
    Oxygen: int
    FoodLevel: int
    FoodSatLevel: int
    UsedStamina: int
    Exp: int
    Level: int
    LastLoginTime: int
    LoginNum: int
    FallDist: float
    Flags: int
    LiveTicks: int
    RideActorID: int
    Pos: PB_Pos
    Dir: PB_BodyDir
    Package: PB_RolePackage
    Buff: PB_ActorBuffList
    CarringActorID: int
    STRENGTH: float
    ENABLE_STRENGTH: bool
    max_strength: float
    Armor: float
    Perseverance: float
    MaxHP: float
    StrengthFoodShowState: int
    StarDebuffStage: int
    StarDebuffTime: int
    CanThrow: bool
    def __init__(self, Uin: _Optional[int] = ..., OWID: _Optional[int] = ..., HP: _Optional[float] = ..., Oxygen: _Optional[int] = ..., FoodLevel: _Optional[int] = ..., FoodSatLevel: _Optional[int] = ..., UsedStamina: _Optional[int] = ..., Exp: _Optional[int] = ..., Level: _Optional[int] = ..., LastLoginTime: _Optional[int] = ..., LoginNum: _Optional[int] = ..., FallDist: _Optional[float] = ..., Flags: _Optional[int] = ..., LiveTicks: _Optional[int] = ..., RideActorID: _Optional[int] = ..., Pos: _Optional[_Union[PB_Pos, _Mapping]] = ..., Dir: _Optional[_Union[PB_BodyDir, _Mapping]] = ..., Package: _Optional[_Union[PB_RolePackage, _Mapping]] = ..., Buff: _Optional[_Union[PB_ActorBuffList, _Mapping]] = ..., CarringActorID: _Optional[int] = ..., STRENGTH: _Optional[float] = ..., ENABLE_STRENGTH: _Optional[bool] = ..., max_strength: _Optional[float] = ..., Armor: _Optional[float] = ..., Perseverance: _Optional[float] = ..., MaxHP: _Optional[float] = ..., StrengthFoodShowState: _Optional[int] = ..., StarDebuffStage: _Optional[int] = ..., StarDebuffTime: _Optional[int] = ..., CanThrow: _Optional[bool] = ...) -> None: ...

class PB_BodyEffectBrief(_message.Message):
    __slots__ = ("effectID", "effectScale", "effectClass", "effectTime", "v3fScale", "rot", "offset", "effectName")
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTCLASS_FIELD_NUMBER: _ClassVar[int]
    EFFECTTIME_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    effectID: int
    effectScale: float
    effectClass: int
    effectTime: float
    v3fScale: PB_Vector3f
    rot: PB_Vector3f
    offset: PB_Vector3f
    effectName: str
    def __init__(self, effectID: _Optional[int] = ..., effectScale: _Optional[float] = ..., effectClass: _Optional[int] = ..., effectTime: _Optional[float] = ..., v3fScale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., effectName: _Optional[str] = ...) -> None: ...

class PB_AOIBodyEffectBrief(_message.Message):
    __slots__ = ("effectID", "effectScale", "effectClass", "effecttime", "v3fScale", "rot", "offset", "effectName")
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    EFFECTSCALE_FIELD_NUMBER: _ClassVar[int]
    EFFECTCLASS_FIELD_NUMBER: _ClassVar[int]
    EFFECTTIME_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    effectID: int
    effectScale: int
    effectClass: int
    effecttime: int
    v3fScale: PB_Vector3f
    rot: PB_Vector3f
    offset: PB_Vector3f
    effectName: str
    def __init__(self, effectID: _Optional[int] = ..., effectScale: _Optional[int] = ..., effectClass: _Optional[int] = ..., effecttime: _Optional[int] = ..., v3fScale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., effectName: _Optional[str] = ...) -> None: ...

class PB_PlayerInfo(_message.Message):
    __slots__ = ("ObjID", "anim", "anim1", "RoleData", "BodyColor", "bodyscale_invalid", "effectList", "customscale", "soundList", "actSeqId", "accountSkinID", "TeamID", "sawtooth", "fishing", "nodeid", "CurDisplayHorseObjID", "animweapon", "useCustomModel", "scale", "isAIPlayer", "AIVoiceType")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ANIM_FIELD_NUMBER: _ClassVar[int]
    ANIM1_FIELD_NUMBER: _ClassVar[int]
    ROLEDATA_FIELD_NUMBER: _ClassVar[int]
    BODYCOLOR_FIELD_NUMBER: _ClassVar[int]
    BODYSCALE_INVALID_FIELD_NUMBER: _ClassVar[int]
    EFFECTLIST_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSCALE_FIELD_NUMBER: _ClassVar[int]
    SOUNDLIST_FIELD_NUMBER: _ClassVar[int]
    ACTSEQID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSKINID_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    SAWTOOTH_FIELD_NUMBER: _ClassVar[int]
    FISHING_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    CURDISPLAYHORSEOBJID_FIELD_NUMBER: _ClassVar[int]
    ANIMWEAPON_FIELD_NUMBER: _ClassVar[int]
    USECUSTOMMODEL_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ISAIPLAYER_FIELD_NUMBER: _ClassVar[int]
    AIVOICETYPE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    anim: int
    anim1: int
    RoleData: PB_RoleData
    BodyColor: int
    bodyscale_invalid: float
    effectList: _containers.RepeatedCompositeFieldContainer[PB_BodyEffectBrief]
    customscale: float
    soundList: _containers.RepeatedCompositeFieldContainer[PB_EffectTriggerSound]
    actSeqId: int
    accountSkinID: int
    TeamID: int
    sawtooth: _containers.RepeatedCompositeFieldContainer[PB_SawtoothInfo]
    fishing: PB_FishingInfo
    nodeid: int
    CurDisplayHorseObjID: int
    animweapon: int
    useCustomModel: bool
    scale: PB_Vector3f
    isAIPlayer: bool
    AIVoiceType: str
    def __init__(self, ObjID: _Optional[int] = ..., anim: _Optional[int] = ..., anim1: _Optional[int] = ..., RoleData: _Optional[_Union[PB_RoleData, _Mapping]] = ..., BodyColor: _Optional[int] = ..., bodyscale_invalid: _Optional[float] = ..., effectList: _Optional[_Iterable[_Union[PB_BodyEffectBrief, _Mapping]]] = ..., customscale: _Optional[float] = ..., soundList: _Optional[_Iterable[_Union[PB_EffectTriggerSound, _Mapping]]] = ..., actSeqId: _Optional[int] = ..., accountSkinID: _Optional[int] = ..., TeamID: _Optional[int] = ..., sawtooth: _Optional[_Iterable[_Union[PB_SawtoothInfo, _Mapping]]] = ..., fishing: _Optional[_Union[PB_FishingInfo, _Mapping]] = ..., nodeid: _Optional[int] = ..., CurDisplayHorseObjID: _Optional[int] = ..., animweapon: _Optional[int] = ..., useCustomModel: _Optional[bool] = ..., scale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., isAIPlayer: _Optional[bool] = ..., AIVoiceType: _Optional[str] = ...) -> None: ...

class PB_RedStoneIdx(_message.Message):
    __slots__ = ("x", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: int
    z: int
    def __init__(self, x: _Optional[int] = ..., z: _Optional[int] = ...) -> None: ...

class PB_RedStoneData(_message.Message):
    __slots__ = ("RedStoneIdxList",)
    REDSTONEIDXLIST_FIELD_NUMBER: _ClassVar[int]
    RedStoneIdxList: _containers.RepeatedCompositeFieldContainer[PB_RedStoneIdx]
    def __init__(self, RedStoneIdxList: _Optional[_Iterable[_Union[PB_RedStoneIdx, _Mapping]]] = ...) -> None: ...

class PB_GlobalBin(_message.Message):
    __slots__ = ("BinLen", "BinContent")
    BINLEN_FIELD_NUMBER: _ClassVar[int]
    BINCONTENT_FIELD_NUMBER: _ClassVar[int]
    BinLen: int
    BinContent: str
    def __init__(self, BinLen: _Optional[int] = ..., BinContent: _Optional[str] = ...) -> None: ...

class PB_OWGlobalMisc(_message.Message):
    __slots__ = ("GlobalFlag", "ChunkVer", "ChunkVerBroadCast", "InitPos", "RevicePos", "RedStoneData", "GlobalBin")
    GLOBALFLAG_FIELD_NUMBER: _ClassVar[int]
    CHUNKVER_FIELD_NUMBER: _ClassVar[int]
    CHUNKVERBROADCAST_FIELD_NUMBER: _ClassVar[int]
    INITPOS_FIELD_NUMBER: _ClassVar[int]
    REVICEPOS_FIELD_NUMBER: _ClassVar[int]
    REDSTONEDATA_FIELD_NUMBER: _ClassVar[int]
    GLOBALBIN_FIELD_NUMBER: _ClassVar[int]
    GlobalFlag: int
    ChunkVer: int
    ChunkVerBroadCast: int
    InitPos: PB_Pos
    RevicePos: PB_Pos
    RedStoneData: PB_RedStoneData
    GlobalBin: PB_GlobalBin
    def __init__(self, GlobalFlag: _Optional[int] = ..., ChunkVer: _Optional[int] = ..., ChunkVerBroadCast: _Optional[int] = ..., InitPos: _Optional[_Union[PB_Pos, _Mapping]] = ..., RevicePos: _Optional[_Union[PB_Pos, _Mapping]] = ..., RedStoneData: _Optional[_Union[PB_RedStoneData, _Mapping]] = ..., GlobalBin: _Optional[_Union[PB_GlobalBin, _Mapping]] = ...) -> None: ...

class PB_OWGlobal(_message.Message):
    __slots__ = ("OWID", "ID", "Uin", "SvrStart", "GridChgNum", "Misc")
    OWID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    SVRSTART_FIELD_NUMBER: _ClassVar[int]
    GRIDCHGNUM_FIELD_NUMBER: _ClassVar[int]
    MISC_FIELD_NUMBER: _ClassVar[int]
    OWID: int
    ID: int
    Uin: int
    SvrStart: int
    GridChgNum: int
    Misc: PB_OWGlobalMisc
    def __init__(self, OWID: _Optional[int] = ..., ID: _Optional[int] = ..., Uin: _Optional[int] = ..., SvrStart: _Optional[int] = ..., GridChgNum: _Optional[int] = ..., Misc: _Optional[_Union[PB_OWGlobalMisc, _Mapping]] = ...) -> None: ...

class PB_WorldCreateData(_message.Message):
    __slots__ = ("TerrType", "RandSeed1", "RandSeed2", "RoleModel", "SeedStr", "TilesX", "TilesZ")
    TERRTYPE_FIELD_NUMBER: _ClassVar[int]
    RANDSEED1_FIELD_NUMBER: _ClassVar[int]
    RANDSEED2_FIELD_NUMBER: _ClassVar[int]
    ROLEMODEL_FIELD_NUMBER: _ClassVar[int]
    SEEDSTR_FIELD_NUMBER: _ClassVar[int]
    TILESX_FIELD_NUMBER: _ClassVar[int]
    TILESZ_FIELD_NUMBER: _ClassVar[int]
    TerrType: int
    RandSeed1: int
    RandSeed2: int
    RoleModel: int
    SeedStr: str
    TilesX: int
    TilesZ: int
    def __init__(self, TerrType: _Optional[int] = ..., RandSeed1: _Optional[int] = ..., RandSeed2: _Optional[int] = ..., RoleModel: _Optional[int] = ..., SeedStr: _Optional[str] = ..., TilesX: _Optional[int] = ..., TilesZ: _Optional[int] = ...) -> None: ...

class PB_WorldDesc(_message.Message):
    __slots__ = ("WorldId", "WorldType", "OwnerUin", "CreateData", "DeveloperFlag", "FromOWID", "RealOwnerUin", "WorldOpen", "WorldName", "TempType", "pwid", "SpecialType", "editorSceneSwitch", "ctype", "fissionType", "fissionFrom", "fissionVersion", "extraInfo")
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    WORLDTYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERUIN_FIELD_NUMBER: _ClassVar[int]
    CREATEDATA_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERFLAG_FIELD_NUMBER: _ClassVar[int]
    FROMOWID_FIELD_NUMBER: _ClassVar[int]
    REALOWNERUIN_FIELD_NUMBER: _ClassVar[int]
    WORLDOPEN_FIELD_NUMBER: _ClassVar[int]
    WORLDNAME_FIELD_NUMBER: _ClassVar[int]
    TEMPTYPE_FIELD_NUMBER: _ClassVar[int]
    PWID_FIELD_NUMBER: _ClassVar[int]
    SPECIALTYPE_FIELD_NUMBER: _ClassVar[int]
    EDITORSCENESWITCH_FIELD_NUMBER: _ClassVar[int]
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    FISSIONTYPE_FIELD_NUMBER: _ClassVar[int]
    FISSIONFROM_FIELD_NUMBER: _ClassVar[int]
    FISSIONVERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRAINFO_FIELD_NUMBER: _ClassVar[int]
    WorldId: int
    WorldType: int
    OwnerUin: int
    CreateData: PB_WorldCreateData
    DeveloperFlag: int
    FromOWID: int
    RealOwnerUin: int
    WorldOpen: int
    WorldName: str
    TempType: int
    pwid: int
    SpecialType: int
    editorSceneSwitch: int
    ctype: int
    fissionType: int
    fissionFrom: int
    fissionVersion: int
    extraInfo: str
    def __init__(self, WorldId: _Optional[int] = ..., WorldType: _Optional[int] = ..., OwnerUin: _Optional[int] = ..., CreateData: _Optional[_Union[PB_WorldCreateData, _Mapping]] = ..., DeveloperFlag: _Optional[int] = ..., FromOWID: _Optional[int] = ..., RealOwnerUin: _Optional[int] = ..., WorldOpen: _Optional[int] = ..., WorldName: _Optional[str] = ..., TempType: _Optional[int] = ..., pwid: _Optional[int] = ..., SpecialType: _Optional[int] = ..., editorSceneSwitch: _Optional[int] = ..., ctype: _Optional[int] = ..., fissionType: _Optional[int] = ..., fissionFrom: _Optional[int] = ..., fissionVersion: _Optional[int] = ..., extraInfo: _Optional[str] = ...) -> None: ...

class PB_SkillCDData(_message.Message):
    __slots__ = ("NumSkillCD", "ItemID", "CD")
    NUMSKILLCD_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    NumSkillCD: int
    ItemID: _containers.RepeatedScalarFieldContainer[int]
    CD: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, NumSkillCD: _Optional[int] = ..., ItemID: _Optional[_Iterable[int]] = ..., CD: _Optional[_Iterable[float]] = ...) -> None: ...

class PB_RoleInfo(_message.Message):
    __slots__ = ("Model", "NickName", "SkinID", "CustomJson", "FrameID", "BPtitle", "ModAvatar", "JoinFromSrc")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMJSON_FIELD_NUMBER: _ClassVar[int]
    FRAMEID_FIELD_NUMBER: _ClassVar[int]
    BPTITLE_FIELD_NUMBER: _ClassVar[int]
    MODAVATAR_FIELD_NUMBER: _ClassVar[int]
    JOINFROMSRC_FIELD_NUMBER: _ClassVar[int]
    Model: int
    NickName: str
    SkinID: int
    CustomJson: str
    FrameID: int
    BPtitle: str
    ModAvatar: str
    JoinFromSrc: str
    def __init__(self, Model: _Optional[int] = ..., NickName: _Optional[str] = ..., SkinID: _Optional[int] = ..., CustomJson: _Optional[str] = ..., FrameID: _Optional[int] = ..., BPtitle: _Optional[str] = ..., ModAvatar: _Optional[str] = ..., JoinFromSrc: _Optional[str] = ...) -> None: ...

class PB_ActorRoleInfo(_message.Message):
    __slots__ = ("Info", "Player")
    INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    Info: PB_RoleInfo
    Player: PB_PlayerInfo
    def __init__(self, Info: _Optional[_Union[PB_RoleInfo, _Mapping]] = ..., Player: _Optional[_Union[PB_PlayerInfo, _Mapping]] = ...) -> None: ...

class PB_ActorAttInfo(_message.Message):
    __slots__ = ("maxhp", "hprecover", "walkspeed", "swimspeed", "jumppower", "punchattack", "rangeattack", "punchdefense", "rangedefense", "dodge", "attacktype", "immunetype", "settingatt")
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    HPRECOVER_FIELD_NUMBER: _ClassVar[int]
    WALKSPEED_FIELD_NUMBER: _ClassVar[int]
    SWIMSPEED_FIELD_NUMBER: _ClassVar[int]
    JUMPPOWER_FIELD_NUMBER: _ClassVar[int]
    PUNCHATTACK_FIELD_NUMBER: _ClassVar[int]
    RANGEATTACK_FIELD_NUMBER: _ClassVar[int]
    PUNCHDEFENSE_FIELD_NUMBER: _ClassVar[int]
    RANGEDEFENSE_FIELD_NUMBER: _ClassVar[int]
    DODGE_FIELD_NUMBER: _ClassVar[int]
    ATTACKTYPE_FIELD_NUMBER: _ClassVar[int]
    IMMUNETYPE_FIELD_NUMBER: _ClassVar[int]
    SETTINGATT_FIELD_NUMBER: _ClassVar[int]
    maxhp: int
    hprecover: int
    walkspeed: int
    swimspeed: int
    jumppower: int
    punchattack: int
    rangeattack: int
    punchdefense: int
    rangedefense: int
    dodge: int
    attacktype: int
    immunetype: int
    settingatt: int
    def __init__(self, maxhp: _Optional[int] = ..., hprecover: _Optional[int] = ..., walkspeed: _Optional[int] = ..., swimspeed: _Optional[int] = ..., jumppower: _Optional[int] = ..., punchattack: _Optional[int] = ..., rangeattack: _Optional[int] = ..., punchdefense: _Optional[int] = ..., rangedefense: _Optional[int] = ..., dodge: _Optional[int] = ..., attacktype: _Optional[int] = ..., immunetype: _Optional[int] = ..., settingatt: _Optional[int] = ...) -> None: ...

class PB_SawtoothInfo(_message.Message):
    __slots__ = ("sawtoothid", "pos")
    SAWTOOTHID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    sawtoothid: int
    pos: PB_Vector3
    def __init__(self, sawtoothid: _Optional[int] = ..., pos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_FishingInfo(_message.Message):
    __slots__ = ("FishingState", "FishingItemId", "HookID")
    FISHINGSTATE_FIELD_NUMBER: _ClassVar[int]
    FISHINGITEMID_FIELD_NUMBER: _ClassVar[int]
    HOOKID_FIELD_NUMBER: _ClassVar[int]
    FishingState: int
    FishingItemId: int
    HookID: int
    def __init__(self, FishingState: _Optional[int] = ..., FishingItemId: _Optional[int] = ..., HookID: _Optional[int] = ...) -> None: ...

class PB_ActorCommon(_message.Message):
    __slots__ = ("wid", "pos", "motion", "yaw", "pitch", "falldist", "flags", "liveticks", "attinfo", "masterobjid", "sawtooth", "sandboxnodes", "teamid", "cancollide")
    WID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FALLDIST_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    LIVETICKS_FIELD_NUMBER: _ClassVar[int]
    ATTINFO_FIELD_NUMBER: _ClassVar[int]
    MASTEROBJID_FIELD_NUMBER: _ClassVar[int]
    SAWTOOTH_FIELD_NUMBER: _ClassVar[int]
    SANDBOXNODES_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    CANCOLLIDE_FIELD_NUMBER: _ClassVar[int]
    wid: int
    pos: PB_Vector3
    motion: PB_Vector3
    yaw: int
    pitch: int
    falldist: int
    flags: int
    liveticks: int
    attinfo: PB_ActorAttInfo
    masterobjid: int
    sawtooth: _containers.RepeatedCompositeFieldContainer[PB_SawtoothInfo]
    sandboxnodes: bytes
    teamid: int
    cancollide: bool
    def __init__(self, wid: _Optional[int] = ..., pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., motion: _Optional[_Union[PB_Vector3, _Mapping]] = ..., yaw: _Optional[int] = ..., pitch: _Optional[int] = ..., falldist: _Optional[int] = ..., flags: _Optional[int] = ..., liveticks: _Optional[int] = ..., attinfo: _Optional[_Union[PB_ActorAttInfo, _Mapping]] = ..., masterobjid: _Optional[int] = ..., sawtooth: _Optional[_Iterable[_Union[PB_SawtoothInfo, _Mapping]]] = ..., sandboxnodes: _Optional[bytes] = ..., teamid: _Optional[int] = ..., cancollide: _Optional[bool] = ...) -> None: ...

class PB_AOIActorBuff(_message.Message):
    __slots__ = ("buffid", "bufflv", "ticks")
    BUFFID_FIELD_NUMBER: _ClassVar[int]
    BUFFLV_FIELD_NUMBER: _ClassVar[int]
    TICKS_FIELD_NUMBER: _ClassVar[int]
    buffid: int
    bufflv: int
    ticks: int
    def __init__(self, buffid: _Optional[int] = ..., bufflv: _Optional[int] = ..., ticks: _Optional[int] = ...) -> None: ...

class PB_AttribMod(_message.Message):
    __slots__ = ("attr", "val")
    ATTR_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    attr: int
    val: int
    def __init__(self, attr: _Optional[int] = ..., val: _Optional[int] = ...) -> None: ...

class PB_ItemIndexGrid(_message.Message):
    __slots__ = ("index", "itemid", "num", "durable", "enchants", "userdata", "userdata_str", "sid_str", "userdataEx", "runes", "effects", "toughness", "datacomponents", "iteminsid", "lock")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    ENCHANTS_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    USERDATA_STR_FIELD_NUMBER: _ClassVar[int]
    SID_STR_FIELD_NUMBER: _ClassVar[int]
    USERDATAEX_FIELD_NUMBER: _ClassVar[int]
    RUNES_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    TOUGHNESS_FIELD_NUMBER: _ClassVar[int]
    DATACOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMINSID_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    index: int
    itemid: int
    num: int
    durable: int
    enchants: _containers.RepeatedScalarFieldContainer[int]
    userdata: int
    userdata_str: str
    sid_str: str
    userdataEx: int
    runes: _containers.RepeatedCompositeFieldContainer[PB_ItemRune]
    effects: _containers.RepeatedCompositeFieldContainer[PB_ItemGridEffects]
    toughness: int
    datacomponents: _containers.RepeatedCompositeFieldContainer[PB_ItemDataComponent]
    iteminsid: int
    lock: bool
    def __init__(self, index: _Optional[int] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ..., durable: _Optional[int] = ..., enchants: _Optional[_Iterable[int]] = ..., userdata: _Optional[int] = ..., userdata_str: _Optional[str] = ..., sid_str: _Optional[str] = ..., userdataEx: _Optional[int] = ..., runes: _Optional[_Iterable[_Union[PB_ItemRune, _Mapping]]] = ..., effects: _Optional[_Iterable[_Union[PB_ItemGridEffects, _Mapping]]] = ..., toughness: _Optional[int] = ..., datacomponents: _Optional[_Iterable[_Union[PB_ItemDataComponent, _Mapping]]] = ..., iteminsid: _Optional[int] = ..., lock: _Optional[bool] = ...) -> None: ...

class PB_ActorItem(_message.Message):
    __slots__ = ("basedata", "itemid", "num", "durable", "delayticks", "enchants", "userdatastr", "serverid", "runes", "toughness", "datacomponents", "iteminsid", "beltPosition")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    DELAYTICKS_FIELD_NUMBER: _ClassVar[int]
    ENCHANTS_FIELD_NUMBER: _ClassVar[int]
    USERDATASTR_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    RUNES_FIELD_NUMBER: _ClassVar[int]
    TOUGHNESS_FIELD_NUMBER: _ClassVar[int]
    DATACOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMINSID_FIELD_NUMBER: _ClassVar[int]
    BELTPOSITION_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    itemid: int
    num: int
    durable: int
    delayticks: int
    enchants: _containers.RepeatedScalarFieldContainer[int]
    userdatastr: str
    serverid: str
    runes: _containers.RepeatedCompositeFieldContainer[PB_ItemRune]
    toughness: int
    datacomponents: _containers.RepeatedCompositeFieldContainer[PB_ItemDataComponent]
    iteminsid: int
    beltPosition: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ..., durable: _Optional[int] = ..., delayticks: _Optional[int] = ..., enchants: _Optional[_Iterable[int]] = ..., userdatastr: _Optional[str] = ..., serverid: _Optional[str] = ..., runes: _Optional[_Iterable[_Union[PB_ItemRune, _Mapping]]] = ..., toughness: _Optional[int] = ..., datacomponents: _Optional[_Iterable[_Union[PB_ItemDataComponent, _Mapping]]] = ..., iteminsid: _Optional[int] = ..., beltPosition: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_ActorFlyBlock(_message.Message):
    __slots__ = ("basedata", "blockid", "blockdata", "maxdist", "dropitem", "startblock")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKDATA_FIELD_NUMBER: _ClassVar[int]
    MAXDIST_FIELD_NUMBER: _ClassVar[int]
    DROPITEM_FIELD_NUMBER: _ClassVar[int]
    STARTBLOCK_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    blockid: int
    blockdata: int
    maxdist: int
    dropitem: bool
    startblock: PB_Vector3
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., blockid: _Optional[int] = ..., blockdata: _Optional[int] = ..., maxdist: _Optional[int] = ..., dropitem: _Optional[bool] = ..., startblock: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorProjectile(_message.Message):
    __slots__ = ("basedata", "shooter", "itemid", "durable", "enchants", "color", "blockid", "blockpos", "rotatequat", "runes", "prerotatequat", "inground")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    SHOOTER_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    ENCHANTS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ROTATEQUAT_FIELD_NUMBER: _ClassVar[int]
    RUNES_FIELD_NUMBER: _ClassVar[int]
    PREROTATEQUAT_FIELD_NUMBER: _ClassVar[int]
    INGROUND_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    shooter: int
    itemid: int
    durable: int
    enchants: _containers.RepeatedScalarFieldContainer[int]
    color: int
    blockid: int
    blockpos: PB_Vector3
    rotatequat: _containers.RepeatedScalarFieldContainer[int]
    runes: _containers.RepeatedCompositeFieldContainer[PB_ItemRune]
    prerotatequat: _containers.RepeatedScalarFieldContainer[int]
    inground: bool
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., shooter: _Optional[int] = ..., itemid: _Optional[int] = ..., durable: _Optional[int] = ..., enchants: _Optional[_Iterable[int]] = ..., color: _Optional[int] = ..., blockid: _Optional[int] = ..., blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., rotatequat: _Optional[_Iterable[int]] = ..., runes: _Optional[_Iterable[_Union[PB_ItemRune, _Mapping]]] = ..., prerotatequat: _Optional[_Iterable[int]] = ..., inground: _Optional[bool] = ...) -> None: ...

class PB_ActorThornBall(_message.Message):
    __slots__ = ("ActorProjectile", "impactActor", "isDrop")
    ACTORPROJECTILE_FIELD_NUMBER: _ClassVar[int]
    IMPACTACTOR_FIELD_NUMBER: _ClassVar[int]
    ISDROP_FIELD_NUMBER: _ClassVar[int]
    ActorProjectile: PB_ActorProjectile
    impactActor: bool
    isDrop: bool
    def __init__(self, ActorProjectile: _Optional[_Union[PB_ActorProjectile, _Mapping]] = ..., impactActor: _Optional[bool] = ..., isDrop: _Optional[bool] = ...) -> None: ...

class PB_ActorFishhook(_message.Message):
    __slots__ = ("ActorProjectile", "resultId")
    ACTORPROJECTILE_FIELD_NUMBER: _ClassVar[int]
    RESULTID_FIELD_NUMBER: _ClassVar[int]
    ActorProjectile: PB_ActorProjectile
    resultId: int
    def __init__(self, ActorProjectile: _Optional[_Union[PB_ActorProjectile, _Mapping]] = ..., resultId: _Optional[int] = ...) -> None: ...

class PB_ActorFlyMob(_message.Message):
    __slots__ = ("mobdata", "moveTarget", "luadata")
    MOBDATA_FIELD_NUMBER: _ClassVar[int]
    MOVETARGET_FIELD_NUMBER: _ClassVar[int]
    LUADATA_FIELD_NUMBER: _ClassVar[int]
    mobdata: PB_ActorMob
    moveTarget: PB_Vector3
    luadata: str
    def __init__(self, mobdata: _Optional[_Union[PB_ActorMob, _Mapping]] = ..., moveTarget: _Optional[_Union[PB_Vector3, _Mapping]] = ..., luadata: _Optional[str] = ...) -> None: ...

class PB_ActorGhost(_message.Message):
    __slots__ = ("basedata", "defid", "hp", "missionflags")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    DEFID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    MISSIONFLAGS_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    defid: int
    hp: int
    missionflags: int
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., defid: _Optional[int] = ..., hp: _Optional[int] = ..., missionflags: _Optional[int] = ...) -> None: ...

class PB_ActorPipeline(_message.Message):
    __slots__ = ("itemData",)
    ITEMDATA_FIELD_NUMBER: _ClassVar[int]
    itemData: PB_ActorItem
    def __init__(self, itemData: _Optional[_Union[PB_ActorItem, _Mapping]] = ...) -> None: ...

class PB_BindPlayerToPhysicsPlat(_message.Message):
    __slots__ = ("uin", "objId", "localPos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    LOCALPOS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    objId: int
    localPos: PB_Vector3f
    def __init__(self, uin: _Optional[int] = ..., objId: _Optional[int] = ..., localPos: _Optional[_Union[PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_UnBindPlayerToPhysicsPlat(_message.Message):
    __slots__ = ("objId", "uin")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    objId: int
    uin: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, objId: _Optional[int] = ..., uin: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_OnPlatPlayerInfo(_message.Message):
    __slots__ = ("uin", "localPos")
    UIN_FIELD_NUMBER: _ClassVar[int]
    LOCALPOS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    localPos: PB_Vector3f
    def __init__(self, uin: _Optional[int] = ..., localPos: _Optional[_Union[PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_ActorPhysicsCom(_message.Message):
    __slots__ = ("type", "shape", "centerOffset", "boxSize", "radius", "height", "drag", "angularDrag", "useGravity", "mass", "isKinematic", "centerOfMass", "bConvex", "bPlatform", "staticFriction", "dynamicFriction", "restitution", "onPlatPlayers")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    CENTEROFFSET_FIELD_NUMBER: _ClassVar[int]
    BOXSIZE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DRAG_FIELD_NUMBER: _ClassVar[int]
    ANGULARDRAG_FIELD_NUMBER: _ClassVar[int]
    USEGRAVITY_FIELD_NUMBER: _ClassVar[int]
    MASS_FIELD_NUMBER: _ClassVar[int]
    ISKINEMATIC_FIELD_NUMBER: _ClassVar[int]
    CENTEROFMASS_FIELD_NUMBER: _ClassVar[int]
    BCONVEX_FIELD_NUMBER: _ClassVar[int]
    BPLATFORM_FIELD_NUMBER: _ClassVar[int]
    STATICFRICTION_FIELD_NUMBER: _ClassVar[int]
    DYNAMICFRICTION_FIELD_NUMBER: _ClassVar[int]
    RESTITUTION_FIELD_NUMBER: _ClassVar[int]
    ONPLATPLAYERS_FIELD_NUMBER: _ClassVar[int]
    type: int
    shape: int
    centerOffset: PB_Vector3f
    boxSize: PB_Vector3f
    radius: float
    height: float
    drag: float
    angularDrag: float
    useGravity: bool
    mass: float
    isKinematic: bool
    centerOfMass: PB_Vector3f
    bConvex: bool
    bPlatform: bool
    staticFriction: float
    dynamicFriction: float
    restitution: float
    onPlatPlayers: _containers.RepeatedCompositeFieldContainer[PB_OnPlatPlayerInfo]
    def __init__(self, type: _Optional[int] = ..., shape: _Optional[int] = ..., centerOffset: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., boxSize: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., radius: _Optional[float] = ..., height: _Optional[float] = ..., drag: _Optional[float] = ..., angularDrag: _Optional[float] = ..., useGravity: _Optional[bool] = ..., mass: _Optional[float] = ..., isKinematic: _Optional[bool] = ..., centerOfMass: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., bConvex: _Optional[bool] = ..., bPlatform: _Optional[bool] = ..., staticFriction: _Optional[float] = ..., dynamicFriction: _Optional[float] = ..., restitution: _Optional[float] = ..., onPlatPlayers: _Optional[_Iterable[_Union[PB_OnPlatPlayerInfo, _Mapping]]] = ...) -> None: ...

class PB_ActorPhysicsComUpdate(_message.Message):
    __slots__ = ("objId", "type", "shape", "centerOffset", "boxSize", "radius", "height", "bConvex", "bPlatform", "objIdRoot")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    CENTEROFFSET_FIELD_NUMBER: _ClassVar[int]
    BOXSIZE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BCONVEX_FIELD_NUMBER: _ClassVar[int]
    BPLATFORM_FIELD_NUMBER: _ClassVar[int]
    OBJIDROOT_FIELD_NUMBER: _ClassVar[int]
    objId: int
    type: int
    shape: int
    centerOffset: PB_Vector3f
    boxSize: PB_Vector3f
    radius: float
    height: float
    bConvex: bool
    bPlatform: bool
    objIdRoot: int
    def __init__(self, objId: _Optional[int] = ..., type: _Optional[int] = ..., shape: _Optional[int] = ..., centerOffset: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., boxSize: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., radius: _Optional[float] = ..., height: _Optional[float] = ..., bConvex: _Optional[bool] = ..., bPlatform: _Optional[bool] = ..., objIdRoot: _Optional[int] = ...) -> None: ...

class PB_EffectComObjTrigPtclInfo(_message.Message):
    __slots__ = ("fxname", "loopPlayTime", "v3fScale", "rot", "offset")
    FXNAME_FIELD_NUMBER: _ClassVar[int]
    LOOPPLAYTIME_FIELD_NUMBER: _ClassVar[int]
    V3FSCALE_FIELD_NUMBER: _ClassVar[int]
    ROT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    fxname: str
    loopPlayTime: float
    v3fScale: PB_Vector3f
    rot: PB_Vector3f
    offset: PB_Vector3f
    def __init__(self, fxname: _Optional[str] = ..., loopPlayTime: _Optional[float] = ..., v3fScale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., rot: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., offset: _Optional[_Union[PB_Vector3f, _Mapping]] = ...) -> None: ...

class PB_EffectComParticleInfo(_message.Message):
    __slots__ = ("particleId", "isLoop", "objTrigPtcls", "particleStrId")
    PARTICLEID_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    OBJTRIGPTCLS_FIELD_NUMBER: _ClassVar[int]
    PARTICLESTRID_FIELD_NUMBER: _ClassVar[int]
    particleId: int
    isLoop: bool
    objTrigPtcls: _containers.RepeatedCompositeFieldContainer[PB_EffectComObjTrigPtclInfo]
    particleStrId: str
    def __init__(self, particleId: _Optional[int] = ..., isLoop: _Optional[bool] = ..., objTrigPtcls: _Optional[_Iterable[_Union[PB_EffectComObjTrigPtclInfo, _Mapping]]] = ..., particleStrId: _Optional[str] = ...) -> None: ...

class PB_EffectComParticleUpd(_message.Message):
    __slots__ = ("objId", "info", "objIdRoot")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    OBJIDROOT_FIELD_NUMBER: _ClassVar[int]
    objId: int
    info: PB_EffectComParticleInfo
    objIdRoot: int
    def __init__(self, objId: _Optional[int] = ..., info: _Optional[_Union[PB_EffectComParticleInfo, _Mapping]] = ..., objIdRoot: _Optional[int] = ...) -> None: ...

class PB_SoundComInfo(_message.Message):
    __slots__ = ("soundId", "isPlayNow", "isLoop", "volume", "pitch", "playingMode", "soundStrId")
    SOUNDID_FIELD_NUMBER: _ClassVar[int]
    ISPLAYNOW_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    PLAYINGMODE_FIELD_NUMBER: _ClassVar[int]
    SOUNDSTRID_FIELD_NUMBER: _ClassVar[int]
    soundId: int
    isPlayNow: bool
    isLoop: bool
    volume: float
    pitch: float
    playingMode: int
    soundStrId: str
    def __init__(self, soundId: _Optional[int] = ..., isPlayNow: _Optional[bool] = ..., isLoop: _Optional[bool] = ..., volume: _Optional[float] = ..., pitch: _Optional[float] = ..., playingMode: _Optional[int] = ..., soundStrId: _Optional[str] = ...) -> None: ...

class PB_SoundComUpd(_message.Message):
    __slots__ = ("objId", "info")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    objId: int
    info: PB_SoundComInfo
    def __init__(self, objId: _Optional[int] = ..., info: _Optional[_Union[PB_SoundComInfo, _Mapping]] = ...) -> None: ...

class PB_MeteorShowerInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: int
    def __init__(self, type: _Optional[int] = ...) -> None: ...

class PB_ActorObj(_message.Message):
    __slots__ = ("basedata", "modelpath", "modeltype", "extradata", "scale", "interacted", "modelcomponent", "roll", "physicsCom", "effectComPtclInfo", "nodeid", "isparent", "parentwid", "children", "script", "soundComInfo", "PB_HeredityVec")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    MODELPATH_FIELD_NUMBER: _ClassVar[int]
    MODELTYPE_FIELD_NUMBER: _ClassVar[int]
    EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    INTERACTED_FIELD_NUMBER: _ClassVar[int]
    MODELCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    PHYSICSCOM_FIELD_NUMBER: _ClassVar[int]
    EFFECTCOMPTCLINFO_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    ISPARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTWID_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SOUNDCOMINFO_FIELD_NUMBER: _ClassVar[int]
    PB_HEREDITYVEC_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    modelpath: str
    modeltype: int
    extradata: int
    scale: PB_Vector3f
    interacted: bool
    modelcomponent: str
    roll: float
    physicsCom: PB_ActorPhysicsCom
    effectComPtclInfo: PB_EffectComParticleInfo
    nodeid: int
    isparent: bool
    parentwid: int
    children: str
    script: str
    soundComInfo: PB_SoundComInfo
    PB_HeredityVec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., modelpath: _Optional[str] = ..., modeltype: _Optional[int] = ..., extradata: _Optional[int] = ..., scale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., interacted: _Optional[bool] = ..., modelcomponent: _Optional[str] = ..., roll: _Optional[float] = ..., physicsCom: _Optional[_Union[PB_ActorPhysicsCom, _Mapping]] = ..., effectComPtclInfo: _Optional[_Union[PB_EffectComParticleInfo, _Mapping]] = ..., nodeid: _Optional[int] = ..., isparent: _Optional[bool] = ..., parentwid: _Optional[int] = ..., children: _Optional[str] = ..., script: _Optional[str] = ..., soundComInfo: _Optional[_Union[PB_SoundComInfo, _Mapping]] = ..., PB_HeredityVec: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_ActorObjArray(_message.Message):
    __slots__ = ("child",)
    CHILD_FIELD_NUMBER: _ClassVar[int]
    child: _containers.RepeatedCompositeFieldContainer[PB_ActorObj]
    def __init__(self, child: _Optional[_Iterable[_Union[PB_ActorObj, _Mapping]]] = ...) -> None: ...

class PB_ActorMob(_message.Message):
    __slots__ = ("basedata", "defid", "hp", "owner", "color", "buffs", "mods", "equips", "growage", "scale", "dieticks", "bags", "food", "bodyscale", "bonfirepos", "animwaketicks", "displayname", "climbing", "serverid", "eaten", "needeat", "maxhp", "growtime", "growdvalue", "componentData", "RideActorID", "modelcomponent", "scriptcomponent", "loctype", "mobeditcomponet", "PB_HeredityVec")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    DEFID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    MODS_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    GROWAGE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    DIETICKS_FIELD_NUMBER: _ClassVar[int]
    BAGS_FIELD_NUMBER: _ClassVar[int]
    FOOD_FIELD_NUMBER: _ClassVar[int]
    BODYSCALE_FIELD_NUMBER: _ClassVar[int]
    BONFIREPOS_FIELD_NUMBER: _ClassVar[int]
    ANIMWAKETICKS_FIELD_NUMBER: _ClassVar[int]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    CLIMBING_FIELD_NUMBER: _ClassVar[int]
    SERVERID_FIELD_NUMBER: _ClassVar[int]
    EATEN_FIELD_NUMBER: _ClassVar[int]
    NEEDEAT_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    GROWTIME_FIELD_NUMBER: _ClassVar[int]
    GROWDVALUE_FIELD_NUMBER: _ClassVar[int]
    COMPONENTDATA_FIELD_NUMBER: _ClassVar[int]
    RIDEACTORID_FIELD_NUMBER: _ClassVar[int]
    MODELCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    SCRIPTCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    LOCTYPE_FIELD_NUMBER: _ClassVar[int]
    MOBEDITCOMPONET_FIELD_NUMBER: _ClassVar[int]
    PB_HEREDITYVEC_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    defid: int
    hp: int
    owner: int
    color: int
    buffs: _containers.RepeatedCompositeFieldContainer[PB_AOIActorBuff]
    mods: _containers.RepeatedCompositeFieldContainer[PB_AttribMod]
    equips: _containers.RepeatedCompositeFieldContainer[PB_ItemIndexGrid]
    growage: int
    scale: int
    dieticks: int
    bags: _containers.RepeatedCompositeFieldContainer[PB_ItemIndexGrid]
    food: int
    bodyscale: int
    bonfirepos: PB_Vector3
    animwaketicks: int
    displayname: str
    climbing: bool
    serverid: str
    eaten: bool
    needeat: int
    maxhp: int
    growtime: int
    growdvalue: int
    componentData: str
    RideActorID: int
    modelcomponent: str
    scriptcomponent: str
    loctype: int
    mobeditcomponet: str
    PB_HeredityVec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., defid: _Optional[int] = ..., hp: _Optional[int] = ..., owner: _Optional[int] = ..., color: _Optional[int] = ..., buffs: _Optional[_Iterable[_Union[PB_AOIActorBuff, _Mapping]]] = ..., mods: _Optional[_Iterable[_Union[PB_AttribMod, _Mapping]]] = ..., equips: _Optional[_Iterable[_Union[PB_ItemIndexGrid, _Mapping]]] = ..., growage: _Optional[int] = ..., scale: _Optional[int] = ..., dieticks: _Optional[int] = ..., bags: _Optional[_Iterable[_Union[PB_ItemIndexGrid, _Mapping]]] = ..., food: _Optional[int] = ..., bodyscale: _Optional[int] = ..., bonfirepos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., animwaketicks: _Optional[int] = ..., displayname: _Optional[str] = ..., climbing: _Optional[bool] = ..., serverid: _Optional[str] = ..., eaten: _Optional[bool] = ..., needeat: _Optional[int] = ..., maxhp: _Optional[int] = ..., growtime: _Optional[int] = ..., growdvalue: _Optional[int] = ..., componentData: _Optional[str] = ..., RideActorID: _Optional[int] = ..., modelcomponent: _Optional[str] = ..., scriptcomponent: _Optional[str] = ..., loctype: _Optional[int] = ..., mobeditcomponet: _Optional[str] = ..., PB_HeredityVec: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_ActorAquaticMob(_message.Message):
    __slots__ = ("mobdata", "droughtTolerance", "moveTarget")
    MOBDATA_FIELD_NUMBER: _ClassVar[int]
    DROUGHTTOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MOVETARGET_FIELD_NUMBER: _ClassVar[int]
    mobdata: PB_ActorMob
    droughtTolerance: int
    moveTarget: PB_Vector3
    def __init__(self, mobdata: _Optional[_Union[PB_ActorMob, _Mapping]] = ..., droughtTolerance: _Optional[int] = ..., moveTarget: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorBlockAwaken(_message.Message):
    __slots__ = ("mobdata", "blockId", "blockData", "sourceBlockPos", "isMultiBlock", "multiBlockDir")
    MOBDATA_FIELD_NUMBER: _ClassVar[int]
    BLOCKID_FIELD_NUMBER: _ClassVar[int]
    BLOCKDATA_FIELD_NUMBER: _ClassVar[int]
    SOURCEBLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    ISMULTIBLOCK_FIELD_NUMBER: _ClassVar[int]
    MULTIBLOCKDIR_FIELD_NUMBER: _ClassVar[int]
    mobdata: PB_ActorMob
    blockId: int
    blockData: int
    sourceBlockPos: PB_Vector3
    isMultiBlock: bool
    multiBlockDir: int
    def __init__(self, mobdata: _Optional[_Union[PB_ActorMob, _Mapping]] = ..., blockId: _Optional[int] = ..., blockData: _Optional[int] = ..., sourceBlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., isMultiBlock: _Optional[bool] = ..., multiBlockDir: _Optional[int] = ...) -> None: ...

class PB_ActorGeneral(_message.Message):
    __slots__ = ("MapId", "InfoLen", "ActorDetail", "actorType")
    MAPID_FIELD_NUMBER: _ClassVar[int]
    INFOLEN_FIELD_NUMBER: _ClassVar[int]
    ACTORDETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTORTYPE_FIELD_NUMBER: _ClassVar[int]
    MapId: int
    InfoLen: int
    ActorDetail: str
    actorType: str
    def __init__(self, MapId: _Optional[int] = ..., InfoLen: _Optional[int] = ..., ActorDetail: _Optional[str] = ..., actorType: _Optional[str] = ...) -> None: ...

class PB_ActorInfo(_message.Message):
    __slots__ = ("ActorGeneral", "RoleInfo")
    ACTORGENERAL_FIELD_NUMBER: _ClassVar[int]
    ROLEINFO_FIELD_NUMBER: _ClassVar[int]
    ActorGeneral: PB_ActorGeneral
    RoleInfo: PB_ActorRoleInfo
    def __init__(self, ActorGeneral: _Optional[_Union[PB_ActorGeneral, _Mapping]] = ..., RoleInfo: _Optional[_Union[PB_ActorRoleInfo, _Mapping]] = ...) -> None: ...

class PB_MechaBlockData(_message.Message):
    __slots__ = ("pos", "block", "blockStateIndex")
    POS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCKSTATEINDEX_FIELD_NUMBER: _ClassVar[int]
    pos: int
    block: int
    blockStateIndex: int
    def __init__(self, pos: _Optional[int] = ..., block: _Optional[int] = ..., blockStateIndex: _Optional[int] = ...) -> None: ...

class PB_BlockStructData(_message.Message):
    __slots__ = ("leftbottompos", "righttoppos", "boxsize", "ContainerBuf", "ContainerBufUnzipLen", "blockdata", "mechaBlockId", "dir", "meshoffset", "meshlength", "recoveryhead")
    LEFTBOTTOMPOS_FIELD_NUMBER: _ClassVar[int]
    RIGHTTOPPOS_FIELD_NUMBER: _ClassVar[int]
    BOXSIZE_FIELD_NUMBER: _ClassVar[int]
    CONTAINERBUF_FIELD_NUMBER: _ClassVar[int]
    CONTAINERBUFUNZIPLEN_FIELD_NUMBER: _ClassVar[int]
    BLOCKDATA_FIELD_NUMBER: _ClassVar[int]
    MECHABLOCKID_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    MESHOFFSET_FIELD_NUMBER: _ClassVar[int]
    MESHLENGTH_FIELD_NUMBER: _ClassVar[int]
    RECOVERYHEAD_FIELD_NUMBER: _ClassVar[int]
    leftbottompos: PB_Vector3
    righttoppos: PB_Vector3
    boxsize: PB_Vector3
    ContainerBuf: str
    ContainerBufUnzipLen: int
    blockdata: _containers.RepeatedCompositeFieldContainer[PB_MechaBlockData]
    mechaBlockId: int
    dir: int
    meshoffset: PB_Vector3
    meshlength: PB_Vector3
    recoveryhead: PB_Vector3
    def __init__(self, leftbottompos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., righttoppos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., boxsize: _Optional[_Union[PB_Vector3, _Mapping]] = ..., ContainerBuf: _Optional[str] = ..., ContainerBufUnzipLen: _Optional[int] = ..., blockdata: _Optional[_Iterable[_Union[PB_MechaBlockData, _Mapping]]] = ..., mechaBlockId: _Optional[int] = ..., dir: _Optional[int] = ..., meshoffset: _Optional[_Union[PB_Vector3, _Mapping]] = ..., meshlength: _Optional[_Union[PB_Vector3, _Mapping]] = ..., recoveryhead: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorBlockStruct(_message.Message):
    __slots__ = ("basedata", "blockstructdata")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    BLOCKSTRUCTDATA_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorCommon
    blockstructdata: PB_BlockStructData
    def __init__(self, basedata: _Optional[_Union[PB_ActorCommon, _Mapping]] = ..., blockstructdata: _Optional[_Union[PB_BlockStructData, _Mapping]] = ...) -> None: ...

class PB_ActorBlockStructWormTab(_message.Message):
    __slots__ = ("basedata", "shaftDir", "moveDir", "offsetForPush")
    BASEDATA_FIELD_NUMBER: _ClassVar[int]
    SHAFTDIR_FIELD_NUMBER: _ClassVar[int]
    MOVEDIR_FIELD_NUMBER: _ClassVar[int]
    OFFSETFORPUSH_FIELD_NUMBER: _ClassVar[int]
    basedata: PB_ActorBlockStruct
    shaftDir: int
    moveDir: int
    offsetForPush: PB_Vector3
    def __init__(self, basedata: _Optional[_Union[PB_ActorBlockStruct, _Mapping]] = ..., shaftDir: _Optional[int] = ..., moveDir: _Optional[int] = ..., offsetForPush: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_MoveMotion(_message.Message):
    __slots__ = ("Position", "Yaw", "Pitch", "MapID", "ChangeFlags")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    CHANGEFLAGS_FIELD_NUMBER: _ClassVar[int]
    Position: PB_Vector3
    Yaw: int
    Pitch: int
    MapID: int
    ChangeFlags: int
    def __init__(self, Position: _Optional[_Union[PB_Vector3, _Mapping]] = ..., Yaw: _Optional[int] = ..., Pitch: _Optional[int] = ..., MapID: _Optional[int] = ..., ChangeFlags: _Optional[int] = ...) -> None: ...

class PB_ItemData(_message.Message):
    __slots__ = ("Index", "ItemID", "Durable", "Num", "UserData", "Enchs", "UserDataStr", "Runes", "grideffects", "Toughness", "datacomponents", "iteminsid", "lock")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    ENCHS_FIELD_NUMBER: _ClassVar[int]
    USERDATASTR_FIELD_NUMBER: _ClassVar[int]
    RUNES_FIELD_NUMBER: _ClassVar[int]
    GRIDEFFECTS_FIELD_NUMBER: _ClassVar[int]
    TOUGHNESS_FIELD_NUMBER: _ClassVar[int]
    DATACOMPONENTS_FIELD_NUMBER: _ClassVar[int]
    ITEMINSID_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    Index: int
    ItemID: int
    Durable: int
    Num: int
    UserData: int
    Enchs: _containers.RepeatedScalarFieldContainer[int]
    UserDataStr: str
    Runes: _containers.RepeatedCompositeFieldContainer[PB_ItemRune]
    grideffects: _containers.RepeatedCompositeFieldContainer[PB_ItemGridEffects]
    Toughness: int
    datacomponents: _containers.RepeatedCompositeFieldContainer[PB_ItemDataComponent]
    iteminsid: int
    lock: bool
    def __init__(self, Index: _Optional[int] = ..., ItemID: _Optional[int] = ..., Durable: _Optional[int] = ..., Num: _Optional[int] = ..., UserData: _Optional[int] = ..., Enchs: _Optional[_Iterable[int]] = ..., UserDataStr: _Optional[str] = ..., Runes: _Optional[_Iterable[_Union[PB_ItemRune, _Mapping]]] = ..., grideffects: _Optional[_Iterable[_Union[PB_ItemGridEffects, _Mapping]]] = ..., Toughness: _Optional[int] = ..., datacomponents: _Optional[_Iterable[_Union[PB_ItemDataComponent, _Mapping]]] = ..., iteminsid: _Optional[int] = ..., lock: _Optional[bool] = ...) -> None: ...

class PB_PlayerBriefInfo(_message.Message):
    __slots__ = ("Uin", "MapID", "HP", "NickName", "PlayerIndex", "TeamID", "CGVars", "InSpectator", "Pos", "VipInfo", "CustomJson", "SkinID", "FrameID", "CustomModel", "AcctountSkinID", "Strength", "MaxHP", "OverflowHP", "MaxStrength", "OverflowStrength", "Armor", "Perseverance", "exposePosToOther", "IronHp", "isAIPlayer", "JoinFromSrc")
    UIN_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    CGVARS_FIELD_NUMBER: _ClassVar[int]
    INSPECTATOR_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    VIPINFO_FIELD_NUMBER: _ClassVar[int]
    CUSTOMJSON_FIELD_NUMBER: _ClassVar[int]
    SKINID_FIELD_NUMBER: _ClassVar[int]
    FRAMEID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMODEL_FIELD_NUMBER: _ClassVar[int]
    ACCTOUNTSKINID_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    MAXHP_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWHP_FIELD_NUMBER: _ClassVar[int]
    MAXSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    OVERFLOWSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    PERSEVERANCE_FIELD_NUMBER: _ClassVar[int]
    EXPOSEPOSTOOTHER_FIELD_NUMBER: _ClassVar[int]
    IRONHP_FIELD_NUMBER: _ClassVar[int]
    ISAIPLAYER_FIELD_NUMBER: _ClassVar[int]
    JOINFROMSRC_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    MapID: int
    HP: float
    NickName: str
    PlayerIndex: int
    TeamID: int
    CGVars: _containers.RepeatedScalarFieldContainer[int]
    InSpectator: int
    Pos: PB_Vector3
    VipInfo: PB_PlayerVipInfo
    CustomJson: str
    SkinID: int
    FrameID: int
    CustomModel: str
    AcctountSkinID: int
    Strength: float
    MaxHP: float
    OverflowHP: float
    MaxStrength: float
    OverflowStrength: float
    Armor: float
    Perseverance: float
    exposePosToOther: float
    IronHp: float
    isAIPlayer: bool
    JoinFromSrc: str
    def __init__(self, Uin: _Optional[int] = ..., MapID: _Optional[int] = ..., HP: _Optional[float] = ..., NickName: _Optional[str] = ..., PlayerIndex: _Optional[int] = ..., TeamID: _Optional[int] = ..., CGVars: _Optional[_Iterable[int]] = ..., InSpectator: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., VipInfo: _Optional[_Union[PB_PlayerVipInfo, _Mapping]] = ..., CustomJson: _Optional[str] = ..., SkinID: _Optional[int] = ..., FrameID: _Optional[int] = ..., CustomModel: _Optional[str] = ..., AcctountSkinID: _Optional[int] = ..., Strength: _Optional[float] = ..., MaxHP: _Optional[float] = ..., OverflowHP: _Optional[float] = ..., MaxStrength: _Optional[float] = ..., OverflowStrength: _Optional[float] = ..., Armor: _Optional[float] = ..., Perseverance: _Optional[float] = ..., exposePosToOther: _Optional[float] = ..., IronHp: _Optional[float] = ..., isAIPlayer: _Optional[bool] = ..., JoinFromSrc: _Optional[str] = ...) -> None: ...

class PB_EffectParticle(_message.Message):
    __slots__ = ("Name", "Age", "Color", "Yaw", "Pitch", "Pos", "ziprespath", "isPersistent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ZIPRESPATH_FIELD_NUMBER: _ClassVar[int]
    ISPERSISTENT_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Age: int
    Color: int
    Yaw: int
    Pitch: int
    Pos: PB_Vector3
    ziprespath: str
    isPersistent: bool
    def __init__(self, Name: _Optional[str] = ..., Age: _Optional[int] = ..., Color: _Optional[int] = ..., Yaw: _Optional[int] = ..., Pitch: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., ziprespath: _Optional[str] = ..., isPersistent: _Optional[bool] = ...) -> None: ...

class PB_EffectParticle_V2(_message.Message):
    __slots__ = ("Id", "Name", "Age", "Color", "YawPitch", "Pos", "ZipResPath", "IsPersistent", "Scale", "Rotation", "Offset", "VisibleDist")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    YAWPITCH_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ZIPRESPATH_FIELD_NUMBER: _ClassVar[int]
    ISPERSISTENT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    VISIBLEDIST_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    Age: int
    Color: int
    YawPitch: int
    Pos: _containers.RepeatedScalarFieldContainer[int]
    ZipResPath: str
    IsPersistent: bool
    Scale: _containers.RepeatedScalarFieldContainer[int]
    Rotation: _containers.RepeatedScalarFieldContainer[int]
    Offset: _containers.RepeatedScalarFieldContainer[int]
    VisibleDist: int
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., Age: _Optional[int] = ..., Color: _Optional[int] = ..., YawPitch: _Optional[int] = ..., Pos: _Optional[_Iterable[int]] = ..., ZipResPath: _Optional[str] = ..., IsPersistent: _Optional[bool] = ..., Scale: _Optional[_Iterable[int]] = ..., Rotation: _Optional[_Iterable[int]] = ..., Offset: _Optional[_Iterable[int]] = ..., VisibleDist: _Optional[int] = ...) -> None: ...

class PB_EffectParticleID(_message.Message):
    __slots__ = ("id", "Age", "Color", "Yaw", "Pitch", "Pos", "ziprespath")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ZIPRESPATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    Age: int
    Color: int
    Yaw: int
    Pitch: int
    Pos: PB_Vector3
    ziprespath: str
    def __init__(self, id: _Optional[int] = ..., Age: _Optional[int] = ..., Color: _Optional[int] = ..., Yaw: _Optional[int] = ..., Pitch: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., ziprespath: _Optional[str] = ...) -> None: ...

class PB_EffectParticleID_V2(_message.Message):
    __slots__ = ("id", "Age", "Color", "Yaw_Pitch", "Pos", "ziprespath")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    YAW_PITCH_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ZIPRESPATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    Age: int
    Color: int
    Yaw_Pitch: int
    Pos: _containers.RepeatedScalarFieldContainer[int]
    ziprespath: str
    def __init__(self, id: _Optional[int] = ..., Age: _Optional[int] = ..., Color: _Optional[int] = ..., Yaw_Pitch: _Optional[int] = ..., Pos: _Optional[_Iterable[int]] = ..., ziprespath: _Optional[str] = ...) -> None: ...

class PB_EffectPickItem(_message.Message):
    __slots__ = ("PickerObj", "ItemObj", "YOffset", "destPos")
    PICKEROBJ_FIELD_NUMBER: _ClassVar[int]
    ITEMOBJ_FIELD_NUMBER: _ClassVar[int]
    YOFFSET_FIELD_NUMBER: _ClassVar[int]
    DESTPOS_FIELD_NUMBER: _ClassVar[int]
    PickerObj: int
    ItemObj: int
    YOffset: int
    destPos: PB_Vector3
    def __init__(self, PickerObj: _Optional[int] = ..., ItemObj: _Optional[int] = ..., YOffset: _Optional[int] = ..., destPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_EffectSound(_message.Message):
    __slots__ = ("Name", "Volume", "Pitch", "Flags", "Segment", "Pos", "fixpitch")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    FIXPITCH_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Volume: float
    Pitch: float
    Flags: int
    Segment: int
    Pos: PB_Vector3
    fixpitch: bool
    def __init__(self, Name: _Optional[str] = ..., Volume: _Optional[float] = ..., Pitch: _Optional[float] = ..., Flags: _Optional[int] = ..., Segment: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., fixpitch: _Optional[bool] = ...) -> None: ...

class PB_EffectSound_V2(_message.Message):
    __slots__ = ("Name", "Effnd")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EFFND_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Effnd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Name: _Optional[str] = ..., Effnd: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_EffectSoundID(_message.Message):
    __slots__ = ("id", "Volume", "Pitch", "Flags", "Segment", "Pos", "fixpitch")
    ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    FIXPITCH_FIELD_NUMBER: _ClassVar[int]
    id: int
    Volume: int
    Pitch: int
    Flags: int
    Segment: int
    Pos: PB_Vector3
    fixpitch: bool
    def __init__(self, id: _Optional[int] = ..., Volume: _Optional[int] = ..., Pitch: _Optional[int] = ..., Flags: _Optional[int] = ..., Segment: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., fixpitch: _Optional[bool] = ...) -> None: ...

class PB_EffectSoundID_V2(_message.Message):
    __slots__ = ("Effd",)
    EFFD_FIELD_NUMBER: _ClassVar[int]
    Effd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Effd: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_EffectTriggerSound(_message.Message):
    __slots__ = ("Name", "Volume", "Pitch", "IsLoop", "PlayState", "ObjId", "Pos", "position", "dist")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    PLAYSTATE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DIST_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Volume: float
    Pitch: float
    IsLoop: bool
    PlayState: int
    ObjId: int
    Pos: PB_Vector3
    position: int
    dist: int
    def __init__(self, Name: _Optional[str] = ..., Volume: _Optional[float] = ..., Pitch: _Optional[float] = ..., IsLoop: _Optional[bool] = ..., PlayState: _Optional[int] = ..., ObjId: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., position: _Optional[int] = ..., dist: _Optional[int] = ...) -> None: ...

class PB_EffectTriggerSound_V2(_message.Message):
    __slots__ = ("Name", "ObjId", "Effd")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EFFD_FIELD_NUMBER: _ClassVar[int]
    Name: str
    ObjId: int
    Effd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Name: _Optional[str] = ..., ObjId: _Optional[int] = ..., Effd: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_AOIEffectTriggerSound(_message.Message):
    __slots__ = ("Name", "Volume", "Pitch", "IsLoop", "PlayState", "ObjId", "Pos", "position")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    PLAYSTATE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Volume: int
    Pitch: int
    IsLoop: bool
    PlayState: int
    ObjId: int
    Pos: PB_Vector3
    position: int
    def __init__(self, Name: _Optional[str] = ..., Volume: _Optional[int] = ..., Pitch: _Optional[int] = ..., IsLoop: _Optional[bool] = ..., PlayState: _Optional[int] = ..., ObjId: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., position: _Optional[int] = ...) -> None: ...

class PB_EffectActorBody(_message.Message):
    __slots__ = ("ObjId", "BodyEffect", "Status")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    BODYEFFECT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    BodyEffect: int
    Status: int
    def __init__(self, ObjId: _Optional[int] = ..., BodyEffect: _Optional[int] = ..., Status: _Optional[int] = ...) -> None: ...

class PB_EffectStringActorBody(_message.Message):
    __slots__ = ("ObjId", "EffectName", "Status", "loopPlayTime")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EFFECTNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOOPPLAYTIME_FIELD_NUMBER: _ClassVar[int]
    ObjId: int
    EffectName: str
    Status: int
    loopPlayTime: float
    def __init__(self, ObjId: _Optional[int] = ..., EffectName: _Optional[str] = ..., Status: _Optional[int] = ..., loopPlayTime: _Optional[float] = ...) -> None: ...

class PB_EffectDestroyBlock(_message.Message):
    __slots__ = ("Face", "SubType", "Age", "Pos", "ID")
    FACE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Face: int
    SubType: int
    Age: int
    Pos: PB_Vector3
    ID: int
    def __init__(self, Face: _Optional[int] = ..., SubType: _Optional[int] = ..., Age: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., ID: _Optional[int] = ...) -> None: ...

class PB_EffectDestroyBlock_V2(_message.Message):
    __slots__ = ("Effd",)
    EFFD_FIELD_NUMBER: _ClassVar[int]
    Effd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Effd: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_EffectCrackBlock(_message.Message):
    __slots__ = ("Stage", "ActorId", "BlockPos")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    Stage: int
    ActorId: int
    BlockPos: PB_Vector3
    def __init__(self, Stage: _Optional[int] = ..., ActorId: _Optional[int] = ..., BlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_EffectVehicle(_message.Message):
    __slots__ = ("Name", "ActorId", "BlockPos", "Age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    ActorId: int
    BlockPos: PB_Vector3
    Age: int
    def __init__(self, Name: _Optional[str] = ..., ActorId: _Optional[int] = ..., BlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., Age: _Optional[int] = ...) -> None: ...

class PB_EffectPlayMusicGrid(_message.Message):
    __slots__ = ("Name", "Pitch", "Flags", "Segment", "BlockPos")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Pitch: float
    Flags: int
    Segment: int
    BlockPos: PB_Vector3
    def __init__(self, Name: _Optional[str] = ..., Pitch: _Optional[float] = ..., Flags: _Optional[int] = ..., Segment: _Optional[int] = ..., BlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_EffectPlayMusicGrid_V2(_message.Message):
    __slots__ = ("Name", "Effd")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EFFD_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Effd: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Name: _Optional[str] = ..., Effd: _Optional[_Iterable[int]] = ...) -> None: ...

class PB_EffectStopMusicGrid(_message.Message):
    __slots__ = ("BlockPos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    BlockPos: PB_Vector3
    def __init__(self, BlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_IntertactData(_message.Message):
    __slots__ = ("Type", "ID", "Show")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ID: int
    Show: int
    def __init__(self, Type: _Optional[int] = ..., ID: _Optional[int] = ..., Show: _Optional[int] = ...) -> None: ...

class PB_TaskContentData(_message.Message):
    __slots__ = ("Type", "ID", "Num", "CompletedNum")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    COMPLETEDNUM_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ID: int
    Num: int
    CompletedNum: int
    def __init__(self, Type: _Optional[int] = ..., ID: _Optional[int] = ..., Num: _Optional[int] = ..., CompletedNum: _Optional[int] = ...) -> None: ...

class PB_TaskInfoData(_message.Message):
    __slots__ = ("ID", "State", "PlotID", "Contents")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PLOTID_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    State: int
    PlotID: int
    Contents: _containers.RepeatedCompositeFieldContainer[PB_TaskContentData]
    def __init__(self, ID: _Optional[int] = ..., State: _Optional[int] = ..., PlotID: _Optional[int] = ..., Contents: _Optional[_Iterable[_Union[PB_TaskContentData, _Mapping]]] = ...) -> None: ...

class PB_PreBlockData(_message.Message):
    __slots__ = ("ID", "BlockPos", "SpecialBlockColor", "EXID")
    ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    SPECIALBLOCKCOLOR_FIELD_NUMBER: _ClassVar[int]
    EXID_FIELD_NUMBER: _ClassVar[int]
    ID: int
    BlockPos: PB_Vector3
    SpecialBlockColor: int
    EXID: int
    def __init__(self, ID: _Optional[int] = ..., BlockPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., SpecialBlockColor: _Optional[int] = ..., EXID: _Optional[int] = ...) -> None: ...

class PB_CustomModelClassData(_message.Message):
    __slots__ = ("ClassName", "ModelNames", "folderindex")
    CLASSNAME_FIELD_NUMBER: _ClassVar[int]
    MODELNAMES_FIELD_NUMBER: _ClassVar[int]
    FOLDERINDEX_FIELD_NUMBER: _ClassVar[int]
    ClassName: str
    ModelNames: _containers.RepeatedScalarFieldContainer[str]
    folderindex: int
    def __init__(self, ClassName: _Optional[str] = ..., ModelNames: _Optional[_Iterable[str]] = ..., folderindex: _Optional[int] = ...) -> None: ...

class PB_MobDisplayData(_message.Message):
    __slots__ = ("mobId", "itemId", "itemCount", "animId")
    MOBID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMCOUNT_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    mobId: int
    itemId: int
    itemCount: int
    animId: int
    def __init__(self, mobId: _Optional[int] = ..., itemId: _Optional[int] = ..., itemCount: _Optional[int] = ..., animId: _Optional[int] = ...) -> None: ...

class PB_NpcShopItemData(_message.Message):
    __slots__ = ("SkuID", "ItemID", "OnceBuyNum", "MaxCanBuyCount", "RefreshDuration", "StarNum", "CostItemInfo1", "CostItemInfo2", "LeftCount", "EndTime", "iShowAD")
    SKUID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ONCEBUYNUM_FIELD_NUMBER: _ClassVar[int]
    MAXCANBUYCOUNT_FIELD_NUMBER: _ClassVar[int]
    REFRESHDURATION_FIELD_NUMBER: _ClassVar[int]
    STARNUM_FIELD_NUMBER: _ClassVar[int]
    COSTITEMINFO1_FIELD_NUMBER: _ClassVar[int]
    COSTITEMINFO2_FIELD_NUMBER: _ClassVar[int]
    LEFTCOUNT_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    ISHOWAD_FIELD_NUMBER: _ClassVar[int]
    SkuID: int
    ItemID: int
    OnceBuyNum: int
    MaxCanBuyCount: int
    RefreshDuration: int
    StarNum: int
    CostItemInfo1: int
    CostItemInfo2: int
    LeftCount: int
    EndTime: int
    iShowAD: int
    def __init__(self, SkuID: _Optional[int] = ..., ItemID: _Optional[int] = ..., OnceBuyNum: _Optional[int] = ..., MaxCanBuyCount: _Optional[int] = ..., RefreshDuration: _Optional[int] = ..., StarNum: _Optional[int] = ..., CostItemInfo1: _Optional[int] = ..., CostItemInfo2: _Optional[int] = ..., LeftCount: _Optional[int] = ..., EndTime: _Optional[int] = ..., iShowAD: _Optional[int] = ...) -> None: ...

class PB_NpcShopData(_message.Message):
    __slots__ = ("ShopID", "ShopName", "ShopDesc", "InnerKey", "ShopItemData")
    SHOPID_FIELD_NUMBER: _ClassVar[int]
    SHOPNAME_FIELD_NUMBER: _ClassVar[int]
    SHOPDESC_FIELD_NUMBER: _ClassVar[int]
    INNERKEY_FIELD_NUMBER: _ClassVar[int]
    SHOPITEMDATA_FIELD_NUMBER: _ClassVar[int]
    ShopID: int
    ShopName: str
    ShopDesc: str
    InnerKey: str
    ShopItemData: _containers.RepeatedCompositeFieldContainer[PB_NpcShopItemData]
    def __init__(self, ShopID: _Optional[int] = ..., ShopName: _Optional[str] = ..., ShopDesc: _Optional[str] = ..., InnerKey: _Optional[str] = ..., ShopItemData: _Optional[_Iterable[_Union[PB_NpcShopItemData, _Mapping]]] = ...) -> None: ...

class PB_ActorOneAvatarModelData(_message.Message):
    __slots__ = ("ModelFilename", "Scale", "Yaw", "Pitch", "OffsetPos", "Roll", "NewRotateMode", "Scale3")
    MODELFILENAME_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    OFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    NEWROTATEMODE_FIELD_NUMBER: _ClassVar[int]
    SCALE3_FIELD_NUMBER: _ClassVar[int]
    ModelFilename: str
    Scale: float
    Yaw: int
    Pitch: int
    OffsetPos: PB_Vector3
    Roll: int
    NewRotateMode: bool
    Scale3: PB_Vector3
    def __init__(self, ModelFilename: _Optional[str] = ..., Scale: _Optional[float] = ..., Yaw: _Optional[int] = ..., Pitch: _Optional[int] = ..., OffsetPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., Roll: _Optional[int] = ..., NewRotateMode: _Optional[bool] = ..., Scale3: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_ActorOneBoneModelData(_message.Message):
    __slots__ = ("BoneName", "AvatarModels")
    BONENAME_FIELD_NUMBER: _ClassVar[int]
    AVATARMODELS_FIELD_NUMBER: _ClassVar[int]
    BoneName: str
    AvatarModels: _containers.RepeatedCompositeFieldContainer[PB_ActorOneAvatarModelData]
    def __init__(self, BoneName: _Optional[str] = ..., AvatarModels: _Optional[_Iterable[_Union[PB_ActorOneAvatarModelData, _Mapping]]] = ...) -> None: ...

class PB_BasketBallOperate(_message.Message):
    __slots__ = ("Type", "ActorID", "IsSelectedTarget", "FallResult", "ExtendData", "Uin", "pos", "yaw", "SelectedActorID", "pitch")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTORID_FIELD_NUMBER: _ClassVar[int]
    ISSELECTEDTARGET_FIELD_NUMBER: _ClassVar[int]
    FALLRESULT_FIELD_NUMBER: _ClassVar[int]
    EXTENDDATA_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    SELECTEDACTORID_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ActorID: int
    IsSelectedTarget: bool
    FallResult: int
    ExtendData: int
    Uin: int
    pos: PB_Vector3
    yaw: float
    SelectedActorID: int
    pitch: float
    def __init__(self, Type: _Optional[int] = ..., ActorID: _Optional[int] = ..., IsSelectedTarget: _Optional[bool] = ..., FallResult: _Optional[int] = ..., ExtendData: _Optional[int] = ..., Uin: _Optional[int] = ..., pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., yaw: _Optional[float] = ..., SelectedActorID: _Optional[int] = ..., pitch: _Optional[float] = ...) -> None: ...

class PB_CSAuthorityData(_message.Message):
    __slots__ = ("Uin", "Type", "Flag")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Type: int
    Flag: int
    def __init__(self, Uin: _Optional[int] = ..., Type: _Optional[int] = ..., Flag: _Optional[int] = ...) -> None: ...

class PB_CSPermitData(_message.Message):
    __slots__ = ("Uin", "Type", "Flag")
    UIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    Uin: int
    Type: int
    Flag: int
    def __init__(self, Uin: _Optional[int] = ..., Type: _Optional[int] = ..., Flag: _Optional[int] = ...) -> None: ...

class PB_Edu_RoleInfo(_message.Message):
    __slots__ = ("objId", "yaw")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    objId: int
    yaw: float
    def __init__(self, objId: _Optional[int] = ..., yaw: _Optional[float] = ...) -> None: ...

class PB_ImportModelData(_message.Message):
    __slots__ = ("Key", "Name", "Desc", "Type", "AuthUin", "AuthName", "FileName")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHUIN_FIELD_NUMBER: _ClassVar[int]
    AUTHNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Name: str
    Desc: str
    Type: int
    AuthUin: int
    AuthName: str
    FileName: str
    def __init__(self, Key: _Optional[str] = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ..., Type: _Optional[int] = ..., AuthUin: _Optional[int] = ..., AuthName: _Optional[str] = ..., FileName: _Optional[str] = ...) -> None: ...

class PB_GraphicsAttr(_message.Message):
    __slots__ = ("grapicsid", "Type", "Groupid", "Title", "Apha", "CurVal", "MaxVal", "Color", "Fontsize", "WordPos", "bindObjID", "x2", "y2", "offset", "destObjID", "Translate", "AutoWrap", "nMapId", "size")
    GRAPICSID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    APHA_FIELD_NUMBER: _ClassVar[int]
    CURVAL_FIELD_NUMBER: _ClassVar[int]
    MAXVAL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    WORDPOS_FIELD_NUMBER: _ClassVar[int]
    BINDOBJID_FIELD_NUMBER: _ClassVar[int]
    X2_FIELD_NUMBER: _ClassVar[int]
    Y2_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DESTOBJID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATE_FIELD_NUMBER: _ClassVar[int]
    AUTOWRAP_FIELD_NUMBER: _ClassVar[int]
    NMAPID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    grapicsid: int
    Type: int
    Groupid: int
    Title: str
    Apha: int
    CurVal: int
    MaxVal: int
    Color: int
    Fontsize: float
    WordPos: PB_Vector3
    bindObjID: int
    x2: int
    y2: int
    offset: PB_Vector3
    destObjID: int
    Translate: str
    AutoWrap: bytes
    nMapId: int
    size: PB_Vector3
    def __init__(self, grapicsid: _Optional[int] = ..., Type: _Optional[int] = ..., Groupid: _Optional[int] = ..., Title: _Optional[str] = ..., Apha: _Optional[int] = ..., CurVal: _Optional[int] = ..., MaxVal: _Optional[int] = ..., Color: _Optional[int] = ..., Fontsize: _Optional[float] = ..., WordPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., bindObjID: _Optional[int] = ..., x2: _Optional[int] = ..., y2: _Optional[int] = ..., offset: _Optional[_Union[PB_Vector3, _Mapping]] = ..., destObjID: _Optional[int] = ..., Translate: _Optional[str] = ..., AutoWrap: _Optional[bytes] = ..., nMapId: _Optional[int] = ..., size: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_UnfinishedStarStationTransferRecord(_message.Message):
    __slots__ = ("destStarStationID", "destMapID", "srcCabinPos", "cabinStatus")
    DESTSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    DESTMAPID_FIELD_NUMBER: _ClassVar[int]
    SRCCABINPOS_FIELD_NUMBER: _ClassVar[int]
    CABINSTATUS_FIELD_NUMBER: _ClassVar[int]
    destStarStationID: int
    destMapID: int
    srcCabinPos: PB_Vector3
    cabinStatus: int
    def __init__(self, destStarStationID: _Optional[int] = ..., destMapID: _Optional[int] = ..., srcCabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., cabinStatus: _Optional[int] = ...) -> None: ...

class PB_StarStationCabinDef(_message.Message):
    __slots__ = ("cabinPos", "cabinStatus", "bindPlayerUin", "cabinLevel")
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    CABINSTATUS_FIELD_NUMBER: _ClassVar[int]
    BINDPLAYERUIN_FIELD_NUMBER: _ClassVar[int]
    CABINLEVEL_FIELD_NUMBER: _ClassVar[int]
    cabinPos: PB_Vector3
    cabinStatus: int
    bindPlayerUin: int
    cabinLevel: int
    def __init__(self, cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., cabinStatus: _Optional[int] = ..., bindPlayerUin: _Optional[int] = ..., cabinLevel: _Optional[int] = ...) -> None: ...

class PB_StarStationDef(_message.Message):
    __slots__ = ("starStationID", "starStationName", "mapID", "isConsoleActive", "consolePos", "isConsoleSign", "stationType", "stationExtraData")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONNAME_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    ISCONSOLEACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONSOLEPOS_FIELD_NUMBER: _ClassVar[int]
    ISCONSOLESIGN_FIELD_NUMBER: _ClassVar[int]
    STATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    STATIONEXTRADATA_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    starStationName: str
    mapID: int
    isConsoleActive: bool
    consolePos: PB_Vector3
    isConsoleSign: bool
    stationType: int
    stationExtraData: int
    def __init__(self, starStationID: _Optional[int] = ..., starStationName: _Optional[str] = ..., mapID: _Optional[int] = ..., isConsoleActive: _Optional[bool] = ..., consolePos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., isConsoleSign: _Optional[bool] = ..., stationType: _Optional[int] = ..., stationExtraData: _Optional[int] = ...) -> None: ...

class PB_ChangeStarStationNameStatus(_message.Message):
    __slots__ = ("starStationID", "isActive", "starStationName", "isSign")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    ISACTIVE_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONNAME_FIELD_NUMBER: _ClassVar[int]
    ISSIGN_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    isActive: bool
    starStationName: str
    isSign: bool
    def __init__(self, starStationID: _Optional[int] = ..., isActive: _Optional[bool] = ..., starStationName: _Optional[str] = ..., isSign: _Optional[bool] = ...) -> None: ...

class PB_EnterStarStationCabin(_message.Message):
    __slots__ = ("uin", "starStationID", "cabinPos", "status", "result")
    UIN_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    uin: int
    starStationID: int
    cabinPos: PB_Vector3
    status: int
    result: bool
    def __init__(self, uin: _Optional[int] = ..., starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., status: _Optional[int] = ..., result: _Optional[bool] = ...) -> None: ...

class PB_LeaveStarStationCabin(_message.Message):
    __slots__ = ("uin", "starStationID", "cabinPos", "status")
    UIN_FIELD_NUMBER: _ClassVar[int]
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    uin: int
    starStationID: int
    cabinPos: PB_Vector3
    status: int
    def __init__(self, uin: _Optional[int] = ..., starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., status: _Optional[int] = ...) -> None: ...

class PB_UpdateStarStationCabinAdded(_message.Message):
    __slots__ = ("starStationID", "cabinDef")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINDEF_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinDef: PB_StarStationCabinDef
    def __init__(self, starStationID: _Optional[int] = ..., cabinDef: _Optional[_Union[PB_StarStationCabinDef, _Mapping]] = ...) -> None: ...

class PB_UpdateStarStationCabinRemoved(_message.Message):
    __slots__ = ("starStationID", "cabinPos", "mapID")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    MAPID_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: PB_Vector3
    mapID: int
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., mapID: _Optional[int] = ...) -> None: ...

class PB_UpdateStarStationCabinStatus(_message.Message):
    __slots__ = ("starStationID", "cabinPos", "status")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: PB_Vector3
    status: int
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., status: _Optional[int] = ...) -> None: ...

class PB_addStarStationTransferDesc(_message.Message):
    __slots__ = ("srcStarStationID", "descStarStationID")
    SRCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    DESCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    srcStarStationID: int
    descStarStationID: int
    def __init__(self, srcStarStationID: _Optional[int] = ..., descStarStationID: _Optional[int] = ...) -> None: ...

class PB_AddStarStationDef(_message.Message):
    __slots__ = ("starStationDef",)
    STARSTATIONDEF_FIELD_NUMBER: _ClassVar[int]
    starStationDef: PB_StarStationDef
    def __init__(self, starStationDef: _Optional[_Union[PB_StarStationDef, _Mapping]] = ...) -> None: ...

class PB_DelStarStationDef(_message.Message):
    __slots__ = ("srcStarStationID", "cabinPos")
    SRCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    srcStarStationID: int
    cabinPos: PB_Vector3
    def __init__(self, srcStarStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_AddUnfinishedTransferRecord(_message.Message):
    __slots__ = ("srcStarStationID", "unfinishedTransferRecord")
    SRCSTARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    UNFINISHEDTRANSFERRECORD_FIELD_NUMBER: _ClassVar[int]
    srcStarStationID: int
    unfinishedTransferRecord: PB_UnfinishedStarStationTransferRecord
    def __init__(self, srcStarStationID: _Optional[int] = ..., unfinishedTransferRecord: _Optional[_Union[PB_UnfinishedStarStationTransferRecord, _Mapping]] = ...) -> None: ...

class PB_UpdateUnfinishedTransferRecordStatus(_message.Message):
    __slots__ = ("starStationID", "cabinPos", "status")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: PB_Vector3
    status: int
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., status: _Optional[int] = ...) -> None: ...

class PB_RemoveUnfinishedTransferRecord(_message.Message):
    __slots__ = ("starStationID", "cabinPos")
    STARSTATIONID_FIELD_NUMBER: _ClassVar[int]
    CABINPOS_FIELD_NUMBER: _ClassVar[int]
    starStationID: int
    cabinPos: PB_Vector3
    def __init__(self, starStationID: _Optional[int] = ..., cabinPos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_AchievementInfo(_message.Message):
    __slots__ = ("playerID", "achievementID", "achievementState", "rewardState", "arryNum", "completeYear", "completeMonth", "completeDay")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENTID_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENTSTATE_FIELD_NUMBER: _ClassVar[int]
    REWARDSTATE_FIELD_NUMBER: _ClassVar[int]
    ARRYNUM_FIELD_NUMBER: _ClassVar[int]
    COMPLETEYEAR_FIELD_NUMBER: _ClassVar[int]
    COMPLETEMONTH_FIELD_NUMBER: _ClassVar[int]
    COMPLETEDAY_FIELD_NUMBER: _ClassVar[int]
    playerID: int
    achievementID: int
    achievementState: int
    rewardState: int
    arryNum: int
    completeYear: int
    completeMonth: int
    completeDay: int
    def __init__(self, playerID: _Optional[int] = ..., achievementID: _Optional[int] = ..., achievementState: _Optional[int] = ..., rewardState: _Optional[int] = ..., arryNum: _Optional[int] = ..., completeYear: _Optional[int] = ..., completeMonth: _Optional[int] = ..., completeDay: _Optional[int] = ...) -> None: ...

class PB_EffectSoundNew(_message.Message):
    __slots__ = ("Name", "Volume", "Pitch", "SoundType", "Pos", "ObjId", "StartTime", "Duration", "SoundPos", "TrackId", "InstrumentCode", "Url", "WorldId", "ExtraStr", "IsLoop", "NoteCode", "TpqCount")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    SOUNDTYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SOUNDPOS_FIELD_NUMBER: _ClassVar[int]
    TRACKID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTCODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    EXTRASTR_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    NOTECODE_FIELD_NUMBER: _ClassVar[int]
    TPQCOUNT_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Volume: float
    Pitch: float
    SoundType: int
    Pos: PB_Vector3
    ObjId: int
    StartTime: int
    Duration: int
    SoundPos: int
    TrackId: int
    InstrumentCode: int
    Url: str
    WorldId: int
    ExtraStr: str
    IsLoop: bool
    NoteCode: int
    TpqCount: int
    def __init__(self, Name: _Optional[str] = ..., Volume: _Optional[float] = ..., Pitch: _Optional[float] = ..., SoundType: _Optional[int] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., ObjId: _Optional[int] = ..., StartTime: _Optional[int] = ..., Duration: _Optional[int] = ..., SoundPos: _Optional[int] = ..., TrackId: _Optional[int] = ..., InstrumentCode: _Optional[int] = ..., Url: _Optional[str] = ..., WorldId: _Optional[int] = ..., ExtraStr: _Optional[str] = ..., IsLoop: _Optional[bool] = ..., NoteCode: _Optional[int] = ..., TpqCount: _Optional[int] = ...) -> None: ...

class PB_EffectSoundNew_V2(_message.Message):
    __slots__ = ("Name", "Volume", "Pitch", "SoundType", "Pos", "ObjId", "StartTime", "Duration", "SoundPos", "TrackId", "InstrumentCode", "Url", "WorldId", "ExtraStr", "IsLoop", "NoteCode", "TpqCount")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    SOUNDTYPE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SOUNDPOS_FIELD_NUMBER: _ClassVar[int]
    TRACKID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTCODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    EXTRASTR_FIELD_NUMBER: _ClassVar[int]
    ISLOOP_FIELD_NUMBER: _ClassVar[int]
    NOTECODE_FIELD_NUMBER: _ClassVar[int]
    TPQCOUNT_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Volume: float
    Pitch: float
    SoundType: int
    Pos: _containers.RepeatedScalarFieldContainer[int]
    ObjId: int
    StartTime: int
    Duration: int
    SoundPos: int
    TrackId: int
    InstrumentCode: int
    Url: str
    WorldId: int
    ExtraStr: str
    IsLoop: bool
    NoteCode: int
    TpqCount: int
    def __init__(self, Name: _Optional[str] = ..., Volume: _Optional[float] = ..., Pitch: _Optional[float] = ..., SoundType: _Optional[int] = ..., Pos: _Optional[_Iterable[int]] = ..., ObjId: _Optional[int] = ..., StartTime: _Optional[int] = ..., Duration: _Optional[int] = ..., SoundPos: _Optional[int] = ..., TrackId: _Optional[int] = ..., InstrumentCode: _Optional[int] = ..., Url: _Optional[str] = ..., WorldId: _Optional[int] = ..., ExtraStr: _Optional[str] = ..., IsLoop: _Optional[bool] = ..., NoteCode: _Optional[int] = ..., TpqCount: _Optional[int] = ...) -> None: ...

class PB_TeamScore(_message.Message):
    __slots__ = ("teamID", "score", "flags")
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    teamID: int
    score: int
    flags: int
    def __init__(self, teamID: _Optional[int] = ..., score: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class PB_ActorSnowHare(_message.Message):
    __slots__ = ("mobdata", "FurColor")
    MOBDATA_FIELD_NUMBER: _ClassVar[int]
    FURCOLOR_FIELD_NUMBER: _ClassVar[int]
    mobdata: PB_ActorMob
    FurColor: int
    def __init__(self, mobdata: _Optional[_Union[PB_ActorMob, _Mapping]] = ..., FurColor: _Optional[int] = ...) -> None: ...

class PB_EffectShader(_message.Message):
    __slots__ = ("Name", "Radius", "Duration", "Pos", "EffectType", "Yaw", "Width", "Height", "InnerRadius", "Angle")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    EFFECTTYPE_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INNERRADIUS_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Radius: float
    Duration: float
    Pos: PB_Vector3
    EffectType: int
    Yaw: float
    Width: float
    Height: float
    InnerRadius: float
    Angle: float
    def __init__(self, Name: _Optional[str] = ..., Radius: _Optional[float] = ..., Duration: _Optional[float] = ..., Pos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., EffectType: _Optional[int] = ..., Yaw: _Optional[float] = ..., Width: _Optional[float] = ..., Height: _Optional[float] = ..., InnerRadius: _Optional[float] = ..., Angle: _Optional[float] = ...) -> None: ...

class PB_SkillExpandCDData_SkillInfo(_message.Message):
    __slots__ = ("cd", "maxCd", "cdDisplay", "button")
    CD_FIELD_NUMBER: _ClassVar[int]
    MAXCD_FIELD_NUMBER: _ClassVar[int]
    CDDISPLAY_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    cd: float
    maxCd: float
    cdDisplay: int
    button: str
    def __init__(self, cd: _Optional[float] = ..., maxCd: _Optional[float] = ..., cdDisplay: _Optional[int] = ..., button: _Optional[str] = ...) -> None: ...

class PB_SkillExpandCDData_Skill(_message.Message):
    __slots__ = ("name", "info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    info: PB_SkillExpandCDData_SkillInfo
    def __init__(self, name: _Optional[str] = ..., info: _Optional[_Union[PB_SkillExpandCDData_SkillInfo, _Mapping]] = ...) -> None: ...

class PB_SkillExpandCDData(_message.Message):
    __slots__ = ("ItemID", "skillData")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    SKILLDATA_FIELD_NUMBER: _ClassVar[int]
    ItemID: int
    skillData: _containers.RepeatedCompositeFieldContainer[PB_SkillExpandCDData_Skill]
    def __init__(self, ItemID: _Optional[int] = ..., skillData: _Optional[_Iterable[_Union[PB_SkillExpandCDData_Skill, _Mapping]]] = ...) -> None: ...

class PB_SkillExpandCDDataGather(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[PB_SkillExpandCDData]
    def __init__(self, data: _Optional[_Iterable[_Union[PB_SkillExpandCDData, _Mapping]]] = ...) -> None: ...

class PB_Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarryCompData(_message.Message):
    __slots__ = ("carryingActorID", "carriedActorID", "carryType", "AnimA", "AnimB", "offset", "rote", "playspeed", "playmodel", "anchorId")
    CARRYINGACTORID_FIELD_NUMBER: _ClassVar[int]
    CARRIEDACTORID_FIELD_NUMBER: _ClassVar[int]
    CARRYTYPE_FIELD_NUMBER: _ClassVar[int]
    ANIMA_FIELD_NUMBER: _ClassVar[int]
    ANIMB_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROTE_FIELD_NUMBER: _ClassVar[int]
    PLAYSPEED_FIELD_NUMBER: _ClassVar[int]
    PLAYMODEL_FIELD_NUMBER: _ClassVar[int]
    ANCHORID_FIELD_NUMBER: _ClassVar[int]
    carryingActorID: int
    carriedActorID: int
    carryType: int
    AnimA: int
    AnimB: int
    offset: PB_Vector3f
    rote: PB_Vector3f
    playspeed: int
    playmodel: int
    anchorId: int
    def __init__(self, carryingActorID: _Optional[int] = ..., carriedActorID: _Optional[int] = ..., carryType: _Optional[int] = ..., AnimA: _Optional[int] = ..., AnimB: _Optional[int] = ..., offset: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., rote: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., playspeed: _Optional[int] = ..., playmodel: _Optional[int] = ..., anchorId: _Optional[int] = ...) -> None: ...

class PB_RideOtherInfo(_message.Message):
    __slots__ = ("rideID", "boneId", "rideoffsetpos", "ridescale", "riderote", "isRote")
    RIDEID_FIELD_NUMBER: _ClassVar[int]
    BONEID_FIELD_NUMBER: _ClassVar[int]
    RIDEOFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    RIDESCALE_FIELD_NUMBER: _ClassVar[int]
    RIDEROTE_FIELD_NUMBER: _ClassVar[int]
    ISROTE_FIELD_NUMBER: _ClassVar[int]
    rideID: int
    boneId: int
    rideoffsetpos: PB_Vector3f
    ridescale: PB_Vector3f
    riderote: PB_Vector3f
    isRote: bool
    def __init__(self, rideID: _Optional[int] = ..., boneId: _Optional[int] = ..., rideoffsetpos: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., ridescale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., riderote: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., isRote: _Optional[bool] = ...) -> None: ...

class PB_RideCompData(_message.Message):
    __slots__ = ("otherinfos", "isRote", "triggerAdd", "ridingConditions", "usingItem", "tempriderunable", "temprideendtick")
    OTHERINFOS_FIELD_NUMBER: _ClassVar[int]
    ISROTE_FIELD_NUMBER: _ClassVar[int]
    TRIGGERADD_FIELD_NUMBER: _ClassVar[int]
    RIDINGCONDITIONS_FIELD_NUMBER: _ClassVar[int]
    USINGITEM_FIELD_NUMBER: _ClassVar[int]
    TEMPRIDERUNABLE_FIELD_NUMBER: _ClassVar[int]
    TEMPRIDEENDTICK_FIELD_NUMBER: _ClassVar[int]
    otherinfos: _containers.RepeatedCompositeFieldContainer[PB_RideOtherInfo]
    isRote: bool
    triggerAdd: bool
    ridingConditions: int
    usingItem: int
    tempriderunable: bool
    temprideendtick: int
    def __init__(self, otherinfos: _Optional[_Iterable[_Union[PB_RideOtherInfo, _Mapping]]] = ..., isRote: _Optional[bool] = ..., triggerAdd: _Optional[bool] = ..., ridingConditions: _Optional[int] = ..., usingItem: _Optional[int] = ..., tempriderunable: _Optional[bool] = ..., temprideendtick: _Optional[int] = ...) -> None: ...

class PB_IronCompData(_message.Message):
    __slots__ = ("host",)
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: int
    def __init__(self, host: _Optional[int] = ...) -> None: ...

class PB_IronDomeEssenceData(_message.Message):
    __slots__ = ("state", "type", "hp")
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    state: int
    type: int
    hp: float
    def __init__(self, state: _Optional[int] = ..., type: _Optional[int] = ..., hp: _Optional[float] = ...) -> None: ...

class PB_PartInfoData(_message.Message):
    __slots__ = ("host", "part", "hostdefid")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    HOSTDEFID_FIELD_NUMBER: _ClassVar[int]
    host: int
    part: int
    hostdefid: int
    def __init__(self, host: _Optional[int] = ..., part: _Optional[int] = ..., hostdefid: _Optional[int] = ...) -> None: ...

class PB_PartData(_message.Message):
    __slots__ = ("parttype", "state", "objid")
    PARTTYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OBJID_FIELD_NUMBER: _ClassVar[int]
    parttype: int
    state: int
    objid: int
    def __init__(self, parttype: _Optional[int] = ..., state: _Optional[int] = ..., objid: _Optional[int] = ...) -> None: ...

class PB_PartManagerData(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[PB_PartData]
    def __init__(self, infos: _Optional[_Iterable[_Union[PB_PartData, _Mapping]]] = ...) -> None: ...

class PB_MoveData(_message.Message):
    __slots__ = ("walkSpeed", "runSpeed", "flySpeed", "swimSpeed", "jumpSpeed", "sprintRatio", "swimmingRatio")
    WALKSPEED_FIELD_NUMBER: _ClassVar[int]
    RUNSPEED_FIELD_NUMBER: _ClassVar[int]
    FLYSPEED_FIELD_NUMBER: _ClassVar[int]
    SWIMSPEED_FIELD_NUMBER: _ClassVar[int]
    JUMPSPEED_FIELD_NUMBER: _ClassVar[int]
    SPRINTRATIO_FIELD_NUMBER: _ClassVar[int]
    SWIMMINGRATIO_FIELD_NUMBER: _ClassVar[int]
    walkSpeed: float
    runSpeed: int
    flySpeed: int
    swimSpeed: int
    jumpSpeed: int
    sprintRatio: float
    swimmingRatio: float
    def __init__(self, walkSpeed: _Optional[float] = ..., runSpeed: _Optional[int] = ..., flySpeed: _Optional[int] = ..., swimSpeed: _Optional[int] = ..., jumpSpeed: _Optional[int] = ..., sprintRatio: _Optional[float] = ..., swimmingRatio: _Optional[float] = ...) -> None: ...

class PB_NewTameData(_message.Message):
    __slots__ = ("ownerUin", "tameItemsK", "tameItemsV", "showTameFlag", "tamedModel")
    OWNERUIN_FIELD_NUMBER: _ClassVar[int]
    TAMEITEMSK_FIELD_NUMBER: _ClassVar[int]
    TAMEITEMSV_FIELD_NUMBER: _ClassVar[int]
    SHOWTAMEFLAG_FIELD_NUMBER: _ClassVar[int]
    TAMEDMODEL_FIELD_NUMBER: _ClassVar[int]
    ownerUin: int
    tameItemsK: _containers.RepeatedScalarFieldContainer[int]
    tameItemsV: _containers.RepeatedScalarFieldContainer[float]
    showTameFlag: bool
    tamedModel: str
    def __init__(self, ownerUin: _Optional[int] = ..., tameItemsK: _Optional[_Iterable[int]] = ..., tameItemsV: _Optional[_Iterable[float]] = ..., showTameFlag: _Optional[bool] = ..., tamedModel: _Optional[str] = ...) -> None: ...

class PB_ReproductionTriggerItem(_message.Message):
    __slots__ = ("itemId", "num")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    num: int
    def __init__(self, itemId: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class PB_ReproductionCompData(_message.Message):
    __slots__ = ("state", "isForbidden", "itemArray")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ISFORBIDDEN_FIELD_NUMBER: _ClassVar[int]
    ITEMARRAY_FIELD_NUMBER: _ClassVar[int]
    state: int
    isForbidden: bool
    itemArray: _containers.RepeatedCompositeFieldContainer[PB_ReproductionTriggerItem]
    def __init__(self, state: _Optional[int] = ..., isForbidden: _Optional[bool] = ..., itemArray: _Optional[_Iterable[_Union[PB_ReproductionTriggerItem, _Mapping]]] = ...) -> None: ...

class FB_FeedCompData(_message.Message):
    __slots__ = ("enableFeed", "enableHp", "enablePower", "numItems", "itemId", "addHeal", "addStamina", "addFavor", "enablefeedback", "numExchangeItems", "exchangeItems", "enableFavor")
    class ExchangeItem(_message.Message):
        __slots__ = ("itemId", "procMotionId", "procSoundId", "procEffectId", "rewardAfterTime", "enableBeforeTame", "enableSuccFeedback", "groupArray")
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        PROCMOTIONID_FIELD_NUMBER: _ClassVar[int]
        PROCSOUNDID_FIELD_NUMBER: _ClassVar[int]
        PROCEFFECTID_FIELD_NUMBER: _ClassVar[int]
        REWARDAFTERTIME_FIELD_NUMBER: _ClassVar[int]
        ENABLEBEFORETAME_FIELD_NUMBER: _ClassVar[int]
        ENABLESUCCFEEDBACK_FIELD_NUMBER: _ClassVar[int]
        GROUPARRAY_FIELD_NUMBER: _ClassVar[int]
        itemId: int
        procMotionId: int
        procSoundId: int
        procEffectId: int
        rewardAfterTime: int
        enableBeforeTame: bool
        enableSuccFeedback: bool
        groupArray: _containers.RepeatedCompositeFieldContainer[FB_FeedCompData.ExchangeRewardGroup]
        def __init__(self, itemId: _Optional[int] = ..., procMotionId: _Optional[int] = ..., procSoundId: _Optional[int] = ..., procEffectId: _Optional[int] = ..., rewardAfterTime: _Optional[int] = ..., enableBeforeTame: _Optional[bool] = ..., enableSuccFeedback: _Optional[bool] = ..., groupArray: _Optional[_Iterable[_Union[FB_FeedCompData.ExchangeRewardGroup, _Mapping]]] = ...) -> None: ...
    class ExchangeRewardItem(_message.Message):
        __slots__ = ("type", "itemId", "minNum", "maxNum", "buffId", "weight")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        MINNUM_FIELD_NUMBER: _ClassVar[int]
        MAXNUM_FIELD_NUMBER: _ClassVar[int]
        BUFFID_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        type: int
        itemId: int
        minNum: int
        maxNum: int
        buffId: int
        weight: int
        def __init__(self, type: _Optional[int] = ..., itemId: _Optional[int] = ..., minNum: _Optional[int] = ..., maxNum: _Optional[int] = ..., buffId: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...
    class ExchangeRewardGroup(_message.Message):
        __slots__ = ("rewardProb", "sumWeight", "rewardList")
        REWARDPROB_FIELD_NUMBER: _ClassVar[int]
        SUMWEIGHT_FIELD_NUMBER: _ClassVar[int]
        REWARDLIST_FIELD_NUMBER: _ClassVar[int]
        rewardProb: float
        sumWeight: int
        rewardList: _containers.RepeatedCompositeFieldContainer[FB_FeedCompData.ExchangeRewardItem]
        def __init__(self, rewardProb: _Optional[float] = ..., sumWeight: _Optional[int] = ..., rewardList: _Optional[_Iterable[_Union[FB_FeedCompData.ExchangeRewardItem, _Mapping]]] = ...) -> None: ...
    ENABLEFEED_FIELD_NUMBER: _ClassVar[int]
    ENABLEHP_FIELD_NUMBER: _ClassVar[int]
    ENABLEPOWER_FIELD_NUMBER: _ClassVar[int]
    NUMITEMS_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ADDHEAL_FIELD_NUMBER: _ClassVar[int]
    ADDSTAMINA_FIELD_NUMBER: _ClassVar[int]
    ADDFAVOR_FIELD_NUMBER: _ClassVar[int]
    ENABLEFEEDBACK_FIELD_NUMBER: _ClassVar[int]
    NUMEXCHANGEITEMS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEITEMS_FIELD_NUMBER: _ClassVar[int]
    ENABLEFAVOR_FIELD_NUMBER: _ClassVar[int]
    enableFeed: bool
    enableHp: bool
    enablePower: bool
    numItems: int
    itemId: _containers.RepeatedScalarFieldContainer[int]
    addHeal: _containers.RepeatedScalarFieldContainer[int]
    addStamina: _containers.RepeatedScalarFieldContainer[int]
    addFavor: _containers.RepeatedScalarFieldContainer[int]
    enablefeedback: _containers.RepeatedScalarFieldContainer[bool]
    numExchangeItems: int
    exchangeItems: _containers.RepeatedCompositeFieldContainer[FB_FeedCompData.ExchangeItem]
    enableFavor: bool
    def __init__(self, enableFeed: _Optional[bool] = ..., enableHp: _Optional[bool] = ..., enablePower: _Optional[bool] = ..., numItems: _Optional[int] = ..., itemId: _Optional[_Iterable[int]] = ..., addHeal: _Optional[_Iterable[int]] = ..., addStamina: _Optional[_Iterable[int]] = ..., addFavor: _Optional[_Iterable[int]] = ..., enablefeedback: _Optional[_Iterable[bool]] = ..., numExchangeItems: _Optional[int] = ..., exchangeItems: _Optional[_Iterable[_Union[FB_FeedCompData.ExchangeItem, _Mapping]]] = ..., enableFavor: _Optional[bool] = ...) -> None: ...

class PB_NewGrowData(_message.Message):
    __slots__ = ("enableItem", "growState", "growthItemId")
    ENABLEITEM_FIELD_NUMBER: _ClassVar[int]
    GROWSTATE_FIELD_NUMBER: _ClassVar[int]
    GROWTHITEMID_FIELD_NUMBER: _ClassVar[int]
    enableItem: bool
    growState: int
    growthItemId: int
    def __init__(self, enableItem: _Optional[bool] = ..., growState: _Optional[int] = ..., growthItemId: _Optional[int] = ...) -> None: ...

class PB_DropItemCompData(_message.Message):
    __slots__ = ("dropCounter", "needCheckRecover", "interactDropTime", "timedDropTime")
    DROPCOUNTER_FIELD_NUMBER: _ClassVar[int]
    NEEDCHECKRECOVER_FIELD_NUMBER: _ClassVar[int]
    INTERACTDROPTIME_FIELD_NUMBER: _ClassVar[int]
    TIMEDDROPTIME_FIELD_NUMBER: _ClassVar[int]
    dropCounter: int
    needCheckRecover: bool
    interactDropTime: int
    timedDropTime: int
    def __init__(self, dropCounter: _Optional[int] = ..., needCheckRecover: _Optional[bool] = ..., interactDropTime: _Optional[int] = ..., timedDropTime: _Optional[int] = ...) -> None: ...

class PB_SleepData(_message.Message):
    __slots__ = ("currentAnim",)
    CURRENTANIM_FIELD_NUMBER: _ClassVar[int]
    currentAnim: int
    def __init__(self, currentAnim: _Optional[int] = ...) -> None: ...

class PB_TrainFollowData(_message.Message):
    __slots__ = ("prev_actor_id", "spacing", "tail_actor_id")
    PREV_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    TAIL_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    prev_actor_id: int
    spacing: float
    tail_actor_id: int
    def __init__(self, prev_actor_id: _Optional[int] = ..., spacing: _Optional[float] = ..., tail_actor_id: _Optional[int] = ...) -> None: ...

class PB_BroomFlyData(_message.Message):
    __slots__ = ("is_active", "move_speed", "acce_speed", "jump_cd", "bounce_motion_y", "accel_duration", "current_speed", "jump_pitch", "fly_tail_effect_id", "gravity_scale", "model_rotation_transition_duration", "pc_yaw_follow_sharpness", "mobile_yaw_follow_sharpness", "flight_move_pitch_return_duration", "model_rotation_active_duration", "model_rotation_transition_ease_power")
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MOVE_SPEED_FIELD_NUMBER: _ClassVar[int]
    ACCE_SPEED_FIELD_NUMBER: _ClassVar[int]
    JUMP_CD_FIELD_NUMBER: _ClassVar[int]
    BOUNCE_MOTION_Y_FIELD_NUMBER: _ClassVar[int]
    ACCEL_DURATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SPEED_FIELD_NUMBER: _ClassVar[int]
    JUMP_PITCH_FIELD_NUMBER: _ClassVar[int]
    FLY_TAIL_EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    GRAVITY_SCALE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ROTATION_TRANSITION_DURATION_FIELD_NUMBER: _ClassVar[int]
    PC_YAW_FOLLOW_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    MOBILE_YAW_FOLLOW_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_MOVE_PITCH_RETURN_DURATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ROTATION_ACTIVE_DURATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ROTATION_TRANSITION_EASE_POWER_FIELD_NUMBER: _ClassVar[int]
    is_active: bool
    move_speed: float
    acce_speed: float
    jump_cd: float
    bounce_motion_y: float
    accel_duration: float
    current_speed: float
    jump_pitch: float
    fly_tail_effect_id: int
    gravity_scale: float
    model_rotation_transition_duration: float
    pc_yaw_follow_sharpness: float
    mobile_yaw_follow_sharpness: float
    flight_move_pitch_return_duration: float
    model_rotation_active_duration: float
    model_rotation_transition_ease_power: float
    def __init__(self, is_active: _Optional[bool] = ..., move_speed: _Optional[float] = ..., acce_speed: _Optional[float] = ..., jump_cd: _Optional[float] = ..., bounce_motion_y: _Optional[float] = ..., accel_duration: _Optional[float] = ..., current_speed: _Optional[float] = ..., jump_pitch: _Optional[float] = ..., fly_tail_effect_id: _Optional[int] = ..., gravity_scale: _Optional[float] = ..., model_rotation_transition_duration: _Optional[float] = ..., pc_yaw_follow_sharpness: _Optional[float] = ..., mobile_yaw_follow_sharpness: _Optional[float] = ..., flight_move_pitch_return_duration: _Optional[float] = ..., model_rotation_active_duration: _Optional[float] = ..., model_rotation_transition_ease_power: _Optional[float] = ...) -> None: ...

class PB_ActorCompData(_message.Message):
    __slots__ = ("atkanim", "boundsize", "boundheight", "hitbound", "walkanim", "runanim", "flyanim", "swimanim", "sneakanim", "phystype", "scale", "jumpanim", "modelKv", "attackdistance", "rideID", "boneId", "rideHp", "rideoffsetpos", "ridescale", "riderote", "carryComp", "ridecomp", "ironInfo", "ironDomeEssenceInfo", "partinfo", "partmanagerinfo", "hitcenter", "moveData", "interact", "newTameData", "repComp", "newGrowData", "feedCompData", "dropItemComp", "sleepData", "trainFollowData", "broomFlyData")
    ATKANIM_FIELD_NUMBER: _ClassVar[int]
    BOUNDSIZE_FIELD_NUMBER: _ClassVar[int]
    BOUNDHEIGHT_FIELD_NUMBER: _ClassVar[int]
    HITBOUND_FIELD_NUMBER: _ClassVar[int]
    WALKANIM_FIELD_NUMBER: _ClassVar[int]
    RUNANIM_FIELD_NUMBER: _ClassVar[int]
    FLYANIM_FIELD_NUMBER: _ClassVar[int]
    SWIMANIM_FIELD_NUMBER: _ClassVar[int]
    SNEAKANIM_FIELD_NUMBER: _ClassVar[int]
    PHYSTYPE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    JUMPANIM_FIELD_NUMBER: _ClassVar[int]
    MODELKV_FIELD_NUMBER: _ClassVar[int]
    ATTACKDISTANCE_FIELD_NUMBER: _ClassVar[int]
    RIDEID_FIELD_NUMBER: _ClassVar[int]
    BONEID_FIELD_NUMBER: _ClassVar[int]
    RIDEHP_FIELD_NUMBER: _ClassVar[int]
    RIDEOFFSETPOS_FIELD_NUMBER: _ClassVar[int]
    RIDESCALE_FIELD_NUMBER: _ClassVar[int]
    RIDEROTE_FIELD_NUMBER: _ClassVar[int]
    CARRYCOMP_FIELD_NUMBER: _ClassVar[int]
    RIDECOMP_FIELD_NUMBER: _ClassVar[int]
    IRONINFO_FIELD_NUMBER: _ClassVar[int]
    IRONDOMEESSENCEINFO_FIELD_NUMBER: _ClassVar[int]
    PARTINFO_FIELD_NUMBER: _ClassVar[int]
    PARTMANAGERINFO_FIELD_NUMBER: _ClassVar[int]
    HITCENTER_FIELD_NUMBER: _ClassVar[int]
    MOVEDATA_FIELD_NUMBER: _ClassVar[int]
    INTERACT_FIELD_NUMBER: _ClassVar[int]
    NEWTAMEDATA_FIELD_NUMBER: _ClassVar[int]
    REPCOMP_FIELD_NUMBER: _ClassVar[int]
    NEWGROWDATA_FIELD_NUMBER: _ClassVar[int]
    FEEDCOMPDATA_FIELD_NUMBER: _ClassVar[int]
    DROPITEMCOMP_FIELD_NUMBER: _ClassVar[int]
    SLEEPDATA_FIELD_NUMBER: _ClassVar[int]
    TRAINFOLLOWDATA_FIELD_NUMBER: _ClassVar[int]
    BROOMFLYDATA_FIELD_NUMBER: _ClassVar[int]
    atkanim: int
    boundsize: int
    boundheight: int
    hitbound: PB_Vector3
    walkanim: int
    runanim: int
    flyanim: int
    swimanim: int
    sneakanim: int
    phystype: int
    scale: PB_Vector3f
    jumpanim: int
    modelKv: str
    attackdistance: float
    rideID: int
    boneId: int
    rideHp: int
    rideoffsetpos: PB_Vector3f
    ridescale: PB_Vector3f
    riderote: PB_Vector3f
    carryComp: CarryCompData
    ridecomp: PB_RideCompData
    ironInfo: PB_IronCompData
    ironDomeEssenceInfo: PB_IronDomeEssenceData
    partinfo: PB_PartInfoData
    partmanagerinfo: PB_PartManagerData
    hitcenter: PB_Vector3
    moveData: PB_MoveData
    interact: bool
    newTameData: PB_NewTameData
    repComp: PB_ReproductionCompData
    newGrowData: PB_NewGrowData
    feedCompData: FB_FeedCompData
    dropItemComp: PB_DropItemCompData
    sleepData: PB_SleepData
    trainFollowData: PB_TrainFollowData
    broomFlyData: PB_BroomFlyData
    def __init__(self, atkanim: _Optional[int] = ..., boundsize: _Optional[int] = ..., boundheight: _Optional[int] = ..., hitbound: _Optional[_Union[PB_Vector3, _Mapping]] = ..., walkanim: _Optional[int] = ..., runanim: _Optional[int] = ..., flyanim: _Optional[int] = ..., swimanim: _Optional[int] = ..., sneakanim: _Optional[int] = ..., phystype: _Optional[int] = ..., scale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., jumpanim: _Optional[int] = ..., modelKv: _Optional[str] = ..., attackdistance: _Optional[float] = ..., rideID: _Optional[int] = ..., boneId: _Optional[int] = ..., rideHp: _Optional[int] = ..., rideoffsetpos: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., ridescale: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., riderote: _Optional[_Union[PB_Vector3f, _Mapping]] = ..., carryComp: _Optional[_Union[CarryCompData, _Mapping]] = ..., ridecomp: _Optional[_Union[PB_RideCompData, _Mapping]] = ..., ironInfo: _Optional[_Union[PB_IronCompData, _Mapping]] = ..., ironDomeEssenceInfo: _Optional[_Union[PB_IronDomeEssenceData, _Mapping]] = ..., partinfo: _Optional[_Union[PB_PartInfoData, _Mapping]] = ..., partmanagerinfo: _Optional[_Union[PB_PartManagerData, _Mapping]] = ..., hitcenter: _Optional[_Union[PB_Vector3, _Mapping]] = ..., moveData: _Optional[_Union[PB_MoveData, _Mapping]] = ..., interact: _Optional[bool] = ..., newTameData: _Optional[_Union[PB_NewTameData, _Mapping]] = ..., repComp: _Optional[_Union[PB_ReproductionCompData, _Mapping]] = ..., newGrowData: _Optional[_Union[PB_NewGrowData, _Mapping]] = ..., feedCompData: _Optional[_Union[FB_FeedCompData, _Mapping]] = ..., dropItemComp: _Optional[_Union[PB_DropItemCompData, _Mapping]] = ..., sleepData: _Optional[_Union[PB_SleepData, _Mapping]] = ..., trainFollowData: _Optional[_Union[PB_TrainFollowData, _Mapping]] = ..., broomFlyData: _Optional[_Union[PB_BroomFlyData, _Mapping]] = ...) -> None: ...

class PB_PlayWeaponMotionData(_message.Message):
    __slots__ = ("objID", "effectID", "name", "reset", "mclass", "scale")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    EFFECTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    MCLASS_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    objID: int
    effectID: int
    name: str
    reset: bool
    mclass: int
    scale: int
    def __init__(self, objID: _Optional[int] = ..., effectID: _Optional[int] = ..., name: _Optional[str] = ..., reset: _Optional[bool] = ..., mclass: _Optional[int] = ..., scale: _Optional[int] = ...) -> None: ...

class PB_PlayWeaponAnimData(_message.Message):
    __slots__ = ("objID", "animID", "loop", "speed")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    ANIMID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    objID: int
    animID: int
    loop: int
    speed: int
    def __init__(self, objID: _Optional[int] = ..., animID: _Optional[int] = ..., loop: _Optional[int] = ..., speed: _Optional[int] = ...) -> None: ...

class PB_PhysicsTimestamp(_message.Message):
    __slots__ = ("WorldId", "ServerFrame", "LocalFrame")
    WORLDID_FIELD_NUMBER: _ClassVar[int]
    SERVERFRAME_FIELD_NUMBER: _ClassVar[int]
    LOCALFRAME_FIELD_NUMBER: _ClassVar[int]
    WorldId: int
    ServerFrame: int
    LocalFrame: int
    def __init__(self, WorldId: _Optional[int] = ..., ServerFrame: _Optional[int] = ..., LocalFrame: _Optional[int] = ...) -> None: ...

class PB_TimeDilationData(_message.Message):
    __slots__ = ("TimeDilation", "ServerStep")
    TIMEDILATION_FIELD_NUMBER: _ClassVar[int]
    SERVERSTEP_FIELD_NUMBER: _ClassVar[int]
    TimeDilation: float
    ServerStep: int
    def __init__(self, TimeDilation: _Optional[float] = ..., ServerStep: _Optional[int] = ...) -> None: ...

class PB_InputFrameData(_message.Message):
    __slots__ = ("PlayerId", "Frame", "Data")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PlayerId: int
    Frame: int
    Data: bytes
    def __init__(self, PlayerId: _Optional[int] = ..., Frame: _Optional[int] = ..., Data: _Optional[bytes] = ...) -> None: ...

class PB_PhysicsReplicatedInput(_message.Message):
    __slots__ = ("PlayerId", "Data")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PlayerId: int
    Data: bytes
    def __init__(self, PlayerId: _Optional[int] = ..., Data: _Optional[bytes] = ...) -> None: ...

class PB_PhysicsReplicatedState(_message.Message):
    __slots__ = ("PlayerId", "Data")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PlayerId: int
    Data: bytes
    def __init__(self, PlayerId: _Optional[int] = ..., Data: _Optional[bytes] = ...) -> None: ...

class PB_CommonPhysicsReplication(_message.Message):
    __slots__ = ("PlayerId", "Data")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PlayerId: int
    Data: bytes
    def __init__(self, PlayerId: _Optional[int] = ..., Data: _Optional[bytes] = ...) -> None: ...

class PB_WBPRegionMsg(_message.Message):
    __slots__ = ("blockpos", "knotpos", "state", "knotstate")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    KNOTPOS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    KNOTSTATE_FIELD_NUMBER: _ClassVar[int]
    blockpos: PB_Vector3
    knotpos: PB_Vector3
    state: int
    knotstate: int
    def __init__(self, blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., knotpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., state: _Optional[int] = ..., knotstate: _Optional[int] = ...) -> None: ...

class PB_WBPCreateBluePrintMsg(_message.Message):
    __slots__ = ("resId", "gridIndex", "blockpos", "dim", "name")
    RESID_FIELD_NUMBER: _ClassVar[int]
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    DIM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    resId: str
    gridIndex: int
    blockpos: PB_Vector3
    dim: PB_Vector3
    name: str
    def __init__(self, resId: _Optional[str] = ..., gridIndex: _Optional[int] = ..., blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., dim: _Optional[_Union[PB_Vector3, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class PB_WBPClickResultGrid(_message.Message):
    __slots__ = ("gridIndex", "blockpos")
    GRIDINDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    gridIndex: int
    blockpos: PB_Vector3
    def __init__(self, gridIndex: _Optional[int] = ..., blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_WBPAddMtlMsg(_message.Message):
    __slots__ = ("blockids", "nums", "blockpos")
    BLOCKIDS_FIELD_NUMBER: _ClassVar[int]
    NUMS_FIELD_NUMBER: _ClassVar[int]
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockids: _containers.RepeatedScalarFieldContainer[int]
    nums: _containers.RepeatedScalarFieldContainer[int]
    blockpos: PB_Vector3
    def __init__(self, blockids: _Optional[_Iterable[int]] = ..., nums: _Optional[_Iterable[int]] = ..., blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_SimpleItemData(_message.Message):
    __slots__ = ("index", "itemid", "num", "durable", "userdata")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    index: int
    itemid: int
    num: int
    durable: int
    userdata: int
    def __init__(self, index: _Optional[int] = ..., itemid: _Optional[int] = ..., num: _Optional[int] = ..., durable: _Optional[int] = ..., userdata: _Optional[int] = ...) -> None: ...

class PB_WBPSyncGridsMsg(_message.Message):
    __slots__ = ("blockpos", "grids")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    GRIDS_FIELD_NUMBER: _ClassVar[int]
    blockpos: PB_Vector3
    grids: _containers.RepeatedCompositeFieldContainer[PB_SimpleItemData]
    def __init__(self, blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., grids: _Optional[_Iterable[_Union[PB_SimpleItemData, _Mapping]]] = ...) -> None: ...

class PB_WBPAutoPlaceMsg(_message.Message):
    __slots__ = ("blockpos",)
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    blockpos: PB_Vector3
    def __init__(self, blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ...) -> None: ...

class PB_WBPAutoPlaceStateMsg(_message.Message):
    __slots__ = ("blockpos", "autoplace")
    BLOCKPOS_FIELD_NUMBER: _ClassVar[int]
    AUTOPLACE_FIELD_NUMBER: _ClassVar[int]
    blockpos: PB_Vector3
    autoplace: bool
    def __init__(self, blockpos: _Optional[_Union[PB_Vector3, _Mapping]] = ..., autoplace: _Optional[bool] = ...) -> None: ...

class PB_ActorPhyType(_message.Message):
    __slots__ = ("ObjID", "physicType")
    OBJID_FIELD_NUMBER: _ClassVar[int]
    PHYSICTYPE_FIELD_NUMBER: _ClassVar[int]
    ObjID: int
    physicType: int
    def __init__(self, ObjID: _Optional[int] = ..., physicType: _Optional[int] = ...) -> None: ...
