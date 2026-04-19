mc_to_mini_mapping = {
    10: 3107,  # bat - 蝙蝠
    11: 3418,  # bee - 蜜蜂
    26: 3282,  # chicken - 鸡
    30: 3284,  # cow - 奶牛
    32: 3109,  # creeper - 爆爆蛋
    36: 3404,  # donkey - 马（迷你世界马为3404）
    38: 3105,  # drowned - 野人投矛手
    41: 3101,  # enderman - 野人战士
    54: 3407,  # fox - 狐狸
    62: 3288,  # goat - 野羊
    66: 3404,  # horse - 马
    70: 3130,  # iron_golem - 熔岩巨人
    78: 3403,  # llama - 角鹿
    86: 3286,  # mooshroom - 野牛（蘑菇牛近似野牛）
    91: 3278,  # ocelot - 猫
    96: 3416,  # panda - 熊猫
    98: 3410,  # parrot - 鸵鸟（驯服）
    100: 3284,  # pig - 猪
    101: 3101,  # piglin - 野人战士
    103: 3105,  # pillager - 野人投矛手
    104: 3412,  # polar_bear - 冰熊
    108: 3280,  # rabbit - 野兔
    111: 3292,  # sheep - 绵羊
    115: 3105,  # skeleton - 野人投矛手
    124: 3101,  # spider - 野人战士
    127: 3601,  # squid - 乌贼
    128: 3105,  # stray - 野人投矛手
    136: 3607,  # tropical_fish - 淡蓝奇奇鱼
    139: 3204,  # villager - 沙漠年轻男村民
    141: 3010,  # wandering_trader - 游商
    148: 3276,  # wolf - 狗
    150: 3101,  # zombie - 野人战士
    154: 3101,  # zombified_piglin - 野人战士
}

mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items()}


def mc_to_mini(id: int) -> int:
    if id in mc_to_mini_mapping:
        return mc_to_mini_mapping[id]
    else:
        return 3284  # 猪


def mini_to_mc(id: int) -> int:
    if id in mini_to_mc_mapping:
        return mini_to_mc_mapping[id]
    else:
        return 100  # 猪
