"""
MITM script: intercept Mini World room registration (create_room), change
use_proxy from 0 to 1, and regenerate the auth MD5 signature.

Usage:
    mitmdump --mode local:wineserver -s tools/mitm_room_proxy.py

Or combine with the existing mitm.py (load both):
    mitmdump --mode local:wineserver -s tools/mitm.py -s tools/mitm_room_proxy.py
"""
import hashlib
import logging
import urllib.parse

from mitmproxy import http

logger = logging.getLogger(__name__)

AUTH_KEY = "f5711eb1640712de051e5aedc35329c3"

# These params appear in the query string AFTER the signed params and are NOT
# included in the auth hash calculation.
EXTEND_PARAMS_KEYS = {
    "public_type",
    "prei_room_name_idx",
    "regapiid",
    "cltapiid",
    "cltversion",
    "lang",
    "game_session_id",
    "session_id",
    "room_token",
}


def _make_auth(params: dict) -> str:
    """MD5(sorted non-None params + AUTH_KEY) — mirrors room.MiniRoom._make_auth."""
    body = "&".join(
        f"{k}={v}" for k, v in sorted(params.items()) if v is not None
    )
    return hashlib.md5((body + AUTH_KEY).encode()).hexdigest()


def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url

    # Only intercept room creation requests
    if "/server/room" not in url or "cmd=create_room" not in url:
        return

    parsed = urllib.parse.urlparse(url)
    raw_params = dict(
        urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    )

    if "auth" not in raw_params:
        return

    old_auth = raw_params.pop("auth")

    # Peel off extend params — they hang off the end of the query string but
    # are NOT part of the auth payload.
    extend_params = {}
    for key in list(raw_params.keys()):
        if key in EXTEND_PARAMS_KEYS:
            extend_params[key] = raw_params.pop(key)

    # raw_params now holds ONLY the params that feed into _make_auth
    if raw_params.get("use_proxy") != "0":
        # Nothing to patch (already 1, or missing)
        return

    raw_params["use_proxy"] = "1"
    new_auth = _make_auth(raw_params)

    # Rebuild query string: signed params first, then extend params, then auth
    ordered = {}
    ordered.update(raw_params)
    ordered.update(extend_params)
    new_query = urllib.parse.urlencode(ordered) + f"&auth={new_auth}"

    flow.request.url = urllib.parse.urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            new_query,
            parsed.fragment,
        )
    )

    uin = raw_params.get("uin", "?")
    print(
        f"[mitm_room_proxy] Patched use_proxy 0→1 for room create "
        f"(uin={uin}) — auth {old_auth[:12]}… → {new_auth[:12]}…"
    )
