from flask import Blueprint
from flask_restful import Api

from apis.latest_used.views import ApplicationVIew, ProjectView

bp_latest_used = Blueprint('latest_used', __name__, url_prefix='/api/v1')
api = Api(bp_latest_used)
api.add_resource(ApplicationVIew, '/application')
api.add_resource(ProjectView, '/project')
