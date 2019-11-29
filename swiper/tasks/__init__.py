import os
from celery import Celery
from tasks import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

celery_app = Celery('asyns_tasks')
celery_app.config_from_object(config) # 设置配置
celery_app.autodiscover_tasks() #自动 查找django的任务