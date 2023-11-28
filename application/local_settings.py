# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database engine
        'NAME': 'postgres',                     # Database name
        'USER': 'postgres',                     # Database user
        'PASSWORD': 'postgres',             # Database password
        'HOST': 'db',                        # Database host (leave empty for localhost)
        'PORT': '',                                 # Database port (leave empty for default)
    }
}

CELERY_BROKER_URL = "redis://redis:6379"
