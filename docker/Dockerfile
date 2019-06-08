FROM python:3.6
MAINTAINER wangxiangbo
WORKDIR /bobo/.workspace/flask_pro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
CMD echo "SUCCESS"