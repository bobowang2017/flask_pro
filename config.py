# 设置debug模式
DEBUG = True
SECRET_KEY = "123#234"

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'study'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                          PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_COMMIT_ON_TEARDOWN = True