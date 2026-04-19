import os  # Make sure this is at the very top of the file

# ... (keep your existing BASE_DIR, SECRET_KEY, DEBUG, etc.)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # For static files on Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ... (keep ROOT_URLCONF, TEMPLATES, DATABASES, etc.)

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Required for Render to accept your site
ALLOWED_HOSTS = ['*'] 

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"