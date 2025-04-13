import configs.settings as settings
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        'configs.server:back_app',
        host=settings.BACKEND_HOST,
        port=settings.BACKEND_PORT,
        log_level=settings.LOG_LEVEL,
        workers=settings.BACKEND_WORKERS,
        reload=settings.RUN_MODE.lower() == "dev"
    )
