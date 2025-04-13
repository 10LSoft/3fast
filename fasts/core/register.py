import importlib
from typing import List

from fastapi import FastAPI


def register_apps(
    applications: List[str],
    project_name: str,
    app: FastAPI,
    root_app: str | None = None
):
    """
    Registra os aplicativos dentro do servidor.
    """

    for app_name in applications:
        # Registering the backend apps
        try:
            if project_name:
                backend_module_path = f"{project_name}.apps.{app_name}.api"
            else:
                backend_module_path = f"apps.{app_name}.api"

            backend_module = importlib.import_module(backend_module_path)

            if hasattr(backend_module, "router"):
                app.include_router(
                    backend_module.router,
                    prefix=f"/api/{app_name.lower()}",
                    tags=[app_name.lower()],
                )
            else:
                print(f"App {app_name} has no api backend.")
        except Exception as e:
            print(f"Backend register {app_name}: {e}")

        # Registering the frontend apps
        try:
            if project_name:
                frontend_module_path = f"{project_name}.apps.{app_name}.pages"
            else:
                frontend_module_path = f"apps.{app_name}.pages"

            frontend_module = importlib.import_module(frontend_module_path)

            if hasattr(frontend_module, "app"):
                app.mount(
                    '' if root_app == app_name else f"/{app_name}",
                    frontend_module.app,
                    name=f"{app_name}-front"
                )
            else:
                print(f"App {app_name} has no frontend pages.")
        except Exception as e:
            print(f"Frontend register {app_name}: {e}")
