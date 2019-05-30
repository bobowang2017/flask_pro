import json

from flask.json import jsonify
from flask.views import MethodView

from apis.latest_used.functions import serializer
from apis.latest_used.models import Project, ApplicationProjectMapping
from exts import db
from flask_restful import request
from tools.execute_sql import dict_fetchall


class ProjectView(MethodView):

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


class AppProMappingVIew(MethodView):

    def post(self):
        app_pro_mapping = ApplicationProjectMapping(app_name="456", pro_id=1)
        db.session.add(app_pro_mapping)
        db.session.commit()
        return json.dumps({"code": 0, "msg": "success"})

    def get(self):
        data = ApplicationProjectMapping.query.filter(ApplicationProjectMapping.id == 1)
        print(data)
        return json.dumps({"code": 0, "msg": data})
