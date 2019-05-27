from flask import Blueprint
from flask_restful import Api, reqparse, Resource, fields

from health.services.consumer_services import ConsumerService

from health.app.blueprints.api.errors import (
    patient_not_found,
    invalid_syntax,
    )

bp = Blueprint('prescriptions_api', __name__, url_prefix='/api/v2')
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('clinic', type=dict)
parser.add_argument('physician', type=dict)
parser.add_argument('patient', type=dict)
parser.add_argument('text', type=str)

resource_fields = {
    'id': fields.Integer,
    'clinic_id': fields.Integer,
    'physician_id': fields.Integer,
    'patient_id': fields.Integer,
    'text': fields.String
}


class ParserServiceResponse:
    pass


class PrescriptionsAPI(Resource):

    def __init__(self):
        self.args = parser.parse_args()
        self.service = ConsumerService()
        self.parser = ParserServiceResponse()

    def post(self):
        clinic = self.args['clinic']
        patient = self.args['patient']
        physician = self.args['physician']
        text = self.args['text']

        patient_response = self.service.get_patient(patient['id'])
        if patient_response == '404':
            return patient_not_found()

        if patient_response == '400':
            return invalid_syntax()


def init_app(app):
    api.add_resource(PrescriptionsAPI, '/prescriptions', endpoint='prescriptions')
    app.register_blueprint(bp)
