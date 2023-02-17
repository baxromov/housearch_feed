from databases import DatabaseURL
# from starlette.config import Config
from starlette.datastructures import Secret

# config = Config(".env")
PROJECT_NAME = "Lesson 2"
VERSION = "1.0.0"
API_PREFIX = "/api"

database = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'prisma',
    'USER': 'prisma',
    'PASSWORD': 'prismaJ82hHD21',
    'HOST': '162.55.34.2',
    'PORT': 5533,
    'CONN_MAX_AGE': 60 * 10,  # 10 minutes, don't close connection
}

# SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")
# POSTGRES_USER = config("POSTGRES_USER", cast=str)
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
# POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="localhost")
# POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
# POSTGRES_DB = config("POSTGRES_DB", cast=str)
# SECRET_KEY = database.get()
POSTGRES_USER = database.get('USER')
POSTGRES_PASSWORD = database.get('PASSWORD')
POSTGRES_SERVER = database.get('HOST')
POSTGRES_PORT = database.get('PORT')
POSTGRES_DB = database.get('NAME')
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# DATABASE_URL = config(
#     "DATABASE_URL",
#     cast=DatabaseURL,
#     default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
# )
