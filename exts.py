# 防止循环引用问题
import logging

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# 定义日志配置
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('app.log', encoding='UTF-8')
handler.setLevel(logging.INFO)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
logger.addHandler(handler)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)
