import requests

from health.authorization_keys import (
    PATIENTS_AUTH,
    PHYSICIANS_AUTH,
    CLINICS_AUTH,
    METRICS_AUTH
    )


class ServiceRequest:

    def __init__(self, host, authorization, timeout):
        self.service_host = host
        self.authorization = authorization
        self.timeout = timeout
        self.request = requests

    def get_service(self):
        header = {
            'Authorization': self.authorization
        }

        try:
            response = self.request.get(self.service_host, headers=header, timeout=self.timeout)
        except requests.ConnectTimeout:
            return '408'

        if response.status_code == 401:
            return '401'

        if response.status_code == 404:
            return '404'

        if response.status_code == 400:
            return '400'

        if response.status_code == 503:
            return '503'

        return response.json()

    def post_service(self, data):
        header = {
            'Authorization': self.authorization,
            'Content-Type': 'application/json'
        }

        try:
            response = self.request.post(
                self.service_host,  headers=header, json=data, timeout=self.timeout)
        except requests.ConnectTimeout:
            return '408'

        try:
            if response.json()['errorCode'] == '4000':
                return '400'
        except KeyError:
            pass

        if response.status_code == 401:
            return '401'

        if response.status_code == 503:
            return '503'

        return response.json()


class ServiceConsumer:

    @staticmethod
    def get_clinic(_id: int):
        service_host = f"https://agile-earth-43435.herokuapp.com/v1/clinics/{_id}"

        r = ServiceRequest(
            service_host,
            CLINICS_AUTH,
            5
        )
        response = r.get_service()
        return response

    @staticmethod
    def get_physicians(_id: int):
        service_host = f"https://cryptic-scrubland-98389.herokuapp.com/v2/physicians/{_id}"

        r = ServiceRequest(
            service_host,
            PHYSICIANS_AUTH,
            4
        )

        response = r.get_service()
        return response

    @staticmethod
    def get_patients(_id: int):
        service_host = f"https://limitless-shore-81569.herokuapp.com/v3/patients/{_id}"

        r = ServiceRequest(
            service_host,
            PATIENTS_AUTH,
            3
        )

        response = r.get_service()
        return response

    @staticmethod
    def post_metrics(data: dict):
        service_host = 'https://mysterious-island-73235.herokuapp.com/api/metrics'

        r = ServiceRequest(
            service_host,
            METRICS_AUTH,
            6
        )

        response = r.post_service(data)
        return response
