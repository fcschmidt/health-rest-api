from flask import Blueprint
from flask_restful import Api, reqparse, Resource, fields

from health.services.consumer_services import ConsumerService

from health.app.blueprints.api.models import Prescription as PrescriptionModel

from health.app.blueprints.api.utils import (
    patients_response_parser,
    physicians_response_parser,
    clinics_response_parser,
    metrics_response_parser,
    prescription_parser,
    serializer
    )

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

        response_parser = prescription_parser([clinic, patient, physician, text])
        if response_parser:
            return response_parser

        patients_response = self.service.get_patients(patient['id'])
        physicians_response = self.service.get_physicians(physician['id'])
        clinics_response = self.service.get_clinic(clinic['id'])

        response_patients_parser = patients_response_parser(patients_response)
        if response_patients_parser:
            return response_patients_parser

        response_physicians_parser = physicians_response_parser(physicians_response)
        if response_physicians_parser:
            return response_physicians_parser

        response_clinics_parser = clinics_response_parser(clinics_response)
        if response_clinics_parser:
            return response_clinics_parser

        if clinics_response == '408':
            clinic_name = ''
            clinic_id = clinic['id']
        else:
            clinic_name = clinics_response['data']['name']
            clinic_id = clinics_response['data']['id']

        prescription = PrescriptionModel(
            patient_id=patient['id'],
            physician_id=physician['id'],
            clinic_id=clinic['id'],
            text=text
        )
        prescription.save()
        query_prescription = PrescriptionModel.get_prescription(prescription.id)

        data_compose = {
            'clinic_id': clinic_id,
            'clinic_name': clinic_name,
            'physician_id': physicians_response['data']['id'],
            'physician_name': physicians_response['data']['fullName'],
            'physician_crm': physicians_response['data']['crm'],
            'patient_id':  patients_response['data']['id'],
            'patient_name': patients_response['data']['fullName'],
            'patient_email': patients_response['data']['email'],
            'patient_phone': patients_response['data']['phone']
        }

        metrics_response = self.service.post_metrics(data_compose)
        response_metrics_parser = metrics_response_parser(metrics_response, query_prescription)
        if response_metrics_parser:
            return response_metrics_parser

        serialized = serializer(query_prescription, False)
        return resp_content_successfully(serialized)


def init_app(app):
    api.add_resource(PrescriptionsAPI, '/prescriptions', endpoint='prescriptions')
    app.register_blueprint(bp)
