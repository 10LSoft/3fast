from urllib.parse import urlencode

from fastapi.routing import APIRouter

router = APIRouter()
_named_routes = {}


def route(path: str, *, name: str, methods: list[str] = ["GET"]):
    def decorator(func):
        router.add_api_route(
            path,
            func,
            name=name,
            methods=methods,
        )
        _named_routes[name] = path
        return func
    return decorator


def reverse(name: str, **params) -> str:
    """
    Gera uma URL a partir do nome da rota e parâmetros nomeados.
    """
    if name not in _named_routes:
        raise ValueError(f"Route named '{name}' not found.")

    path_template = _named_routes[name]
    path = path_template

    for key, value in params.items():
        path = path.replace(f"{{{key}}}", str(value))

    # Se ainda sobrou algo com {param}, está faltando parâmetro
    if "{" in path:
        raise ValueError(f"Missing parameters for route '{name}'.")

    return path


def url(name: str, **params) -> str:
    """
    Mesmo que reverse, mas permite parâmetros extras como query strings.
    """
    query_params = {
        k: v for k, v in params.items()
        if "{" + k + "}" not in _named_routes.get(name, "")
    }

    base_url = reverse(name, **params)
    return (
        f"{base_url}?{urlencode(query_params)}" if query_params else base_url
    )
