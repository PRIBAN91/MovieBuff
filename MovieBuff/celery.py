# from __future__ import absolute_import, unicode_literals
# import os
# import django
# import logging
# from celery import Celery
#
# logger = logging.getLogger(__name__)
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieBuff.settings')
#
# app = Celery('MovieBuff')
#
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
#
# django.setup()
#
# # from ScheduledTasks import *
