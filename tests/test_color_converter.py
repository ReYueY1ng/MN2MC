import pytest
from mn2mc.utils.color_converter import (
    convert_minecraft_to_miniworld,
    process_string,
    MINECRAFT_TO_MINIWORLD,
    STYLE_CODES,
)


class TestConvertMinecraftToMiniworld:
    """Test convert_minecraft_to_miniworld function."""

    def test_empty_string(self):
        assert convert_minecraft_to_miniworld("") == ""

    def test_none_input(self):
        assert convert_minecraft_to_miniworld(None) is None

    def test_plain_text_no_codes(self):
        assert convert_minecraft_to_miniworld("hello world") == "hello world"

    def test_section_sign_color_codes(self):
        # §a = green
        result = convert_minecraft_to_miniworld("§ahello")
        assert result == "#Ghello"

    def test_ampersand_color_codes(self):
        # &a = green
        result = convert_minecraft_to_miniworld("&ahello")
        assert result == "#Ghello"

    def test_section_sign_black(self):
        result = convert_minecraft_to_miniworld("§0text")
        assert result == "#Ktext"

    def test_section_sign_white(self):
        result = convert_minecraft_to_miniworld("§ftext")
        assert result == "#Wtext"

    def test_section_sign_red(self):
        result = convert_minecraft_to_miniworld("§4text")
        assert result == "#Rtext"

    def test_section_sign_blue(self):
        result = convert_minecraft_to_miniworld("§1text")
        assert result == "#Btext"

    def test_section_sign_yellow(self):
        result = convert_minecraft_to_miniworld("§6text")
        assert result == "#Ytext"

    def test_hex_color_section_sign(self):
        # §#RRGGBB → #cRRGGBB
        result = convert_minecraft_to_miniworld("§#349FDAtext")
        assert result == "#c349FDAtext"

    def test_hex_color_ampersand(self):
        # &#RRGGBB → #cRRGGBB
        result = convert_minecraft_to_miniworld("&#00FF00text")
        assert result == "#c00FF00text"

    def test_hex_color_red(self):
        result = convert_minecraft_to_miniworld("§#FF0000text")
        assert result == "#cFF0000text"

    def test_style_codes_removed(self):
        # §l (bold), §o (italic), §r (reset) should be removed
        result = convert_minecraft_to_miniworld("§lbold§ritalic")
        assert result == "bolditalic"

    def test_style_codes_with_ampersand(self):
        result = convert_minecraft_to_miniworld("&lbold&ritalic")
        assert result == "bolditalic"

    def test_all_style_codes(self):
        for style in STYLE_CODES:
            result = convert_minecraft_to_miniworld(f"before§{style}after")
            assert result == "beforeafter"

    def test_multiple_colors(self):
        result = convert_minecraft_to_miniworld("§aGreen§bCyan")
        assert result == "#GGreen#c00FFFFCyan"

    def test_mixed_section_and_ampersand(self):
        # Only one prefix type at a time is expected, but function handles both
        result = convert_minecraft_to_miniworld("§ared&bblue")
        # &b should be converted since it's a standard color code
        assert "#Gred" in result

    def test_case_insensitive_hex(self):
        result = convert_minecraft_to_miniworld("§#abcdef")
        assert result == "#cabcdef"

    def test_uppercase_hex(self):
        result = convert_minecraft_to_miniworld("§#ABCDEF")
        assert result == "#cABCDEF"

    def test_purple_color(self):
        result = convert_minecraft_to_miniworld("§5text")
        assert result == "#c9900fftext"

    def test_pink_color(self):
        result = convert_minecraft_to_miniworld("§dtext")
        assert result == "#cFF0aFFtext"

    def test_gray_color(self):
        result = convert_minecraft_to_miniworld("§7text")
        assert result == "#c4F4F2Ftext"

    def test_deep_gray_maps_to_black(self):
        # §8 → #K (black)
        result = convert_minecraft_to_miniworld("§8text")
        assert result == "#Ktext"

    def test_complex_message(self):
        text = "§a欢迎来到 §b迷你世界！"
        result = convert_minecraft_to_miniworld(text)
        assert "#G欢迎来到" in result
        assert "#c00FFFF迷你世界！" in result

    def test_style_code_k_removed(self):
        result = convert_minecraft_to_miniworld("§kobfuscated")
        assert result == "obfuscated"

    def test_style_code_l_removed(self):
        result = convert_minecraft_to_miniworld("§lbold")
        assert result == "bold"

    def test_style_code_m_removed(self):
        result = convert_minecraft_to_miniworld("§mstrikethrough")
        assert result == "strikethrough"

    def test_style_code_n_removed(self):
        result = convert_minecraft_to_miniworld("§nunderline")
        assert result == "underline"

    def test_style_code_o_removed(self):
        result = convert_minecraft_to_miniworld("§oitalic")
        assert result == "italic"


class TestProcessString:
    """Test process_string function."""

    def test_empty_string(self):
        assert process_string("") == ""

    def test_none_input(self):
        assert process_string(None) is None

    def test_section_sign_default(self):
        result = process_string("§ahello")
        assert result == "#Ghello"

    def test_ampersand_mode(self):
        result = process_string("&ahello", use_ampersand=True)
        assert result == "#Ghello"

    def test_section_sign_with_ampersand_mode(self):
        # When use_ampersand=True, § is replaced with &
        result = process_string("§ahello", use_ampersand=True)
        assert result == "#Ghello"

    def test_ampersand_with_default_mode(self):
        # When use_ampersand=False, & is replaced with §
        result = process_string("&ahello", use_ampersand=False)
        assert result == "#Ghello"

    def test_hex_with_ampersand_mode(self):
        result = process_string("&#FF0000red", use_ampersand=True)
        assert result == "#cFF0000red"

    def test_plain_text(self):
        assert process_string("hello", use_ampersand=True) == "hello"
        assert process_string("hello", use_ampersand=False) == "hello"

    def test_style_removal_with_section(self):
        result = process_string("§lbold§r", use_ampersand=False)
        assert result == "bold"

    def test_style_removal_with_ampersand(self):
        result = process_string("&lbold&r", use_ampersand=True)
        assert result == "bold"
