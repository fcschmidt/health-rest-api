from health.tests.dictionaries.prescriptions import (
    CLINIC_NOT_CONTENT,
    PATIENTS_NOT_CONTENT,
    PHYSICIANS_NOT_CONTENT,
    TEXT_NOT_CONTENT
    )

API_ENDPOINT = '/api/v2/prescriptions'

expected = {
    'error': {
        'code': '01',
        'message': 'malformed request'
    }
}


class TestPrescriptionsAPINotContent:

    def test_not_clinic_content(self, client):
        response = client.post(API_ENDPOINT, json=CLINIC_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == expected

    def test_not_patient_content(self, client):
        response = client.post(API_ENDPOINT, json=PATIENTS_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == expected

    def test_not_physicians_content(self, client):
        response = client.post(API_ENDPOINT, json=PHYSICIANS_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == expected

    def test_not_text_content(self, client):
        response = client.post(API_ENDPOINT, json=TEXT_NOT_CONTENT)
        assert response.status_code == 400

        response_json = response.get_json()
        assert response_json == expected
