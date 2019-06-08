FROM python:3.6
MAINTAINER wangxiangbo
RUN pip install -U pip
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
CMD python app.py