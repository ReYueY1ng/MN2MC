"""Tests for the 1.58 chunk builder light table and cross-chunk light grid.

Covers build_section_light_blob (the 105 network blob) and
compute_light_grid_158 (3x3 cross-chunk light propagation), including the
regression where a light source at a chunk's right edge must illuminate the
neighbor's left edge.

Run standalone: python tests/test_chunk_builder_158.py
Run via pytest:  pytest tests/test_chunk_builder_158.py -v
"""

from __future__ import annotations

import os
import struct
import sys
import unittest

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from mn2mc.mini.chunk.chunk_builder_158 import (  # noqa: E402
    compute_light_grid_158,
)
from mn2mc.mini.chunk.section_light_blob_builder import (  # noqa: E402
    build_section_light_blob,
)
from mn2mc.mini.chunk.validate_section_light_blob import (  # noqa: E402
    verify_section_light_blob,
)


def _empty_sections(lava_idx: int | None = None) -> list[dict]:
    blocks = [0] * 4096
    if lava_idx is not None:
        blocks[lava_idx] = 5  # lava mini id (LightSrc 15)
    return [{"sec_y": 4, "blocks": blocks}]


def _nibble(data: bytes | None, linear: int) -> int:
    """Read a nibble (0..15) at linear index from a 2048-byte packed array."""
    if data is None:
        return 0
    b = data[linear >> 1]
    return b & 0xF if linear % 2 == 0 else (b >> 4) & 0xF


class TestSectionLightBlob(unittest.TestCase):
    def test_blob_4_field_structure(self):
        """105 blob: root 4-field table -> nested Layer tables (f0=sky, f1..=block)."""
        sky = bytes([0xFF] * 2048)
        block = bytes([0x0F] + [0] * 2047)
        raw = build_section_light_blob(sky, block)
        ok, reason = verify_section_light_blob(raw)
        self.assertTrue(ok, reason)  # game-equivalent verify must pass

        root = struct.unpack_from("<I", raw, 0)[0]
        soff = struct.unpack_from("<i", raw, root)[0]
        vsize, _ = struct.unpack_from("<HH", raw, root - soff)
        nf = (vsize - 4) // 2
        foffs = struct.unpack_from(f"<{nf}H", raw, root - soff + 4)
        self.assertEqual(list(foffs), [4, 8, 12, 16])  # 4 field slots

        # Each field is a uoffset to a nested Layer table, not a bare vector.
        for fi in range(4):
            pos = root + foffs[fi]
            layer = pos + struct.unpack_from("<I", raw, pos)[0]
            lsoff = struct.unpack_from("<i", raw, layer)[0]
            lvsize, _ = struct.unpack_from("<HH", raw, layer - lsoff)
            # Layer table has f0 (uoffset to vector) and optional f1 (flag)
            self.assertGreaterEqual(lvsize, 8)
            self.assertGreaterEqual(struct.unpack_from("<H", raw, layer - lsoff + 4)[0], 4)
        self.assertEqual(len(raw), 8324)

    def test_blob_verify_rejects_old_direct_vector(self):
        """The old direct-vector layout must FAIL game verify (it was dropped)."""
        from mn2mc.mini.chunk.validate_section_light_blob import (
            build_section_light_blob_old_style,
        )
        raw = build_section_light_blob_old_style(b"\xff" * 2048, b"\x0f" + b"\x00" * 2047)
        ok, _ = verify_section_light_blob(raw)
        self.assertFalse(ok)  # old structure is rejected by the game verifier

    def test_blob_rejects_bad_length(self):
        with self.assertRaises(ValueError):
            build_section_light_blob(b"\x00" * 100, b"\x00" * 2048)


class TestLightGrid(unittest.TestCase):
    def test_single_chunk_source_center(self):
        """Lava at chunk center: light 15 at source, decays to edges."""
        res = compute_light_grid_158({(0, 0): _empty_sections(lava_idx=7 * 256 + 7 * 16 + 7)})
        blk = res[(0, 0)]["block"][4]
        self.assertEqual(_nibble(blk, 7 * 256 + 7 * 16 + 7), 15)
        self.assertEqual(_nibble(blk, 7 * 256 + 7 * 16 + 8), 14)  # 1 step away

    def test_cross_chunk_right_edge(self):
        """Regression: lava at A's right edge (mini x=15) must light B's left edge.

        Previously a double x-flip mirrored chunks in the grid, so the neighbor
        got no light at all.
        """
        res = compute_light_grid_158({
            (0, 0): _empty_sections(lava_idx=15),  # A right edge, mini x=15
            (1, 0): _empty_sections(),             # B empty
        })
        b_blk = res[(1, 0)]["block"][4]
        self.assertIsNotNone(b_blk)
        self.assertEqual(_nibble(b_blk, 0), 14)   # B mini x=0, distance 1
        self.assertEqual(_nibble(b_blk, 1), 13)   # distance 2

    def test_cross_chunk_left_edge(self):
        """Lava at A's left edge (mini x=0) lights the neighbor on the other side."""
        res = compute_light_grid_158({
            (0, 0): _empty_sections(lava_idx=0),  # A left edge
            (-1, 0): _empty_sections(),           # B to the west
        })
        b_blk = res[(-1, 0)]["block"][4]
        self.assertIsNotNone(b_blk)
        self.assertEqual(_nibble(b_blk, 15), 14)  # B mini x=15 adjacent to A x=0

    def test_far_side_no_light(self):
        """Light from A's edge should not reach the far side of B (16+ blocks)."""
        res = compute_light_grid_158({
            (0, 0): _empty_sections(lava_idx=15),
            (1, 0): _empty_sections(),
        })
        b_blk = res[(1, 0)]["block"][4]
        self.assertEqual(_nibble(b_blk, 15), 0)  # mini x=15 is 16 away


if __name__ == "__main__":
    unittest.main()
