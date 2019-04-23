class DefaultConfig(object):
    """
    Flask默认配置
    """
    ERROR_404_HELP = False

    # 日志配置
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = '/home/python/logs'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 10

    # flask-sqlalchemy使用的参数
    SQLALCHEMY_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/study'
    # 追踪数据的修改信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # redis 配置
    REDIS_CONFIG = {
        "host": "localhost",
        "port": 6379
    }

    # ElasticSearch配置
    ES_CONFIG = {
        "host": "localhost",
        "port": 63790
    }
