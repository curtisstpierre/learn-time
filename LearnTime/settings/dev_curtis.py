from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'LearnTime',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': 'PLSQL_Horse_Dog',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

STATIC_ROOT = (
    "/home/curtis/Documents/learn-time/LearnTime/"
)

DEBUG = True