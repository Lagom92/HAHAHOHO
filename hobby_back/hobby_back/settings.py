import sys
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
# SECRETS_PATH = os.path.join(ROOT_DIR, 'hobby_back/secrets.json')
# secrets = json.loads(open(SECRETS_PATH).read())
# Secret Key
# for key, value in secrets.items():
#     setattr(sys.modules[__name__], key, value)

SECRET_KEY = '-vy6&3jcv%chue-&m6pvlzb5vvpy59opby06ezxr6s8o!-&@y2'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    # 'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    'corsheaders',
    # 'imagekit',
    # 'django_extensions',
    'drf_yasg',
    'debug_toolbar',
    'boards',
    'accounts',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'hobby_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates') ],
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

WSGI_APPLICATION = 'hobby_back.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'hobby',
#         'USER': 'admin',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',

    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'SEARCH_PARAM': 'q',    
}

# JWT_AUTH = { 
#     'JWT_ALLOW_REFRESH': True, 
# }

REST_USE_JWT = True

SITE_ID = 1

SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

# cors
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# graph model
# GRAPH_MODELS = {
#   'all_applications': True,
#   'group_models': True,
# }

SUIT_CONFIG = {
    'ADMIN_NAME': '관리자 페이지',
    'HEADER_DATE_FORMAT': 'Y F j일',
    'HEADER_TIME_FORMAT': 'h:i',    
}

# 해당 IP에서 디버그 툴바가 보인다.
INTERNAL_IPS = ('127.0.0.1',)
