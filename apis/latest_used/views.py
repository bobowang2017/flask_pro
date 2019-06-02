import json

from apis.latest_used.functions import serializer
from apis.latest_used.models import Project, Application
from apis.latest_used.schema import app_schema
from exts import db
from flask_restful import request, Resource
from tools.execute_sql import dict_fetchall


class ProjectView(Resource):

    def get(self):
        print(request.args)
        sql = """select * from project order by updated_time desc limit {}""".format(10)
        result = dict_fetchall(sql)
        return json.dumps({'code': 0, 'msg': serializer(result, many=True)})

    def post(self):
        print(request.get_json())
        project = Project(1, "123", name="wangbobo", description="test")
        db.session.add(project)
        db.session.commit()
        return json.dumps({"code": 0, "msg": "success"})

    def put(self):
        print(request.get_json())
        return json.dumps({"code": 0, "msg": "success"})


class ApplicationVIew(Resource):

    def post(self):
        app_pro_mapping = Application(app_name="456", pro_id=1)
        db.session.add(app_pro_mapping)
        db.session.commit()
        return json.dumps({"code": 0, "msg": "success"})

    def get(self):
        params = request.args
        data = Application.query.all()
        result = app_schema.dump(data, many=True)
        return {"code": 0, "msg": result.data}
