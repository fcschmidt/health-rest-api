import pytest
from health.tests.dictionaries.prescriptions import (
    CLINIC_NOT_CONTENT,
    PATIENTS_NOT_CONTENT,
    PHYSICIANS_NOT_CONTENT,
    TEXT_NOT_CONTENT,
    PRESCRIPTION_DATA
    )

from health.tests.dictionaries.patients_errors import PATIENTS_NOT_FOUND, PATIENTS_INVALID_SYNTAX
from health.tests.dictionaries.physicians_errors import PHYSICIANS_NOT_FOUND, PHYSICIANS_INVALID_SYNTAX


API_ENDPOINT = '/api/v2/prescriptions'

EXPECTED_ERROR_01 = {
    'error': {
        'code': '01',
        'message': 'malformed request'
    }
}


class TestPrescriptionsAPINotContent:
    """Teste Prescriptions API Not Content Error Response"""

    def test_not_clinic_content(self, client):
        response = client.post(API_ENDPOINT, json=CLINIC_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_01

    def test_not_patient_content(self, client):
        response = client.post(API_ENDPOINT, json=PATIENTS_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_01

    def test_not_physicians_content(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_01

    def test_not_text_content(self, client):
        response = client.post(API_ENDPOINT, json=TEXT_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_01


class TestPrescriptionAPIIntegratePatientsService:
    """Test Prescription API Integrate Patients Service, Return Errors Responses"""

    def test_patients_service_not_found(self, client):
        response = client.post(API_ENDPOINT, json=PATIENTS_NOT_FOUND)
        assert response.status_code == 404

        response_json = response.get_json()
        expected = {
            'error': {
                'code': '03',
                'message': 'patient not found'
            }
        }

        assert response_json == expected

    def test_patients_service_invalid_syntax(self, client):
        response = client.post(API_ENDPOINT, json=PATIENTS_INVALID_SYNTAX)
        assert response.status_code == 400

        response_json = response.get_json()
        expected = {
            'error': {
                'code': '07',
                'message': 'parameter must be integer'
            }
        }

        assert response_json == expected


class TestPrescriptionsAPIIntegratePhysiciansService:
    """Test Prescription API Integrate Physicians Service, Return Errors Responses"""

    def test_physicians_service_not_found(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_NOT_FOUND)
        assert response.status_code == 404

        response_json = response.get_json()
        expected = {
            'error': {
                'code': '02',
                'message': 'physician not found'}
        }

        assert response_json == expected

    def test_physicians_service_invalid_syntax(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_INVALID_SYNTAX)
        assert response.status_code == 400

        response_json = response.get_json()
        expected = {
            'error': {
                'code': '07',
                'message': 'parameter must be integer'
            }
        }

        assert response_json == expected


@pytest.mark.usefixtures('session')
class TestPrescriptionsAPI:
    """
    Test Prescription API Integrate Services:  Patients, Clinic, Physicians and Metrics
    Return Successfully status code and Content
    """

    def test_prescription_successfully(self, client):
        response = client.post(API_ENDPOINT, json=PRESCRIPTION_DATA)
        assert response.status_code == 201

        response_json = response.get_json()
        expected = {
            'data': {
                'clinic_id': 1,
                'patient_id': 1,
                'physician_id': 1,
                'id': 1,
                'text': 'Dipirona 1x ao dia'
            }
        }
        assert response_json == expected
