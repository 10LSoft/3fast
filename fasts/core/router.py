from fastapi import APIRouter
from fasthtml.common import fast_app


class Routers:
    """
    Esta classe tem como objetivo fornecer objetos singleton para representar
    as rotas de frontend e backend para uso nas pages (frontend) e api
    (backend).
    """
    _front_route = None
    _back_route = None

    @classmethod
    def frontend(cls):
        """Retorna o roteador de frontend (FastHTML)."""
        if not cls._front_route:
            cls._front_route, _ = fast_app(live=True)

        return cls._front_route

    @classmethod
    def backend(cls):
        """Retorna o roteador de backend (FastAPI)."""
        if not cls._back_route:
            cls._back_route = APIRouter()

        return cls._back_route


__all__ = ['Routers']
