import pytest
import math
from mn2mc.utils.angle import Angle


class TestAngleConstruction:
    """Test Angle construction and normalization."""

    def test_basic_construction(self):
        a = Angle(90.0, 45.0)
        assert a.get_yaw() == 90.0
        assert a.get_pitch() == 45.0

    def test_zero_angles(self):
        a = Angle(0.0, 0.0)
        assert a.get_yaw() == 0.0
        assert a.get_pitch() == 0.0

    def test_negative_angles(self):
        a = Angle(-90.0, -45.0)
        assert a.get_yaw() == -90.0
        assert a.get_pitch() == -45.0

    def test_normalization_above_180(self):
        a = Angle(270.0, 200.0)
        # 270 normalized to -90, 200 normalized to -160
        assert a.get_yaw() == pytest.approx(-90.0)
        assert a.get_pitch() == pytest.approx(-160.0)

    def test_normalization_below_neg180(self):
        a = Angle(-270.0, -200.0)
        # -270 normalized to 90, -200 normalized to 160
        assert a.get_yaw() == pytest.approx(90.0)
        assert a.get_pitch() == pytest.approx(160.0)

    def test_normalization_exactly_180(self):
        a = Angle(180.0, 180.0)
        # 180 stays as 180 (>= 180 then -= 360 → -180, but -180 is the boundary)
        assert a.get_yaw() == pytest.approx(-180.0)
        assert a.get_pitch() == pytest.approx(-180.0)

    def test_normalization_360(self):
        a = Angle(360.0, 0.0)
        assert a.get_yaw() == pytest.approx(0.0)

    def test_normalization_large_values(self):
        a = Angle(720.0, -540.0)
        assert a.get_yaw() == pytest.approx(0.0)
        assert a.get_pitch() == pytest.approx(-180.0)


class TestAngleRepr:
    def test_repr(self):
        a = Angle(90.0, 45.0)
        assert "Angle(yaw=90.000, pitch=45.000)" in repr(a)
        assert "[MC]" in repr(a)


class TestAngleMCFloatConversions:
    """Test MC float format (from_mc_float is identity)."""

    def test_from_mc_float(self):
        a = Angle.from_mc_float(90.0, 45.0)
        assert a.get_yaw() == 90.0
        assert a.get_pitch() == 45.0


class TestAngleMCInt8Conversions:
    """Test MC int8 format round-trip."""

    def test_roundtrip_zero(self):
        a = Angle(0.0, 0.0)
        y8, p8 = a.to_mc_int8()
        a2 = Angle.from_mc_int8(y8, p8)
        assert a2.get_yaw() == pytest.approx(0.0, abs=2.0)
        assert a2.get_pitch() == pytest.approx(0.0, abs=2.0)

    def test_roundtrip_90(self):
        a = Angle(90.0, 0.0)
        y8, p8 = a.to_mc_int8()
        a2 = Angle.from_mc_int8(y8, p8)
        assert a2.get_yaw() == pytest.approx(90.0, abs=2.0)

    def test_int8_range(self):
        a = Angle(180.0, 90.0)
        y8, p8 = a.to_mc_int8()
        assert -128 <= y8 <= 127
        assert -128 <= p8 <= 127

    def test_int8_clamping(self):
        # Extreme values should be clamped
        a = Angle(180.0, 180.0)
        y8, p8 = a.to_mc_int8()
        assert -128 <= y8 <= 127
        assert -128 <= p8 <= 127


class TestAngleMiniFormats:
    """Test Mini World format conversions."""

    def test_mini_yaw_float(self):
        a = Angle(45.0, 30.0)
        assert a.to_mini_yaw_float() == 45.0

    def test_mini_yaw_int32(self):
        a = Angle(45.0, 30.0)
        assert a.to_mini_yaw_int32() == 45000

    def test_mini_yaw_uint32(self):
        a = Angle(0.0, 0.0)
        assert a.to_mini_yaw_uint32() == 180000

    def test_mini_pitch_float(self):
        a = Angle(45.0, 30.0)
        assert a.to_mini_pitch_float() == 30.0

    def test_mini_pitch_int32(self):
        a = Angle(45.0, 30.0)
        assert a.to_mini_pitch_int32() == 30000

    def test_mini_pitch_uint32(self):
        a = Angle(0.0, 0.0)
        assert a.to_mini_pitch_uint32() == 180000

    def test_from_mini_float(self):
        # from_mini_float subtracts 180 from yaw
        a = Angle.from_mini_float(270.0, 45.0)
        assert a.get_yaw() == pytest.approx(90.0)
        assert a.get_pitch() == pytest.approx(45.0)

    def test_from_mini_int32(self):
        # int32 is float * 1000
        a = Angle.from_mini_int32(270000, 45000)
        assert a.get_yaw() == pytest.approx(90.0)
        assert a.get_pitch() == pytest.approx(45.0)

    def test_from_mini_uint32(self):
        # uint32 is (angle + 180) * 1000
        a = Angle.from_mini_uint32(270000, 225000)
        assert a.get_yaw() == pytest.approx(90.0)
        assert a.get_pitch() == pytest.approx(45.0)

    def test_mini_uint8_roundtrip(self):
        a = Angle(45.0, 30.0)
        y8, p8 = a.to_mini_uint8()
        a2 = Angle.from_mini_uint8(y8, p8)
        assert a2.get_yaw() == pytest.approx(45.0, abs=2.0)
        assert a2.get_pitch() == pytest.approx(30.0, abs=2.0)

    def test_mini_uint8_zero(self):
        a = Angle(0.0, 0.0)
        y8, p8 = a.to_mini_uint8()
        assert 0 <= y8 <= 255
        assert 0 <= p8 <= 255

    def test_mini_uint8_negative(self):
        a = Angle(-90.0, -45.0)
        y8, p8 = a.to_mini_uint8()
        assert 0 <= y8 <= 255
        assert 0 <= p8 <= 255


class TestAngleOperators:
    """Test Angle arithmetic operators."""

    def test_add_two_angles(self):
        a1 = Angle(30.0, 20.0)
        a2 = Angle(10.0, 5.0)
        result = a1 + a2
        assert result.get_yaw() == pytest.approx(40.0)
        assert result.get_pitch() == pytest.approx(25.0)

    def test_add_tuple(self):
        a = Angle(30.0, 20.0)
        result = a + (10.0, 5.0)
        assert result.get_yaw() == pytest.approx(40.0)
        assert result.get_pitch() == pytest.approx(25.0)

    def test_add_list(self):
        a = Angle(30.0, 20.0)
        result = a + [10.0, 5.0]
        assert result.get_yaw() == pytest.approx(40.0)
        assert result.get_pitch() == pytest.approx(25.0)

    def test_add_unsupported_type(self):
        a = Angle(30.0, 20.0)
        with pytest.raises(TypeError):
            a + 5

    def test_sub_two_angles(self):
        a1 = Angle(30.0, 20.0)
        a2 = Angle(10.0, 5.0)
        result = a1 - a2
        assert result.get_yaw() == pytest.approx(20.0)
        assert result.get_pitch() == pytest.approx(15.0)

    def test_sub_tuple(self):
        a = Angle(30.0, 20.0)
        result = a - (10.0, 5.0)
        assert result.get_yaw() == pytest.approx(20.0)
        assert result.get_pitch() == pytest.approx(15.0)

    def test_sub_unsupported_type(self):
        a = Angle(30.0, 20.0)
        with pytest.raises(TypeError):
            a - "invalid"

    def test_iadd_angle(self):
        a = Angle(30.0, 20.0)
        a += Angle(10.0, 5.0)
        assert a.get_yaw() == pytest.approx(40.0)
        assert a.get_pitch() == pytest.approx(25.0)

    def test_iadd_tuple(self):
        a = Angle(30.0, 20.0)
        a += (10.0, 5.0)
        assert a.get_yaw() == pytest.approx(40.0)
        assert a.get_pitch() == pytest.approx(25.0)

    def test_iadd_unsupported_type(self):
        a = Angle(30.0, 20.0)
        with pytest.raises(TypeError):
            a += 5

    def test_isub_angle(self):
        a = Angle(30.0, 20.0)
        a -= Angle(10.0, 5.0)
        assert a.get_yaw() == pytest.approx(20.0)
        assert a.get_pitch() == pytest.approx(15.0)

    def test_isub_tuple(self):
        a = Angle(30.0, 20.0)
        a -= (10.0, 5.0)
        assert a.get_yaw() == pytest.approx(20.0)
        assert a.get_pitch() == pytest.approx(15.0)

    def test_isub_unsupported_type(self):
        a = Angle(30.0, 20.0)
        with pytest.raises(TypeError):
            a -= "invalid"

    def test_iadd_normalization(self):
        a = Angle(170.0, 170.0)
        a += (20.0, 20.0)
        # 170 + 20 = 190, normalized to -170
        assert a.get_yaw() == pytest.approx(-170.0)
        assert a.get_pitch() == pytest.approx(-170.0)

    def test_isub_normalization(self):
        a = Angle(-170.0, -170.0)
        a -= (20.0, 20.0)
        # -170 - 20 = -190, normalized to 170
        assert a.get_yaw() == pytest.approx(170.0)
        assert a.get_pitch() == pytest.approx(170.0)
