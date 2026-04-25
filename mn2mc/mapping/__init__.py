from importlib import import_module, reload, invalidate_caches
from pathlib import Path

for f in Path(__file__).parent.glob("*.py"):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
    del f, module_name


def reload_mapping():
    invalidate_caches()
    for f in Path(__file__).parent.glob("*.py"):
        module_name = f.stem
        if not module_name.startswith("_"):
            if module_name in globals():
                reload(globals()[module_name])
            else:
                import_module(f".{module_name}", __package__)
        del f, module_name
