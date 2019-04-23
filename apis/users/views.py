from flask.views import MethodView
from flask import url_for
from apis.users import bp_users
from apis.users.models import User
from exts import db
from tools.redis_api import redis_cli
from flask import current_app


@bp_users.route('/list/<int:page>', methods=['GET'])
def lists(page=1):
    print(page)
    return "<h1>User List</h1>"


@bp_users.route('/total', methods=['GET'])
def total():
    total = redis_cli.incr_instance('total')
    print(url_for('users.total'))
    return "<h1>The %s Click</h1>" % str(total)


class UserView(MethodView):
    def get(self):
        user = User(username='admin', password='admin@example.com', sex=1, name='bobo')
        db.session.add(user)
        db.session.commit()
        current_app.logger.debug('A value for debugging')
        return "Success"

    def post(self):
        user = User(username='admin', password='admin@example.com')
        db.session.add(user)
        db.session.commit()
        return "Success"


bp_users.add_url_rule('users', view_func=UserView.as_view('users'))
