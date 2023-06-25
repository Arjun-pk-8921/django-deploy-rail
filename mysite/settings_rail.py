from mysite.settings import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['web-production-30e7.up.railway.app']