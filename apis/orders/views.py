from flask import request
from flask.views import MethodView
from apis.orders import bp_orders
from apis.orders.models import Order
from apis.orders.schema import order_schema
from exts import db
from tools.helper import standardize_api_response


@bp_orders.route('/orders/<int:page>', methods=['GET'])
def lists(page=1):
    print(page)
    v = request.args.get('p')
    print('x=%s' % v)
    return "<h1>Bo bo</h1>"


class OrderView(MethodView):
    @standardize_api_response
    def get(self):
        data = Order.query.all()
        return order_schema.jsonify(data, many=True).json

    @standardize_api_response
    def post(self):
        order = Order(user_id=11, good_id=12, good_price=12.6)
        db.session.add(order)
        db.session.commit()
        return "success"

    @standardize_api_response
    def patch(self):
        data = request.get_json()
        order = Order.query.filter_by(id=data.get("id")).first()
        if not order:
            raise Exception("Order Not Found")
        order.good_price = data.get("good_price")
        db.session.commit()
        return "success"

    @standardize_api_response
    def delete(self):
        data = request.get_json()
        order_id = data.get('id')
        Order.query.filter_by(id=order_id).delete()
        db.session.commit()
        return "success"


bp_orders.add_url_rule('/orders', view_func=OrderView.as_view('orders'))
