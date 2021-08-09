from pathlib import Path
import os
import environ

# memo
# SNS認証を追加予定
# メールサーバー追加予定
#

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = os.path.basename(BASE_DIR)

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_pandas',
    'django_sass',
    'sass_processor',
    'app',
]


AUTH_USER_MODEL = 'app.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                # `allauth` needs this from django
                # 'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'app/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = f'/var/www/{PROJECT_NAME}/static'

# ファイルの保管先ディレクトリ
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# model field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##Authentication##
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'app:home'
ACCOUNT_LOGOUT_REDIRECT_URL= 'app:home'

# allauth settings
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 認証方法をメールアドレスにする
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # usernameフィールドの有無
ACCOUNT_USERNAME_REQUIRED = False # ユーザー名の要求
ACCOUNT_LOGOUT_ON_GET = True #ログアウトの確認を非表示
ACCOUNT_EMAIL_REQUIRED = True # メールアドレスの要求
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # 登録時のメール認証の有無 none

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',　削除
]
# Email settings（実際にメールを送りたいときは以下をコメントアウト）
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email server settings
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'sample@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
