import requests
import os

from health.authorization_keys_test import (
    PATIENTS_AUTH_TEST,
    PHYSICIANS_AUTH_TEST,
    CLINICS_AUTH_TEST,
    METRICS_AUTH_TEST
    )


class RequestService:

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

        if response.status_code == 404:
            return '404'

        if response.status_code == 400:
            return '400'

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

        return response.json()


class ConsumerService:

    @staticmethod
    def get_clinic(_id: int):
        service_host = f"https://agile-earth-43435.herokuapp.com/v1/clinics/{_id}"

        r = RequestService(
            service_host,
            os.getenv('CLINICS_AUTH') or CLINICS_AUTH_TEST,
            4
        )
        response = r.get_service()

        return response

    @staticmethod
    def get_physicians(_id: int):
        service_host = f"https://cryptic-scrubland-98389.herokuapp.com/v2/physicians/{_id}"

        r = RequestService(
            service_host,
            os.getenv('PHYSICIANS_AUTH') or PHYSICIANS_AUTH_TEST,
            5
        )

        response = r.get_service()

        return response

    @staticmethod
    def get_patients(_id: int):
        service_host = f"https://limitless-shore-81569.herokuapp.com/v3/patients/{_id}"

        r = RequestService(
            service_host,
            os.getenv('PATIENTS_AUTH') or PATIENTS_AUTH_TEST,
            3
        )

        response = r.get_service()

        return response

    @staticmethod
    def post_metrics(data: dict):
        service_host = 'https://mysterious-island-73235.herokuapp.com/api/metrics'

        r = RequestService(
            service_host,
            os.getenv('METRICS_AUTH') or METRICS_AUTH_TEST,
            6
        )

        response = r.post_service(data)

        return response

