from __future__ import annotations
from dataclasses import dataclass
from mn2mc.mini.proto.common import PB_Vector3, PB_Vector3f


@dataclass
class Vector3:
    x: int = 0
    y: int = 0
    z: int = 0

    def convert(self) -> Vector3:
        return Vector3(-self.x, self.y, self.z)

    @staticmethod
    def from_mini(obj) -> Vector3:
        if isinstance(obj, PB_Vector3f):
            return Vector3(int(obj.X * 100), int(obj.Y * 100), int(obj.Z * 100))
        else:
            return Vector3(obj.X, obj.Y, obj.Z)

    def to_mini(self) -> PB_Vector3:
        return PB_Vector3(X=self.x, Y=self.y, Z=self.z)

    def to_vec3f(self) -> Vector3f:
        return Vector3f(self.x / 100, self.y / 100, self.z / 100)

    def to_dict(self) -> dict:
        return {"x": self.x, "y": self.y, "z": self.z}

    @staticmethod
    def from_dict(data: dict) -> Vector3:
        return Vector3(data["x"], data["y"], data["z"])


@dataclass
class Vector3f:
    x: float = 0
    y: float = 0
    z: float = 0

    def convert(self) -> Vector3f:
        return Vector3f(-self.x, self.y, self.z)

    @staticmethod
    def from_mini(obj) -> Vector3f:
        if isinstance(obj, PB_Vector3):
            return Vector3f(obj.X / 100, obj.Y / 100, obj.Z / 100)
        else:
            return Vector3f(obj.X, obj.Y, obj.Z)

    def to_mini(self) -> PB_Vector3f:
        return PB_Vector3f(X=self.x, Y=self.y, Z=self.z)

    def to_vec3(self) -> Vector3:
        return Vector3(int(self.x * 100), int(self.y * 100), int(self.z * 100))

    def to_dict(self) -> dict:
        return {"x": self.x, "y": self.y, "z": self.z}

    @staticmethod
    def from_dict(data: dict) -> Vector3f:
        return Vector3f(data["x"], data["y"], data["z"])
