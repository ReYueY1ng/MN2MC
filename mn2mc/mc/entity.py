from __future__ import annotations

import minebase
from dataclasses import dataclass, field
from typing import Optional

from mn2mc.config import config
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f

entitytypes: dict[str, int] = {}
for entitydata in minebase.load_version(config.mc["version"])['entities']:
    entitytypes[entitydata['name']] = entitydata['id']


@dataclass
class MCEntity:
    pos: Vector3f
    angle: Angle
    type: int
    motion: Vector3f = field(default_factory=Vector3f)
    uin: Optional[int] = None