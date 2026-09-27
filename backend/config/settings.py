import os
from pathlib import Path

from dotenv import load_dotenv


# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
load_dotenv(BASE_DIR / ".env")


# --------------------------------------------------
# SECURITY
# --------------------------------------------------

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-development-key-change-later"
)

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [

    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "corsheaders",

    # Our apps
    "accounts",
    "doctors",
    "appointments",
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # CORS
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URL CONFIGURATION
# --------------------------------------------------

ROOT_URLCONF = "config.urls"


# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = "config.wsgi.application"


# --------------------------------------------------
# DATABASE - POSTGRESQL
# --------------------------------------------------

DATABASES = {
    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": os.getenv("DB_NAME"),

        "USER": os.getenv("DB_USER"),

        "PASSWORD": os.getenv("DB_PASSWORD"),

        "HOST": os.getenv(
            "DB_HOST",
            "localhost"
        ),

        "PORT": os.getenv(
            "DB_PORT",
            "5432"
        ),
    }
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },

    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "/static/"


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --------------------------------------------------
# LOGIN / LOGOUT SETTINGS
# --------------------------------------------------

LOGIN_URL = "/accounts/login/"

LOGIN_REDIRECT_URL = "/accounts/dashboard/"

LOGOUT_REDIRECT_URL = "/accounts/login/"


# --------------------------------------------------
# DJANGO REST FRAMEWORK
# --------------------------------------------------

REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": (

        "rest_framework_simplejwt.authentication.JWTAuthentication",

        "rest_framework.authentication.SessionAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (

        "rest_framework.permissions.IsAuthenticated",
    ),
}


# --------------------------------------------------
# CORS - REACT FRONTEND
# --------------------------------------------------

CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

    "http://127.0.0.1:3000",

    "http://localhost:5173",

    "http://127.0.0.1:5173",
]