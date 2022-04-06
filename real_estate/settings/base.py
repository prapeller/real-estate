from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

SITE_ID = 1

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field'
]

LOCAL_APPS = [
    'apps.common',
    'apps.users',
    'apps.profiles',
    'apps.ratings',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_estate.urls'

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

WSGI_APPLICATION = 'real_estate.wsgi.application'

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],
    # 'DEFAULT_PARSER_CLASSES': (
    # If you use MultiPartFormParser or FormParser, we also have a camel case version
    # 'djangorestframework_camel_case.parser.CamelCaseFormParser',
    # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    # 'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # passing session id (for debugging in browser)
        'rest_framework.authentication.SessionAuthentication',

        # passing login/password in request.args (http authentification)
        'rest_framework.authentication.BasicAuthentication',

        # passing token in headers
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        # permissions to makeOperations/toViewOnly for authenticated users in current session
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',

        # permissions according to auth_permission
        'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

        # for making own permissions
        # 'rest_framework.permissions.BasePermission',
    ],

    'DEFAULT_VERSIONING_CLASS':
    # http://127.0.0.1:8000/api/v2/users/
        'rest_framework.versioning.URLPathVersioning',

    # path('api/v1/users/', include('userapp.urls', namespace='v1')),
    # 'rest_framework.versioning.NamespaceVersioning',

    # http://v1.example.com/bookings/
    # 'rest_framework.versioning.HostNameVersioning',

    # http://127.0.0.1:8000/api/users/?version=v1/
    # 'rest_framework.versioning.QueryParameterVersioning',

    # requests.get('http://127.0.0.1:8000/api/users/', headers={'Accept': 'application/json; version=v2'})
    # 'rest_framework.versioning.AcceptHeaderVersioning',
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
