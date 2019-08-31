from apis.base.base_model import BaseModel
from exts import db


class Order(db.Model, BaseModel):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    good_id = db.Column(db.Integer, nullable=False)
    good_price = db.Column(db.FLOAT, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.id
