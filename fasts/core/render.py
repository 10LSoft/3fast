from typing import Any

from fastapi.responses import HTMLResponse
from fasthtml.common import to_xml


def render_component(component: Any) -> HTMLResponse:
    """
    Converte um componente FastHTML em uma resposta HTML do FastAPI.

    Isso mantém a flexibilidade de adicionar headers, status codes ou
    wrappers personalizados no futuro.
    """
    def fixing_animations(content: str) -> str:
        """
        Corrige a animação do componente.
        """
        return content.replace("move__", "animate__animated animate__")

    html = to_xml(component)

    return HTMLResponse(content=fixing_animations(html), status_code=200)
