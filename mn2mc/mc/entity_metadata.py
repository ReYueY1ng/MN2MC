from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar, Optional, Self

from mn2mc.mc.enums import MetadataType, Pose


@dataclass
class EntityBaseMetadata:
    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {}
    _present: set[str] = field(default_factory=set, init=False, repr=False)

    @classmethod
    def from_protocol(cls, entries: list[dict]) -> Self:
        kwargs: dict[str, Any] = {}
        present: set[str] = set()
        for entry in entries:
            idx = entry["key"]
            if idx == 0xFF:
                break
            mapped = cls._INDEX_MAP.get(idx)
            if mapped is not None:
                name = mapped[0]
                kwargs[name] = entry.get("value")
                present.add(name)
        obj = cls(**kwargs)
        obj._present = present
        return obj

    def has(self, field_name: str) -> bool:
        return field_name in self._present

    def to_dict(self) -> dict[int, Any]:
        reverse = {name: idx for idx, (name, _) in self._INDEX_MAP.items()}
        out: dict[int, Any] = {}
        for name, idx in reverse.items():
            if name in self._present:
                out[idx] = getattr(self, name)
        return out


@dataclass
class EntityMetadata(EntityBaseMetadata):
    entity_flags: int = 0
    air_ticks: int = 300
    custom_name: Optional[Any] = None
    custom_name_visible: bool = False
    is_silent: bool = False
    has_no_gravity: bool = False
    pose: Pose = Pose.STANDING
    frozen_ticks: int = 0

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        0: ("entity_flags", MetadataType.BYTE),
        1: ("air_ticks", MetadataType.VARINT),
        2: ("custom_name", MetadataType.OPTIONAL_TEXT_COMPONENT),
        3: ("custom_name_visible", MetadataType.BOOLEAN),
        4: ("is_silent", MetadataType.BOOLEAN),
        5: ("has_no_gravity", MetadataType.BOOLEAN),
        6: ("pose", MetadataType.POSE),
        7: ("frozen_ticks", MetadataType.VARINT),
    }


@dataclass
class LivingEntityMetadata(EntityMetadata):
    hand_states: int = 0
    health: float = 1.0
    potion_effect_color: int = 0
    is_potion_effect_ambient: bool = False
    arrow_count: int = 0
    bee_stinger_count: int = 0
    sleeping_position: Optional[Any] = None

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        **EntityMetadata._INDEX_MAP,
        8: ("hand_states", MetadataType.BYTE),
        9: ("health", MetadataType.FLOAT),
        10: ("potion_effect_color", MetadataType.PARTICLES),
        11: ("is_potion_effect_ambient", MetadataType.BOOLEAN),
        12: ("arrow_count", MetadataType.VARINT),
        13: ("bee_stinger_count", MetadataType.VARINT),
        14: ("sleeping_position", MetadataType.OPTIONAL_POSITION),
    }


@dataclass
class AvatarMetadata(LivingEntityMetadata):
    main_hand: int = 1
    skin_parts: int = 0

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        **LivingEntityMetadata._INDEX_MAP,
        15: ("main_hand", MetadataType.BYTE),
        16: ("skin_parts", MetadataType.BYTE),
    }


@dataclass
class PlayerMetadata(AvatarMetadata):
    additional_hearts: float = 0.0
    score: int = 0
    left_shoulder_entity: Optional[int] = None
    right_shoulder_entity: Optional[int] = None

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        **AvatarMetadata._INDEX_MAP,
        17: ("additional_hearts", MetadataType.FLOAT),
        18: ("score", MetadataType.VARINT),
        19: ("left_shoulder_entity", MetadataType.OPTIONAL_VARINT),
        20: ("right_shoulder_entity", MetadataType.OPTIONAL_VARINT),
    }


@dataclass
class MobMetadata(LivingEntityMetadata):
    mob_flags: int = 0

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        **LivingEntityMetadata._INDEX_MAP,
        15: ("mob_flags", MetadataType.BYTE),
    }


@dataclass
class ItemEntityMetadata(EntityMetadata):
    item: Optional[Any] = None

    _INDEX_MAP: ClassVar[dict[int, tuple[str, MetadataType]]] = {
        **EntityMetadata._INDEX_MAP,
        8: ("item", MetadataType.SLOT),
    }
