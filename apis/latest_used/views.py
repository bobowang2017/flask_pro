import json
from flask.views import MethodView
from apis.latest_used.models import Project, ApplicationProjectMapping
from exts import db


class ProjectView(MethodView):

    def get(self):
        return json.dumps({"code": 0, "msg": Project.query.all()})

    def post(self):
        project = Project(1, "123", name="wangbobo", description="test")
        db.session.add(project)
        db.session.commit()
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
