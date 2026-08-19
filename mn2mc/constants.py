"""Magic constants extracted from the Minecraft protocol and Mini World bridge.

These values are not arbitrary: they come directly from the MC 1.21.11 protocol
and the Mini World server expectations, so they should be treated as public
contracts rather than internal tuning knobs.

ID semantics:
- Player UIN values are uint32 (0 to UIN_MAX).
- Entity/object IDs start at MINI_OBJ_ID_BASE to avoid collision with player UINs.
"""

# Minecraft dimension identifiers
# References:
# - mn2mc/mc/client.py:75  "_dimension = 0  # -1: the_nether | 0: overworld | 1: the_end"
DIMENSION_NETHER = -1
DIMENSION_OVERWORLD = 0
DIMENSION_END = 1

# Mini World player UIN range: 0 to UIN_MAX (uint32)
# Entity/object IDs start at MINI_OBJ_ID_BASE (UIN_MAX + 1, 64-bit)
# References:
# - mn2mc/mc/packetevents/spawn_entity.py:78  "4294967294 + entityid"
# - mn2mc/mc/packetevents/spawn_entity.py:84  "4294967294 + entityid"
UIN_MAX = 4294967295  # 0xFFFFFFFF, uint32 最大值
MINI_OBJ_ID_BASE = UIN_MAX + 1  # 4294967296, entity ID 偏移起点（64 位）

# Chunk section flags sent in initial SyncChunkDataHC packets.
# References:
# - mn2mc/mc/packetevents/chunk/map_chunk.py:96  "SectionFlags=65535"
SECTION_FLAGS = 65535

# Minecraft player game modes (matching the MC protocol semantics).
# References:
# - Verified against MC 1.21.11 protocol expectations
GAMEMODE_SURVIVAL = 1
GAMEMODE_CREATIVE = 3

# Velocity scaling num
VELOCITY_SCALING = 70
