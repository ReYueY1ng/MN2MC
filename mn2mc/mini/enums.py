"""Mini World protocol enums and constants."""

from enum import IntEnum


class MotionStateType(IntEnum):
    RUN = 2
    JUMP = 4
    SNEAK = 6


class MoveOperation(IntEnum):
    BASE = 0
    SNEAK = 1
    FORWARD = 2
    BACK = 3
    LEFT = 4
    RIGHT = 5
    JUMP = 6
