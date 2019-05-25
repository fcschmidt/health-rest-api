from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint('prescriptions_api', __name__, url_prefix='/api/v2')
api = Api(bp)


class PrescriptionsAPI(Resource):
    pass


def init_app(app):
    api.add_resource(PrescriptionsAPI, '/prescriptions', endpoint='prescriptions')
    app.register_blueprint(bp)
