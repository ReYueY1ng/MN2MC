mc_to_mini_mapping = {
    "base": {
        35: 28,
    },
    "direct": {0: 4000, 1: 4001, 2: 4002, 3: 4003, 40: 29},
    "inventory": {
        0: 36,
        1: 31,
        2: 32,
        3: 33,
        4: 34,
        5: 4000,
        6: 4001,
        7: 4002,
        8: 4003,
        45: 29,
    },
    0: {},  # 9x1
    1: {},  # 9x2
    2: {},  # 9x3
    3: {},  # 9x4
    4: {},  # 9x5
    5: {},  # 9x6
}

for i in range(27):
    mc_to_mini_mapping["base"][i] = i

for i in range(27, 35):
    mc_to_mini_mapping["base"][i] = 1000 + i - 27

for i in range(6):
    for j in range((i + 1) * 9):
        mc_to_mini_mapping[i][j] = 3000 + j

for k, v in mc_to_mini_mapping["base"].items():
    mc_to_mini_mapping["inventory"][k + 9] = v
    mc_to_mini_mapping["direct"][k + 4] = v
    for i in range(6):
        mc_to_mini_mapping[i][k + (i + 1) * 9] = v

mini_to_mc_mapping = {}

for k, v in mc_to_mini_mapping.items():
    mini_to_mc_mapping[k] = {v: k for k, v in mc_to_mini_mapping[k].items()}


def mc_to_mini(window: int | str, id: int) -> int:
    return mc_to_mini_mapping[window][id]


def mini_to_mc(window: int | str, id: int) -> int:
    return mini_to_mc_mapping[window][id]
