from flask import Blueprint
from flask_restful import Api

from apis.latest_used.views import ApplicationVIew

bp_projects = Blueprint('projects', __name__, url_prefix='/api/v1')
api = Api(bp_projects)
api.add_resource(ApplicationVIew, '/application')
