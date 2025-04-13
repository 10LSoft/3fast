import os
from . import settings


TORTOISE_ORM = {
    "connections": {
        "default": os.getenv(
            "DATABASE_URL",
            # "sqlite://fasts.sqlite3"
            settings.DATABASE_URL,
        ),
    },
    "apps": {
        "models": {
            "models": [
                # "fasts.core.orm.models",
                "aerich.models",
                *[f'dev.apps.{app}.models' for app in settings.APPLICATIONS],
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
