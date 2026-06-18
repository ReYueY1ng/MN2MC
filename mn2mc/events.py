"""Unified event system for MN2MC.

Supports both int keys (mini world msgcodes) and str keys (minecraft event names).
Handler dispatch supports both sync and async functions.
"""

import inspect
from typing import TYPE_CHECKING, Any, Callable, Optional

from loguru import logger


class EventManager:
    """Central event registry for MN2MC packet handlers."""

    def __init__(self) -> None:
        self.events: dict[int | str, list[Optional[Callable]]] = {}

    def add_event(self, event_key: int | str, func: Callable) -> int:
        """Register an event handler.

        Args:
            event_key: Event identifier (int for mini world, str for minecraft).
            func: Handler function to call when event fires.

        Returns:
            Index of the registered handler (used for del_event).
        """
        self._check_event(event_key)
        self.events[event_key].append(func)
        return len(self.events[event_key]) - 1

    def del_event(self, event_key: int | str, index: int) -> None:
        """Remove an event handler by index.

        Args:
            event_key: Event identifier.
            index: Handler index returned by add_event.
        """
        self._check_event(event_key)
        self.events[event_key][index] = None

    def reset_events(self) -> None:
        """Clear all registered event handlers.

        Uses dict.clear() to preserve references held by importers
        (e.g. mc/packet.py's ``from mn2mc.events import events``).
        """
        self.events.clear()

    def _check_event(self, event_key: int | str) -> None:
        """Ensure event key exists in registry."""
        if event_key not in self.events:
            self.events[event_key] = []

    async def on_event(self, event_key: int | str, *args: Any, **kwargs: Any) -> None:
        """Trigger all handlers for an event.

        Supports both sync and async handlers. Sync handlers are called directly;
        async handlers are awaited.

        Args:
            event_key: Event identifier.
            *args: Positional arguments passed to each handler.
            **kwargs: Keyword arguments passed to each handler.
        """
        self._check_event(event_key)
        for func in self.events[event_key]:
            if func is None:
                continue
            try:
                if inspect.iscoroutinefunction(func):
                    await func(*args, **kwargs)
                else:
                    func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Exception occurred: {str(e)}")


# Module-level singleton
event_manager = EventManager()

# Module-level aliases for backward-compatible imports
# ``from mn2mc.events import add_event, events`` still works.
add_event = event_manager.add_event
del_event = event_manager.del_event
reset_events = event_manager.reset_events
on_event = event_manager.on_event

if TYPE_CHECKING:
    events: dict[int | str, list[Optional[Callable]]]


def __getattr__(name: str) -> Any:
    """Proxy attribute access to the singleton so ``mn2mc.events.events`` works."""
    if name == "events":
        return event_manager.events
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
