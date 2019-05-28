from health.tests.dictionaries.physicians_errors import PHYSICIANS_NOT_FOUND, PHYSICIANS_INVALID_SYNTAX

api_url = '/api/v2/prescriptions'


def test_physicians_service_not_found(client):
    response = client.post(api_url, json=PHYSICIANS_NOT_FOUND)
    assert response.status_code == 404

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '02',
            'message': 'physician not found'}
    }

    assert response_json == expected


def test_physicians_service_invalid_syntax(client):
    response = client.post(api_url, json=PHYSICIANS_INVALID_SYNTAX)
    assert response.status_code == 400

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '07',
            'message': 'parameter must be integer'
        }
    }

    assert response_json == expected
