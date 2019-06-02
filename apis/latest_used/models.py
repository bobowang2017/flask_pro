from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, Numeric

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

    def __init__(self, id, code, name=None, description=None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description


class Application(db.Model):
    __tablename__ = "application"

    id = Column(Integer, primary_key=True)
    app_name = Column(String(100), nullable=False)
    pro_id = Column(Integer, ForeignKey("project.id"))
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, onupdate=datetime.now)

    # def __init__(self, id, app_name, pro_id, project):
    #     self.id = id
    #     self.app_name = app_name
    #     self.pro_id = pro_id
    #     self.project = project

    def __repr__(self):
        return '<Application %r>' % self.id
