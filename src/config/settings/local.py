from .base import *

SECRET_KEY = get_secret('local', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
