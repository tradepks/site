import os
import register_activate

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#############User defined ###############
#Add the register_activate path
register_activate_dir= BASE_DIR  #os.path.dirname(os.path.dirname(os.path.abspath('register_activate.__file__')))

COMPANY_LIST_DIR = os.path.join(BASE_DIR, "companylist"),

URLS_LIST_FOR_DOWNLOAD = {
 "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download" : "NASDAQ.csv",
 "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download": "NYSE.csv",
 "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download": "AMEX.csv",
}
########################################


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vhd5f(*t3(&&=()81)+57y@0r$&fl8$op+ud06r_p$x+4b5od4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
from machina import get_apps as get_machina_apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register_activate',
    'finance', 
    
   # Machina related apps
   #Django-machina uses django-mptt to handle the tree of forum instances. 
   #Search capabilities are provided by django-haystack.
  'mptt',
  'haystack',
  'widget_tweaks',
  #debug machina 
  'debug_toolbar',
]+ get_machina_apps()


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Machina
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    #debug 
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'examplesite.urls'

from machina import MACHINA_MAIN_TEMPLATE_DIR


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                os.path.join(register_activate_dir,'register_activate/templates/register_activate'),
                #Machina
                MACHINA_MAIN_TEMPLATE_DIR,
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Machina
                'machina.core.context_processors.metadata',
            ],            
        },
    },
]

WSGI_APPLICATION = 'examplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'  #prefix to access static file in URL  it is under my_app/static/

from machina import MACHINA_MAIN_STATIC_DIR

#For any other user defined static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "companylist"),   
    # Machina
    MACHINA_MAIN_STATIC_DIR,    
]

#Machina 
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
  },
  'machina_attachments': {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': os.path.join(BASE_DIR, "tmp"),
  }
}
#Machina 
HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
  },
}
#Machina 
#default permission 
MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]
MACHINA_FORUM_NAME="TradePks"

   
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash. so below URLs are actually  from above MEDIA_ROOT
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


AUTHENTICATION_BACKENDS=[
'django.contrib.auth.backends.ModelBackend', 
'register_activate.email_auth.EmailBackend', 
] 

#for gmail server 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#for console output 
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tradepksfounder@gmail.com'
EMAIL_HOST_PASSWORD = 'April123$%^'  #give correct password
EMAIL_USE_TLS = True

###Login required 

SESSION_EXPIRE_AT_BROWSER_CLOSE = True    # everytime browser is closed, session is expired, ELSE persistant session 
SESSION_COOKIE_AGE  = 5*60 # in seconds 


##Logging 
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'file.log',
            'formatter': 'simple'
            },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
         'examplesite': {                      #Put the root of your module to handle the logging
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
        }
    }

#This is required for correct logging 
import logging.config
logging.config.dictConfig(LOGGING)