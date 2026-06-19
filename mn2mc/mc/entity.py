from mn2mc.config import config
from typing import Optional
from dataclasses import dataclass
from mn2mc.utils.vector import Vector3f
from mn2mc.utils.angle import Angle
import minebase

entitytypes: dict[str, int] = {}
for entitydata in minebase.load_version(config.mc["version"])['entities']:
    entitytypes[entitydata['name']] = entitydata['id']

@dataclass
class MCEntity:
    pos: Vector3f
    angle: Angle
    type: int
    uin: Optional[int] = None