"""
Block-state hash lookup for the 1.58 chunk builder.

The game reader (libsandboxengine SectionPaletteDecoder @0x1807F9210) resolves a
palette entry's effective BlockState via ``BlockStateContainer_FindState``
(libMiniBlock @0x1800482C0), a binary search over the block state's sorted
container keyed by (hash, data). The wire StateTable carries:

    f0 = state hash      (lookup key 0)
    f1 = state data      (lookup key 1 - real saves omit it, i.e. 0)
    f2 = variant value   (validated then set on the resolved state)

A wrong/zero hash makes the lookup fail and the block falls back to its base
variant. This module provides the hash so variants actually apply.

Sources for the table (schema/block_state_hashes.json):
  1. Real 1.58.0 / 1.58.2 saves (test/real_chunk_158_*.bin)
  2. Frida runtime dump of the live game registry (tools/capture_state_hashes.js)
"""

import json
import os
from functools import lru_cache
from typing import Dict, List, Tuple

# Hash of the "empty / no-property" block state — real 1.58 saves write this for
# every single-state block whose definition carries no properties (9/10 blocks
# in real_chunk_158_0.bin). FindState((DEFAULT, 0)) succeeds for such blocks, so
# writing it as the fallback makes variants work for the common case and is a
# safe no-op otherwise (lookup fails -> base state).
DEFAULT_STATE_HASH = 0x2B461888

_TABLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "block_state_hashes.json")


def _load_table() -> Dict[int, List[Tuple[int, int, int]]]:
    """Load {block_id: [(hash, data, extra), ...]} from the bundled JSON."""
    with open(_TABLE_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)
    blocks: Dict[int, List[Tuple[int, int, int]]] = {}
    for key, states in raw.get("blocks", {}).items():
        bid = int(key, 16)
        blocks[bid] = [
            (int(s["hash"], 16), int(s.get("data", 0)), int(s.get("extra", 0)))
            for s in states
        ]
    return blocks


_TABLE = _load_table()


@lru_cache(maxsize=None)
def state_hash_for(block_id: int, state_data: int = 0) -> int:
    """Return the state hash to write for (block_id, state_data).

    Strategy:
      - exact match: a table state whose extra == state_data -> its hash
      - any state: first table entry's hash (block known)
      - unknown block -> DEFAULT_STATE_HASH
    """
    states = _TABLE.get(block_id)
    if states:
        for h, _d, extra in states:
            if extra == state_data:
                return h
        return states[0][0]
    return DEFAULT_STATE_HASH


def known_hashes(block_id: int) -> List[Tuple[int, int, int]]:
    """Raw table entries for a block id (empty list if unknown)."""
    return _TABLE.get(block_id, [])


def table_size() -> int:
    return len(_TABLE)
