"""Map MC status effect IDs to Mini World BuffIDs.

Reference: https://minecraft.wiki/w/Effect
MC effect IDs from minecraft-data (1.21).
Mini World buff IDs are speculative — verified ones are marked.
"""

# MC effect ID → Mini World BuffID
# Format: (miniworld_buff_id, notes)
MC_TO_MINI_BUFF: dict[int, tuple[int, str]] = {
    1:  (1001, "Speed → movement speed boost"),
    2:  (1002, "Slowness → movement speed reduction"),
    3:  (1003, "Haste → mining speed boost"),
    4:  (1004, "Mining Fatigue → mining speed reduction"),
    5:  (1005, "Strength → damage boost"),
    6:  (1006, "Instant Health → instant heal"),
    7:  (1007, "Instant Damage → instant harm"),
    8:  (1008, "Jump Boost → jump height increase"),
    9:  (1009, "Nausea → screen distortion"),
    10: (1010, "Regeneration → regen HP over time"),
    11: (1011, "Resistance → damage reduction"),
    12: (1012, "Fire Resistance → fire immunity"),
    13: (1013, "Water Breathing → breath underwater"),
    14: (1014, "Invisibility → invisible"),
    15: (1015, "Blindness → blindness"),
    16: (1016, "Night Vision → bright vision"),
    17: (1017, "Hunger → food drain"),
    18: (1018, "Weakness → damage reduction"),
    19: (1019, "Poison → poison damage over time"),
    20: (1020, "Wither → wither damage over time"),
    21: (1021, "Health Boost → bonus HP"),
    22: (1022, "Absorption → absorption HP"),
    23: (1023, "Saturation → instant food"),
    24: (1024, "Glowing → outline glow"),
    25: (1025, "Levitation → float upward"),
    26: (1026, "Luck → better loot"),
    27: (1027, "Bad Luck → worse loot"),
    28: (1028, "Slow Falling → slow descent"),
    29: (1029, "Conduit Power → underwater buff"),
    30: (1030, "Dolphin's Grace → swim speed"),
    31: (1031, "Bad Omen → raid trigger"),
    32: (1032, "Hero of the Village → discount trades"),
    33: (1033, "Darkness → dim vision"),
}

# Reverse: Mini BuffID → MC effect ID
MINI_TO_MC_BUFF: dict[int, int] = {v[0]: k for k, v in MC_TO_MINI_BUFF.items()}
