from health.tests.dictionaries.patients_errors import PATIENTS_NOT_FOUND, PATIENTS_INVALID_SYNTAX

api_url = '/api/v2/prescriptions'


def test_patients_service_not_found(client):
    response = client.post(api_url, json=PATIENTS_NOT_FOUND)
    assert response.status_code == 404

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '03',
            'message': 'patient not found'
        }
    }

    assert response_json == expected


def test_patients_service_invalid_syntax(client):
    response = client.post(api_url, json=PATIENTS_INVALID_SYNTAX)
    assert response.status_code == 400

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '07',
            'message': 'parameter must be integer'
        }
    }

    assert response_json == expected

