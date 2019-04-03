from .settings_base import *


ENV = 'local'

DEBUG = True
TEMPLATE_DEBUG = DEBUG


EMAIL_SUBJECT_PREFIX = "[Sheljar Ankit Local] "

ADMINS = (
    ('Ankit Agarwal', 'ankit@sheljar.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'sheljar_ankit_local - '
                      '[%(name)s]- '
                      '%(levelname)s- '
                      '%(asctime)s '
                      '%(filename)s: %(lineno)d - '
                      '%(funcName)s '
                      '%(message)s',
        },
    },
    'filters': {
    },
    'handlers': {
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     # 'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'formatter': 'standard',
        # },
    },
    'loggers': {
        '': {
            'handlers': [ ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}