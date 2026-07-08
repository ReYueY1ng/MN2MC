"""Tests for the singleton + __getattr__ backward-compat refactoring.

Verifies that all refactored modules (auth, room, wsconn, config, events)
expose a singleton instance at module level and that the module-level
__getattr__ proxy returns live values from that singleton.

Also verifies that the ``players`` list in mn2mc.mini.player is still
accessible as a plain module-level list.
"""

import importlib

import pytest

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def auth_mod():
    """Import mn2mc.mini.auth (triggers MiniAuth singleton creation)."""
    return importlib.import_module("mn2mc.mini.auth")


@pytest.fixture()
def room_mod():
    """Import mn2mc.mini.room (triggers MiniRoom singleton creation)."""
    return importlib.import_module("mn2mc.mini.room")


@pytest.fixture()
def wsconn_mod():
    """Import mn2mc.mini.wsconn (triggers WsConnManager singleton creation)."""
    return importlib.import_module("mn2mc.mini.wsconn")


@pytest.fixture()
def config_mod():
    """Import mn2mc.config (triggers ConfigManager singleton creation)."""
    return importlib.import_module("mn2mc.config")


@pytest.fixture()
def events_mod():
    """Import mn2mc.events (triggers EventManager singleton creation)."""
    return importlib.import_module("mn2mc.events")


@pytest.fixture()
def player_mod():
    """Import mn2mc.mini.player."""
    return importlib.import_module("mn2mc.mini.player")


# ===========================================================================
# MiniAuth (mn2mc/mini/auth.py)
# ===========================================================================


class TestMiniAuthSingleton:
    """The module-level ``auth`` object must be a MiniAuth instance."""

    def test_auth_singleton_exists(self, auth_mod):
        assert hasattr(auth_mod, "auth")

    def test_auth_has_uin(self, auth_mod):
        assert hasattr(auth_mod.auth, "uin")
        assert isinstance(auth_mod.auth.uin, int)

    def test_auth_has_api_id(self, auth_mod):
        assert hasattr(auth_mod.auth, "api_id")
        assert isinstance(auth_mod.auth.api_id, int)

    def test_auth_has_jwt(self, auth_mod):
        assert hasattr(auth_mod.auth, "jwt")
        assert isinstance(auth_mod.auth.jwt, str)

    def test_auth_has_name(self, auth_mod):
        assert hasattr(auth_mod.auth, "name")
        assert isinstance(auth_mod.auth.name, str)

    def test_auth_has_s2_s2t(self, auth_mod):
        assert hasattr(auth_mod.auth, "s2")
        assert hasattr(auth_mod.auth, "s2t")
        assert isinstance(auth_mod.auth.s2, str)
        assert isinstance(auth_mod.auth.s2t, str)


class TestMiniAuthGetattr:
    """Module-level __getattr__ must proxy to the auth singleton."""

    def test_module_uin_equals_singleton_uin(self, auth_mod):
        assert auth_mod.uin is auth_mod.auth.uin

    def test_module_api_id_equals_singleton_api_id(self, auth_mod):
        assert auth_mod.api_id is auth_mod.auth.api_id

    def test_module_jwt_equals_singleton_jwt(self, auth_mod):
        assert auth_mod.jwt is auth_mod.auth.jwt

    def test_module_name_equals_singleton_name(self, auth_mod):
        assert auth_mod.name is auth_mod.auth.name

    def test_module_s2_equals_singleton_s2(self, auth_mod):
        assert auth_mod.s2 is auth_mod.auth.s2

    def test_module_s2t_equals_singleton_s2t(self, auth_mod):
        assert auth_mod.s2t is auth_mod.auth.s2t

    def test_unknown_attr_raises(self, auth_mod):
        with pytest.raises(AttributeError):
            _ = auth_mod.nonexistent_attr


# ===========================================================================
# MiniRoom (mn2mc/mini/room.py)
# ===========================================================================


class TestMiniRoomSingleton:
    """The module-level ``room`` object must be a MiniRoom instance."""

    def test_room_singleton_exists(self, room_mod):
        assert hasattr(room_mod, "room")

    def test_room_has_room_token(self, room_mod):
        assert hasattr(room_mod.room, "room_token")
        assert isinstance(room_mod.room.room_token, str)

    def test_room_has_config(self, room_mod):
        assert hasattr(room_mod.room, "config")
        assert isinstance(room_mod.room.config, dict)

    def test_room_has_player_count(self, room_mod):
        assert hasattr(room_mod.room, "player_count")
        assert isinstance(room_mod.room.player_count, int)

    def test_room_has_session_id(self, room_mod):
        assert hasattr(room_mod.room, "session_id")
        assert isinstance(room_mod.room.session_id, str)
        assert len(room_mod.room.session_id) == 32

    def test_room_has_room_url(self, room_mod):
        assert hasattr(room_mod.room, "room_url")
        assert isinstance(room_mod.room.room_url, str)


class TestMiniRoomGetattr:
    """Module-level __getattr__ must proxy whitelisted attrs to the room singleton."""

    def test_module_room_token_equals_singleton(self, room_mod):
        assert room_mod.room_token is room_mod.room.room_token

    def test_module_config_equals_singleton(self, room_mod):
        assert room_mod.config is room_mod.room.config

    def test_module_player_count_equals_singleton(self, room_mod):
        assert room_mod.player_count is room_mod.room.player_count

    def test_module_session_id_equals_singleton(self, room_mod):
        assert room_mod.session_id is room_mod.room.session_id

    def test_module_room_url_equals_singleton(self, room_mod):
        assert room_mod.room_url is room_mod.room.room_url

    def test_module_set_player_count_is_method(self, room_mod):
        assert callable(room_mod.set_player_count)

    def test_unknown_attr_raises(self, room_mod):
        with pytest.raises(AttributeError):
            _ = room_mod.nonexistent_attr


# ===========================================================================
# WsConnManager (mn2mc/mini/wsconn.py)
# ===========================================================================


class TestWsConnManagerSingleton:
    """The module-level ``wsconn`` object must be a WsConnManager instance."""

    def test_wsconn_singleton_exists(self, wsconn_mod):
        assert hasattr(wsconn_mod, "wsconn")

    def test_wsconn_has_s2(self, wsconn_mod):
        assert hasattr(wsconn_mod.wsconn, "s2")
        assert isinstance(wsconn_mod.wsconn.s2, str)

    def test_wsconn_has_s2t(self, wsconn_mod):
        assert hasattr(wsconn_mod.wsconn, "s2t")
        assert isinstance(wsconn_mod.wsconn.s2t, str)

    def test_wsconn_has_encode(self, wsconn_mod):
        assert callable(wsconn_mod.wsconn.encode)

    def test_wsconn_has_decode(self, wsconn_mod):
        assert callable(wsconn_mod.wsconn.decode)


class TestWsConnManagerGetattr:
    """Module-level __getattr__ must proxy to the wsconn singleton."""

    def test_module_s2_equals_singleton(self, wsconn_mod):
        assert wsconn_mod.s2 is wsconn_mod.wsconn.s2

    def test_module_s2t_equals_singleton(self, wsconn_mod):
        assert wsconn_mod.s2t is wsconn_mod.wsconn.s2t

    def test_module_encode_equals_singleton(self, wsconn_mod):
        assert wsconn_mod.encode is wsconn_mod.wsconn.encode

    def test_module_decode_equals_singleton(self, wsconn_mod):
        assert wsconn_mod.decode is wsconn_mod.wsconn.decode

    def test_unknown_attr_raises(self, wsconn_mod):
        with pytest.raises(AttributeError):
            _ = wsconn_mod.nonexistent_attr


# ===========================================================================
# ConfigManager (mn2mc/config.py)
# ===========================================================================


class TestConfigManagerSingleton:
    """The module-level ``config`` object must be a ConfigManager instance."""

    def test_config_singleton_exists(self, config_mod):
        assert hasattr(config_mod, "config")

    def test_config_has_mini(self, config_mod):
        assert hasattr(config_mod.config, "mini")
        from mn2mc.config import MiniConfig
        assert isinstance(config_mod.config.mini, MiniConfig)

    def test_config_has_mc(self, config_mod):
        assert hasattr(config_mod.config, "mc")
        from mn2mc.config import MCConfig
        assert isinstance(config_mod.config.mc, MCConfig)

    def test_config_has_debug(self, config_mod):
        assert hasattr(config_mod.config, "debug")
        assert isinstance(config_mod.config.debug, bool)

    def test_config_mini_has_auth_key(self, config_mod):
        assert hasattr(config_mod.config.mini, "auth")

    def test_config_mini_has_server_key(self, config_mod):
        assert hasattr(config_mod.config.mini, "server")

    def test_config_mc_has_ip(self, config_mod):
        assert hasattr(config_mod.config.mc, "ip")

    def test_config_mc_has_port(self, config_mod):
        assert hasattr(config_mod.config.mc, "port")


class TestConfigManagerGetattr:
    """Module-level __getattr__ must proxy live values from the singleton."""

    def test_module_mini_equals_singleton(self, config_mod):
        """config.mini must be the SAME dict object as config.mini (live reference)."""
        assert config_mod.mini is config_mod.config.mini

    def test_module_mc_equals_singleton(self, config_mod):
        assert config_mod.mc is config_mod.config.mc

    def test_module_debug_equals_singleton(self, config_mod):
        assert config_mod.debug is config_mod.config.debug

    def test_module_load_is_callable(self, config_mod):
        assert callable(config_mod.load)

    def test_module_save_is_callable(self, config_mod):
        assert callable(config_mod.save)

    def test_unknown_attr_raises(self, config_mod):
        with pytest.raises(AttributeError):
            _ = config_mod.nonexistent_attr


# ===========================================================================
# EventManager (mn2mc/events.py)
# ===========================================================================


class TestEventManagerSingleton:
    """The module-level ``event_manager`` object must be an EventManager instance."""

    def test_event_manager_singleton_exists(self, events_mod):
        assert hasattr(events_mod, "event_manager")

    def test_event_manager_has_events_dict(self, events_mod):
        assert hasattr(events_mod.event_manager, "events")
        assert isinstance(events_mod.event_manager.events, dict)

    def test_event_manager_has_add_event(self, events_mod):
        assert callable(events_mod.event_manager.add_event)

    def test_event_manager_has_del_event(self, events_mod):
        assert callable(events_mod.event_manager.del_event)

    def test_event_manager_has_reset_events(self, events_mod):
        assert callable(events_mod.event_manager.reset_events)

    def test_event_manager_has_on_event(self, events_mod):
        assert callable(events_mod.event_manager.on_event)


class TestEventManagerBackwardCompat:
    """Module-level aliases and __getattr__ must work for backward compat."""

    def test_module_add_event_is_bound_to_singleton(self, events_mod):
        """add_event must be a bound method of the singleton."""
        assert events_mod.add_event.__self__ is events_mod.event_manager

    def test_module_del_event_is_bound_to_singleton(self, events_mod):
        assert events_mod.del_event.__self__ is events_mod.event_manager

    def test_module_reset_events_is_bound_to_singleton(self, events_mod):
        assert events_mod.reset_events.__self__ is events_mod.event_manager

    def test_module_on_event_is_bound_to_singleton(self, events_mod):
        assert events_mod.on_event.__self__ is events_mod.event_manager

    def test_module_events_via_getattr(self, events_mod):
        """mn2mc.events.events must resolve to event_manager.events via __getattr__."""
        assert events_mod.events is events_mod.event_manager.events

    def test_unknown_attr_raises(self, events_mod):
        with pytest.raises(AttributeError):
            _ = events_mod.nonexistent_attr


# ===========================================================================
# players list (mn2mc/mini/player.py)
# ===========================================================================


class TestPlayersList:
    """The ``players`` list must remain a plain module-level list."""

    def test_players_list_exists(self, player_mod):
        assert hasattr(player_mod, "players")

    def test_players_is_list(self, player_mod):
        assert isinstance(player_mod.players, list)
