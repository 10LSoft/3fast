import importlib
from pathlib import Path

from tortoise.contrib.fastapi import RegisterTortoise

# from fasts.core.orm.tortoise_config import TORTOISE_ORM
from dev.configs.databases import TORTOISE_ORM


def register_orm(app):
    RegisterTortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True
    )


def scan_models(base_path: str, base_module: str):
    model_modules = []

    for app_dir in Path(base_path).iterdir():
        if (app_dir / "models.py").exists():
            module_path = f"{base_module}.{app_dir.name}.models"
            try:
                importlib.import_module(module_path)
                model_modules.append(module_path)
            except ModuleNotFoundError:
                pass

    return model_modules
