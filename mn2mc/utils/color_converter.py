import re
from typing import Dict, List


# Minecraft 标准颜色代码与迷你世界代码的映射表
MINECRAFT_TO_MINIWORLD: Dict[str, str] = {
    # 基础颜色映射
    "0": "#K",  # 黑色
    "1": "#B",  # 深蓝 → 蓝色
    "2": "#G",  # 深绿 → 绿色
    "3": "#c00FFFF",  # 湖蓝 → 青色
    "4": "#R",  # 暗红 → 红色
    "5": "#c9900ff",  # 紫色
    "6": "#Y",  # 金色 → 黄色
    "7": "#c4F4F2F",  # 灰色
    "8": "#K",  # 深灰 → 黑色
    "9": "#B",  # 亮蓝 → 蓝色
    "a": "#G",  # 亮绿 → 绿色
    "b": "#c00FFFF",  # 水蓝 → 青色
    "c": "#R",  # 亮红 → 红色
    "d": "#cFF0aFF",  # 粉红
    "e": "#Y",  # 亮黄 → 黄色
    "f": "#W",  # 白色
}

# 需要移除的 Minecraft 样式代码（迷你世界不支持）
STYLE_CODES: List[str] = ["k", "l", "m", "n", "o", "r"]


def convert_minecraft_to_miniworld(text: str) -> str:
    """
    将包含 Minecraft 颜色代码的文本转换为迷你世界格式。

    支持格式：
        - 标准颜色代码：§a、&a
        - 十六进制颜色代码：§#RRGGBB、&#RRGGBB
        - 样式代码：§l、§o 等（会被移除）

    Args:
        text: 包含 Minecraft 颜色代码的字符串

    Returns:
        转换后的迷你世界格式字符串
    """
    if not text:
        return text

    # 1. 移除样式代码（迷你世界不支持）
    for style in STYLE_CODES:
        text = text.replace(f"§{style}", "")
        text = text.replace(f"&{style}", "")

    # 2. 处理十六进制颜色代码：§#RRGGBB 或 &#RRGGBB → #cRRGGBB
    def replace_hex(match: re.Match) -> str:
        """将 §#RRGGBB 转换为 #cRRGGBB"""
        hex_value = match.group(1)  # 6位十六进制数
        return f"#c{hex_value}"

    hex_pattern = re.compile(r"[§&]#([0-9a-fA-F]{6})")
    text = hex_pattern.sub(replace_hex, text)

    # 3. 处理标准颜色代码：§X 或 &X（X 为单个字符）
    def replace_std_color(match: re.Match) -> str:
        code = match.group(1).lower()
        return MINECRAFT_TO_MINIWORLD.get(code, "")

    std_pattern = re.compile(r"[§&]([0-9a-f])", re.IGNORECASE)
    text = std_pattern.sub(replace_std_color, text)

    # 4. 清理未被匹配的残留代码标记（可选）
    text = re.sub(r"[§&][0-9a-fk-or]", "", text, flags=re.IGNORECASE)

    return text


def process_string(text: str, use_ampersand: bool = False) -> str:
    """
    处理 Minecraft 颜色代码转换，支持选择输入格式。

    Args:
        text: 输入字符串
        use_ampersand: 如果为 True，则使用 & 作为颜色代码前缀（服务器插件格式）
                       如果为 False，则使用 § 作为前缀（原版格式）

    Returns:
        转换后的字符串
    """
    if not text:
        return text

    # 统一为 § 前缀，方便处理
    if use_ampersand:
        text = text.replace("§", "&")
    else:
        text = text.replace("&", "§")

    return convert_minecraft_to_miniworld(text)


def demo() -> None:
    """演示脚本用法"""
    test_strings = [
        "§a欢迎来到 §b迷你世界！",
        "&4重要&f提示&6: 请阅读说明",
        "§l§c警告§r: §e这是一个危险区域",
        "§#349FDA自定义颜色 §r和 §#FF5500另一个颜色",
        "&#00FF00亮绿色文本，&#FF0000红色文本",
        "混合使用：§a普通绿色和 §#AA66CC紫色调",
    ]

    print("=" * 60)
    print("Minecraft → 迷你世界 颜色代码转换演示（支持十六进制）")
    print("=" * 60)

    for original in test_strings:
        converted = convert_minecraft_to_miniworld(original)
        print(f"原文本: {original}")
        print(f"转换后: {converted}")
        print("-" * 60)

    # 交互式转换
    print("\n交互式模式：")
    while True:
        user_input = input("请输入Minecraft文本（支持 §#RRGGBB，输入 'exit' 退出）: ")
        if user_input.lower() == "exit":
            break
        if user_input.strip():
            converted = convert_minecraft_to_miniworld(user_input)
            print(f"转换结果: {converted}\n")


if __name__ == "__main__":
    demo()
