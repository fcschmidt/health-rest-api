import pytest
from health.tests.dictionaries.prescriptions_data_test import (
    CLINIC_NOT_CONTENT,
    PATIENTS_NOT_CONTENT,
    PHYSICIANS_NOT_CONTENT,
    TEXT_NOT_CONTENT,
    PRESCRIPTION_DATA
    )

from health.tests.dictionaries.patients_data_test import PATIENTS_NOT_FOUND, PATIENTS_INVALID_SYNTAX
from health.tests.dictionaries.physicians_data_test import PHYSICIANS_NOT_FOUND, PHYSICIANS_INVALID_SYNTAX
from health.tests.dictionaries.clinics_data_test import CLINICS_NOT_FOUND, CLINICS_INVALID_SYNTAX
from health.tests.dictionaries.expected_errors import (
    EXPECTED_ERROR_01,
    EXPECTED_ERROR_02,
    EXPECTED_ERROR_03,
    EXPECTED_ERROR_07,
    EXPECTED_ERROR_08,
    EXPECTED_DATA_SUCCESSFULLY
    )

API_ENDPOINT = '/api/v2/prescriptions'


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
        assert response_json == EXPECTED_ERROR_03

    def test_patients_service_invalid_syntax(self, client):
        response = client.post(API_ENDPOINT, json=PATIENTS_INVALID_SYNTAX)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_07


class TestPrescriptionsAPIIntegratePhysiciansService:
    """Test Prescription API Integrate Physicians Service, Return Errors Responses"""

    def test_physicians_service_not_found(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_NOT_FOUND)
        assert response.status_code == 404

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_02

    def test_physicians_service_invalid_syntax(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_INVALID_SYNTAX)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_07


class TestPrescriptionsAPIIntegrateClinicsService:
    """Test Prescription API Integrate Clinics Service, Return Errors Responses"""

    def test_clinics_service_not_found(self, client):
        response = client.post(API_ENDPOINT, json=CLINICS_NOT_FOUND)
        assert response.status_code == 404

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_08

    def test_clinics_service_invalid_syntax(self, client):
        response = client.post(API_ENDPOINT, json=CLINICS_INVALID_SYNTAX)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == EXPECTED_ERROR_07


@pytest.mark.usefixtures('session')
class TestPrescriptionsAPI:
    """
    Test Prescription API Integrate Services:  Patients, Clinic, Physicians and Metrics
    Return Successfully status code and Content
    """

    def test_prescription_api_integrate_successfully(self, client):
        response = client.post(API_ENDPOINT, json=PRESCRIPTION_DATA)
        assert response.status_code == 201

        response_json = response.get_json()
        assert response_json == EXPECTED_DATA_SUCCESSFULLY
