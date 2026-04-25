# MC id: Mini id
mc_to_mini_mapping = {
    0: 0,     # air - 空气
    1: 104,   # stone - 岩石
    2: 104,   # granite - 岩石
    3: 505,   # polished_granite - 碎石块
    4: 104,   # diorite - 岩石
    5: 505,   # polished_diorite - 碎石块
    6: 104,   # andesite - 岩石
    7: 505,   # polished_andesite - 碎石块
    8: 100,   # grass_block - 长草土块
    9: 101,   # dirt - 土块
    10: 101,  # coarse_dirt - 土块
    11: 233,  # podzol - 红土
    12: 502,  # cobblestone - 裂纹石砖
    13: 206,  # oak_planks - 木板
    14: 206,  # spruce_planks - 木板
    15: 207,  # birch_planks - 秋叶橙木板
    16: 209,  # jungle_planks - 海棠红木板
    17: 210,  # acacia_planks - 落日橙木板
    18: 562,  # cherry_planks - 胭脂红木板
    19: 211,  # dark_oak_planks - 深栗红木板
    22: 206,  # mangrove_planks - 木板
    23: 251,  # bamboo_planks - 竹子
    34: 1,    # bedrock - 地心基石
    35: 3,    # water - 静态水
    36: 5,    # lava - 静态岩浆
    37: 106,  # sand - 黄沙
    39: 128,  # red_sand - 红沙
    40: 107,  # gravel - 碎石堆
    42: 408,  # gold_ore - 钨金块
    43: 408,  # deepslate_gold_ore - 钨金块
    44: 456,  # iron_ore - 黄铜块
    45: 456,  # deepslate_iron_ore - 黄铜块
    46: 402,  # coal_ore - 凝能矿
    47: 402,  # deepslate_coal_ore - 凝能矿
    48: 132,  # nether_gold_ore - 硫黄晶砂
    49: 200,  # oak_log - 樱桃木
    50: 201,  # spruce_log - 落叶松木
    51: 202,  # birch_log - 白杨木
    52: 203,  # jungle_log - 红杉木
    53: 205,  # acacia_log - 核桃木
    54: 254,  # cherry_log - 桃花木
    55: 205,  # dark_oak_log - 核桃木
    57: 386,  # mangrove_log - 香蕉树干
    60: 563,  # bamboo_block - 竹板
    61: 201,  # stripped_spruce_log - 落叶松木
    62: 202,  # stripped_birch_log - 白杨木
    63: 203,  # stripped_jungle_log - 红杉木
    64: 205,  # stripped_acacia_log - 核桃木
    65: 254,  # stripped_cherry_log - 桃花木
    66: 205,  # stripped_dark_oak_log - 核桃木
    68: 200,  # stripped_oak_log - 樱桃木
    69: 386,  # stripped_mangrove_log - 香蕉树干
    71: 200,  # oak_wood - 樱桃木
    72: 201,  # spruce_wood - 落叶松木
    73: 202,  # birch_wood - 白杨木
    74: 203,  # jungle_wood - 红杉木
    75: 205,  # acacia_wood - 核桃木
    76: 254,  # cherry_wood - 桃花木
    77: 205,  # dark_oak_wood - 核桃木
    78: 386,  # mangrove_wood - 香蕉树干
    79: 200,  # stripped_oak_wood - 樱桃木
    80: 201,  # stripped_spruce_wood - 落叶松木
    81: 202,  # stripped_birch_wood - 白杨木
    82: 203,  # stripped_jungle_wood - 红杉木
    83: 205,  # stripped_acacia_wood - 核桃木
    84: 254,  # stripped_cherry_wood - 桃花木
    85: 205,  # stripped_dark_oak_wood - 核桃木
    87: 386,  # stripped_mangrove_wood - 香蕉树干
    88: 218,  # oak_leaves - 樱桃木树叶
    89: 219,  # spruce_leaves - 落叶松树叶
    90: 220,  # birch_leaves - 白杨树叶
    91: 221,  # jungle_leaves - 红杉树叶
    92: 223,  # acacia_leaves - 核桃树叶
    93: 255,  # cherry_leaves - 桃花树叶
    94: 223,  # dark_oak_leaves - 核桃树叶
    96: 384,  # mangrove_leaves - 香蕉树叶
    97: 218,  # azalea_leaves - 樱桃木树叶
    98: 218,  # flowering_azalea_leaves - 樱桃木树叶
    99: 127,  # sponge - 泡沫块
    100: 127, # wet_sponge - 泡沫块
    101: 632, # glass - 透明玻璃块
    102: 411, # lapis_ore - 铁块
    103: 411, # deepslate_lapis_ore - 铁块
    104: 411, # lapis_block - 铁块
    106: 108, # sandstone - 素纹黄砖
    107: 108, # chiseled_sandstone - 素纹黄砖
    108: 108, # cut_sandstone - 素纹黄砖
    109: 726, # note_block - 钢琴
    110: 883, # white_bed - 精致木床
    111: 883, # orange_bed - 精致木床
    112: 884, # magenta_bed - 豪华木床
    113: 885, # light_blue_bed - 公主床
    114: 883, # yellow_bed - 精致木床
    115: 883, # lime_bed - 精致木床
    116: 883, # pink_bed - 精致木床
    117: 883, # gray_bed - 精致木床
    118: 883, # light_gray_bed - 精致木床
    119: 885, # cyan_bed - 公主床
    120: 884, # purple_bed - 豪华木床
    121: 885, # blue_bed - 公主床
    122: 883, # brown_bed - 精致木床
    123: 883, # green_bed - 精致木床
    124: 884, # red_bed - 豪华木床
    125: 883, # black_bed - 精致木床
    129: 232, # cobweb - 气根
    131: 238, # fern - 荆棘草
    132: 225, # dead_bush - 枯草
    136: 245, # seagrass - 水草
    137: 245, # tall_seagrass - 水草
    138: 505, # piston - 碎石块
    139: 505, # piston_head - 碎石块
    140: 600, # white_wool - 棉花块
    141: 601, # orange_wool - 棉花块
    142: 602, # magenta_wool - 棉花块
    143: 603, # light_blue_wool - 棉花块
    144: 604, # yellow_wool - 棉花块
    145: 605, # lime_wool - 棉花块
    146: 606, # pink_wool - 棉花块
    147: 607, # gray_wool - 棉花块
    148: 608, # light_gray_wool - 棉花块
    149: 609, # cyan_wool - 棉花块
    150: 610, # purple_wool - 棉花块
    151: 611, # blue_wool - 棉花块
    152: 612, # brown_wool - 棉花块
    153: 613, # green_wool - 棉花块
    154: 614, # red_wool - 棉花块
    155: 615, # black_wool - 棉花块
    156: 505, # moving_piston - 碎石块
    157: 302, # dandelion - 星辰花
    158: 302, # torchflower - 星辰花
    159: 313, # poppy - 月季
    160: 304, # blue_orchid - 风信子
    161: 301, # allium - 若兰
    162: 311, # azure_bluet - 雪滴花
    163: 313, # red_tulip - 月季
    164: 303, # orange_tulip - 龙血花
    165: 311, # white_tulip - 雪滴花
    166: 310, # pink_tulip - 粉色忘忧草
    167: 311, # oxeye_daisy - 雪滴花
    168: 304, # cornflower - 风信子
    169: 313, # wither_rose - 月季
    170: 311, # lily_of_the_valley - 雪滴花
    171: 465, # brown_mushroom - 洋红毒菇
    172: 465, # red_mushroom - 洋红毒菇
    173: 408, # gold_block - 钨金块
    174: 456, # iron_block - 黄铜块
    175: 547, # bricks - 水泥砖块
    176: 132, # tnt - 硫黄晶砂
    177: 820, # bookshelf - 书柜
    178: 820, # chiseled_bookshelf - 书柜
    191: 503, # mossy_cobblestone - 青石砖
    192: 962, # obsidian - 白色基石
    193: 934, # torch - 典雅壁灯
    194: 934, # wall_torch - 典雅壁灯
    195: 141, # fire - 勇气石座
    196: 141, # soul_fire - 勇气石座
    197: 684, # spawner - 斜纹黑石块
    199: 520, # oak_stairs - 楼梯
    200: 801, # chest - 储物箱
    202: 410, # diamond_ore - 炽炎块
    203: 410, # deepslate_diamond_ore - 炽炎块
    204: 410, # diamond_block - 炽炎块
    205: 797, # crafting_table - 工匠台
    206: 234, # wheat - 水稻
    207: 102, # farmland - 耕地
    208: 802, # furnace - 冶炼台
    209: 892, # oak_sign - 木质字牌
    210: 894, # spruce_sign - 铁制字牌
    211: 893, # birch_sign - 石质字牌
    212: 897, # acacia_sign - 熔岩字牌
    213: 892, # cherry_sign - 木质字牌
    214: 895, # jungle_sign - 炽炎字牌
    215: 896, # dark_oak_sign - 钨金字牌
    217: 892, # mangrove_sign - 木质字牌
    218: 892, # bamboo_sign - 木质字牌
    219: 854, # oak_door - 落日橙门
    220: 813, # ladder - 绳索
    222: 529, # cobblestone_stairs - 石质楼梯
    223: 892, # oak_wall_sign - 木质字牌
    224: 894, # spruce_wall_sign - 铁制字牌
    225: 893, # birch_wall_sign - 石质字牌
    226: 897, # acacia_wall_sign - 熔岩字牌
    227: 892, # cherry_wall_sign - 木质字牌
    228: 895, # jungle_wall_sign - 炽炎字牌
    229: 896, # dark_oak_wall_sign - 钨金字牌
    231: 892, # mangrove_wall_sign - 木质字牌
    232: 892, # bamboo_wall_sign - 木质字牌
    233: 892, # oak_hanging_sign - 木质字牌
    234: 894, # spruce_hanging_sign - 铁制字牌
    235: 893, # birch_hanging_sign - 石质字牌
    236: 897, # acacia_hanging_sign - 熔岩字牌
    238: 895, # jungle_hanging_sign - 炽炎字牌
    239: 896, # dark_oak_hanging_sign - 钨金字牌
    257: 363, # lever - 按钮-触碰
    258: 360, # stone_pressure_plate - 感压板-普通
    259: 857, # iron_door - 炽炎门
    260: 359, # oak_pressure_plate - 感压板-触碰
    261: 359, # spruce_pressure_plate - 感压板-触碰
    262: 359, # birch_pressure_plate - 感压板-触碰
    263: 359, # jungle_pressure_plate - 感压板-触碰
    264: 359, # acacia_pressure_plate - 感压板-触碰
    265: 359, # cherry_pressure_plate - 感压板-触碰
    266: 359, # dark_oak_pressure_plate - 感压板-触碰
    268: 359, # mangrove_pressure_plate - 感压板-触碰
    269: 359, # bamboo_pressure_plate - 感压板-触碰
    270: 412, # redstone_ore - 硅石块
    271: 412, # deepslate_redstone_ore - 硅石块
    272: 934, # redstone_torch - 典雅壁灯
    273: 934, # redstone_wall_torch - 典雅壁灯
    274: 364, # stone_button - 按钮-普通
    275: 115, # snow - 松软的雪
    276: 123, # ice - 自然冰
    277: 115, # snow_block - 松软的雪
    278: 242, # cactus - 仙人掌茎
    279: 313, # cactus_flower - 月季
    280: 421, # clay - 土砖
    281: 253, # sugar_cane - 竹笋
    282: 726, # jukebox - 钢琴
    283: 534, # oak_fence - 木围栏
    284: 132, # netherrack - 硫黄晶砂
    285: 109, # soul_sand - 砂土
    286: 109, # soul_soil - 砂土
    287: 104, # basalt - 岩石
    288: 505, # polished_basalt - 碎石块
    289: 934, # soul_torch - 典雅壁灯
    290: 934, # soul_wall_torch - 典雅壁灯
    293: 550, # glowstone - 荧光晶块
    295: 102, # carved_pumpkin - 耕地
    296: 550, # jack_o_lantern - 荧光晶块
    297: 831, # cake - 蔬果披萨
    298: 360, # repeater - 感压板-普通
    299: 633, # white_stained_glass - 玻璃块
    300: 634, # orange_stained_glass - 玻璃块
    301: 635, # magenta_stained_glass - 玻璃块
    302: 636, # light_blue_stained_glass - 玻璃块
    303: 637, # yellow_stained_glass - 玻璃块
    304: 638, # lime_stained_glass - 玻璃块
    305: 639, # pink_stained_glass - 玻璃块
    306: 640, # gray_stained_glass - 玻璃块
    307: 641, # light_gray_stained_glass - 玻璃块
    308: 642, # cyan_stained_glass - 玻璃块
    309: 643, # purple_stained_glass - 玻璃块
    310: 644, # blue_stained_glass - 玻璃块
    311: 645, # brown_stained_glass - 玻璃块
    312: 646, # green_stained_glass - 玻璃块
    313: 647, # red_stained_glass - 玻璃块
    314: 648, # black_stained_glass - 玻璃块
    315: 555, # oak_trapdoor - 木窗
    316: 555, # spruce_trapdoor - 木窗
    317: 555, # birch_trapdoor - 木窗
    318: 555, # jungle_trapdoor - 木窗
    319: 555, # acacia_trapdoor - 木窗
    320: 555, # cherry_trapdoor - 木窗
    321: 555, # dark_oak_trapdoor - 木窗
    323: 555, # mangrove_trapdoor - 木窗
    324: 555, # bamboo_trapdoor - 木窗
    325: 501, # stone_bricks - 精制石砖
    326: 503, # mossy_stone_bricks - 青石砖
    327: 502, # cracked_stone_bricks - 裂纹石砖
    328: 504, # chiseled_stone_bricks - 花纹岩石砖
    329: 421, # packed_mud - 土砖
    337: 270, # brown_mushroom_block - 白色星光孢子块
    338: 270, # red_mushroom_block - 白色星光孢子块
    339: 270, # mushroom_stem - 白色星光孢子块
    340: 526, # iron_bars - 铸铁栅栏
    358: 556, # glass_pane - 玻璃窗
    359: 102, # pumpkin - 耕地
    360: 230, # melon - 巨布鲁果
    363: 229, # pumpkin_stem - 玉米
    364: 243, # melon_stem - 野生玉米
    365: 232, # vine - 气根
    366: 232, # glow_lichen - 气根
    368: 535, # oak_fence_gate - 木围栏门
    369: 530, # brick_stairs - 水泥砖楼梯
    370: 531, # stone_brick_stairs - 精制石楼梯
    372: 101, # mycelium - 土块
    373: 247, # lily_pad - 漂浮的花瓣
    374: 134, # resin_block - 满的蜂巢
    380: 683, # nether_bricks - 龙纹石块
    381: 538, # nether_brick_fence - 硫黄砖围栏
    382: 532, # nether_brick_stairs - 硫黄砖楼梯
    383: 227, # nether_wart - 紫苏
    384: 797, # enchanting_table - 工匠台
    385: 738, # brewing_stand - 陶土罐子
    386: 738, # cauldron - 陶土罐子
    387: 738, # water_cauldron - 陶土罐子
    388: 738, # lava_cauldron - 陶土罐子
    389: 738, # powder_snow_cauldron - 陶土罐子
    391: 116, # end_portal_frame - 萌眼星石块
    392: 116, # end_stone - 萌眼星石块
    393: 740, # dragon_egg - 熔岩之石
    394: 861, # redstone_lamp - 木纹灯
    395: 228, # cocoa - 独葵
    396: 527, # sandstone_stairs - 黄砖楼梯
    397: 409, # emerald_ore - 琥珀块
    398: 409, # deepslate_emerald_ore - 琥珀块
    399: 390048, # ender_chest - [水墨]中式组合柜
    400: 364, # tripwire_hook - 按钮-普通
    401: 232, # tripwire - 气根
    402: 409, # emerald_block - 琥珀块
    403: 523, # spruce_stairs - 海棠红楼梯
    404: 521, # birch_stairs - 秋叶橙楼梯
    405: 520, # jungle_stairs - 楼梯
    406: 10,  # command_block - 星能块
    407: 1060, # beacon - 反射镜
    408: 502, # cobblestone_wall - 裂纹石砖
    409: 503, # mossy_cobblestone_wall - 青石砖
    410: 737, # flower_pot - 简易罐子
    412: 737, # potted_oak_sapling - 简易罐子
    418: 737, # potted_dark_oak_sapling - 简易罐子
    424: 737, # potted_blue_orchid - 简易罐子
    437: 737, # potted_dead_bush - 简易罐子
    439: 236, # carrots - 青瓜
    440: 241, # potatoes - 番薯
    441: 363, # oak_button - 按钮-触碰
    442: 363, # spruce_button - 按钮-触碰
    443: 363, # birch_button - 按钮-触碰
    444: 363, # jungle_button - 按钮-触碰
    445: 363, # acacia_button - 按钮-触碰
    446: 363, # cherry_button - 按钮-触碰
    447: 363, # dark_oak_button - 按钮-触碰
    449: 363, # mangrove_button - 按钮-触碰
    450: 363, # bamboo_button - 按钮-触碰
    465: 797, # anvil - 工匠台
    466: 797, # chipped_anvil - 工匠台
    467: 797, # damaged_anvil - 工匠台
    468: 801, # trapped_chest - 储物箱
    469: 360, # light_weighted_pressure_plate - 感压板-普通
    470: 360, # heavy_weighted_pressure_plate - 感压板-普通
    471: 360, # comparator - 感压板-普通
    472: 731, # daylight_detector - 木质天窗
    473: 412, # redstone_block - 硅石块
    474: 132, # nether_quartz_ore - 硫黄晶砂
    475: 802, # hopper - 冶炼台
    476: 540, # quartz_block - 古老黄砖
    477: 540, # chiseled_quartz_block - 古老黄砖
    478: 540, # quartz_pillar - 古老黄砖
    479: 529, # quartz_stairs - 石质楼梯
    482: 666,  # white_terracotta - 水泥块 (白色)
    483: 667,  # orange_terracotta - 上色水泥块 (橙色)
    484: 668,  # magenta_terracotta - 上色水泥块 (红紫色)
    485: 669,  # light_blue_terracotta - 上色水泥块 (浅蓝色)
    486: 670,  # yellow_terracotta - 上色水泥块 (黄色)
    487: 671,  # lime_terracotta - 上色水泥块 (浅绿色)
    488: 672,  # pink_terracotta - 上色水泥块 (浅红色)
    489: 673,  # gray_terracotta - 上色水泥块 (灰色)
    490: 674,  # light_gray_terracotta - 上色水泥块 (浅灰色)
    491: 675,  # cyan_terracotta - 上色水泥块 (蓝绿色)
    492: 676,  # purple_terracotta - 上色水泥块 (紫色)
    493: 677,  # blue_terracotta - 上色水泥块 (蓝色)
    494: 678,  # brown_terracotta - 上色水泥块 (深红色)
    495: 679,  # green_terracotta - 上色水泥块 (绿色)
    496: 680,  # red_terracotta - 上色水泥块 (红色)
    497: 681,  # black_terracotta - 上色水泥块 (黑色)
    498: 650,  # white_stained_glass_pane - 玻璃片 (白色)
    499: 651,  # orange_stained_glass_pane - 玻璃片 (橙色)
    500: 652,  # magenta_stained_glass_pane - 玻璃片 (红紫色)
    501: 653,  # light_blue_stained_glass_pane - 玻璃片 (浅蓝色)
    502: 654,  # yellow_stained_glass_pane - 玻璃片 (黄色)
    503: 655,  # lime_stained_glass_pane - 玻璃片 (浅绿色)
    504: 656,  # pink_stained_glass_pane - 玻璃片 (浅红色)
    505: 657,  # gray_stained_glass_pane - 玻璃片 (灰色)
    506: 658,  # light_gray_stained_glass_pane - 玻璃片 (浅灰色)
    507: 659,  # cyan_stained_glass_pane - 玻璃片 (蓝绿色)
    508: 660,  # purple_stained_glass_pane - 玻璃片 (紫色)
    509: 661,  # blue_stained_glass_pane - 玻璃片 (蓝色)
    510: 662,  # brown_stained_glass_pane - 玻璃片 (深红色)
    511: 663,  # green_stained_glass_pane - 玻璃片 (绿色)
    512: 664,  # red_stained_glass_pane - 玻璃片 (红色)
    513: 665,  # black_stained_glass_pane - 玻璃片 (黑色)
    514: 524, # acacia_stairs - 落日橙楼梯
    515: 520, # cherry_stairs - 楼梯
    516: 525, # dark_oak_stairs - 深栗红楼梯
    518: 520, # mangrove_stairs - 楼梯
    519: 520, # bamboo_stairs - 楼梯
    521: 412, # slime_block - 硅石块
    524: 526, # iron_trapdoor - 铸铁栅栏
    525: 502, # prismarine - 裂纹石砖
    526: 501, # prismarine_bricks - 精制石砖
    527: 502, # dark_prismarine - 裂纹石砖
    528: 529, # prismarine_stairs - 石质楼梯
    529: 529, # prismarine_brick_stairs - 石质楼梯
    530: 529, # dark_prismarine_stairs - 石质楼梯
    531: 506, # prismarine_slab - 青石薄板
    532: 506, # prismarine_brick_slab - 青石薄板
    533: 506, # dark_prismarine_slab - 青石薄板
    534: 550, # sea_lantern - 荧光晶块
    535: 822, # hay_block - 草垛
    536: 616, # white_carpet - 棉毡
    537: 617, # orange_carpet - 棉毡
    538: 618, # magenta_carpet - 棉毡
    539: 619, # light_blue_carpet - 棉毡
    540: 620, # yellow_carpet - 棉毡
    541: 621, # lime_carpet - 棉毡
    542: 622, # pink_carpet - 棉毡
    543: 623, # gray_carpet - 棉毡
    544: 624, # light_gray_carpet - 棉毡
    545: 625, # cyan_carpet - 棉毡
    546: 626, # purple_carpet - 棉毡
    547: 627, # blue_carpet - 棉毡
    548: 628, # brown_carpet - 棉毡
    549: 629, # green_carpet - 棉毡
    550: 630, # red_carpet - 棉毡
    551: 631, # black_carpet - 棉毡
    552: 424, # terracotta - 精制黄砖
    553: 402, # coal_block - 凝能矿
    554: 131, # packed_ice - 坚固的冰
    555: 312, # sunflower - 黄钟花
    556: 313, # lilac - 月季
    557: 313, # rose_bush - 月季
    558: 313, # peony - 月季
    559: 224, # tall_grass - 小草
    560: 238, # large_fern - 荆棘草
    561: 919,  # white_banner - 红色战旗 (颜色不对但作为旗帜)
    562: 920,  # orange_banner - 蓝色战旗
    563: 921,  # magenta_banner - 绿色战旗
    564: 922,  # light_blue_banner - 黄战旗
    565: 923,  # yellow_banner - 橙色战旗
    566: 924,  # lime_banner - 紫色战旗
    567: 925,  # pink_banner - 白色战旗
    568: 561,  # gray_banner - 白色战旗 (重复)
    577: 925, # white_wall_banner - 白色战旗
    581: 922, # yellow_wall_banner - 黄战旗
    590: 923, # green_wall_banner - 橙色战旗
    593: 108, # red_sandstone - 素纹黄砖
    594: 108, # chiseled_red_sandstone - 素纹黄砖
    595: 108, # cut_red_sandstone - 素纹黄砖
    596: 527, # red_sandstone_stairs - 黄砖楼梯
    597: 514, # oak_slab - 薄板
    598: 517, # spruce_slab - 海棠红薄板
    599: 515, # birch_slab - 秋叶橙薄板
    600: 514, # jungle_slab - 薄板
    601: 518, # acacia_slab - 落日橙薄板
    602: 514, # cherry_slab - 薄板
    603: 519, # dark_oak_slab - 深栗红薄板
    605: 514, # mangrove_slab - 薄板
    606: 514, # bamboo_slab - 薄板
    608: 506, # stone_slab - 青石薄板
    609: 506, # smooth_stone_slab - 青石薄板
    610: 507, # sandstone_slab - 黄砖薄板
    611: 507, # cut_sandstone_slab - 黄砖薄板
    613: 509, # cobblestone_slab - 石质薄板
    614: 510, # brick_slab - 水泥砖薄板
    615: 511, # stone_brick_slab - 精制石薄板
    617: 512, # nether_brick_slab - 硫黄砖薄板
    618: 506, # quartz_slab - 青石薄板
    619: 507, # red_sandstone_slab - 黄砖薄板
    620: 507, # cut_red_sandstone_slab - 黄砖薄板
    621: 112, # purpur_slab - 黑晶石
    622: 505, # smooth_stone - 碎石块
    623: 540, # smooth_sandstone - 古老黄砖
    624: 540, # smooth_quartz - 古老黄砖
    625: 540, # smooth_red_sandstone - 古老黄砖
    626: 535, # spruce_fence_gate - 木围栏门
    627: 535, # birch_fence_gate - 木围栏门
    628: 535, # jungle_fence_gate - 木围栏门
    629: 535, # acacia_fence_gate - 木围栏门
    630: 535, # cherry_fence_gate - 木围栏门
    631: 535, # dark_oak_fence_gate - 木围栏门
    633: 535, # mangrove_fence_gate - 木围栏门
    634: 535, # bamboo_fence_gate - 木围栏门
    635: 539, # spruce_fence - 象牙白围栏
    636: 553, # birch_fence - 薄木围栏
    637: 534, # jungle_fence - 木围栏
    638: 553, # acacia_fence - 薄木围栏
    639: 553, # cherry_fence - 薄木围栏
    640: 539, # dark_oak_fence - 象牙白围栏
    642: 534, # mangrove_fence - 木围栏
    643: 534, # bamboo_fence - 木围栏
    644: 860, # spruce_door - 秋叶橙木门
    645: 856, # birch_door - 象牙白门
    646: 855, # jungle_door - 深栗红门
    647: 854, # acacia_door - 落日橙门
    648: 854, # cherry_door - 落日橙门
    649: 858, # dark_oak_door - 海棠红门
    651: 854, # mangrove_door - 落日橙门
    652: 854, # bamboo_door - 落日橙门
    653: 934, # end_rod - 典雅壁灯
    654: 112, # chorus_plant - 黑晶石
    655: 112, # chorus_flower - 黑晶石
    656: 112, # purpur_block - 黑晶石
    657: 112, # purpur_pillar - 黑晶石
    658: 112, # purpur_stairs - 黑晶石
    659: 116, # end_stone_bricks - 萌眼星石块
    662: 313, # pitcher_plant - 月季
    663: 227, # beetroots - 紫苏
    664: 99,  # dirt_path - 混凝土
    666: 10,  # repeating_command_block - 星能块
    667: 10,  # chain_command_block - 星能块
    668: 123, # frosted_ice - 自然冰
    669: 140, # magma_block - 生命石座
    670: 132, # nether_wart_block - 硫黄晶砂
    671: 683, # red_nether_bricks - 龙纹石块
    672: 447, # bone_block - 神秘化石
    674: 505, # observer - 碎石块
    675: 1180, # shulker_box - 大型储物箱（横）
    676: 1180, # white_shulker_box - 大型储物箱（横）
    677: 1180, # orange_shulker_box - 大型储物箱（横）
    678: 1180, # magenta_shulker_box - 大型储物箱（横）
    679: 1180, # light_blue_shulker_box - 大型储物箱（横）
    680: 1180, # yellow_shulker_box - 大型储物箱（横）
    681: 1180, # lime_shulker_box - 大型储物箱（横）
    682: 1180, # pink_shulker_box - 大型储物箱（横）
    683: 1180, # gray_shulker_box - 大型储物箱（横）
    684: 1180, # light_gray_shulker_box - 大型储物箱（横）
    685: 1180, # cyan_shulker_box - 大型储物箱（横）
    686: 1180, # purple_shulker_box - 大型储物箱（横）
    687: 1180, # blue_shulker_box - 大型储物箱（横）
    688: 1180, # brown_shulker_box - 大型储物箱（横）
    689: 1180, # green_shulker_box - 大型储物箱（横）
    690: 1180, # red_shulker_box - 大型储物箱（横）
    691: 1180, # black_shulker_box - 大型储物箱（横）
    692: 425, # white_glazed_terracotta - 釉面砖
    693: 426, # orange_glazed_terracotta - 横格釉面砖
    694: 427, # magenta_glazed_terracotta - 竖格釉面砖
    695: 428, # light_blue_glazed_terracotta - 四格釉面砖
    696: 429, # yellow_glazed_terracotta - 不规则釉面砖
    697: 425, # lime_glazed_terracotta - 釉面砖
    698: 426, # pink_glazed_terracotta - 横格釉面砖
    699: 427, # gray_glazed_terracotta - 竖格釉面砖
    700: 428, # light_gray_glazed_terracotta - 四格釉面砖
    701: 429, # cyan_glazed_terracotta - 不规则釉面砖
    702: 425, # purple_glazed_terracotta - 釉面砖
    703: 426, # blue_glazed_terracotta - 横格釉面砖
    704: 427, # brown_glazed_terracotta - 竖格釉面砖
    705: 428, # green_glazed_terracotta - 四格釉面砖
    706: 429, # red_glazed_terracotta - 不规则釉面砖
    707: 425, # black_glazed_terracotta - 釉面砖
    708: 667, # white_concrete - 上色水泥块
    709: 668, # orange_concrete - 上色水泥块
    710: 669, # magenta_concrete - 上色水泥块
    711: 670, # light_blue_concrete - 上色水泥块
    712: 671, # yellow_concrete - 上色水泥块
    713: 672, # lime_concrete - 上色水泥块
    714: 673, # pink_concrete - 上色水泥块
    715: 674, # gray_concrete - 上色水泥块
    716: 675, # light_gray_concrete - 上色水泥块
    717: 676, # cyan_concrete - 上色水泥块
    718: 677, # purple_concrete - 上色水泥块
    719: 678, # blue_concrete - 上色水泥块
    720: 679, # brown_concrete - 上色水泥块
    721: 680, # green_concrete - 上色水泥块
    722: 681, # red_concrete - 上色水泥块
    723: 682, # black_concrete - 上色水泥块
    724: 667, # white_concrete_powder - 上色水泥块
    725: 668, # orange_concrete_powder - 上色水泥块
    726: 669, # magenta_concrete_powder - 上色水泥块
    727: 670, # light_blue_concrete_powder - 上色水泥块
    728: 671, # yellow_concrete_powder - 上色水泥块
    729: 672, # lime_concrete_powder - 上色水泥块
    730: 673, # pink_concrete_powder - 上色水泥块
    731: 674, # gray_concrete_powder - 上色水泥块
    732: 675, # light_gray_concrete_powder - 上色水泥块
    733: 676, # cyan_concrete_powder - 上色水泥块
    734: 677, # purple_concrete_powder - 上色水泥块
    735: 678, # blue_concrete_powder - 上色水泥块
    736: 679, # brown_concrete_powder - 上色水泥块
    737: 680, # green_concrete_powder - 上色水泥块
    738: 681, # red_concrete_powder - 上色水泥块
    739: 682, # black_concrete_powder - 上色水泥块
    740: 246, # kelp - 海带
    741: 246, # kelp_plant - 海带
    742: 822, # dried_kelp_block - 草垛
    743: 740, # turtle_egg - 熔岩之石
    744: 740, # sniffer_egg - 熔岩之石
    746: 489, # dead_tube_coral_block - 白化气泡珊瑚
    747: 491, # dead_brain_coral_block - 白化圆盘珊瑚
    748: 489, # dead_bubble_coral_block - 白化气泡珊瑚
    749: 493, # dead_fire_coral_block - 白化树珊瑚
    750: 487, # dead_horn_coral_block - 白化角珊瑚
    751: 488, # tube_coral_block - 气泡珊瑚
    752: 490, # brain_coral_block - 圆盘珊瑚
    753: 488, # bubble_coral_block - 气泡珊瑚
    754: 492, # fire_coral_block - 树珊瑚
    755: 486, # horn_coral_block - 角珊瑚
    756: 489, # dead_tube_coral - 白化气泡珊瑚
    757: 491, # dead_brain_coral - 白化圆盘珊瑚
    758: 489, # dead_bubble_coral - 白化气泡珊瑚
    759: 493, # dead_fire_coral - 白化树珊瑚
    760: 487, # dead_horn_coral - 白化角珊瑚
    761: 488, # tube_coral - 气泡珊瑚
    762: 490, # brain_coral - 圆盘珊瑚
    763: 488, # bubble_coral - 气泡珊瑚
    764: 492, # fire_coral - 树珊瑚
    765: 486, # horn_coral - 角珊瑚
    766: 489, # dead_tube_coral_fan - 白化气泡珊瑚
    767: 491, # dead_brain_coral_fan - 白化圆盘珊瑚
    768: 489, # dead_bubble_coral_fan - 白化气泡珊瑚
    769: 493, # dead_fire_coral_fan - 白化树珊瑚
    770: 487, # dead_horn_coral_fan - 白化角珊瑚
    771: 488, # tube_coral_fan - 气泡珊瑚
    772: 490, # brain_coral_fan - 圆盘珊瑚
    773: 488, # bubble_coral_fan - 气泡珊瑚
    774: 492, # fire_coral_fan - 树珊瑚
    775: 486, # horn_coral_fan - 角珊瑚
    786: 247, # sea_pickle - 漂浮的花瓣
    787: 123, # blue_ice - 自然冰
    788: 550, # conduit - 荧光晶块
    790: 251, # bamboo - 竹子
    795: 529, # polished_granite_stairs - 石质楼梯
    797: 531, # mossy_stone_brick_stairs - 精制石楼梯
    798: 529, # polished_diorite_stairs - 石质楼梯
    800: 116, # end_stone_brick_stairs - 萌眼星石块
    801: 529, # stone_stairs - 石质楼梯
    803: 529, # smooth_quartz_stairs - 石质楼梯
    804: 529, # granite_stairs - 石质楼梯
    805: 529, # andesite_stairs - 石质楼梯
    806: 532, # red_nether_brick_stairs - 硫黄砖楼梯
    807: 529, # polished_andesite_stairs - 石质楼梯
    808: 529, # diorite_stairs - 石质楼梯
    809: 506, # polished_granite_slab - 青石薄板
    810: 507, # smooth_red_sandstone_slab - 黄砖薄板
    811: 511, # mossy_stone_brick_slab - 精制石薄板
    812: 506, # polished_diorite_slab - 青石薄板
    813: 511, # mossy_cobblestone_slab - 精制石薄板
    814: 116, # end_stone_brick_slab - 萌眼星石块
    815: 507, # smooth_sandstone_slab - 黄砖薄板
    816: 506, # smooth_quartz_slab - 青石薄板
    817: 506, # granite_slab - 青石薄板
    818: 506, # andesite_slab - 青石薄板
    819: 512, # red_nether_brick_slab - 硫黄砖薄板
    820: 506, # polished_andesite_slab - 青石薄板
    821: 506, # diorite_slab - 青石薄板
    822: 547, # brick_wall - 水泥砖块
    824: 108, # red_sandstone_wall - 素纹黄砖
    825: 503, # mossy_stone_brick_wall - 青石砖
    826: 502, # granite_wall - 裂纹石砖
    827: 501, # stone_brick_wall - 精制石砖
    829: 683, # nether_brick_wall - 龙纹石块
    830: 502, # andesite_wall - 裂纹石砖
    831: 683, # red_nether_brick_wall - 龙纹石块
    832: 108, # sandstone_wall - 素纹黄砖
    833: 116, # end_stone_brick_wall - 萌眼星石块
    834: 502, # diorite_wall - 裂纹石砖
    835: 813, # scaffolding - 绳索
    836: 797, # loom - 工匠台
    837: 739, # barrel - 彩陶罐子
    838: 799, # smoker - 铜冶炼台
    839: 798, # blast_furnace - 铁冶炼台
    840: 797, # cartography_table - 工匠台
    841: 797, # fletching_table - 工匠台
    842: 802, # grindstone - 冶炼台
    843: 1143, # lectern - 编书台
    844: 797, # smithing_table - 工匠台
    845: 802, # stonecutter - 冶炼台
    846: 931, # bell - 蜡烛台
    847: 899, # lantern - 古典路灯
    848: 907, # soul_lantern - 石荧光菇灯
    857: 1200, # campfire - 篝火
    858: 1200, # soul_campfire - 篝火
    859: 227, # sweet_berry_bush - 紫苏
    860: 683, # warped_stem - 龙纹石块
    861: 683, # stripped_warped_stem - 龙纹石块
    862: 683, # warped_hyphae - 龙纹石块
    863: 683, # stripped_warped_hyphae - 龙纹石块
    864: 132, # warped_nylium - 硫黄晶砂
    865: 465, # warped_fungus - 洋红毒菇
    866: 132, # warped_wart_block - 硫黄晶砂
    867: 238, # warped_roots - 荆棘草
    868: 238, # nether_sprouts - 荆棘草
    869: 683, # crimson_stem - 龙纹石块
    870: 683, # stripped_crimson_stem - 龙纹石块
    871: 683, # crimson_hyphae - 龙纹石块
    872: 683, # stripped_crimson_hyphae - 龙纹石块
    873: 132, # crimson_nylium - 硫黄晶砂
    874: 465, # crimson_fungus - 洋红毒菇
    875: 550, # shroomlight - 荧光晶块
    876: 232, # weeping_vines - 气根
    878: 232, # twisting_vines - 气根
    880: 238, # crimson_roots - 荆棘草
    881: 206, # crimson_planks - 木板
    882: 206, # warped_planks - 木板
    883: 514, # crimson_slab - 薄板
    884: 514, # warped_slab - 薄板
    885: 359, # crimson_pressure_plate - 感压板-触碰
    886: 359, # warped_pressure_plate - 感压板-触碰
    887: 683, # crimson_fence - 龙纹石块
    888: 683, # warped_fence - 龙纹石块
    889: 555, # crimson_trapdoor - 木窗
    890: 555, # warped_trapdoor - 木窗
    891: 535, # crimson_fence_gate - 木围栏门
    892: 535, # warped_fence_gate - 木围栏门
    893: 520, # crimson_stairs - 楼梯
    894: 520, # warped_stairs - 楼梯
    895: 363, # crimson_button - 按钮-触碰
    896: 363, # warped_button - 按钮-触碰
    897: 683, # crimson_door - 龙纹石块
    898: 683, # warped_door - 龙纹石块
    899: 892, # crimson_sign - 木质字牌
    900: 892, # warped_sign - 木质字牌
    901: 892, # crimson_wall_sign - 木质字牌
    902: 892, # warped_wall_sign - 木质字牌
    903: 10,  # structure_block - 星能块
    904: 10,  # jigsaw - 星能块
    907: 821, # composter - 木桩
    908: 822, # target - 草垛
    909: 1019, # bee_nest - 窝
    910: 133, # beehive - 空的蜂巢
    911: 558, # honey_block - 蜂蜜块
    912: 134, # honeycomb_block - 满的蜂巢
    913: 457, # netherite_block - 钛合金块
    914: 457, # ancient_debris - 钛合金块
    915: 962, # crying_obsidian - 白色基石
    916: 140, # respawn_anchor - 生命石座
    921: 410, # lodestone - 炽炎块
    922: 682, # blackstone - 上色水泥块
    923: 529, # blackstone_stairs - 石质楼梯
    924: 682, # blackstone_wall - 上色水泥块
    925: 506, # blackstone_slab - 青石薄板
    926: 505, # polished_blackstone - 碎石块
    927: 501, # polished_blackstone_bricks - 精制石砖
    929: 504, # chiseled_polished_blackstone - 花纹岩石砖
    930: 511, # polished_blackstone_brick_slab - 精制石薄板
    931: 531, # polished_blackstone_brick_stairs - 精制石楼梯
    932: 501, # polished_blackstone_brick_wall - 精制石砖
    933: 682, # gilded_blackstone - 上色水泥块
    934: 529, # polished_blackstone_stairs - 石质楼梯
    935: 506, # polished_blackstone_slab - 青石薄板
    936: 360, # polished_blackstone_pressure_plate - 感压板-普通
    937: 364, # polished_blackstone_button - 按钮-普通
    938: 505, # polished_blackstone_wall - 碎石块
    939: 683, # chiseled_nether_bricks - 龙纹石块
    940: 683, # cracked_nether_bricks - 龙纹石块
    941: 540, # quartz_bricks - 古老黄砖
    947: 931, # yellow_candle - 蜡烛台
    950: 931, # gray_candle - 蜡烛台
    951: 931, # light_gray_candle - 蜡烛台
    955: 931, # brown_candle - 蜡烛台
    957: 931, # red_candle - 蜡烛台
    976: 112, # amethyst_block - 黑晶石
    977: 112, # budding_amethyst - 黑晶石
    978: 112, # amethyst_cluster - 黑晶石
    979: 112, # large_amethyst_bud - 黑晶石
    980: 112, # medium_amethyst_bud - 黑晶石
    981: 112, # small_amethyst_bud - 黑晶石
    982: 104, # tuff - 岩石
    983: 506, # tuff_slab - 青石薄板
    984: 529, # tuff_stairs - 石质楼梯
    985: 502, # tuff_wall - 裂纹石砖
    987: 506, # polished_tuff_slab - 青石薄板
    988: 529, # polished_tuff_stairs - 石质楼梯
    989: 505, # polished_tuff_wall - 碎石块
    992: 511, # tuff_brick_slab - 精制石薄板
    993: 531, # tuff_brick_stairs - 精制石楼梯
    994: 501, # tuff_brick_wall - 精制石砖
    996: 505, # calcite - 碎石块
    997: 1206, # tinted_glass - 透明硬质玻璃块
    998: 115, # powder_snow - 松软的雪
    999: 104, # sculk_sensor - 岩石
    1000: 104, # calibrated_sculk_sensor - 岩石
    1001: 104, # sculk - 岩石
    1002: 232, # sculk_vein - 气根
    1003: 104, # sculk_catalyst - 岩石
    1004: 104, # sculk_shrieker - 岩石
    1005: 456, # copper_block - 黄铜块
    1006: 456, # exposed_copper - 黄铜块
    1007: 456, # weathered_copper - 黄铜块
    1008: 456, # oxidized_copper - 黄铜块
    1009: 456, # copper_ore - 黄铜块
    1010: 456, # deepslate_copper_ore - 黄铜块
    1014: 456, # cut_copper - 黄铜块
    1026: 529, # cut_copper_stairs - 石质楼梯
    1030: 506, # cut_copper_slab - 青石薄板
    1031: 456, # waxed_copper_block - 黄铜块
    1032: 456, # waxed_weathered_copper - 黄铜块
    1033: 456, # waxed_exposed_copper - 黄铜块
    1034: 456, # waxed_oxidized_copper - 黄铜块
    1035: 456, # waxed_oxidized_cut_copper - 黄铜块
    1036: 456, # waxed_weathered_cut_copper - 黄铜块
    1039: 529, # waxed_oxidized_cut_copper_stairs - 石质楼梯
    1040: 529, # waxed_weathered_cut_copper_stairs - 石质楼梯
    1041: 529, # waxed_exposed_cut_copper_stairs - 石质楼梯
    1042: 529, # waxed_cut_copper_stairs - 石质楼梯
    1043: 506, # waxed_oxidized_cut_copper_slab - 青石薄板
    1044: 506, # waxed_weathered_cut_copper_slab - 青石薄板
    1045: 506, # waxed_exposed_cut_copper_slab - 青石薄板
    1046: 506, # waxed_cut_copper_slab - 青石薄板
    1047: 857, # copper_door - 炽炎门
    1048: 857, # exposed_copper_door - 炽炎门
    1049: 857, # oxidized_copper_door - 炽炎门
    1050: 857, # weathered_copper_door - 炽炎门
    1051: 857, # waxed_copper_door - 炽炎门
    1052: 857, # waxed_exposed_copper_door - 炽炎门
    1053: 857, # waxed_oxidized_copper_door - 炽炎门
    1054: 857, # waxed_weathered_copper_door - 炽炎门
    1055: 526, # copper_trapdoor - 铸铁栅栏
    1056: 526, # exposed_copper_trapdoor - 铸铁栅栏
    1057: 526, # oxidized_copper_trapdoor - 铸铁栅栏
    1058: 526, # weathered_copper_trapdoor - 铸铁栅栏
    1059: 526, # waxed_copper_trapdoor - 铸铁栅栏
    1060: 526, # waxed_exposed_copper_trapdoor - 铸铁栅栏
    1061: 526, # waxed_oxidized_copper_trapdoor - 铸铁栅栏
    1062: 526, # waxed_weathered_copper_trapdoor - 铸铁栅栏
    1095: 526, # lightning_rod - 铸铁栅栏
    1104: 104, # dripstone_block - 岩石
    1105: 232, # cave_vines - 气根
    1106: 232, # cave_vines_plant - 气根
    1107: 247, # spore_blossom - 漂浮的花瓣
    1108: 300, # azalea - 风铃花
    1109: 300, # flowering_azalea - 风铃花
    1110: 262, # moss_carpet - 苔藓
    1114: 262, # moss_block - 苔藓
    1115: 247, # big_dripleaf - 漂浮的花瓣
    1116: 247, # big_dripleaf_stem - 漂浮的花瓣
    1117: 247, # small_dripleaf - 漂浮的花瓣
    1118: 232, # hanging_roots - 气根
    1119: 101, # rooted_dirt - 土块
    1120: 101, # mud - 土块
    1121: 104, # deepslate - 岩石
    1122: 502, # cobbled_deepslate - 裂纹石砖
    1123: 529, # cobbled_deepslate_stairs - 石质楼梯
    1124: 509, # cobbled_deepslate_slab - 石质薄板
    1125: 502, # cobbled_deepslate_wall - 裂纹石砖
    1126: 505, # polished_deepslate - 碎石块
    1127: 529, # polished_deepslate_stairs - 石质楼梯
    1128: 509, # polished_deepslate_slab - 石质薄板
    1129: 505, # polished_deepslate_wall - 碎石块
    1130: 501, # deepslate_tiles - 精制石砖
    1131: 531, # deepslate_tile_stairs - 精制石楼梯
    1132: 511, # deepslate_tile_slab - 精制石薄板
    1133: 501, # deepslate_tile_wall - 精制石砖
    1134: 501, # deepslate_bricks - 精制石砖
    1135: 531, # deepslate_brick_stairs - 精制石楼梯
    1136: 511, # deepslate_brick_slab - 精制石薄板
    1137: 501, # deepslate_brick_wall - 精制石砖
    1138: 504, # chiseled_deepslate - 花纹岩石砖
    1139: 502, # cracked_deepslate_bricks - 裂纹石砖
    1140: 502, # cracked_deepslate_tiles - 裂纹石砖
    1142: 505, # smooth_basalt - 碎石块
    1143: 449, # raw_iron_block - 星瞳石块
    1144: 449, # raw_copper_block - 星瞳石块
    1145: 408, # raw_gold_block - 钨金块
    1147: 737, # potted_flowering_azalea_bush - 简易罐子
    1151: 247, # frogspawn - 漂浮的花瓣
    1152: 962, # reinforced_deepslate - 白色基石
    1153: 737, # decorated_pot - 简易罐子
    1154: 802, # crafter - 冶炼台
    1155: 684, # trial_spawner - 斜纹黑石块
    1156: 1180, # vault - 大型储物箱（横）
    1157: 962, # heavy_core - 白色基石
    1162: 301, # closed_eyeblossom - 若兰
}

old_mc_to_mini_mapping = {
    0: 0,  # air - 空气
    1: 104,  # stone - 岩石
    8: 100,  # grass_block - 长草土块
    9: 101,  # dirt - 土块
    12: 105,  # cobblestone - 青石
    13: 206,  # oak_planks - 木板
    14: 201,  # spruce_planks - 落叶松木 (作为木板使用)
    15: 202,  # birch_planks - 白杨木
    16: 203,  # jungle_planks - 红杉木
    17: 204,  # acacia_planks - 楠木
    18: 200,  # cherry_planks - 樱桃木
    19: 211,  # dark_oak_planks - 深栗红木板
    22: 563,  # mangrove_planks - 竹板 (近似)
    23: 563,  # bamboo_planks - 竹板
    34: 1,  # bedrock - 地心基石
    35: 3,  # water - 静态水
    36: 5,  # lava - 静态岩浆
    37: 106,  # sand - 黄沙
    40: 107,  # gravel - 碎石堆
    49: 200,  # oak_log - 樱桃木 (作为原木近似)
    50: 201,  # spruce_log - 落叶松木
    51: 202,  # birch_log - 白杨木
    52: 203,  # jungle_log - 红杉木
    53: 204,  # acacia_log - 楠木
    54: 200,  # cherry_log - 樱桃木
    55: 211,  # dark_oak_log - 深栗红原木
    56: 209,  # pale_oak_log - 海棠红原木 (近似)
    57: 204,  # mangrove_log - 楠木 (近似)
    60: 251,  # bamboo_block - 竹子
    88: 218,  # oak_leaves - 樱桃木树叶
    89: 219,  # spruce_leaves - 落叶松树叶
    90: 220,  # birch_leaves - 白杨树叶
    91: 221,  # jungle_leaves - 红杉树叶
    92: 222,  # acacia_leaves - 楠木树叶
    93: 218,  # cherry_leaves - 樱桃木树叶
    94: 223,  # dark_oak_leaves - 核桃树叶
    99: 127,  # sponge - 泡沫块
    100: 127,  # wet_sponge - 泡沫块
    101: 632,  # glass - 透明玻璃块
    104: 415,  # lapis_block - 星能块 (颜色近似)
    105: 717,  # dispenser - 发射装置
    106: 108,  # sandstone - 素纹黄砖
    109: 690,  # note_block - 低音块
    126: 729,  # powered_rail - 加速轨道节点
    127: 725,  # detector_rail - 轨道节点
    128: 368,  # sticky_piston - 推拉机械臂
    129: 113,  # cobweb - 脆冰 (近似)
    130: 224,  # short_grass - 小草
    131: 224,  # fern - 小草
    132: 225,  # dead_bush - 枯草
    138: 367,  # piston - 机械臂
    140: 600,  # white_wool - 棉花块 (白色)
    141: 601,  # orange_wool - 棉花块 (橙色)
    142: 602,  # magenta_wool - 棉花块 (红紫色)
    143: 603,  # light_blue_wool - 棉花块 (浅蓝色)
    144: 604,  # yellow_wool - 棉花块 (黄色)
    145: 605,  # lime_wool - 棉花块 (浅绿色)
    146: 606,  # pink_wool - 棉花块 (浅红色)
    147: 607,  # gray_wool - 棉花块 (灰色)
    148: 608,  # light_gray_wool - 棉花块 (浅灰色)
    149: 609,  # cyan_wool - 棉花块 (蓝绿色)
    150: 610,  # purple_wool - 棉花块 (紫色)
    151: 611,  # blue_wool - 棉花块 (蓝色)
    152: 612,  # brown_wool - 棉花块 (深红色)
    153: 613,  # green_wool - 棉花块 (绿色)
    154: 614,  # red_wool - 棉花块 (红色)
    155: 615,  # black_wool - 棉花块 (黑色)
    157: 157,  # dandelion - 蒲公英 (ID 157? 实际mini中有蒲公英?)
    159: 159,  # poppy - 罂粟 (近似)
    171: 465,  # brown_mushroom - 洋红毒菇
    172: 465,  # red_mushroom - 洋红毒菇
    173: 174,  # gold_block - 金块 (ID 174 是金块吗？mini中有黄金块)
    174: 411,  # iron_block - 铁块
    175: 425,  # bricks - 釉面砖
    176: 834,  # tnt - 炸药桶
    177: 820,  # bookshelf - 书柜
    192: 112,  # obsidian - 黑晶石
    193: 817,  # torch - 火炬
    194: 817,  # wall_torch - 火炬 (墙挂)
    195: 500,  # fire - 火
    199: 520,  # oak_stairs - 木楼梯
    200: 734,  # chest - 普通宝箱
    205: 797,  # crafting_table - 工匠台
    207: 102,  # farmland - 耕地
    208: 802,  # furnace - 冶炼台
    219: 812,  # oak_door - 轻木门
    220: 813,  # ladder - 绳索
    221: 725,  # rail - 轨道节点
    222: 529,  # cobblestone_stairs - 石质楼梯
    257: 724,  # lever - 开关
    258: 360,  # stone_pressure_plate - 感压板-普通
    259: 814,  # iron_door - 铁门
    260: 359,  # oak_pressure_plate - 感压板-触碰
    274: 716,  # stone_button - 普通按钮
    275: 115,  # snow - 松软的雪
    276: 123,  # ice - 自然冰
    277: 122,  # snow_block - 厚实的雪
    278: 242,  # cactus - 仙人掌茎
    280: 113,  # clay - 脆冰 (黏土近似)
    281: 1468,  # sugar_cane - 甘蔗
    283: 534,  # oak_fence - 木围栏
    284: 284,  # netherrack - 下界岩 (无，保留ID)
    293: 293,  # glowstone - 荧石 (无，保留)
    294: 7,  # nether_portal - 传送光效
    295: 295,  # carved_pumpkin - 大椰子 (南瓜近似)
    296: 296,  # jack_o_lantern - 异化大椰子
    315: 315,  # oak_trapdoor - 木质天窗 (ID 731)
    325: 501,  # stone_bricks - 精制石砖
    340: 526,  # iron_bars - 铸铁栅栏
    358: 649,  # glass_pane - 透明玻璃片
    359: 295,  # pumpkin - 大椰子
    360: 200116,  # melon - 西瓜 (使用丰硕西瓜)
    365: 365,  # vine - 藤蔓 (无)
    368: 535,  # oak_fence_gate - 木围栏门
    370: 531,  # stone_brick_stairs - 精制石楼梯
    372: 464,  # mycelium - 菌丝体
    373: 250,  # lily_pad - 荷花
    379: 379,  # chiseled_resin_bricks - 树脂砖 (无)
    380: 380,  # nether_bricks - 地狱砖 (无)
    382: 382,  # nether_brick_stairs - 地狱砖楼梯
    384: 384,  # enchanting_table - 附魔台 (无)
    385: 385,  # brewing_stand - 酿造台 (无)
    386: 386,  # cauldron - 炼药锅 (无)
    393: 819,  # dragon_egg - 黑龙蛋
    394: 707,  # redstone_lamp - 星能信号灯
    396: 527,  # sandstone_stairs - 黄砖楼梯
    399: 399,  # ender_chest - 末影箱 (无)
    402: 173,  # emerald_block - 绿宝石块 (无，用ID173)
    407: 407,  # beacon - 信标 (无)
    408: 548,  # cobblestone_wall - 碎石墙
    409: 549,  # mossy_cobblestone_wall - 青石墙
    410: 928,  # flower_pot - 小花盆
    436: 436,  # potted_brown_mushroom - 花盆蘑菇
    441: 715,  # oak_button - 触碰按钮
    451: 451,  # skeleton_skull - 骷髅头 (无)
    465: 855,  # anvil - 铁砧 (无)
    468: 811,  # trapped_chest - 陷阱箱
    469: 469,  # light_weighted_pressure_plate - 轻质感压板
    470: 470,  # heavy_weighted_pressure_plate - 重质感压板
    471: 374,  # comparator - 星能比较器
    472: 472,  # daylight_detector - 光照感应器 (ID 1169)
    473: 415,  # redstone_block - 星能块
    474: 406,  # nether_quartz_ore - 琥珀原石
    475: 475,  # hopper - 漏斗 (无)
    476: 406,  # quartz_block - 琥珀块
    479: 479,  # quartz_stairs - 石英楼梯 (无)
    480: 480,  # activator_rail - 激活铁轨 (无)
    481: 720,  # dropper - 投掷发射装置
    482: 666,  # white_terracotta - 水泥块 (白色)
    483: 667,  # orange_terracotta - 上色水泥块 (橙色)
    484: 668,  # magenta_terracotta - 上色水泥块 (红紫色)
    485: 669,  # light_blue_terracotta - 上色水泥块 (浅蓝色)
    486: 670,  # yellow_terracotta - 上色水泥块 (黄色)
    487: 671,  # lime_terracotta - 上色水泥块 (浅绿色)
    488: 672,  # pink_terracotta - 上色水泥块 (浅红色)
    489: 673,  # gray_terracotta - 上色水泥块 (灰色)
    490: 674,  # light_gray_terracotta - 上色水泥块 (浅灰色)
    491: 675,  # cyan_terracotta - 上色水泥块 (蓝绿色)
    492: 676,  # purple_terracotta - 上色水泥块 (紫色)
    493: 677,  # blue_terracotta - 上色水泥块 (蓝色)
    494: 678,  # brown_terracotta - 上色水泥块 (深红色)
    495: 679,  # green_terracotta - 上色水泥块 (绿色)
    496: 680,  # red_terracotta - 上色水泥块 (红色)
    497: 681,  # black_terracotta - 上色水泥块 (黑色)
    498: 650,  # white_stained_glass_pane - 玻璃片 (白色)
    499: 651,  # orange_stained_glass_pane - 玻璃片 (橙色)
    500: 652,  # magenta_stained_glass_pane - 玻璃片 (红紫色)
    501: 653,  # light_blue_stained_glass_pane - 玻璃片 (浅蓝色)
    502: 654,  # yellow_stained_glass_pane - 玻璃片 (黄色)
    503: 655,  # lime_stained_glass_pane - 玻璃片 (浅绿色)
    504: 656,  # pink_stained_glass_pane - 玻璃片 (浅红色)
    505: 657,  # gray_stained_glass_pane - 玻璃片 (灰色)
    506: 658,  # light_gray_stained_glass_pane - 玻璃片 (浅灰色)
    507: 659,  # cyan_stained_glass_pane - 玻璃片 (蓝绿色)
    508: 660,  # purple_stained_glass_pane - 玻璃片 (紫色)
    509: 661,  # blue_stained_glass_pane - 玻璃片 (蓝色)
    510: 662,  # brown_stained_glass_pane - 玻璃片 (深红色)
    511: 663,  # green_stained_glass_pane - 玻璃片 (绿色)
    512: 664,  # red_stained_glass_pane - 玻璃片 (红色)
    513: 665,  # black_stained_glass_pane - 玻璃片 (黑色)
    514: 514,  # acacia_stairs - 金合欢楼梯 (无)
    521: 521,  # slime_block - 粘液块 (无)
    522: 522,  # barrier - 屏障 (无)
    523: 523,  # light - 光 (无)
    524: 524,  # iron_trapdoor - 铁活板门 (无)
    525: 525,  # prismarine - 海晶石 (无)
    534: 534,  # sea_lantern - 海晶灯 (无)
    535: 822,  # hay_block - 草垛
    536: 616,  # white_carpet - 棉毡 (白色)
    537: 617,  # orange_carpet - 棉毡 (橙色)
    538: 618,  # magenta_carpet - 棉毡 (红紫色)
    539: 619,  # light_blue_carpet - 棉毡 (浅蓝色)
    540: 620,  # yellow_carpet - 棉毡 (黄色)
    541: 621,  # lime_carpet - 棉毡 (浅绿色)
    542: 622,  # pink_carpet - 棉毡 (浅红色)
    543: 623,  # gray_carpet - 棉毡 (灰色)
    544: 624,  # light_gray_carpet - 棉毡 (浅灰色)
    545: 625,  # cyan_carpet - 棉毡 (蓝绿色)
    546: 626,  # purple_carpet - 棉毡 (紫色)
    547: 627,  # blue_carpet - 棉毡 (蓝色)
    548: 628,  # brown_carpet - 棉毡 (深红色)
    549: 629,  # green_carpet - 棉毡 (绿色)
    550: 630,  # red_carpet - 棉毡 (红色)
    551: 631,  # black_carpet - 棉毡 (黑色)
    552: 114,  # terracotta - 淤泥 (陶瓦近似)
    553: 553,  # coal_block - 煤炭块 (无)
    554: 554,  # packed_ice - 浮冰 (无)
    561: 919,  # white_banner - 红色战旗 (颜色不对但作为旗帜)
    562: 920,  # orange_banner - 蓝色战旗
    563: 921,  # magenta_banner - 绿色战旗
    564: 922,  # light_blue_banner - 黄战旗
    565: 923,  # yellow_banner - 橙色战旗
    566: 924,  # lime_banner - 紫色战旗
    567: 925,  # pink_banner - 白色战旗
    568: 561,  # gray_banner - 白色战旗 (重复)
    597: 514,  # oak_slab - 薄板
    608: 509,  # stone_slab - 石质薄板
    613: 506,  # cobblestone_slab - 青石薄板
    626: 535,  # spruce_fence_gate - 木围栏门
    635: 534,  # spruce_fence - 木围栏
    644: 812,  # spruce_door - 轻木门
    653: 653,  # end_rod - 末地烛 (无)
    654: 654,  # chorus_plant - 紫颂植物 (无)
    656: 656,  # purpur_block - 紫珀块 (无)
    664: 664,  # dirt_path - 土径 (无)
    669: 669,  # magma_block - 岩浆块 (无)
    670: 670,  # nether_wart_block - 地狱疣块 (无)
    672: 672,  # bone_block - 骨块 (无)
    674: 674,  # observer - 观察者 (无)
    675: 675,  # shulker_box - 潜影盒 (无)
    708: 666,  # white_concrete - 水泥块
    709: 667,  # orange_concrete - 上色水泥块
    724: 724,  # white_concrete_powder - 水泥粉末 (无)
    740: 246,  # kelp - 海带
    742: 742,  # dried_kelp_block - 干海带块 (无)
    743: 743,  # turtle_egg - 海龟蛋 (无)
    751: 751,  # tube_coral_block - 管珊瑚块 (无)
    786: 786,  # sea_pickle - 海泡菜 (无)
    787: 787,  # blue_ice - 蓝冰 (无)
    788: 788,  # conduit - 潮涌核心 (无)
    789: 789,  # bamboo_sapling - 竹笋 (ID 253)
    790: 251,  # bamboo - 竹子
    791: 791,  # potted_bamboo - 盆栽竹子 (无)
    794: 794,  # bubble_column - 气泡柱 (无)
    800: 800,  # end_stone_brick_stairs - 末地石砖楼梯 (无)
    809: 809,  # polished_granite_slab - 抛光花岗岩台阶 (无)
    817: 817,  # torch - 火炬
    818: 818,  # soul_torch - 灵魂火炬 (无)
    819: 819,  # copper_torch - 铜火炬 (无)
    825: 825,  # mossy_stone_brick_wall - 苔石砖墙 (无)
    826: 826,  # granite_wall - 花岗岩墙 (无)
    835: 835,  # scaffolding - 脚手架 (无)
    836: 836,  # loom - 织布机 (无)
    837: 837,  # barrel - 桶 (无)
    838: 838,  # smoker - 烟熏炉 (无)
    839: 839,  # blast_furnace - 高炉 (无)
    840: 840,  # cartography_table - 制图台 (无)
    841: 841,  # fletching_table - 制箭台 (无)
    842: 842,  # grindstone - 磨石 (无)
    843: 843,  # lectern - 讲台 (课桌 ID 390000)
    844: 844,  # smithing_table - 锻造台 (无)
    845: 845,  # stonecutter - 切石机 (无)
    846: 846,  # bell - 钟 (无)
    847: 898,  # lantern - 灯笼
    848: 848,  # soul_lantern - 灵魂灯笼 (无)
    857: 1200,  # campfire - 篝火
    858: 858,  # soul_campfire - 灵魂篝火 (无)
    859: 859,  # sweet_berry_bush - 甜浆果丛 (无)
    860: 860,  # warped_stem - 诡异菌柄 (无)
    869: 869,  # crimson_stem - 绯红菌柄 (无)
    881: 881,  # crimson_planks - 绯红木板 (无)
    882: 882,  # warped_planks - 诡异木板 (无)
    907: 907,  # composter - 堆肥桶 (无)
    908: 908,  # target - 标靶 (无)
    909: 909,  # bee_nest - 蜂巢 (空蜂巢 ID 133)
    910: 134,  # beehive - 蜂箱 (满的蜂巢)
    911: 558,  # honey_block - 蜂蜜块
    912: 912,  # honeycomb_block - 蜜脾块 (无)
    913: 913,  # netherite_block - 下界合金块 (无)
    914: 914,  # ancient_debris - 远古残骸 (无)
    915: 915,  # crying_obsidian - 哭泣的黑曜石 (无)
    916: 916,  # respawn_anchor - 重生锚 (无)
    921: 921,  # lodestone - 磁石 (无)
    922: 922,  # blackstone - 黑石 (无)
    976: 976,  # amethyst_block - 紫水晶块 (无)
    977: 977,  # budding_amethyst - 紫水晶母岩 (无)
    978: 978,  # amethyst_cluster - 紫水晶簇 (无)
    982: 982,  # tuff - 凝灰岩 (无)
    996: 996,  # calcite - 方解石 (无)
    997: 997,  # tinted_glass - 遮光玻璃 (无)
    998: 998,  # powder_snow - 细雪 (无)
    999: 999,  # sculk_sensor - 潜声传感器 (无)
    1005: 1005,  # copper_block - 铜块 (无)
    1009: 1009,  # copper_ore - 铜矿 (ID 451 铜矿)
    1010: 451,  # deepslate_copper_ore - 深层铜矿 (铜矿)
    1103: 1103,  # pointed_dripstone - 滴水石锥 (无)
    1104: 1104,  # dripstone_block - 滴水石块 (无)
    1105: 1105,  # cave_vines - 洞穴藤蔓 (无)
    1108: 1108,  # azalea - 杜鹃花 (无)
    1114: 1114,  # moss_block - 苔藓块 (ID 262 苔藓)
    1120: 1120,  # mud - 泥巴
    1121: 1121,  # deepslate - 深板岩 (无)
    1122: 1122,  # cobbled_deepslate - 深板岩圆石 (无)
    1142: 1142,  # smooth_basalt - 平滑玄武岩 (无)
    1143: 1143,  # raw_iron_block - 粗铁块 (无)
    1144: 1144,  # raw_copper_block - 粗铜块 (无)
    1145: 1145,  # raw_gold_block - 粗金块 (无)
    1148: 1148,  # ochre_froglight - 赭黄蛙光体 (无)
    1152: 1152,  # reinforced_deepslate - 强化深板岩 (无)
    1153: 1153,  # decorated_pot - 饰纹陶罐 (无)
    1154: 1154,  # crafter - 合成器 (无)
    1155: 1155,  # trial_spawner - 试炼刷怪笼 (无)
    1156: 1156,  # vault -  vault (无)
    1157: 1157,  # heavy_core - 重核 (无)
    1158: 1158,  # pale_moss_block - 苍白苔藓块 (无)
    1165: 1165,  # firefly_bush - 萤火虫丛 (无)
}

mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items()}


def mc_to_mini(id: int) -> int:
    if id in mc_to_mini_mapping:
        return mc_to_mini_mapping[id]
    else:
        return 470  # 问号方块


def mini_to_mc(id: int) -> int:
    if id in mini_to_mc_mapping:
        return mini_to_mc_mapping[id]
    else:
        return 9  # 土块
