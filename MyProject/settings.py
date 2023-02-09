"""
Django settings for MyProject project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import django
from django.utils.encoding import force_str

django.utils.encoding.force_text = force_str

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='yannassiri26@gmail.com'
EMAIL_HOST_PASSWORD = 'rechlwnstfvqnbmc'
FROM_EMAIL = 'yannassiri26@gmail.com' 
SENDGRID_API_KEY = os.environ.get('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')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sannb-2v9ag4%n09)jaid-#7-6yy+=+q0_f--@fo9yy0)ijq)u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentification',
    'cookies.apps.CookiesConfig',
      
    'myapp.apps.MyappConfig',
    'newsletter.apps.NewsletterConfig',
    'crispy_forms',
    'rest_framework',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
   
    'corsheaders',
    # 'captcha',
    'graphene_django',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


GRAPHENE = {   
    "SCHEMA": "myapp.schema.schema"
}



MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'MyProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # 'social_django.context_processors.backends',  # <--
                # 'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

# QLcyP110OnSv9bxpmkTyhneKJRChyf9lK0xuYvAn : twilio phone 

# API KEY : nCQtA8DCcj4qLQhVu2vQLPhkJGAwTCCw

# AUTHENTICATION_BACKENDS = (
   
#     'social.backends.facebook.FacebookOAuth2',
#     'social.backends.google.GoogleOAuth2',
#     'social.backends.twitter.TwitterOAuth',
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend'

# )

# SOCIALACCOUNT_PROVIDERS = {
#     'github': {
#         'SCOPE': ['user:email'],
#         'AUTH_PARAMS': {'allow_signup': 'false'},
#         'APP': {
#             'client_id': 'YOUR_CLIENT_ID',
#             'secret': 'YOUR_CLIENT_SECRET',
#         }
#     }
# }

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],   clé secrette : 
# clé du site : 6LfQCVYkAAAAAOM43x4cZ_uOIN0KOC2nsnOAkzuL
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }
# firm-moonlight-376921 id du projet
# clapi : AIzaSyBVeLXGzxrKhQSsz8I0kNOkMF_FRAM5oeA


WSGI_APPLICATION = 'MyProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'PORT': '1433',
#         'OPTIONS': {
#                 'driver': 'ODBC Driver 17 for SQL Server',
#             },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'uploaded_newsletters/'




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field



PASSWORD_HASHERS = [
    # 'monprojet.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    # 'accounts.hashers.PBKDF2WrappedSHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
]