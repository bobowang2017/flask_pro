# -*- coding: utf-8 -*-
from exts import celery


@celery.task
def my_background_task(arg1, arg2):
    print(arg1)
    print(arg2)
    return
