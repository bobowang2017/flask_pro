#!/usr/bin/env bash
docker run -it --rm -p 5000:5000 -v /bobo/.workspace/flask_pro:/workspace flask-images:latest /bin/bash