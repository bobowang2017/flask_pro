# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from apis.student.views import StudentView, CeleryTaskView, CeleryTaskResultView

bp_student = Blueprint('student', __name__, url_prefix='/api/v1')
api = Api(bp_student)
api.add_resource(StudentView, '/student')
api.add_resource(CeleryTaskView, '/celery')
api.add_resource(CeleryTaskResultView, '/celery/result')
