# import os
# from pathlib import Path
# import pymysql
# pymysql.install_as_MySQLdb()

# # ----------------------------
# # Base directory
# # ----------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # ----------------------------
# # Security
# # ----------------------------
# SECRET_KEY = 'change-this-to-a-secret-key-for-prod'  # Replace for production
# DEBUG = True  # True for development
# ALLOWED_HOSTS = ['*']  # Accept all hosts for development

# # ----------------------------
# # Installed apps
# # ----------------------------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # Third-party apps
#     'channels',

#     # Your apps
#     'core',
# ]

# # ----------------------------
# # Middleware
# # ----------------------------
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # ----------------------------
# # URL configuration
# # ----------------------------
# ROOT_URLCONF = 'fitfare_project.urls'

# # ----------------------------
# # Templates
# # ----------------------------
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'core' / 'templates'],  # Make sure this folder exists
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # ----------------------------
# # ASGI / Channels
# # ----------------------------
# ASGI_APPLICATION = 'fitfare_project.asgi.application'

# # In-memory channel layer for development
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

# # ----------------------------
# # WSGI (not used for WebSockets)
# # ----------------------------
# WSGI_APPLICATION = 'fitfare_project.wsgi.application'

# # ----------------------------
# # Database (SQLite for dev)
# # ----------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'fitfare_db',
#         'USER': 'fitfare_user',  # MySQL username
#         'PASSWORD': 'B@b@2208',  # MySQL password
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'auth_plugin_map': {'mysql_native_password': 'mysql_native_password'},
#         },
#     }
# }





# # ----------------------------
# # Password validation
# # ----------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # ----------------------------
# # Internationalization
# # ----------------------------
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Kolkata'
# USE_I18N = True
# USE_TZ = True

# # ----------------------------
# # Static files
# # ----------------------------
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']  # Make sure folder exists

# # ----------------------------
# # Default primary key
# # ----------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# # Custom user model
# AUTH_USER_MODEL = 'core.CustomUser'


import os
from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'change-this-to-a-secret-key-for-prod'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'channels',

    # local
    'core',
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

ROOT_URLCONF = 'fitfare_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
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

# ASGI / Channels
ASGI_APPLICATION = 'fitfare_project.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

WSGI_APPLICATION = 'fitfare_project.wsgi.application'

# ----------------- MySQL Database -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitfare_db',
        'USER': 'fitfare_user',      # update if needed
        'PASSWORD': 'B@b@2208',     # update if needed
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'auth_plugin_map': {'mysql_native_password': 'mysql_native_password'},
        },
    }
}

AUTH_USER_MODEL = 'core.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator','OPTIONS': {'min_length': 8},},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication backends (use EmailBackend)
AUTHENTICATION_BACKENDS = [
    'core.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Login redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# ----------------- Email (for OTP) -----------------
# Example using Gmail SMTP — replace with your credentials or use environment vars
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'talikarathod91@gmail.com'        # <-- replace
EMAIL_HOST_PASSWORD = 'mjxnkdaobawhvzin' # <-- replace (app password recommended)
DEFAULT_FROM_EMAIL = 'FitFare <talikarathod91@gmail.com>'
ADMINS = [
    ("Project Admin", "talikarathod91@gmail.com"),    # <- बदल
]
MANAGERS = ADMINS