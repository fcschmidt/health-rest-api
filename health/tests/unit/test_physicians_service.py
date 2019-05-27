api_url = '/api/v2/prescriptions'


def test_physicians_service_not_found(client):
    test_data = {
        'clinic': {'id': 1},
        'physician': {'id': 10},
        'patient': {'id': 1},
        'text': 'Dipirona 1x ao dia'
    }

    response = client.post(api_url, json=test_data)
    assert response.status_code == 404

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '02',
            'message': 'physician not found'}
    }

    assert response_json == expected


def test_physicians_service_invalid_syntax(client):
    test_data = {
        'clinic': {'id': 1},
        'physician': {'id': 'string'},
        'patient': {'id': 1},
        'text': 'Dipirona 1x ao dia'
    }

    response = client.post(api_url, json=test_data)
    assert response.status_code == 400

    response_json = response.get_json()
    expected = {
        'error': {
            'code': '07',
            'message': 'parameter must be integer'}
    }

    assert response_json == expected


def test_physicians_service_not_available(client):
    pass
