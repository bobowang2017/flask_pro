from flask import Blueprint

bp_orders = Blueprint('orders', __name__, url_prefix='/api/v1')
