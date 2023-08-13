import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps加入到sources root列表中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'evpyx#rqtrcjy$7zddw0afu(rut5-i+_f!lvnkzha0pf%uwtl0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 定义允许访问的ip地址
ALLOWED_HOSTS = ['*']

# Application definition

# 自定义用户登录校验
AUTHENTICATION_BACKENDS = (
    'users.views.CustomeBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'files',
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

ROOT_URLCONF = 'wjgl.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'wjgl.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ysd',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '172.17.0.1',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'zh-Hans' 中文会影响很多问题，包括数据库
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# 正式环境中将此项注释掉
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 正式环境中将此项注释取消
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 扩展django自带的user model，添加字段
AUTH_USER_MODEL = 'users.UserProfile'

# 分页的相关设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 8,
    'MARGIN_PAGES_DISPLAYED': 1,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# 定义全局的变量
per_page = 20  # 定义html页面中列表每页显示的数量

# 全局404配置，名称必须是handler404
handler404 = 'users.views.page_not_found'

# 全局500配置，名称必须是handler500
handler500 = 'users.views.page_error'

# 上传的文件保存路径
# root_path = '/home/greatwall/桌面/wjgl-master/ft'
root_path = BASE_DIR+"/folder"
# 设置会话关闭浏览器就失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
