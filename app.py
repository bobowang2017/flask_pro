from flask import Flask
import logging
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import config
from apis.latest_used.views import ProjectView, ApplicationVIew
from exts import db
from apis.orders.views import bp_orders
from apis.users.views import bp_users
from apis.latest_used import bp_projects

# 需要传递一个参数__name__
# 1、方便flask框架去寻找资源
# 2、方便flask插件比如Flask-SQLAlchemy出现错误的时候好去寻找问题所在的位置

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(bp_orders)
app.register_blueprint(bp_users)
app.register_blueprint(bp_projects)
app.add_url_rule("/api/v1/projects", view_func=ProjectView.as_view('projects'))
app.add_url_rule("/api/v1/app_pro_mapping", view_func=ApplicationVIew.as_view('app_pro_mapping'))
# 读取并加载数据库配置
app.config.from_object(config)
db.init_app(app)
# 定义日志配置
handler = logging.FileHandler('app.log', encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

# migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.before_request
def process_request(*args, **kwargs):
    # 验证表示，任何地址请求都会先执行before_request，所以登录验证就可以在before_request里做用户认证功能了
    print("其他请求之前就执行了process_request")


@app.after_request
def process_response(response):
    print("其他请求结束后就执行了process_response")
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    # manager.run()
