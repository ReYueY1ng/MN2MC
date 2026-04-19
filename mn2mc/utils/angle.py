import math


class Angle:
    """
    同时存储 yaw（方位角）和 pitch（俯仰角）的角度类。
    内部使用Minecraft的表示：yaw 和 pitch 范围均为 [-180, 180)，北方向 yaw = 0。

    Mini World uint8 格式映射规则：
        - pitch: angle → raw = round(angle * 128/180); if raw >=0: uint8 = raw else uint8 = 256+raw
        - yaw:   angle → uint8 = pitch_rule(-angle)  (先取负再按 pitch 规则)
    """

    def __init__(self, yaw_a: float, pitch_a: float):
        self.yaw = self._normalize_180(yaw_a)
        self.pitch = self._normalize_180(pitch_a)

    # ------------------------------------------------------------------
    # 内部归一化工具
    # ------------------------------------------------------------------
    @staticmethod
    def _normalize_180(angle: float) -> float:
        angle = math.fmod(angle, 360.0)
        if angle >= 180.0:
            angle -= 360.0
        elif angle < -180.0:
            angle += 360.0
        return angle

    # ------------------------------------------------------------------
    # 原有Mini World格式（float/int32/uint32）
    # ------------------------------------------------------------------
    def to_mini_yaw_float(self) -> float:
        return self._normalize_180(self.yaw)

    def to_mini_yaw_int32(self) -> int:
        return int(round(self.to_mini_yaw_float() * 1000.0))

    def to_mini_yaw_uint32(self) -> int:
        return int(round((self.yaw + 180.0) * 1000.0))

    def to_mini_pitch_float(self) -> float:
        return self.pitch

    def to_mini_pitch_int32(self) -> int:
        return int(round(self.pitch * 1000.0))

    def to_mini_pitch_uint32(self) -> int:
        return int(round((self.pitch + 180.0) * 1000.0))

    # ------------------------------------------------------------------
    # Minecraft int8 格式（线性映射）
    # ------------------------------------------------------------------
    def to_mc_int8(self):
        yaw_int8 = int(round((self.yaw + 180.0) * 255.0 / 360.0)) - 128
        pitch_int8 = int(round((self.pitch + 180.0) * 255.0 / 360.0)) - 128
        yaw_int8 = max(-128, min(127, yaw_int8))
        pitch_int8 = max(-128, min(127, pitch_int8))
        return yaw_int8, pitch_int8

    @classmethod
    def from_mc_int8(cls, yaw_int8: int, pitch_int8: int):
        yaw_0_360 = (yaw_int8 + 128) * 360.0 / 255.0
        pitch_0_360 = (pitch_int8 + 128) * 360.0 / 255.0
        yaw_a = cls._normalize_180(yaw_0_360 - 180.0)
        pitch_a = cls._normalize_180(pitch_0_360 - 180.0)
        return cls(yaw_a, pitch_a)

    # ------------------------------------------------------------------
    # Mini World uint8 格式（pitch 规则，yaw 取负后应用）
    # ------------------------------------------------------------------
    @staticmethod
    def _angle_to_uint8_pitch(angle: float) -> int:
        """pitch 转换：angle -> uint8 (0~255)"""
        raw = int(round(angle * 128.0 / 180.0))
        if raw >= 0:
            val = raw
        else:
            val = 256 + raw
        return max(0, min(255, val))

    @staticmethod
    def _uint8_to_angle_pitch(val: int) -> float:
        """pitch 逆转换：uint8 -> angle"""
        if val <= 128:
            angle = val * 180.0 / 128.0
        else:
            angle = (val - 256) * 180.0 / 128.0
        return angle

    def to_mini_uint8(self):
        """
        返回 (yaw_uint8, pitch_uint8)
        yaw: 旧版映射 round((angle + 180) * 255 / 360)
        pitch: 直接映射
        """
        # yaw_u8 = self._angle_to_uint8_pitch(-self.yaw)
        yaw_u8 = int(round((self.yaw + 180.0) * 255.0 / 360.0))
        yaw_u8 = max(0, min(255, yaw_u8))
        pitch_u8 = self._angle_to_uint8_pitch(self.pitch)
        return yaw_u8, pitch_u8

    @classmethod
    def from_mini_uint8(cls, yaw_uint8: int, pitch_uint8: int):
        """
        从Mini World的 uint8 表示创建 Angle。
        yaw: 旧版映射恢复
        pitch: 直接按 pitch 规则恢复
        """
        # yaw_neg = cls._uint8_to_angle_pitch(yaw_uint8)
        # yaw_a = -yaw_neg
        yaw_0_360 = yaw_uint8 * 360.0 / 255.0
        yaw_a = cls._normalize_180(yaw_0_360 - 180.0)
        pitch_a = cls._uint8_to_angle_pitch(pitch_uint8)
        return cls(yaw_a, pitch_a)

    # ------------------------------------------------------------------
    # 获取Minecraft原始值
    # ------------------------------------------------------------------
    def get_yaw(self) -> float:
        return self.yaw

    def get_pitch(self) -> float:
        return self.pitch

    # ------------------------------------------------------------------
    # 加减操作
    # ------------------------------------------------------------------
    def __add__(self, other):
        if isinstance(other, Angle):
            new_yaw = self.yaw + other.yaw
            new_pitch = self.pitch + other.pitch
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            dyaw, dpitch = other
            new_yaw = self.yaw + dyaw
            new_pitch = self.pitch + dpitch
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'Angle' and {type(other)}"
            )
        return Angle(new_yaw, new_pitch)

    def __sub__(self, other):
        if isinstance(other, Angle):
            new_yaw = self.yaw - other.yaw
            new_pitch = self.pitch - other.pitch
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            dyaw, dpitch = other
            new_yaw = self.yaw - dyaw
            new_pitch = self.pitch - dpitch
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: 'Angle' and {type(other)}"
            )
        return Angle(new_yaw, new_pitch)

    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.yaw = self._normalize_180(self.yaw + other.yaw)
            self.pitch = self._normalize_180(self.pitch + other.pitch)
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            dyaw, dpitch = other
            self.yaw = self._normalize_180(self.yaw + dyaw)
            self.pitch = self._normalize_180(self.pitch + dpitch)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +=: 'Angle' and {type(other)}"
            )
        return self

    def __isub__(self, other):
        if isinstance(other, Angle):
            self.yaw = self._normalize_180(self.yaw - other.yaw)
            self.pitch = self._normalize_180(self.pitch - other.pitch)
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            dyaw, dpitch = other
            self.yaw = self._normalize_180(self.yaw - dyaw)
            self.pitch = self._normalize_180(self.pitch - dpitch)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -=: 'Angle' and {type(other)}"
            )
        return self

    # ------------------------------------------------------------------
    # 从Mini World原有格式构造
    # ------------------------------------------------------------------
    @classmethod
    def from_mini_float(cls, yaw_b: float, pitch_b: float):
        yaw_a = cls._normalize_180(yaw_b - 180.0)
        pitch_a = cls._normalize_180(pitch_b)
        return cls(yaw_a, pitch_a)

    @classmethod
    def from_mini_int32(cls, yaw_int: int, pitch_int: int):
        yaw_b = yaw_int / 1000.0
        pitch_b = pitch_int / 1000.0
        return cls.from_mini_float(yaw_b, pitch_b)

    @classmethod
    def from_mini_uint32(cls, yaw_uint: int, pitch_uint: int):
        yaw_b_unsigned = yaw_uint / 1000.0
        pitch_b_unsigned = pitch_uint / 1000.0
        yaw_a = cls._normalize_180(yaw_b_unsigned - 180.0)
        pitch_a = cls._normalize_180(pitch_b_unsigned - 180.0)
        return cls(yaw_a, pitch_a)

    @classmethod
    def from_mc_float(cls, yaw_a: float, pitch_a: float):
        return cls(yaw_a, pitch_a)

    def __repr__(self):
        return f"Angle(yaw={self.yaw:.3f}, pitch={self.pitch:.3f}) [MC]"
