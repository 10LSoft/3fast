from typing import Callable, Dict
from urllib.parse import quote

from fastapi import APIRouter

router = APIRouter()
named_routes: Dict[str, str] = {}


def route(path: str, *, name: str | None = None, **kwargs):
    """Decorador que registra rota nomeada e adiciona no router."""
    def decorator(func: Callable):
        router.add_api_route(path, func, name=name, **kwargs)
        if name:
            named_routes[name] = path
        return func
    return decorator


def reverse(name: str, **kwargs) -> str:
    """Gera URL a partir do nome da rota e parâmetros."""
    path = named_routes.get(name)
    if not path:
        raise ValueError(f"Named route '{name}' not found.")
    
    for key, value in kwargs.items():
        path = path.replace(f"{{{key}}}", quote(str(value)))
    return path
