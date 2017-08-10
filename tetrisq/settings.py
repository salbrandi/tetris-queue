INSTALLED_APPS = (
    # other apps
    "django_rq",
)


RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0
    }
}
