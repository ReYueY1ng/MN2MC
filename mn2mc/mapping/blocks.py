# MC id: Mini id
mc_to_mini_mapping = {
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
