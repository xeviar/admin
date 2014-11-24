import os.path

PRODUCTION = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = [
	'sa-monitor.garena.com',
]

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MANAGERS = ADMINS

if PRODUCTION :
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'sa_monitor_db',              # Or path to database file if using sqlite3.
			'USER': 'sa_monitor',                 # Not used with sqlite3.
			'PASSWORD': 'I2krPdtUy2Kjd3OTklOs',   # Not used with sqlite3.
			'HOST': '203.116.180.36',             # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '6606',                       # Set to empty string for default. Not used with sqlite3.
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'sa_monitor',                  # Or path to database file if using sqlite3.
			'USER': 'admin',                      # Not used with sqlite3.
			'PASSWORD': '123456',                 # Not used with sqlite3.
			'HOST': 'localhost',                  # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '3306',                       # Set to empty string for default. Not used with sqlite3.
		}
	}

TIME_ZONE = 'Asia/Singapore'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL prefix for static files.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
	os.path.join(PROJECT_PATH, "static_dev"),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rj)_-(=#ba$2c5b=g#=z4u!mo((vagd!slwq^mv2vun_blupn6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_PATH, 'mytemplates'),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'social.apps.django_app.default',
	'start_page',
)

# log
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

# oauth
AUTHENTICATION_BACKENDS = (
	'social.backends.google.GoogleOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'social.apps.django_app.context_processors.backends',
	'social.apps.django_app.context_processors.login_redirect',
)

SOCIAL_AUTH_PIPELINE = (
	'social.pipeline.social_auth.social_details',
	'social.pipeline.social_auth.social_uid',
	'social.pipeline.social_auth.auth_allowed',
	'start_page.mypipeline.load_user',
	'social.pipeline.social_auth.social_user',
	'social.pipeline.social_auth.associate_user',
	'social.pipeline.social_auth.load_extra_data',
	'social.pipeline.user.user_details'
)

LOGIN_URL = '/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/start_page/'
LOGIN_ERROR_URL    = '/start_page/login_error/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "36338072287-t8nrt086n57lkplc6gt1829b4bdg90uo.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "QD1k7RGYsEbFkWtntvDq70MG"

SOCIAL_AUTH_URL_NAMESPACE = 'social'
