import os
from .settings import APPLICATIONS


TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL", "sqlite://fasts.sqlite3"),
    },
    "apps": {
        "models": {
            "models": [
                # "fasts.core.orm.models",
                "aerich.models",
                *[f'dev.apps.{app}.models' for app in APPLICATIONS],
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
