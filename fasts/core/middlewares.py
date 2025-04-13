from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from fastapi import Request

EXCLUDED_PATHS = {
    "/docs",
    "/redoc",
    "/openapi.json",
    "/favicon.ico",
}


class AddTrailingSlashMiddleware(BaseHTTPMiddleware):
    """
    If you use trailing slashes in the end of the URL.
    This is the default behavior of 3Fasts.
    """
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if (
            path != "/"
            and not path.endswith("/")
            and not path.startswith("/static")
            and not path.startswith("/media")
            and not path.startswith("/apple-touch-icon")
            and path not in EXCLUDED_PATHS
        ):
            new_url = path + "/"

            if request.url.query:
                new_url += f"?{request.url.query}"

            return RedirectResponse(url=new_url)

        return await call_next(request)
