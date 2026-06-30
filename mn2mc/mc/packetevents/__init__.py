"""Auto-import and hot-reload Minecraft packet event handlers."""

from importlib import import_module, invalidate_caches, reload
from pathlib import Path

from mn2mc.config import config

for f in Path(__file__).parent.glob("*.py"):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
    del f, module_name


def reloadevents():
    invalidate_caches()
    for f in Path(__file__).parent.glob("*.py"):
        module_name = f.stem
        if not module_name.startswith("_"):
            if module_name in globals():
                reload(globals()[module_name])
            else:
                import_module(f".{module_name}", __package__)
        del f, module_name

    chunk_name = "map_chunk"
    if config.mc["use_new_chunk_parser"]:
        chunk_name = "parsed_chunk"
    if hasattr(globals()['chunk'], chunk_name):
        reload(getattr(globals()['chunk'], chunk_name))
    else:
        import_module(f".chunk.{chunk_name}", __package__)

    del chunk_name
