# -*- coding: utf-8 -*-
from apis.base.base_task import BaseTask
from exts import celery


@celery.task(base=BaseTask)
def my_background_task(arg1, arg2):
    print(arg1)
    print(arg2)
    return arg1 + arg2
