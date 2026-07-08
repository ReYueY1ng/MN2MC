"""Inventory and container management for MC protocol."""
from __future__ import annotations

import threading


class MCInventory:
    """Manages MC inventory, containers, and pending items."""

    MAX_PENDING_ITEMS = 1000

    def __init__(self) -> None:
        self.window_id: int = 0
        self.inventory_type: str | int = "inventory"
        self.container_sequence: int = 0
        self.block_sequence: int = 0
        self.container_ts: float = 0.0
        self._open_pending: bool = False
        self._pending_grids: int = 0
        self._pending_item_packets: list[tuple[int, bytes]] = []
        self._open_timer: threading.Timer | None = None
        self._lock = threading.Lock()

    def reset(self) -> None:
        """Reset all inventory/container state."""
        self.window_id = 0
        self.inventory_type = "inventory"
        self.container_sequence = 0
        self.block_sequence = 0
        self.container_ts = 0.0
        self._open_pending = False
        self._pending_grids = 0
        self._pending_item_packets = []
        self._open_timer = None
