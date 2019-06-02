from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey

from exts import db


class BaseModel(object):
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now)


class Project(db.Model, BaseModel):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(15), nullable=False, unique=True, index=True)
    name = Column(String(100))
    description = Column(Text)


class Application(db.Model):
    __tablename__ = "application"

    id = Column(Integer, primary_key=True)
    app_name = Column(String(100), nullable=False)
    pro_id = Column(Integer, ForeignKey("project.id"))
    project = db.relationship('Project', backref=db.backref('application', lazy='dynamic'))
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return '<Application %r>' % self.id
