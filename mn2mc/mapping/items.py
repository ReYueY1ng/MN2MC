mc_to_mini_mapping = {
    0: 0,  # Air - 空气
    1: 104,  # Stone - 岩石
    2: 104,  # Granite - 岩石 (无直接对应)
    4: 104,  # Diorite - 岩石
    6: 104,  # Andesite - 岩石
    8: 104,  # Deepslate - 岩石
    9: 104,  # Cobbled Deepslate - 岩石
    27: 100,  # Grass Block - 长草土块
    28: 101,  # Dirt - 土块
    29: 101,  # Coarse Dirt - 土块
    30: 101,  # Podzol - 土块
    31: 101,  # Rooted Dirt - 土块
    32: 32,  # Mud - 淤泥 (114号是淤泥，但32号泥更接近)
    35: 104,  # Cobblestone - 岩石
    36: 206,  # Oak Planks - 木板
    37: 206,  # Spruce Planks - 木板
    38: 206,  # Birch Planks - 木板
    39: 206,  # Jungle Planks - 木板
    40: 206,  # Acacia Planks - 木板
    41: 206,  # Cherry Planks - 木板
    42: 206,  # Dark Oak Planks - 木板
    44: 206,  # Mangrove Planks - 木板
    45: 206,  # Bamboo Planks - 木板
    46: 206,  # Crimson Planks - 木板
    47: 206,  # Warped Planks - 木板
    48: 206,  # Bamboo Mosaic - 木板
    49: 62022,  # Oak Sapling - 落叶松树苗
    50: 62022,  # Spruce Sapling - 落叶松树苗
    51: 62022,  # Birch Sapling - 落叶松树苗
    52: 62022,  # Jungle Sapling - 落叶松树苗
    53: 62022,  # Acacia Sapling - 落叶松树苗
    54: 62022,  # Cherry Sapling - 落叶松树苗
    55: 62022,  # Dark Oak Sapling - 落叶松树苗
    56: 62022,  # Pale Oak Sapling - 落叶松树苗
    57: 62022,  # Mangrove Propagule - 落叶松树苗
    58: 0,  # Bedrock - 无对应，占位
    59: 29,  # Sand - 黄沙
    60: 29,  # Suspicious Sand - 黄沙
    61: 107,  # Suspicious Gravel - 碎石堆
    62: 128,  # Red Sand - 红沙
    63: 107,  # Gravel - 碎石堆
    64: 0,  # Coal Ore - 无对应
    66: 0,  # Iron Ore - 无对应
    68: 0,  # Copper Ore - 无对应
    70: 0,  # Gold Ore - 无对应
    72: 0,  # Redstone Ore - 无对应
    74: 0,  # Emerald Ore - 无对应
    76: 0,  # Lapis Ore - 无对应
    78: 0,  # Diamond Ore - 无对应
    80: 0,  # Nether Gold Ore - 无对应
    81: 0,  # Nether Quartz Ore - 无对应
    82: 0,  # Ancient Debris - 无对应
    83: 0,  # Coal Block - 无对应
    87: 0,  # Heavy Core - 无对应
    88: 0,  # Amethyst Block - 无对应
    90: 411,  # Iron Block - 铁块
    91: 456,  # Copper Block - 黄铜块
    92: 0,  # Gold Block - 无对应
    93: 0,  # Diamond Block - 无对应
    94: 0,  # Netherite Block - 无对应
    134: 477,  # Oak Log - 胡杨木
    135: 477,  # Spruce Log - 胡杨木
    136: 477,  # Birch Log - 胡杨木
    137: 477,  # Jungle Log - 胡杨木
    138: 477,  # Acacia Log - 胡杨木
    139: 477,  # Cherry Log - 胡杨木
    141: 477,  # Dark Oak Log - 胡杨木
    142: 477,  # Mangrove Log - 胡杨木
    143: 477,  # Mangrove Roots - 胡杨木
    145: 477,  # Crimson Stem - 胡杨木
    146: 477,  # Warped Stem - 胡杨木
    147: 477,  # Bamboo Block - 胡杨木
    182: 219,  # Oak Leaves - 落叶松树叶
    183: 219,  # Spruce Leaves - 落叶松树叶
    184: 219,  # Birch Leaves - 落叶松树叶
    185: 219,  # Jungle Leaves - 落叶松树叶
    186: 219,  # Acacia Leaves - 落叶松树叶
    187: 219,  # Cherry Leaves - 落叶松树叶
    188: 219,  # Dark Oak Leaves - 落叶松树叶
    190: 219,  # Mangrove Leaves - 落叶松树叶
    193: 127,  # Sponge - 泡沫块
    194: 127,  # Wet Sponge - 泡沫块
    195: 632,  # Glass - 透明玻璃块
    196: 632,  # Tinted Glass - 透明玻璃块
    197: 0,  # Lapis Block - 无对应
    198: 108,  # Sandstone - 素纹黄砖
    199: 108,  # Chiseled Sandstone - 素纹黄砖
    200: 108,  # Cut Sandstone - 素纹黄砖
    201: 0,  # Cobweb - 无对应
    202: 224,  # Short Grass - 小草
    203: 224,  # Fern - 小草
    204: 224,  # Bush - 小草
    205: 205,  # Azalea - 杜鹃花 (未直接对应)
    207: 225,  # Dead Bush - 枯草
    213: 600,  # White Wool - 棉花块(白色)
    214: 601,  # Orange Wool - 棉花块(橙色)
    215: 602,  # Magenta Wool - 棉花块(红紫)
    216: 603,  # Light Blue Wool - 棉花块(浅蓝)
    217: 604,  # Yellow Wool - 棉花块(黄色)
    218: 605,  # Lime Wool - 棉花块(浅绿)
    219: 606,  # Pink Wool - 棉花块(浅红)
    220: 607,  # Gray Wool - 棉花块(灰色)
    221: 608,  # Light Gray Wool - 棉花块(浅灰)
    222: 609,  # Cyan Wool - 棉花块(蓝绿)
    223: 610,  # Purple Wool - 棉花块(紫色)
    224: 611,  # Blue Wool - 棉花块(蓝色)
    225: 612,  # Brown Wool - 棉花块(深红)
    226: 613,  # Green Wool - 棉花块(绿色)
    227: 614,  # Red Wool - 棉花块(红色)
    228: 615,  # Black Wool - 棉花块(黑色)
    229: 62001,  # Dandelion - 向阳花种子
    232: 62002,  # Poppy - 红色忘忧草种子
    233: 62032,  # Blue Orchid - 胡萝卜种子(占位)
    234: 62002,  # Allium - 红色忘忧草种子
    235: 62005,  # Azure Bluet - 小白菊种子
    236: 62002,  # Red Tulip - 红色忘忧草种子
    237: 62033,  # Orange Tulip - 橙色忘忧草种子
    238: 62034,  # White Tulip - 灰色忘忧草种子
    239: 62035,  # Pink Tulip - 粉色忘忧草种子
    240: 62005,  # Oxeye Daisy - 小白菊种子
    241: 62005,  # Cornflower - 小白菊种子
    242: 62005,  # Lily of the Valley - 小白菊种子
    243: 62005,  # Wither Rose - 小白菊种子
    244: 0,  # Torchflower - 无对应
    245: 0,  # Pitcher Plant - 无对应
    246: 0,  # Spore Blossom - 无对应
    247: 62027,  # Brown Mushroom - 小蘑菇种子
    248: 62028,  # Red Mushroom - 小红菇种子
    249: 62028,  # Crimson Fungus - 小红菇种子
    250: 62027,  # Warped Fungus - 小蘑菇种子
    251: 62027,  # Crimson Roots - 小蘑菇种子
    252: 62027,  # Warped Roots - 小蘑菇种子
    253: 62027,  # Nether Sprouts - 小蘑菇种子
    256: 62017,  # Sugar Cane - 甘蔗种子
    257: 62017,  # Kelp - 甘蔗种子
    259: 62002,  # Wildflowers - 红色忘忧草种子
    261: 397,  # Moss Carpet - 苔藓
    262: 397,  # Moss Block - 苔藓
    269: 251,  # Bamboo - 竹子
    270: 514,  # Oak Slab - 薄板
    271: 514,  # Spruce Slab - 薄板
    272: 514,  # Birch Slab - 薄板
    273: 514,  # Jungle Slab - 薄板
    274: 514,  # Acacia Slab - 薄板
    275: 514,  # Cherry Slab - 薄板
    276: 514,  # Dark Oak Slab - 薄板
    278: 514,  # Mangrove Slab - 薄板
    279: 514,  # Bamboo Slab - 薄板
    281: 514,  # Crimson Slab - 薄板
    282: 514,  # Warped Slab - 薄板
    283: 509,  # Stone Slab - 石质薄板
    284: 509,  # Smooth Stone Slab - 石质薄板
    285: 507,  # Sandstone Slab - 黄砖薄板
    286: 507,  # Cut Sandstone Slab - 黄砖薄板
    288: 509,  # Cobblestone Slab - 石质薄板
    289: 0,  # Brick Slab - 无对应
    290: 511,  # Stone Brick Slab - 精制石薄板
    292: 0,  # Nether Brick Slab - 无对应
    293: 0,  # Quartz Slab - 无对应
    294: 0,  # Red Sandstone Slab - 无对应
    296: 0,  # Purpur Slab - 无对应
    297: 0,  # Prismarine Slab - 无对应
    304: 304,  # Bricks - 砖块 (未直接对应，保留)
    317: 820,  # Bookshelf - 书柜
    319: 0,  # Decorated Pot - 无对应
    320: 320,  # Mossy Cobblestone - 苔石 (未直接对应)
    321: 0,  # Obsidian - 无对应
    322: 817,  # Torch - 火炬
    323: 0,  # End Rod - 无对应
    324: 0,  # Chorus Plant - 无对应
    325: 0,  # Chorus Flower - 无对应
    326: 0,  # Purpur Block - 无对应
    328: 0,  # Purpur Stairs - 无对应
    329: 0,  # Spawner - 无对应
    331: 734,  # Chest - 普通宝箱
    332: 0,  # Crafting Table - 无对应
    333: 102,  # Farmland - 耕地
    334: 802,  # Furnace - 冶炼台
    335: 813,  # Ladder - 绳索(梯子)
    336: 529,  # Cobblestone Stairs - 石质楼梯
    337: 115,  # Snow - 松软的雪
    338: 123,  # Ice - 自然冰
    339: 122,  # Snow Block - 厚实的雪
    340: 242,  # Cactus - 仙人掌茎
    342: 342,  # Clay - 粘土 (未直接对应)
    344: 534,  # Oak Fence - 木围栏
    345: 534,  # Spruce Fence - 木围栏
    346: 534,  # Birch Fence - 木围栏
    347: 534,  # Jungle Fence - 木围栏
    348: 534,  # Acacia Fence - 木围栏
    349: 534,  # Cherry Fence - 木围栏
    350: 534,  # Dark Oak Fence - 木围栏
    352: 534,  # Mangrove Fence - 木围栏
    353: 568,  # Bamboo Fence - 竹围栏
    354: 534,  # Crimson Fence - 木围栏
    355: 534,  # Warped Fence - 木围栏
    356: 356,  # Pumpkin - 南瓜 (未直接对应)
    357: 356,  # Carved Pumpkin - 南瓜
    358: 358,  # Jack o'Lantern - 南瓜灯 (未直接对应)
    359: 359,  # Netherrack - 地狱岩 (未直接对应)
    360: 360,  # Soul Sand - 灵魂沙 (未直接对应)
    362: 362,  # Basalt - 玄武岩 (未直接对应)
    364: 364,  # Smooth Basalt - 平滑玄武岩
    367: 367,  # Glowstone - 荧石
    375: 375,  # Stone Bricks - 石砖
    376: 376,  # Mossy Stone Bricks - 苔石砖
    377: 377,  # Cracked Stone Bricks - 裂石砖
    378: 378,  # Chiseled Stone Bricks - 雕纹石砖
    379: 379,  # Packed Mud - 泥坯
    380: 380,  # Mud Bricks - 泥砖
    381: 381,  # Deepslate Bricks - 深板岩砖
    382: 382,  # Cracked Deepslate Bricks - 裂深板岩砖
    383: 383,  # Deepslate Tiles - 深板岩瓦
    384: 384,  # Cracked Deepslate Tiles - 裂深板岩瓦
    385: 385,  # Chiseled Deepslate - 雕纹深板岩
    386: 386,  # Reinforced Deepslate - 强化深板岩
    390: 526,  # Iron Bars - 铸铁栅栏
    399: 399,  # Iron Chain - 锁链
    408: 649,  # Glass Pane - 透明玻璃片
    409: 200115,  # Melon - 西瓜
    410: 410,  # Vine - 藤蔓
    411: 411,  # Glow Lichen - 发光地衣
    419: 530,  # Brick Stairs - 砖楼梯 (未直接对应)
    420: 531,  # Stone Brick Stairs - 精制石楼梯
    422: 422,  # Mycelium - 菌丝体
    423: 423,  # Lily Pad - 荷叶
    424: 424,  # Nether Bricks - 地狱砖
    426: 426,  # Chiseled Nether Bricks - 雕纹地狱砖
    427: 427,  # Nether Brick Fence - 地狱砖栅栏
    428: 428,  # Nether Brick Stairs - 地狱砖楼梯
    429: 429,  # Sculk - 幽匿块
    431: 431,  # Sculk Catalyst - 幽匿催发体
    432: 432,  # Sculk Shrieker - 幽匿尖啸体
    433: 433,  # Enchanting Table - 附魔台
    434: 434,  # End Portal Frame - 末地传送门框架
    435: 435,  # End Stone - 末地石
    436: 436,  # End Stone Bricks - 末地石砖
    437: 437,  # Dragon Egg - 龙蛋
    438: 438,  # Sandstone Stairs - 黄砖楼梯
    439: 439,  # Ender Chest - 末影箱
    440: 440,  # Emerald Block - 绿宝石块
    441: 520,  # Oak Stairs - 楼梯
    442: 520,  # Spruce Stairs - 楼梯
    443: 520,  # Birch Stairs - 楼梯
    444: 520,  # Jungle Stairs - 楼梯
    445: 520,  # Acacia Stairs - 楼梯
    446: 520,  # Cherry Stairs - 楼梯
    447: 520,  # Dark Oak Stairs - 楼梯
    449: 520,  # Mangrove Stairs - 楼梯
    450: 567,  # Bamboo Stairs - 竹板楼梯
    452: 520,  # Crimson Stairs - 楼梯
    453: 520,  # Warped Stairs - 楼梯
    454: 454,  # Command Block - 命令方块
    455: 455,  # Beacon - 信标
    456: 548,  # Cobblestone Wall - 碎石墙
    457: 549,  # Mossy Cobblestone Wall - 青石墙
    458: 0,  # Brick Wall - 无对应
    459: 0,  # Prismarine Wall - 无对应
    460: 0,  # Red Sandstone Wall - 无对应
    461: 549,  # Mossy Stone Brick Wall - 青石墙
    462: 462,  # Granite Wall - 花岗岩墙
    463: 551,  # Stone Brick Wall - 粗制石砖围栏
    466: 466,  # Andesite Wall - 安山岩墙
    470: 470,  # Diorite Wall - 闪长岩墙
    471: 471,  # Blackstone Wall - 黑石墙
    472: 472,  # Polished Blackstone Wall - 磨制黑石墙
    473: 473,  # Polished Blackstone Brick Wall - 磨制黑石砖墙
    474: 474,  # Cobbled Deepslate Wall - 深板岩圆石墙
    475: 475,  # Polished Deepslate Wall - 磨制深板岩墙
    476: 476,  # Deepslate Brick Wall - 深板岩砖墙
    477: 477,  # Deepslate Tile Wall - 深板岩瓦墙
    478: 478,  # Anvil - 铁砧
    479: 479,  # Chipped Anvil - 开裂铁砧
    480: 480,  # Damaged Anvil - 损坏铁砧
    481: 481,  # Chiseled Quartz Block - 雕纹石英块
    482: 482,  # Quartz Block - 石英块
    483: 483,  # Quartz Bricks - 石英砖
    484: 484,  # Quartz Pillar - 石英柱
    485: 485,  # Quartz Stairs - 石英楼梯
    486: 486,  # White Terracotta - 白色陶瓦
    487: 487,  # Orange Terracotta - 橙色陶瓦
    488: 488,  # Magenta Terracotta - 品红陶瓦
    489: 489,  # Light Blue Terracotta - 浅蓝陶瓦
    490: 490,  # Yellow Terracotta - 黄色陶瓦
    491: 491,  # Lime Terracotta - 黄绿陶瓦
    492: 492,  # Pink Terracotta - 粉色陶瓦
    493: 493,  # Gray Terracotta - 灰色陶瓦
    494: 494,  # Light Gray Terracotta - 浅灰陶瓦
    495: 495,  # Cyan Terracotta - 青色陶瓦
    496: 496,  # Purple Terracotta - 紫色陶瓦
    497: 497,  # Blue Terracotta - 蓝色陶瓦
    498: 498,  # Brown Terracotta - 棕色陶瓦
    499: 499,  # Green Terracotta - 绿色陶瓦
    500: 500,  # Red Terracotta - 红色陶瓦
    501: 501,  # Black Terracotta - 黑色陶瓦
    502: 502,  # Barrier - 屏障
    504: 504,  # Hay Block - 干草块
    505: 616,  # White Carpet - 白棉毡
    506: 617,  # Orange Carpet - 橙棉毡
    507: 618,  # Magenta Carpet - 红紫棉毡
    508: 619,  # Light Blue Carpet - 浅蓝棉毡
    509: 620,  # Yellow Carpet - 黄棉毡
    510: 621,  # Lime Carpet - 浅绿棉毡
    511: 622,  # Pink Carpet - 浅红棉毡
    512: 623,  # Gray Carpet - 灰棉毡
    513: 624,  # Light Gray Carpet - 浅灰棉毡
    514: 625,  # Cyan Carpet - 蓝绿棉毡
    515: 626,  # Purple Carpet - 紫棉毡
    516: 627,  # Blue Carpet - 蓝棉毡
    517: 628,  # Brown Carpet - 深红棉毡
    518: 629,  # Green Carpet - 绿棉毡
    519: 630,  # Red Carpet - 红棉毡
    520: 631,  # Black Carpet - 黑棉毡
    521: 521,  # Terracotta - 陶瓦
    522: 522,  # Packed Ice - 浮冰
    523: 523,  # Dirt Path - 土径
    524: 524,  # Sunflower - 向日葵
    525: 525,  # Lilac - 丁香
    526: 526,  # Rose Bush - 玫瑰丛
    527: 527,  # Peony - 牡丹
    528: 528,  # Tall Grass - 高草
    529: 529,  # Large Fern - 大型蕨
    530: 633,  # White Stained Glass - 白玻璃块
    531: 634,  # Orange Stained Glass - 橙玻璃块
    532: 635,  # Magenta Stained Glass - 红紫玻璃块
    533: 636,  # Light Blue Stained Glass - 浅蓝玻璃块
    534: 637,  # Yellow Stained Glass - 黄玻璃块
    535: 638,  # Lime Stained Glass - 浅绿玻璃块
    536: 639,  # Pink Stained Glass - 浅红玻璃块
    537: 640,  # Gray Stained Glass - 灰玻璃块
    538: 641,  # Light Gray Stained Glass - 浅灰玻璃块
    539: 642,  # Cyan Stained Glass - 蓝绿玻璃块
    540: 643,  # Purple Stained Glass - 紫玻璃块
    541: 644,  # Blue Stained Glass - 蓝玻璃块
    542: 645,  # Brown Stained Glass - 深红玻璃块
    543: 646,  # Green Stained Glass - 绿玻璃块
    544: 647,  # Red Stained Glass - 红玻璃块
    545: 648,  # Black Stained Glass - 黑玻璃块
    546: 650,  # White Stained Glass Pane - 白玻璃片
    547: 651,  # Orange Stained Glass Pane - 橙玻璃片
    548: 652,  # Magenta Stained Glass Pane - 红紫玻璃片
    549: 653,  # Light Blue Stained Glass Pane - 浅蓝玻璃片
    550: 654,  # Yellow Stained Glass Pane - 黄玻璃片
    551: 655,  # Lime Stained Glass Pane - 浅绿玻璃片
    552: 656,  # Pink Stained Glass Pane - 浅红玻璃片
    553: 657,  # Gray Stained Glass Pane - 灰玻璃片
    554: 658,  # Light Gray Stained Glass Pane - 浅灰玻璃片
    555: 659,  # Cyan Stained Glass Pane - 蓝绿玻璃片
    556: 660,  # Purple Stained Glass Pane - 紫玻璃片
    557: 661,  # Blue Stained Glass Pane - 蓝玻璃片
    558: 662,  # Brown Stained Glass Pane - 深红玻璃片
    559: 663,  # Green Stained Glass Pane - 绿玻璃片
    560: 664,  # Red Stained Glass Pane - 红玻璃片
    561: 665,  # Black Stained Glass Pane - 黑玻璃片
    562: 562,  # Prismarine - 海晶石
    563: 563,  # Prismarine Bricks - 海晶石砖
    564: 564,  # Dark Prismarine - 暗海晶石
    565: 565,  # Prismarine Stairs - 海晶石楼梯
    566: 566,  # Prismarine Brick Stairs - 海晶石砖楼梯
    567: 567,  # Dark Prismarine Stairs - 暗海晶石楼梯
    568: 568,  # Sea Lantern - 海晶灯
    569: 569,  # Red Sandstone - 红砂岩
    570: 570,  # Chiseled Red Sandstone - 雕纹红砂岩
    571: 571,  # Cut Red Sandstone - 切制红砂岩
    572: 572,  # Red Sandstone Stairs - 红砂岩楼梯
    573: 573,  # Repeating Command Block - 循环命令方块
    574: 574,  # Chain Command Block - 链命令方块
    575: 575,  # Magma Block - 岩浆块
    576: 576,  # Nether Wart Block - 地狱疣块
    577: 577,  # Warped Wart Block - 诡异疣块
    578: 578,  # Red Nether Bricks - 红色地狱砖
    579: 579,  # Bone Block - 骨块
    580: 580,  # Structure Void - 结构空位
    581: 581,  # Shulker Box - 潜影盒
    582: 582,  # White Shulker Box - 白潜影盒
    583: 583,  # Orange Shulker Box - 橙潜影盒
    584: 584,  # Magenta Shulker Box - 品红潜影盒
    585: 585,  # Light Blue Shulker Box - 浅蓝潜影盒
    586: 586,  # Yellow Shulker Box - 黄潜影盒
    587: 587,  # Lime Shulker Box - 黄绿潜影盒
    588: 588,  # Pink Shulker Box - 粉潜影盒
    589: 589,  # Gray Shulker Box - 灰潜影盒
    590: 590,  # Light Gray Shulker Box - 浅灰潜影盒
    591: 591,  # Cyan Shulker Box - 青潜影盒
    592: 592,  # Purple Shulker Box - 紫潜影盒
    593: 593,  # Blue Shulker Box - 蓝潜影盒
    594: 594,  # Brown Shulker Box - 棕潜影盒
    595: 595,  # Green Shulker Box - 绿潜影盒
    596: 596,  # Red Shulker Box - 红潜影盒
    597: 597,  # Black Shulker Box - 黑潜影盒
    598: 598,  # White Glazed Terracotta - 白带釉陶瓦
    599: 599,  # Orange Glazed Terracotta - 橙带釉陶瓦
    600: 600,  # Magenta Glazed Terracotta - 品红带釉陶瓦
    601: 601,  # Light Blue Glazed Terracotta - 浅蓝带釉陶瓦
    602: 602,  # Yellow Glazed Terracotta - 黄带釉陶瓦
    603: 603,  # Lime Glazed Terracotta - 黄绿带釉陶瓦
    604: 604,  # Pink Glazed Terracotta - 粉带釉陶瓦
    605: 605,  # Gray Glazed Terracotta - 灰带釉陶瓦
    606: 606,  # Light Gray Glazed Terracotta - 浅灰带釉陶瓦
    607: 607,  # Cyan Glazed Terracotta - 青带釉陶瓦
    608: 608,  # Purple Glazed Terracotta - 紫带釉陶瓦
    609: 609,  # Blue Glazed Terracotta - 蓝带釉陶瓦
    610: 610,  # Brown Glazed Terracotta - 棕带釉陶瓦
    611: 611,  # Green Glazed Terracotta - 绿带釉陶瓦
    612: 612,  # Red Glazed Terracotta - 红带釉陶瓦
    613: 613,  # Black Glazed Terracotta - 黑带釉陶瓦
    614: 666,  # White Concrete - 水泥块(白色)
    615: 667,  # Orange Concrete - 水泥块(橙色)
    616: 668,  # Magenta Concrete - 水泥块(红紫)
    617: 669,  # Light Blue Concrete - 水泥块(浅蓝)
    618: 670,  # Yellow Concrete - 水泥块(黄色)
    619: 671,  # Lime Concrete - 水泥块(浅绿)
    620: 672,  # Pink Concrete - 水泥块(浅红)
    621: 673,  # Gray Concrete - 水泥块(灰色)
    622: 674,  # Light Gray Concrete - 水泥块(浅灰)
    623: 675,  # Cyan Concrete - 水泥块(蓝绿)
    624: 676,  # Purple Concrete - 水泥块(紫色)
    625: 677,  # Blue Concrete - 水泥块(蓝色)
    626: 678,  # Brown Concrete - 水泥块(深红)
    627: 679,  # Green Concrete - 水泥块(绿色)
    628: 680,  # Red Concrete - 水泥块(红色)
    629: 681,  # Black Concrete - 水泥块(黑色)
    630: 630,  # White Concrete Powder - 白混凝土粉末
    631: 631,  # Orange Concrete Powder - 橙混凝土粉末
    632: 632,  # Magenta Concrete Powder - 品红混凝土粉末
    633: 633,  # Light Blue Concrete Powder - 浅蓝混凝土粉末
    634: 634,  # Yellow Concrete Powder - 黄混凝土粉末
    635: 635,  # Lime Concrete Powder - 黄绿混凝土粉末
    636: 636,  # Pink Concrete Powder - 粉混凝土粉末
    637: 637,  # Gray Concrete Powder - 灰混凝土粉末
    638: 638,  # Light Gray Concrete Powder - 浅灰混凝土粉末
    639: 639,  # Cyan Concrete Powder - 青混凝土粉末
    640: 640,  # Purple Concrete Powder - 紫混凝土粉末
    641: 641,  # Blue Concrete Powder - 蓝混凝土粉末
    642: 642,  # Brown Concrete Powder - 棕混凝土粉末
    643: 643,  # Green Concrete Powder - 绿混凝土粉末
    644: 644,  # Red Concrete Powder - 红混凝土粉末
    645: 645,  # Black Concrete Powder - 黑混凝土粉末
    646: 646,  # Turtle Egg - 海龟蛋
    679: 679,  # Blue Ice - 蓝冰
    680: 680,  # Conduit - 潮涌核心
    681: 681,  # Polished Granite Stairs - 磨制花岗岩楼梯
    682: 682,  # Smooth Red Sandstone Stairs - 平滑红砂岩楼梯
    683: 683,  # Mossy Stone Brick Stairs - 苔石砖楼梯
    684: 684,  # Polished Diorite Stairs - 磨制闪长岩楼梯
    685: 685,  # Mossy Cobblestone Stairs - 苔石楼梯
    686: 686,  # End Stone Brick Stairs - 末地石砖楼梯
    687: 687,  # Stone Stairs - 石楼梯
    688: 688,  # Smooth Sandstone Stairs - 平滑砂岩楼梯
    689: 689,  # Smooth Quartz Stairs - 平滑石英楼梯
    690: 690,  # Granite Stairs - 花岗岩楼梯
    691: 691,  # Andesite Stairs - 安山岩楼梯
    692: 692,  # Red Nether Brick Stairs - 红色地狱砖楼梯
    693: 693,  # Polished Andesite Stairs - 磨制安山岩楼梯
    694: 694,  # Diorite Stairs - 闪长岩楼梯
    695: 695,  # Cobbled Deepslate Stairs - 深板岩圆石楼梯
    696: 696,  # Polished Deepslate Stairs - 磨制深板岩楼梯
    697: 697,  # Deepslate Brick Stairs - 深板岩砖楼梯
    698: 698,  # Deepslate Tile Stairs - 深板岩瓦楼梯
    699: 699,  # Polished Granite Slab - 磨制花岗岩台阶
    700: 700,  # Smooth Red Sandstone Slab - 平滑红砂岩台阶
    701: 701,  # Mossy Stone Brick Slab - 苔石砖台阶
    702: 702,  # Polished Diorite Slab - 磨制闪长岩台阶
    703: 703,  # Mossy Cobblestone Slab - 苔石台阶
    704: 704,  # End Stone Brick Slab - 末地石砖台阶
    705: 705,  # Smooth Sandstone Slab - 平滑砂岩台阶
    706: 706,  # Smooth Quartz Slab - 平滑石英台阶
    707: 707,  # Granite Slab - 花岗岩台阶
    708: 708,  # Andesite Slab - 安山岩台阶
    709: 709,  # Red Nether Brick Slab - 红色地狱砖台阶
    710: 710,  # Polished Andesite Slab - 磨制安山岩台阶
    711: 711,  # Diorite Slab - 闪长岩台阶
    712: 712,  # Cobbled Deepslate Slab - 深板岩圆石台阶
    713: 713,  # Polished Deepslate Slab - 磨制深板岩台阶
    714: 714,  # Deepslate Brick Slab - 深板岩砖台阶
    715: 715,  # Deepslate Tile Slab - 深板岩瓦台阶
    716: 716,  # Scaffolding - 脚手架
    717: 717,  # Redstone Dust - 红石粉
    718: 718,  # Redstone Torch - 红石火把
    719: 719,  # Redstone Block - 红石块
    720: 720,  # Repeater - 红石中继器
    721: 721,  # Comparator - 红石比较器
    722: 722,  # Piston - 活塞
    723: 723,  # Sticky Piston - 粘性活塞
    724: 724,  # Slime Block - 粘液块
    725: 725,  # Honey Block - 蜂蜜块
    726: 726,  # Observer - 观察者
    727: 727,  # Hopper - 漏斗
    728: 728,  # Dispenser - 发射器
    729: 729,  # Dropper - 投掷器
    730: 730,  # Lectern - 讲台
    731: 731,  # Target - 标靶
    732: 732,  # Lever - 拉杆
    733: 733,  # Lightning Rod - 避雷针
    741: 741,  # Daylight Detector - 日光传感器
    742: 742,  # Sculk Sensor - 幽匿感测体
    744: 744,  # Tripwire Hook - 绊线钩
    745: 745,  # Trapped Chest - 陷阱箱
    746: 746,  # TNT - TNT
    747: 747,  # Redstone Lamp - 红石灯
    748: 748,  # Note Block - 音符盒
    749: 716,  # Stone Button - 按钮
    750: 716,  # Polished Blackstone Button - 磨制黑石按钮
    751: 716,  # Oak Button - 橡木按钮
    752: 716,  # Spruce Button - 云杉木按钮
    753: 716,  # Birch Button - 白桦木按钮
    754: 716,  # Jungle Button - 丛林木按钮
    755: 716,  # Acacia Button - 金合欢木按钮
    756: 716,  # Cherry Button - 樱花木按钮
    757: 716,  # Dark Oak Button - 深色橡木按钮
    759: 716,  # Mangrove Button - 红树木按钮
    760: 716,  # Bamboo Button - 竹按钮
    761: 716,  # Crimson Button - 绯红木按钮
    762: 716,  # Warped Button - 诡异木按钮
    763: 712,  # Stone Pressure Plate - 石质压力板
    764: 712,  # Polished Blackstone Pressure Plate - 磨制黑石压力板
    765: 765,  # Light Weighted Pressure Plate - 轻质测重压力板
    766: 766,  # Heavy Weighted Pressure Plate - 重质测重压力板
    767: 712,  # Oak Pressure Plate - 橡木压力板
    768: 712,  # Spruce Pressure Plate - 云杉木压力板
    769: 712,  # Birch Pressure Plate - 白桦木压力板
    770: 712,  # Jungle Pressure Plate - 丛林木压力板
    771: 712,  # Acacia Pressure Plate - 金合欢木压力板
    772: 712,  # Cherry Pressure Plate - 樱花木压力板
    773: 712,  # Dark Oak Pressure Plate - 深色橡木压力板
    775: 712,  # Mangrove Pressure Plate - 红树木压力板
    776: 712,  # Bamboo Pressure Plate - 竹压力板
    777: 712,  # Crimson Pressure Plate - 绯红木压力板
    778: 712,  # Warped Pressure Plate - 诡异木压力板
    779: 814,  # Iron Door - 铁门
    780: 812,  # Oak Door - 木门
    781: 812,  # Spruce Door - 木门
    782: 812,  # Birch Door - 木门
    783: 812,  # Jungle Door - 木门
    784: 812,  # Acacia Door - 木门
    785: 812,  # Cherry Door - 木门
    786: 812,  # Dark Oak Door - 木门
    788: 812,  # Mangrove Door - 木门
    789: 812,  # Bamboo Door - 木门
    790: 812,  # Crimson Door - 木门
    791: 812,  # Warped Door - 木门
    800: 800,  # Iron Trapdoor - 铁活板门
    801: 801,  # Oak Trapdoor - 橡木活板门
    802: 801,  # Spruce Trapdoor - 云杉木活板门
    803: 801,  # Birch Trapdoor - 白桦木活板门
    804: 801,  # Jungle Trapdoor - 丛林木活板门
    805: 801,  # Acacia Trapdoor - 金合欢木活板门
    806: 801,  # Cherry Trapdoor - 樱花木活板门
    807: 801,  # Dark Oak Trapdoor - 深色橡木活板门
    809: 801,  # Mangrove Trapdoor - 红树木活板门
    810: 801,  # Bamboo Trapdoor - 竹活板门
    811: 801,  # Crimson Trapdoor - 绯红木活板门
    812: 801,  # Warped Trapdoor - 诡异木活板门
    821: 535,  # Oak Fence Gate - 木围栏门
    822: 535,  # Spruce Fence Gate - 木围栏门
    823: 535,  # Birch Fence Gate - 木围栏门
    824: 535,  # Jungle Fence Gate - 木围栏门
    825: 535,  # Acacia Fence Gate - 木围栏门
    826: 535,  # Cherry Fence Gate - 木围栏门
    827: 535,  # Dark Oak Fence Gate - 木围栏门
    829: 535,  # Mangrove Fence Gate - 木围栏门
    830: 569,  # Bamboo Fence Gate - 竹围栏门
    831: 535,  # Crimson Fence Gate - 木围栏门
    832: 535,  # Warped Fence Gate - 木围栏门
    833: 833,  # Powered Rail - 充能铁轨
    834: 834,  # Detector Rail - 探测铁轨
    835: 835,  # Rail - 铁轨
    836: 836,  # Activator Rail - 激活铁轨
    837: 11810,  # Saddle - 坐骑的鞍
    838: 11810,  # White Harness - 坐骑的鞍
    839: 11810,  # Orange Harness - 坐骑的鞍
    840: 11810,  # Magenta Harness - 坐骑的鞍
    841: 11810,  # Light Blue Harness - 坐骑的鞍
    842: 11810,  # Yellow Harness - 坐骑的鞍
    843: 11810,  # Lime Harness - 坐骑的鞍
    844: 11810,  # Pink Harness - 坐骑的鞍
    845: 11810,  # Gray Harness - 坐骑的鞍
    846: 11810,  # Light Gray Harness - 坐骑的鞍
    847: 11810,  # Cyan Harness - 坐骑的鞍
    848: 11810,  # Purple Harness - 坐骑的鞍
    849: 11810,  # Blue Harness - 坐骑的鞍
    850: 11810,  # Brown Harness - 坐骑的鞍
    851: 11810,  # Green Harness - 坐骑的鞍
    852: 11810,  # Red Harness - 坐骑的鞍
    853: 11810,  # Black Harness - 坐骑的鞍
    854: 854,  # Minecart - 矿车
    855: 855,  # Chest Minecart - 运输矿车
    856: 856,  # Furnace Minecart - 动力矿车
    857: 857,  # TNT Minecart - TNT矿车
    858: 858,  # Hopper Minecart - 漏斗矿车
    859: 859,  # Carrot on a Stick - 胡萝卜钓竿
    860: 860,  # Warped Fungus on a Stick - 诡异菌钓竿
    861: 861,  # Phantom Membrane - 幻翼膜
    862: 862,  # Elytra - 鞘翅
    863: 863,  # Oak Boat - 橡木船
    864: 864,  # Oak Chest Boat - 橡木运输船
    865: 865,  # Spruce Boat - 云杉木船
    866: 866,  # Spruce Chest Boat - 云杉木运输船
    867: 867,  # Birch Boat - 白桦木船
    868: 868,  # Birch Chest Boat - 白桦木运输船
    869: 869,  # Jungle Boat - 丛林木船
    870: 870,  # Jungle Chest Boat - 丛林木运输船
    871: 871,  # Acacia Boat - 金合欢木船
    872: 872,  # Acacia Chest Boat - 金合欢木运输船
    873: 873,  # Cherry Boat - 樱花木船
    874: 874,  # Cherry Chest Boat - 樱花木运输船
    875: 875,  # Dark Oak Boat - 深色橡木船
    876: 876,  # Dark Oak Chest Boat - 深色橡木运输船
    879: 879,  # Mangrove Boat - 红树木船
    880: 880,  # Mangrove Chest Boat - 红树木运输船
    881: 881,  # Bamboo Raft - 竹筏
    882: 882,  # Bamboo Chest Raft - 竹运输筏
    883: 883,  # Structure Block - 结构方块
    884: 884,  # Jigsaw - 拼图方块
    887: 887,  # Turtle Helmet - 海龟壳
    888: 888,  # Turtle Scute - 海龟鳞甲
    889: 889,  # Armadillo Scute - 犰狳鳞甲
    890: 890,  # Wolf Armor - 狼铠
    891: 11055,  # Flint and Steel - 点火器
    892: 11314,  # Bowl - 简易木碗
    893: 893,  # Apple - 苹果
    894: 12050,  # Bow - 铸铁弓
    895: 12051,  # Arrow - 石箭
    896: 896,  # Coal - 煤炭
    897: 11202,  # Charcoal - 黑炭
    898: 898,  # Diamond - 钻石
    899: 899,  # Emerald - 绿宝石
    900: 900,  # Lapis Lazuli - 青金石
    901: 901,  # Nether Quartz - 下界石英
    902: 902,  # Amethyst Shard - 紫水晶碎片
    903: 903,  # Raw Iron - 粗铁
    904: 904,  # Iron Ingot - 铁锭
    905: 905,  # Raw Copper - 粗铜
    906: 906,  # Copper Ingot - 铜锭
    907: 907,  # Raw Gold - 粗金
    908: 908,  # Gold Ingot - 金锭
    909: 909,  # Netherite Ingot - 下界合金锭
    910: 910,  # Netherite Scrap - 下界合金碎片
    911: 911,  # Wooden Sword - 木剑
    912: 912,  # Wooden Shovel - 木铲
    913: 913,  # Wooden Pickaxe - 木镐
    914: 914,  # Wooden Axe - 木斧
    915: 915,  # Wooden Hoe - 木锄
    916: 916,  # Copper Sword - 铜剑
    917: 917,  # Copper Shovel - 铜铲
    918: 918,  # Copper Pickaxe - 铜镐
    919: 919,  # Copper Axe - 铜斧
    920: 920,  # Copper Hoe - 铜锄
    921: 12012,  # Stone Sword - 石剑
    922: 11022,  # Stone Shovel - 石铲
    923: 11012,  # Stone Pickaxe - 石镐
    924: 11002,  # Stone Axe - 石斧
    925: 11032,  # Stone Hoe - 石耙
    926: 926,  # Golden Sword - 金剑
    927: 927,  # Golden Shovel - 金铲
    928: 928,  # Golden Pickaxe - 金镐
    929: 929,  # Golden Axe - 金斧
    930: 930,  # Golden Hoe - 金锄
    931: 931,  # Iron Sword - 铁剑
    932: 932,  # Iron Shovel - 铁铲
    933: 933,  # Iron Pickaxe - 铁镐
    934: 934,  # Iron Axe - 铁斧
    935: 935,  # Iron Hoe - 铁锄
    936: 936,  # Diamond Sword - 钻石剑
    937: 937,  # Diamond Shovel - 钻石铲
    938: 938,  # Diamond Pickaxe - 钻石镐
    939: 939,  # Diamond Axe - 钻石斧
    940: 940,  # Diamond Hoe - 钻石锄
    941: 941,  # Netherite Sword - 下界合金剑
    942: 942,  # Netherite Shovel - 下界合金铲
    943: 943,  # Netherite Pickaxe - 下界合金镐
    944: 944,  # Netherite Axe - 下界合金斧
    945: 945,  # Netherite Hoe - 下界合金锄
    946: 12001,  # Stick - 木棒
    947: 947,  # Mushroom Stew - 蘑菇煲
    948: 948,  # String - 线
    949: 11303,  # Feather - 细羽毛
    950: 950,  # Gunpowder - 火药
    951: 11400,  # Wheat Seeds - 玉米种子
    952: 952,  # Wheat - 小麦
    953: 953,  # Bread - 面包
    954: 12201,  # Leather Helmet - 皮头盔
    955: 12202,  # Leather Chestplate - 皮胸甲
    956: 12203,  # Leather Leggings - 皮护腿
    957: 12204,  # Leather Boots - 皮靴子
    958: 958,  # Copper Helmet - 铜头盔
    959: 959,  # Copper Chestplate - 铜胸甲
    960: 960,  # Copper Leggings - 铜护腿
    961: 961,  # Copper Boots - 铜靴子
    962: 12211,  # Chainmail Helmet - 链甲头盔
    963: 12212,  # Chainmail Chestplate - 链甲胸甲
    964: 12213,  # Chainmail Leggings - 链甲护腿
    965: 12214,  # Chainmail Boots - 链甲靴子
    966: 12221,  # Iron Helmet - 铸铁头盔
    967: 12222,  # Iron Chestplate - 铸铁胸甲
    968: 12223,  # Iron Leggings - 铸铁护腿
    969: 12224,  # Iron Boots - 铸铁靴子
    970: 12241,  # Diamond Helmet - 钨金头盔
    971: 12242,  # Diamond Chestplate - 钨金胸甲
    972: 12243,  # Diamond Leggings - 钨金护腿
    973: 12244,  # Diamond Boots - 钨金靴子
    974: 974,  # Golden Helmet - 金头盔
    975: 975,  # Golden Chestplate - 金胸甲
    976: 976,  # Golden Leggings - 金护腿
    977: 977,  # Golden Boots - 金靴子
    978: 978,  # Netherite Helmet - 下界合金头盔
    979: 979,  # Netherite Chestplate - 下界合金胸甲
    980: 980,  # Netherite Leggings - 下界合金护腿
    981: 981,  # Netherite Boots - 下界合金靴子
    982: 11304,  # Flint - 火石
    983: 12516,  # Porkchop - 沃沃兽肉
    984: 12517,  # Cooked Porkchop - 烤沃沃兽肉
    985: 985,  # Painting - 画
    986: 986,  # Golden Apple - 金苹果
    987: 987,  # Enchanted Golden Apple - 附魔金苹果
    988: 988,  # Oak Sign - 橡木告示牌
    989: 989,  # Spruce Sign - 云杉木告示牌
    990: 990,  # Birch Sign - 白桦木告示牌
    991: 991,  # Jungle Sign - 丛林木告示牌
    992: 992,  # Acacia Sign - 金合欢木告示牌
    993: 993,  # Cherry Sign - 樱花木告示牌
    994: 994,  # Dark Oak Sign - 深色橡木告示牌
    996: 996,  # Mangrove Sign - 红树木告示牌
    997: 997,  # Bamboo Sign - 竹告示牌
    998: 998,  # Crimson Sign - 绯红木告示牌
    999: 999,  # Warped Sign - 诡异木告示牌
    1012: 11048,  # Bucket - 木桶
    1013: 1013,  # Water Bucket - 水桶
    1014: 1014,  # Lava Bucket - 熔岩桶
    1016: 12054,  # Snowball - 小沙包
    1017: 11309,  # Leather - 软皮革布
    1018: 1018,  # Milk Bucket - 牛奶桶
    1025: 1025,  # Brick - 红砖
    1026: 1026,  # Clay Ball - 黏土球
    1028: 11322,  # Paper - 纸张
    1029: 11803,  # Book - 书本
    1030: 1030,  # Slime Ball - 粘液球
    1031: 12052,  # Egg - 嘟嘟鸟蛋
    1034: 1034,  # Compass - 指南针
    1035: 1035,  # Recovery Compass - 恢复指南针
    1036: 1036,  # Bundle - 收纳袋
    1053: 1053,  # Fishing Rod - 钓鱼竿
    1054: 1054,  # Clock - 时钟
    1055: 1055,  # Spyglass - 望远镜
    1056: 1056,  # Glowstone Dust - 荧石粉
    1057: 12520,  # Cod - 鲜呆呆鱼
    1058: 12524,  # Salmon - 三文鱼
    1059: 12520,  # Tropical Fish - 鲜呆呆鱼
    1060: 12520,  # Pufferfish - 鲜呆呆鱼
    1061: 12521,  # Cooked Cod - 烤呆呆鱼
    1062: 12525,  # Cooked Salmon - 烤三文鱼
    1063: 1063,  # Ink Sac - 墨囊
    1064: 1064,  # Glow Ink Sac - 荧光墨囊
    1065: 1065,  # Cocoa Beans - 可可豆
    1066: 11500,  # White Dye - 象牙白颜料瓶
    1067: 11501,  # Orange Dye - 朱砂橙颜料瓶
    1068: 11502,  # Magenta Dye - 胭脂红颜料瓶
    1069: 11503,  # Light Blue Dye - 天青蓝颜料瓶
    1070: 11504,  # Yellow Dye - 鹅毛黄颜料瓶
    1071: 11505,  # Lime Dye - 松花绿颜料瓶
    1072: 11506,  # Pink Dye - 海棠红颜料瓶
    1073: 11507,  # Gray Dye - 苍石灰颜料瓶
    1074: 11508,  # Light Gray Dye - 浅苍灰颜料瓶
    1075: 11509,  # Cyan Dye - 青碧绿颜料瓶
    1076: 11510,  # Purple Dye - 青莲紫颜料瓶
    1077: 11532,  # Blue Dye - 宝石蓝颜料瓶
    1078: 11512,  # Brown Dye - 深栗红颜料瓶
    1079: 11513,  # Green Dye - 翡翠绿颜料瓶
    1080: 11514,  # Red Dye - 赫赤红颜料瓶
    1081: 11515,  # Black Dye - 煤乌黑颜料瓶
    1082: 1082,  # Bone Meal - 骨粉
    1083: 11302,  # Bone - 兽骨
    1084: 1084,  # Sugar - 糖
    1085: 1085,  # Cake - 蛋糕
    1086: 1086,  # White Bed - 白色床
    1087: 1087,  # Orange Bed - 橙色床
    1088: 1088,  # Magenta Bed - 品红色床
    1089: 1089,  # Light Blue Bed - 浅蓝色床
    1090: 1090,  # Yellow Bed - 黄色床
    1091: 1091,  # Lime Bed - 黄绿色床
    1092: 1092,  # Pink Bed - 粉色床
    1093: 1093,  # Gray Bed - 灰色床
    1094: 1094,  # Light Gray Bed - 浅灰色床
    1095: 1095,  # Cyan Bed - 青色床
    1096: 1096,  # Purple Bed - 紫色床
    1097: 1097,  # Blue Bed - 蓝色床
    1098: 1098,  # Brown Bed - 棕色床
    1099: 1099,  # Green Bed - 绿色床
    1100: 1100,  # Red Bed - 红色床
    1101: 1101,  # Black Bed - 黑色床
    1102: 1102,  # Cookie - 曲奇
    1103: 1103,  # Crafter - 合成器
    1104: 1104,  # Filled Map - 地图
    1105: 1105,  # Shears - 剪刀
    1106: 1106,  # Melon Slice - 西瓜片
    1108: 1108,  # Pumpkin Seeds - 南瓜种子
    1109: 1109,  # Melon Seeds - 西瓜种子
    1110: 12514,  # Beef - 兽肉
    1111: 12515,  # Cooked Beef - 烤肉
    1112: 12741,  # Chicken - 生鸡肉
    1113: 12742,  # Cooked Chicken - 烤鸡
    1114: 12526,  # Rotten Flesh - 奇怪的肘子
    1115: 1115,  # Ender Pearl - 末影珍珠
    1116: 1116,  # Blaze Rod - 烈焰棒
    1117: 1117,  # Ghast Tear - 恶魂之泪
    1118: 1118,  # Gold Nugget - 金粒
    1119: 1119,  # Nether Wart - 下界疣
    1120: 1120,  # Glass Bottle - 玻璃瓶
    1121: 1121,  # Potion - 药水
    1122: 1122,  # Spider Eye - 蜘蛛眼
    1123: 1123,  # Fermented Spider Eye - 发酵蜘蛛眼
    1124: 1124,  # Blaze Powder - 烈焰粉
    1125: 1125,  # Magma Cream - 岩浆膏
    1126: 1126,  # Brewing Stand - 酿造台
    1127: 1127,  # Cauldron - 炼药锅
    1128: 1128,  # Ender Eye - 末影之眼
    1129: 1129,  # Glistering Melon Slice - 闪烁的西瓜片
    1130: 13400,  # Chicken Spawn Egg - 嘟嘟鸟蛋
    1131: 13401,  # Cow Spawn Egg - 沃沃兽蛋
    1132: 13402,  # Pig Spawn Egg - 墩墩蛋
    1133: 13403,  # Sheep Spawn Egg - 角鹿蛋
    1134: 1134,  # Camel Spawn Egg - 骆驼蛋
    1135: 1135,  # Donkey Spawn Egg - 驴蛋
    1136: 13404,  # Horse Spawn Egg - 马蛋
    1137: 1137,  # Mule Spawn Egg - 骡蛋
    1138: 1138,  # Cat Spawn Egg - 猫蛋
    1139: 1139,  # Parrot Spawn Egg - 鹦鹉蛋
    1140: 13407,  # Wolf Spawn Egg - 狐狸蛋
    1141: 1141,  # Armadillo Spawn Egg - 犰狳蛋
    1142: 1142,  # Bat Spawn Egg - 蝙蝠蛋
    1143: 13418,  # Bee Spawn Egg - 蜜蜂蛋
    1144: 13408,  # Fox Spawn Egg - 灵狐蛋
    1145: 1145,  # Goat Spawn Egg - 山羊蛋
    1146: 1146,  # Llama Spawn Egg - 羊驼蛋
    1147: 1147,  # Ocelot Spawn Egg - 豹猫蛋
    1148: 13416,  # Panda Spawn Egg - 熊猫蛋
    1149: 1149,  # Polar Bear Spawn Egg - 北极熊蛋
    1150: 1150,  # Rabbit Spawn Egg - 兔子蛋
    1151: 1151,  # Axolotl Spawn Egg - 美西螈蛋
    1152: 1152,  # Cod Spawn Egg - 鳕鱼蛋
    1153: 1153,  # Dolphin Spawn Egg - 海豚蛋
    1154: 1154,  # Frog Spawn Egg - 青蛙蛋
    1155: 1155,  # Glow Squid Spawn Egg - 发光鱿鱼蛋
    1156: 1156,  # Nautilus Spawn Egg - 鹦鹉螺蛋
    1157: 1157,  # Pufferfish Spawn Egg - 河豚蛋
    1158: 1158,  # Salmon Spawn Egg - 鲑鱼蛋
    1159: 1159,  # Squid Spawn Egg - 鱿鱼蛋
    1160: 1160,  # Tadpole Spawn Egg - 蝌蚪蛋
    1161: 1161,  # Tropical Fish Spawn Egg - 热带鱼蛋
    1162: 1162,  # Turtle Spawn Egg - 海龟蛋
    1163: 1163,  # Allay Spawn Egg - 悦灵蛋
    1164: 1164,  # Mooshroom Spawn Egg - 哞菇蛋
    1165: 1165,  # Sniffer Spawn Egg - 嗅探兽蛋
    1166: 1166,  # Copper Golem Spawn Egg - 铜傀儡蛋
    1167: 1167,  # Iron Golem Spawn Egg - 铁傀儡蛋
    1168: 1168,  # Snow Golem Spawn Egg - 雪傀儡蛋
    1169: 1169,  # Trader Llama Spawn Egg - 商羊驼蛋
    1170: 1170,  # Villager Spawn Egg - 村民蛋
    1171: 1171,  # Wandering Trader Spawn Egg - 流浪商人蛋
    1172: 1172,  # Bogged Spawn Egg - 沼泽怪蛋
    1174: 1174,  # Drowned Spawn Egg - 溺尸蛋
    1175: 1175,  # Husk Spawn Egg - 尸壳蛋
    1177: 1177,  # Skeleton Spawn Egg - 骷髅蛋
    1178: 1178,  # Skeleton Horse Spawn Egg - 骷髅马蛋
    1179: 1179,  # Stray Spawn Egg - 流浪者蛋
    1181: 1181,  # Wither Skeleton Spawn Egg - 凋灵骷髅蛋
    1182: 1182,  # Zombie Spawn Egg - 僵尸蛋
    1183: 1183,  # Zombie Horse Spawn Egg - 僵尸马蛋
    1185: 1185,  # Zombie Villager Spawn Egg - 僵尸村民蛋
    1186: 1186,  # Cave Spider Spawn Egg - 洞穴蜘蛛蛋
    1187: 1187,  # Spider Spawn Egg - 蜘蛛蛋
    1188: 1188,  # Breeze Spawn Egg - 旋风人蛋
    1189: 1189,  # Creaking Spawn Egg - 吱吱怪蛋
    1190: 1190,  # Creeper Spawn Egg - 苦力怕蛋
    1191: 1191,  # Elder Guardian Spawn Egg - 远古守卫者蛋
    1192: 1192,  # Guardian Spawn Egg - 守卫者蛋
    1193: 1193,  # Phantom Spawn Egg - 幻翼蛋
    1194: 1194,  # Silverfish Spawn Egg - 蠹虫蛋
    1195: 1195,  # Slime Spawn Egg - 史莱姆蛋
    1196: 1196,  # Warden Spawn Egg - 监守者蛋
    1197: 1197,  # Witch Spawn Egg - 女巫蛋
    1198: 1198,  # Evoker Spawn Egg - 唤魔者蛋
    1199: 1199,  # Pillager Spawn Egg - 掠夺者蛋
    1200: 1200,  # Ravager Spawn Egg - 劫掠兽蛋
    1201: 1201,  # Vindicator Spawn Egg - 卫道士蛋
    1202: 1202,  # Vex Spawn Egg - 恼鬼蛋
    1203: 1203,  # Blaze Spawn Egg - 烈焰人蛋
    1204: 1204,  # Ghast Spawn Egg - 恶魂蛋
    1205: 1205,  # Happy Ghast Spawn Egg - 快乐恶魂蛋
    1206: 1206,  # Hoglin Spawn Egg - 疣猪兽蛋
    1207: 1207,  # Magma Cube Spawn Egg - 岩浆怪蛋
    1208: 1208,  # Piglin Spawn Egg - 猪灵蛋
    1209: 1209,  # Piglin Brute Spawn Egg - 猪灵蛮兵蛋
    1210: 1210,  # Strider Spawn Egg - 炽足兽蛋
    1211: 1211,  # Zoglin Spawn Egg - 僵尸疣猪兽蛋
    1212: 1212,  # Zombified Piglin Spawn Egg - 僵尸猪灵蛋
    1214: 1214,  # Enderman Spawn Egg - 末影人蛋
    1215: 1215,  # Endermite Spawn Egg - 末影螨蛋
    1216: 1216,  # Shulker Spawn Egg - 潜影贝蛋
    1217: 1217,  # Experience Bottle - 附魔之瓶
    1218: 1218,  # Fire Charge - 火焰弹
    1219: 1219,  # Wind Charge - 风弹
    1220: 1220,  # Writable Book - 书与笔
    1221: 1221,  # Written Book - 成书
    1222: 1222,  # Breeze Rod - 旋风棒
    1223: 1223,  # Mace - 重锤
    1224: 1224,  # Item Frame - 物品展示框
    1225: 1225,  # Glow Item Frame - 荧光物品展示框
    1226: 1226,  # Flower Pot - 花盆
    1227: 1227,  # Carrot - 胡萝卜
    1228: 1228,  # Potato - 马铃薯
    1229: 1229,  # Baked Potato - 烤马铃薯
    1230: 1230,  # Poisonous Potato - 毒马铃薯
    1231: 1231,  # Map - 空地图
    1232: 1232,  # Golden Carrot - 金胡萝卜
    1233: 1233,  # Skeleton Skull - 骷髅头颅
    1234: 1234,  # Wither Skeleton Skull - 凋灵骷髅头颅
    1235: 1235,  # Player Head - 玩家头颅
    1236: 1236,  # Zombie Head - 僵尸头颅
    1237: 1237,  # Creeper Head - 苦力怕头颅
    1238: 1238,  # Dragon Head - 龙首
    1239: 1239,  # Piglin Head - 猪灵头颅
    1240: 1240,  # Nether Star - 下界之星
    1241: 1241,  # Pumpkin Pie - 南瓜派
    1242: 1242,  # Firework Rocket - 烟花火箭
    1243: 1243,  # Firework Star - 烟花球
    1244: 1244,  # Enchanted Book - 附魔书
    1245: 1245,  # Nether Brick - 下界砖
    1247: 1247,  # Prismarine Shard - 海晶碎片
    1248: 1248,  # Prismarine Crystals - 海晶砂粒
    1249: 12532,  # Rabbit - 兔肉
    1250: 12533,  # Cooked Rabbit - 烤兔肉
    1251: 1251,  # Rabbit Stew - 兔肉煲
    1252: 1252,  # Rabbit's Foot - 兔子脚
    1253: 1253,  # Rabbit Hide - 兔子皮
    1254: 1254,  # Armor Stand - 盔甲架
    1255: 1255,  # Copper Horse Armor - 铜马铠
    1256: 12250,  # Iron Horse Armor - 铁制坐骑铠甲
    1257: 12251,  # Golden Horse Armor - 金坐骑铠甲
    1258: 12252,  # Diamond Horse Armor - 钻坐骑铠甲
    1259: 1259,  # Netherite Horse Armor - 下界合金马铠
    1260: 1260,  # Leather Horse Armor - 皮革马铠
    1261: 11057,  # Lead - 拴绳
    1262: 1262,  # Name Tag - 命名牌
    1264: 12514,  # Mutton - 兽肉
    1265: 12515,  # Cooked Mutton - 烤肉
    1266: 1266,  # White Banner - 白色旗帜
    1267: 1267,  # Orange Banner - 橙色旗帜
    1268: 1268,  # Magenta Banner - 品红色旗帜
    1269: 1269,  # Light Blue Banner - 浅蓝色旗帜
    1270: 1270,  # Yellow Banner - 黄色旗帜
    1271: 1271,  # Lime Banner - 黄绿色旗帜
    1272: 1272,  # Pink Banner - 粉色旗帜
    1273: 1273,  # Gray Banner - 灰色旗帜
    1274: 1274,  # Light Gray Banner - 浅灰色旗帜
    1275: 1275,  # Cyan Banner - 青色旗帜
    1276: 1276,  # Purple Banner - 紫色旗帜
    1277: 1277,  # Blue Banner - 蓝色旗帜
    1278: 1278,  # Brown Banner - 棕色旗帜
    1279: 1279,  # Green Banner - 绿色旗帜
    1280: 1280,  # Red Banner - 红色旗帜
    1281: 1281,  # Black Banner - 黑色旗帜
    1282: 1282,  # End Crystal - 末地水晶
    1283: 1283,  # Chorus Fruit - 紫颂果
    1284: 1284,  # Popped Chorus Fruit - 爆裂紫颂果
    1285: 1285,  # Torchflower Seeds - 火把花种子
    1286: 1286,  # Pitcher Pod - 瓶子草荚果
    1287: 1287,  # Beetroot - 甜菜根
    1288: 1288,  # Beetroot Seeds - 甜菜种子
    1289: 1289,  # Beetroot Soup - 甜菜汤
    1290: 1290,  # Dragon's Breath - 龙息
    1291: 1291,  # Splash Potion - 喷溅药水
    1292: 1292,  # Spectral Arrow - 光灵箭
    1293: 1293,  # Tipped Arrow - 药箭
    1294: 1294,  # Lingering Potion - 滞留药水
    1295: 1295,  # Shield - 盾牌
    1296: 1296,  # Wooden Spear - 木矛
    1297: 12002,  # Stone Spear - 石矛
    1298: 1298,  # Copper Spear - 铜矛
    1299: 1299,  # Iron Spear - 铁矛
    1300: 1300,  # Golden Spear - 金矛
    1301: 1301,  # Diamond Spear - 钻石矛
    1302: 1302,  # Netherite Spear - 下界合金矛
    1303: 1303,  # Totem of Undying - 不死图腾
    1304: 1304,  # Shulker Shell - 潜影壳
    1305: 1305,  # Iron Nugget - 铁粒
    1306: 1306,  # Copper Nugget - 铜粒
    1307: 1307,  # Knowledge Book - 知识之书
    1308: 1308,  # Debug Stick - 调试棒
    1309: 1309,  # Music Disc 13 - 音乐唱片
    1310: 1310,  # Music Disc Cat - 音乐唱片
    1311: 1311,  # Music Disc Blocks - 音乐唱片
    1312: 1312,  # Music Disc Chirp - 音乐唱片
    1313: 1313,  # Music Disc Creator - 音乐唱片
    1314: 1314,  # Music Disc Creator Music Box - 音乐唱片
    1315: 1315,  # Music Disc Far - 音乐唱片
    1316: 1316,  # Music Disc Lava Chicken - 音乐唱片
    1317: 1317,  # Music Disc Mall - 音乐唱片
    1318: 1318,  # Music Disc Mellohi - 音乐唱片
    1319: 1319,  # Music Disc Stal - 音乐唱片
    1320: 1320,  # Music Disc Strad - 音乐唱片
    1321: 1321,  # Music Disc Ward - 音乐唱片
    1322: 1322,  # Music Disc 11 - 音乐唱片
    1323: 1323,  # Music Disc Wait - 音乐唱片
    1324: 1324,  # Music Disc Otherside - 音乐唱片
    1325: 1325,  # Music Disc Relic - 音乐唱片
    1326: 1326,  # Music Disc 5 - 音乐唱片
    1327: 1327,  # Music Disc Pigstep - 音乐唱片
    1328: 1328,  # Music Disc Precipice - 音乐唱片
    1329: 1329,  # Music Disc Tears - 音乐唱片
    1330: 1330,  # Disc Fragment 5 - 唱片碎片
    1331: 1331,  # Trident - 三叉戟
    1332: 1332,  # Nautilus Shell - 鹦鹉螺壳
    1338: 1338,  # Heart of the Sea - 海洋之心
    1339: 1339,  # Crossbow - 弩
    1340: 1340,  # Suspicious Stew - 谜之炖菜
    1341: 1341,  # Loom - 织布机
    1342: 1342,  # Flower Banner Pattern - 花朵旗帜图案
    1343: 1343,  # Creeper Banner Pattern - 苦力怕旗帜图案
    1344: 1344,  # Skull Banner Pattern - 头颅旗帜图案
    1345: 1345,  # Mojang Banner Pattern - 东西旗帜图案
    1346: 1346,  # Globe Banner Pattern - 地球旗帜图案
    1347: 1347,  # Piglin Banner Pattern - 猪鼻旗帜图案
    1348: 1348,  # Flow Banner Pattern - 涡流旗帜图案
    1349: 1349,  # Guster Banner Pattern - 旋风旗帜图案
    1352: 1352,  # Goat Horn - 山羊角
    1353: 1353,  # Composter - 堆肥桶
    1354: 1354,  # Barrel - 木桶
    1355: 1355,  # Smoker - 烟熏炉
    1356: 1356,  # Blast Furnace - 高炉
    1357: 1357,  # Cartography Table - 制图台
    1358: 1358,  # Fletching Table - 制箭台
    1359: 1359,  # Grindstone - 砂轮
    1360: 1360,  # Smithing Table - 锻造台
    1361: 1361,  # Stonecutter - 切石机
    1362: 1362,  # Bell - 钟
    1363: 1363,  # Lantern - 灯笼
    1364: 1364,  # Soul Lantern - 灵魂灯笼
    1373: 1373,  # Sweet Berries - 甜浆果
    1374: 1374,  # Glow Berries - 发光浆果
    1375: 1375,  # Campfire - 营火
    1376: 1376,  # Soul Campfire - 灵魂营火
    1377: 1377,  # Shroomlight - 菌光体
    1378: 1378,  # Honeycomb - 蜜脾
    1379: 1379,  # Bee Nest - 蜂巢
    1380: 1380,  # Beehive - 蜂箱
    1381: 1381,  # Honey Bottle - 蜂蜜瓶
    1382: 1382,  # Honeycomb Block - 蜜脾块
    1383: 1383,  # Lodestone - 磁石
    1384: 1384,  # Crying Obsidian - 哭泣的黑曜石
    1385: 1385,  # Blackstone - 黑石
    1386: 1386,  # Blackstone Slab - 黑石台阶
    1387: 1387,  # Blackstone Stairs - 黑石楼梯
    1388: 1388,  # Gilded Blackstone - 镶金黑石
    1389: 1389,  # Polished Blackstone - 磨制黑石
    1390: 1390,  # Polished Blackstone Slab - 磨制黑石台阶
    1391: 1391,  # Polished Blackstone Stairs - 磨制黑石楼梯
    1392: 1392,  # Chiseled Polished Blackstone - 雕纹磨制黑石
    1393: 1393,  # Polished Blackstone Bricks - 磨制黑石砖
    1394: 1394,  # Polished Blackstone Brick Slab - 磨制黑石砖台阶
    1395: 1395,  # Polished Blackstone Brick Stairs - 磨制黑石砖楼梯
    1396: 1396,  # Cracked Polished Blackstone Bricks - 裂纹磨制黑石砖
    1397: 1397,  # Respawn Anchor - 重生锚
    1398: 1398,  # Candle - 蜡烛
    1399: 1399,  # White Candle - 白色蜡烛
    1400: 1400,  # Orange Candle - 橙色蜡烛
    1401: 1401,  # Magenta Candle - 品红色蜡烛
    1402: 1402,  # Light Blue Candle - 浅蓝色蜡烛
    1403: 1403,  # Yellow Candle - 黄色蜡烛
    1404: 1404,  # Lime Candle - 黄绿色蜡烛
    1405: 1405,  # Pink Candle - 粉色蜡烛
    1406: 1406,  # Gray Candle - 灰色蜡烛
    1407: 1407,  # Light Gray Candle - 浅灰色蜡烛
    1408: 1408,  # Cyan Candle - 青色蜡烛
    1409: 1409,  # Purple Candle - 紫色蜡烛
    1410: 1410,  # Blue Candle - 蓝色蜡烛
    1411: 1411,  # Brown Candle - 棕色蜡烛
    1412: 1412,  # Green Candle - 绿色蜡烛
    1413: 1413,  # Red Candle - 红色蜡烛
    1414: 1414,  # Black Candle - 黑色蜡烛
    1415: 1415,  # Small Amethyst Bud - 小型紫晶芽
    1416: 1416,  # Medium Amethyst Bud - 中型紫晶芽
    1417: 1417,  # Large Amethyst Bud - 大型紫晶芽
    1418: 1418,  # Amethyst Cluster - 紫水晶簇
    1419: 1419,  # Pointed Dripstone - 滴水石锥
    1420: 1420,  # Ochre Froglight - 赭黄蛙光体
    1421: 1421,  # Verdant Froglight - 青翠蛙光体
    1422: 1422,  # Pearlescent Froglight - 珠光蛙光体
    1423: 1423,  # Frogspawn - 青蛙卵
    1424: 1424,  # Echo Shard - 回响碎片
    1425: 1425,  # Brush - 刷子
    1426: 1426,  # Netherite Upgrade Smithing Template - 下界合金升级模板
    1427: 1427,  # Sentry Armor Trim Smithing Template - 哨兵盔甲纹饰模板
    1428: 1428,  # Dune Armor Trim Smithing Template - 沙丘盔甲纹饰模板
    1429: 1429,  # Coast Armor Trim Smithing Template - 海岸盔甲纹饰模板
    1430: 1430,  # Wild Armor Trim Smithing Template - 荒野盔甲纹饰模板
    1431: 1431,  # Ward Armor Trim Smithing Template - 监守盔甲纹饰模板
    1432: 1432,  # Eye Armor Trim Smithing Template - 眼眸盔甲纹饰模板
    1433: 1433,  # Vex Armor Trim Smithing Template - 恼鬼盔甲纹饰模板
    1434: 1434,  # Tide Armor Trim Smithing Template - 潮汐盔甲纹饰模板
    1435: 1435,  # Snout Armor Trim Smithing Template - 猪鼻盔甲纹饰模板
    1436: 1436,  # Rib Armor Trim Smithing Template - 肋骨盔甲纹饰模板
    1437: 1437,  # Spire Armor Trim Smithing Template - 尖塔盔甲纹饰模板
    1438: 1438,  # Wayfinder Armor Trim Smithing Template - 向导盔甲纹饰模板
    1439: 1439,  # Shaper Armor Trim Smithing Template - 塑造盔甲纹饰模板
    1440: 1440,  # Silence Armor Trim Smithing Template - 沉默盔甲纹饰模板
    1441: 1441,  # Raiser Armor Trim Smithing Template - 牧民盔甲纹饰模板
    1442: 1442,  # Host Armor Trim Smithing Template - 主人盔甲纹饰模板
    1443: 1443,  # Flow Armor Trim Smithing Template - 涡流盔甲纹饰模板
    1444: 1444,  # Bolt Armor Trim Smithing Template - 镶铆盔甲纹饰模板
    1445: 1445,  # Angler Pottery Sherd - 垂钓陶片
    1446: 1446,  # Archer Pottery Sherd - 弓箭陶片
    1447: 1447,  # Arms Up Pottery Sherd - 举臂陶片
    1448: 1448,  # Blade Pottery Sherd - 利刃陶片
    1449: 1449,  # Brewer Pottery Sherd - 佳酿陶片
    1450: 1450,  # Burn Pottery Sherd - 烈焰陶片
    1451: 1451,  # Danger Pottery Sherd - 危机陶片
    1452: 1452,  # Explorer Pottery Sherd - 探险陶片
    1453: 1453,  # Flow Pottery Sherd - 涡流陶片
    1454: 1454,  # Friend Pottery Sherd - 好友陶片
    1455: 1455,  # Guster Pottery Sherd - 旋风陶片
    1456: 1456,  # Heart Pottery Sherd - 爱心陶片
    1457: 1457,  # Heartbreak Pottery Sherd - 心碎陶片
    1458: 1458,  # Howl Pottery Sherd - 狼嚎陶片
    1459: 1459,  # Miner Pottery Sherd - 采矿陶片
    1460: 1460,  # Mourner Pottery Sherd - 悲恸陶片
    1461: 1461,  # Plenty Pottery Sherd - 富饶陶片
    1462: 1462,  # Prize Pottery Sherd - 珍宝陶片
    1463: 1463,  # Scrape Pottery Sherd - 树皮陶片
    1464: 1464,  # Sheaf Pottery Sherd - 麦捆陶片
    1465: 1465,  # Shelter Pottery Sherd - 树荫陶片
    1466: 1466,  # Skull Pottery Sherd - 头颅陶片
    1467: 1467,  # Snort Pottery Sherd - 嗅探陶片
    1468: 1468,  # Copper Grate - 铜格栅
    1469: 1469,  # Exposed Copper Grate - 斑驳的铜格栅
    1470: 1470,  # Weathered Copper Grate - 锈蚀的铜格栅
    1471: 1471,  # Oxidized Copper Grate - 氧化的铜格栅
    1472: 1472,  # Waxed Copper Grate - 涂蜡铜格栅
    1473: 1473,  # Waxed Exposed Copper Grate - 涂蜡斑驳铜格栅
    1474: 1474,  # Waxed Weathered Copper Grate - 涂蜡锈蚀铜格栅
    1475: 1475,  # Waxed Oxidized Copper Grate - 涂蜡氧化铜格栅
    1476: 1476,  # Copper Bulb - 铜灯
    1477: 1477,  # Exposed Copper Bulb - 斑驳铜灯
    1478: 1478,  # Weathered Copper Bulb - 锈蚀铜灯
    1479: 1479,  # Oxidized Copper Bulb - 氧化铜灯
    1480: 1480,  # Waxed Copper Bulb - 涂蜡铜灯
    1481: 1481,  # Waxed Exposed Copper Bulb - 涂蜡斑驳铜灯
    1482: 1482,  # Waxed Weathered Copper Bulb - 涂蜡锈蚀铜灯
    1483: 1483,  # Waxed Oxidized Copper Bulb - 涂蜡氧化铜灯
    1500: 1500,  # Trial Spawner - 试炼刷怪笼
    1501: 1501,  # Trial Key - 试炼钥匙
    1502: 1502,  # Ominous Trial Key - 不祥试炼钥匙
    1503: 1503,  # Vault -  vault
    1504: 1504,  # Ominous Bottle - 不祥之瓶
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
        return 28  # 土块
