"""
Django settings for libuntl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
import django.conf.locale
from django.utils.translation import ugettext_lazy as _
from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django_extensions',
        # 'debug_toolbar',
        'django_js_reverse',
        'javascript_settings',
        'rest_framework',
        'rest_framework_swagger',
        'graphene_django',

        'libuntl',
        'library',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'libuntl.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'libuntl.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        # 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
        'postgresql://libuntl:libuntl@localhost:5435/libuntl_db'
    )


    # Password validation
    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
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

    # Internationalization
    # https://docs.djangoproject.com/en/1.11/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'node_modules'),
        os.path.join(BASE_DIR, 'static'),
    )

    GRAPHENE = {
        'SCHEMA': 'libuntl.schema.schema'
    }


    LANGUAGES = [
        ('en', _('English')),
        ('tet', _('Tetum')),
        ('id', _('Bahasa Indonesia')),
        ('pt', _('Portugese')),

    ]

    EXTRA_LANG_INFO = {
        'tet': {
            'bidi': False,  # right-to-left
            'code': 'tet',
            'name': 'Tetum',
            'name_local': 'Tetum',  # unicode codepoints here
        },
    }

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

    # Add custom languages not provided by Django
    # LANG_INFO = dict(django.conf.locale.LANG_INFO.items() + EXTRA_LANG_INFO.items())
    django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    # MIDDLEWARE = Common.MIDDLEWARE + [
    #     'debug_toolbar.middleware.DebugToolbarMiddleware'
    # ]


class Staging(Common):
    """
    The in-staging settings.
    """
    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    SECURE_SSL_HOST = values.Value(None)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )


class Production(Staging):
    """
    The in-production settings.
    """
    pass
