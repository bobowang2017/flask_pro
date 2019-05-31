from flask import Blueprint
from flask_restful import Api

bp_projects = Blueprint('projects', __name__, url_prefix='/api/v1')
api = Api(bp_projects, prefix='api/v1')
# api.add_resource()