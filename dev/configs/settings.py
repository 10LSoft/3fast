# General settings
RUN_MODE = 'dev'

PROJECT_NAME = 'dev'
PROJECT_DESCRIPTION = '''
Um projeto básico usando o 3Fast para desenvolvimento web
'''

APPLICATIONS = [
    # Registered applications
    'welcome',
]

CORS_ORIGINS = ['*']


# Frontend settings
ROOT_APPLICATION = 'welcome'


# Backend settings
BACKEND_HOST = 'localhost'
BACKEND_PORT = 8000

LOG_LEVEL = 'info'

BACKEND_WORKERS = 1

DATABASE_URL = f'sqlite://{PROJECT_NAME}/data/fasts.sqlite3'
