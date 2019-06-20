# -*- coding: utf-8 -*-
from apis.base.base_task import BaseTask
from exts import celery
import time


@celery.task(base=BaseTask)
def my_background_task(arg1, arg2):
    print('=' * 60)
    time.sleep(10)
    print('*'*60)
    return arg1 + arg2
