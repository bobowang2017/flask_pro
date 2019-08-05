# -*- coding: utf-8 -*-
from exts import ma


class OrderSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "good_id", "good_price", "create_at", "update_at")


order_schema = OrderSchema()
