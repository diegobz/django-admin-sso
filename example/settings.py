# Django settings for example project.
import os.path

ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = True

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'd$vcdxp(who0bvg5)8-mkaejq@f58z!h4*l)98y^i3z!3)*0zh'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ROOT, 'admin_sso/templates/')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# add admin_sso to INSTALLED_APPS
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'admin_sso',
)

# add admin_sso.auth.DjangoSSOAuthBackend to AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = 'your client id here'
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = 'your client secret here'

# these are the default values
# they are only set here because unit tests rely on them
DJANGO_ADMIN_SSO_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
DJANGO_ADMIN_SSO_REVOKE_URI = 'https://accounts.google.com/o/oauth2/revoke'
DJANGO_ADMIN_SSO_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
