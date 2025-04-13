from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from fasts.core.lifespan import get_lifespan
from fasts.core.middlewares import AddTrailingSlashMiddleware
from fasts.core.register import register_apps

from . import settings
from .databases import TORTOISE_ORM

back_app = FastAPI(
    title=settings.PROJECT_NAME.upper(),
    description=settings.PROJECT_DESCRIPTION,
    lifespan=get_lifespan(config=TORTOISE_ORM),
)

back_app.mount(
    '/static',
    StaticFiles(directory="dev/statics/", html=True),
    name='static'
)

# Register all applications
register_apps(
    applications=settings.APPLICATIONS,
    project_name=settings.PROJECT_NAME,
    app=back_app,
    root_app=settings.ROOT_APPLICATION,
)

back_app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

back_app.add_middleware(AddTrailingSlashMiddleware)
