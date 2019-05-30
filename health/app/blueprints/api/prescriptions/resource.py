from flask import Blueprint
from flask_restful import Api, reqparse, Resource, fields

from health.app.blueprints.api.errors import (
    malformed_request,
    patient_not_found,
    patients_service_not_available,
    physician_not_found,
    physicians_service_not_available,
    metrics_service_not_available,
    invalid_syntax,
    )


from health.services.consumer_services import ConsumerService

from health.app.blueprints.api.models import Prescription as PrescriptionModel
from health.app.blueprints.api.utils import serializer
from health.app.blueprints.api.responses import resp_content_successfully

bp = Blueprint('prescriptions_api', __name__, url_prefix='/api/v2')
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('clinic', type=dict)
parser.add_argument('physician', type=dict)
parser.add_argument('patient', type=dict)
parser.add_argument('text', type=str)

resource_fields = {
    'id': fields.Integer,
    'clinic': fields.Integer,
    'physician': fields.Integer,
    'patient': fields.Integer,
    'text': fields.String
}


class PrescriptionsAPI(Resource):

    def __init__(self):
        self.args = parser.parse_args()
        self.service = ConsumerService()

    def post(self):
        clinic = self.args['clinic']
        patient = self.args['patient']
        physician = self.args['physician']
        text = self.args['text']

        if not clinic:
            return malformed_request()

        if not patient:
            return malformed_request()

        if not physician:
            return malformed_request()

        if not text:
            return malformed_request()

        patient_response = self.service.get_patients(patient['id'])
        physician_response = self.service.get_physicians(physician['id'])
        clinic_response = self.service.get_clinic(clinic['id'])

        if patient_response == '404':
            return patient_not_found()

        if patient_response == '400':
            return invalid_syntax()

        if patient_response == '408':
            return patients_service_not_available()

        if physician_response == '404':
            return physician_not_found()

        if physician_response == '400':
            return invalid_syntax()

        if physician_response == '408':
            return physicians_service_not_available()

        prescription = PrescriptionModel(
            patient_id=patient['id'],
            physician_id=physician['id'],
            clinic_id=clinic['id'],
            text=text
        )
        prescription.save()
        query_prescription = PrescriptionModel.get_prescription(prescription.id)

        data_compose = {
            'clinic_id': clinic_response['data']['id'],
            'clinic_name': clinic_response['data']['name'],
            'physician_id': physician_response['data']['id'],
            'physician_name': physician_response['data']['fullName'],
            'physician_crm': physician_response['data']['crm'],
            'patient_id':  patient_response['data']['id'],
            'patient_name': patient_response['data']['fullName'],
            'patient_email': patient_response['data']['email'],
            'patient_phone': patient_response['data']['phone']
        }

        metrics_response = self.service.post_metrics(data_compose)

        if metrics_response == '400':
            query_prescription.delete()
            return malformed_request()

        if metrics_response == '408':
            query_prescription.delete()
            return metrics_service_not_available()

        serialized = serializer(query_prescription, False)
        return resp_content_successfully(serialized)


def init_app(app):
    api.add_resource(PrescriptionsAPI, '/prescriptions', endpoint='prescriptions')
    app.register_blueprint(bp)
