from flask import Flask

import config
from exts import db
from apis.orders.views import bp_orders
from apis.users.views import bp_users

# 需要传递一个参数__name__
# 1、方便flask框架去寻找资源
# 2、方便flask插件比如Flask-SQLAlchemy出现错误的时候好去寻找问题所在的位置
app = Flask(__name__)
# 注册蓝图
app.register_blueprint(bp_orders)
app.register_blueprint(bp_users)
# 读取并加载数据库配置
app.config.from_object(config)
db.init_app(app)


@app.before_request
def process_request(*args, **kwargs):
    # 验证表示，任何地址请求都会先执行before_request，所以登录验证就可以在before_request里做用户认证功能了
    print("其他请求之前就执行了process_request")


@app.after_request
def process_response(response):
    print("其他请求结束后就执行了process_response")
    return response


if __name__ == '__main__':
    app.run()
