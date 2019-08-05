import datetime

from exts import db


class BaseModel(object):
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.datetime.now)
