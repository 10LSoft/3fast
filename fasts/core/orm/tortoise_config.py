import os

TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL", "sqlite://fasts.sqlite3"),
    },
    "apps": {
        "models": {
            "models": [
                "dev.apps",
                # "fasts.core.orm.models",
                # "aerich.models"
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
