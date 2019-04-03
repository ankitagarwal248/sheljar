from .settings_base import *
import django_heroku

django_heroku.settings(locals())

ENV = 'staging'

DEBUG = True
TEMPLATE_DEBUG = DEBUG


EMAIL_SUBJECT_PREFIX = "[Sheljar Staging] "

ADMINS = (
    ('Ankit Agarwal', 'ankit@sheljar.com'),
)

MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'sheljar_staging - '
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
        'sys_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'address': ('logs7.papertrailapp.com', 33237),
        }
    },
    'loggers': {
        '': {
            'handlers': ['sys_log', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}