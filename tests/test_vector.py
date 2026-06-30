import sys
import types
from unittest.mock import MagicMock

import pytest

# Mock the proto package chain before importing vector
# This avoids the circular import / missing ch_ver2.py issue
_proto_common = types.ModuleType("mn2mc.mini.proto.common")


class MockPB_Vector3:
    def __init__(self, X=0, Y=0, Z=0):
        self.X = X
        self.Y = Y
        self.Z = Z


class MockPB_Vector3f:
    def __init__(self, X=0.0, Y=0.0, Z=0.0):
        self.X = X
        self.Y = Y
        self.Z = Z


_proto_common.PB_Vector3 = MockPB_Vector3
_proto_common.PB_Vector3f = MockPB_Vector3f

# Inject mocks into sys.modules before vector.py tries to import
_mock_proto = types.ModuleType("mn2mc.mini.proto")
_mock_proto.common = _proto_common
_mock_proto.ch = MagicMock()
_mock_proto.ch_ver2 = MagicMock()
_mock_proto.hc = MagicMock()
_mock_proto.hc_ver2 = MagicMock()

sys.modules.setdefault("mn2mc.mini.proto", _mock_proto)
sys.modules.setdefault("mn2mc.mini.proto.common", _proto_common)

from mn2mc.utils.vector import Vector3, Vector3f  # noqa: E402

PB_Vector3 = MockPB_Vector3
PB_Vector3f = MockPB_Vector3f


class TestVector3:
    """Test Vector3 (int) dataclass."""

    def test_default_construction(self):
        v = Vector3()
        assert v.x == 0
        assert v.y == 0
        assert v.z == 0

    def test_construction_with_values(self):
        v = Vector3(1, 2, 3)
        assert v.x == 1
        assert v.y == 2
        assert v.z == 3

    def test_construction_negative(self):
        v = Vector3(-10, -20, -30)
        assert v.x == -10
        assert v.y == -20
        assert v.z == -30

    def test_convert(self):
        v = Vector3(10, 20, 30)
        result = v.convert()
        assert result.x == -10
        assert result.y == 20
        assert result.z == 30

    def test_convert_negative_x(self):
        v = Vector3(-5, 10, 15)
        result = v.convert()
        assert result.x == 5
        assert result.y == 10
        assert result.z == 15

    def test_from_mini_vector3(self):
        """from_mini with PB_Vector3 object."""
        mock_pb = PB_Vector3(X=100, Y=200, Z=300)
        v = Vector3.from_mini(mock_pb)
        assert v.x == 100
        assert v.y == 200
        assert v.z == 300

    def test_from_mini_vector3f(self):
        """from_mini with PB_Vector3f object (multiplies by 100)."""
        mock_pb = PB_Vector3f(X=1.5, Y=2.5, Z=3.5)
        v = Vector3.from_mini(mock_pb)
        assert v.x == 150
        assert v.y == 250
        assert v.z == 350

    def test_to_mini(self):
        v = Vector3(10, 20, 30)
        result = v.to_mini()
        assert isinstance(result, PB_Vector3)
        assert result.X == 10
        assert result.Y == 20
        assert result.Z == 30

    def test_to_vec3f(self):
        v = Vector3(100, 200, 300)
        result = v.to_vec3f()
        assert isinstance(result, Vector3f)
        assert result.x == pytest.approx(1.0)
        assert result.y == pytest.approx(2.0)
        assert result.z == pytest.approx(3.0)

    def test_to_dict(self):
        v = Vector3(1, 2, 3)
        d = v.to_dict()
        assert d == {"x": 1, "y": 2, "z": 3}

    def test_from_dict(self):
        d = {"x": 10, "y": 20, "z": 30}
        v = Vector3.from_dict(d)
        assert v.x == 10
        assert v.y == 20
        assert v.z == 30

    def test_roundtrip_dict(self):
        v = Vector3(5, 10, 15)
        d = v.to_dict()
        v2 = Vector3.from_dict(d)
        assert v == v2

    def test_roundtrip_convert(self):
        """convert twice should return to original."""
        v = Vector3(10, 20, 30)
        v2 = v.convert().convert()
        assert v2.x == 10
        assert v2.y == 20
        assert v2.z == 30


class TestVector3f:
    """Test Vector3f (float) dataclass."""

    def test_default_construction(self):
        v = Vector3f()
        assert v.x == 0.0
        assert v.y == 0.0
        assert v.z == 0.0

    def test_construction_with_values(self):
        v = Vector3f(1.5, 2.5, 3.5)
        assert v.x == 1.5
        assert v.y == 2.5
        assert v.z == 3.5

    def test_construction_negative(self):
        v = Vector3f(-1.0, -2.0, -3.0)
        assert v.x == -1.0
        assert v.y == -2.0
        assert v.z == -3.0

    def test_convert(self):
        v = Vector3f(1.5, 2.5, 3.5)
        result = v.convert()
        assert result.x == -1.5
        assert result.y == 2.5
        assert result.z == 3.5

    def test_convert_negative_x(self):
        v = Vector3f(-0.5, 1.0, 1.5)
        result = v.convert()
        assert result.x == 0.5
        assert result.y == 1.0
        assert result.z == 1.5

    def test_from_mini_vector3(self):
        """from_mini with PB_Vector3 object (divides by 100)."""
        mock_pb = PB_Vector3(X=150, Y=250, Z=350)
        v = Vector3f.from_mini(mock_pb)
        assert v.x == pytest.approx(1.5)
        assert v.y == pytest.approx(2.5)
        assert v.z == pytest.approx(3.5)

    def test_from_mini_vector3f(self):
        """from_mini with PB_Vector3f object."""
        mock_pb = PB_Vector3f(X=1.5, Y=2.5, Z=3.5)
        v = Vector3f.from_mini(mock_pb)
        assert v.x == pytest.approx(1.5)
        assert v.y == pytest.approx(2.5)
        assert v.z == pytest.approx(3.5)

    def test_to_mini(self):
        v = Vector3f(1.5, 2.5, 3.5)
        result = v.to_mini()
        assert isinstance(result, PB_Vector3f)
        assert result.X == pytest.approx(1.5)
        assert result.Y == pytest.approx(2.5)
        assert result.Z == pytest.approx(3.5)

    def test_to_vec3(self):
        v = Vector3f(1.5, 2.5, 3.5)
        result = v.to_vec3()
        assert isinstance(result, Vector3)
        assert result.x == 150
        assert result.y == 250
        assert result.z == 350

    def test_to_dict(self):
        v = Vector3f(1.5, 2.5, 3.5)
        d = v.to_dict()
        assert d == {"x": 1.5, "y": 2.5, "z": 3.5}

    def test_from_dict(self):
        d = {"x": 1.5, "y": 2.5, "z": 3.5}
        v = Vector3f.from_dict(d)
        assert v.x == pytest.approx(1.5)
        assert v.y == pytest.approx(2.5)
        assert v.z == pytest.approx(3.5)

    def test_roundtrip_dict(self):
        v = Vector3f(0.5, 1.0, 1.5)
        d = v.to_dict()
        v2 = Vector3f.from_dict(d)
        assert v == v2

    def test_roundtrip_convert(self):
        """convert twice should return to original."""
        v = Vector3f(1.5, 2.5, 3.5)
        v2 = v.convert().convert()
        assert v2.x == pytest.approx(1.5)
        assert v2.y == pytest.approx(2.5)
        assert v2.z == pytest.approx(3.5)


class TestVectorCrossConversions:
    """Test cross-conversion between Vector3 and Vector3f."""

    def test_vector3_to_vec3f_and_back(self):
        v = Vector3(100, 200, 300)
        vf = v.to_vec3f()
        v2 = vf.to_vec3()
        assert v == v2

    def test_vector3f_to_vec3_and_back(self):
        vf = Vector3f(1.0, 2.0, 3.0)
        v = vf.to_vec3()
        vf2 = v.to_vec3f()
        assert vf2.x == pytest.approx(1.0)
        assert vf2.y == pytest.approx(2.0)
        assert vf2.z == pytest.approx(3.0)
