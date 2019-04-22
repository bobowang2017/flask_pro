from flask import Blueprint, request
from flask.views import MethodView

bp_orders = Blueprint('orders', __name__, url_prefix='/api/v1')


@bp_orders.route('/orders/<int:page>', methods=['GET'])
def lists(page=1):
    print(page)
    v = request.args.get('p')
    print('x=%s' % v)
    return "<h1>Bo bo</h1>"


class OrderView(MethodView):
    def get(self):
        return "<h1>Get Bo bo wang</h1>"

    def post(self):
        return "<h1>Post Bo bo wang</h1>"


bp_orders.add_url_rule('/orders', view_func=OrderView.as_view('orders'))