#!/usr/bin/env bash
# linux
celery -A app.celery worker --loglevel=info
# windows 下启动celery会报错，用如下方式启动即可
celery -A app.celery worker --loglevel=info -P eventlet