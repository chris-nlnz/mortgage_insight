from os.path import join, dirname, abspath

DEBUG = False

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
VIRTUALENV_ROOT = dirname(PROJECT_ROOT)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6a!@2o9n1esl2$!igjsj=(t!w9^jocx+1)=*l$_d%el))s%03'

ALLOWED_HOSTS = ['*']


ADMINS = [
    ('Chris', 'i.mynah@gmail.com'),
]
MANAGERS = ADMINS


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mortgage_insight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mortgage_insight.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(PROJECT_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_ROOT = join(VIRTUALENV_ROOT, 'public-www', 'static')
MEDIA_ROOT = join(VIRTUALENV_ROOT, 'public-www', 'media')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'details': {'format': '%(asctime)s %(levelname)-8s - %(name)-30.30s - %(message)s'},
    },
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
        },
        'general': {
            'level': 'DEBUG',
            'formatter': 'details',
            'class': 'logging.FileHandler',
            'filename': join(VIRTUALENV_ROOT, 'log/application.log'),
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'details',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'default': {
            'handlers': ['general', 'console', ],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
        }
    },
}


from mortgage_insight.local_settings import *
