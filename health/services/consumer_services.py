import requests
import os
from health.authorization_keys import (
    PATIENTS_AUTH,
    PHYSICIANS_AUTH,
    CLINICS_AUTH,
    METRICS_AUTH
    )


class RequestService:

    def __init__(self, host, authorization):
        self.service_host = host
        self.authorization = authorization
        self.request = requests

    def get_service(self):
        header = {
            'Authorization': self.authorization
        }
        response = self.request.get(self.service_host, headers=header)

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
        response = self.request.post(self.service_host,  headers=header, json=data)
        return response


class ConsumerService:

    @staticmethod
    def get_clinic(_id: int):
        service_host = f"https://agile-earth-43435.herokuapp.com/v1/clinics/{_id}"

        r = RequestService(
            service_host,
            os.getenv('CLINICS_AUTH') or CLINICS_AUTH
        )
        response = r.get_service()

        return response.json()

    @staticmethod
    def get_physicians(_id: int):
        service_host = f"https://cryptic-scrubland-98389.herokuapp.com/v2/physicians/{_id}"

        r = RequestService(
            service_host,
            os.getenv('PHYSICIANS_AUTH') or PHYSICIANS_AUTH
        )

        response = r.get_service()

        return response

    @staticmethod
    def get_patient(_id: int):
        service_host = f"https://limitless-shore-81569.herokuapp.com/v3/patients/{_id}"

        r = RequestService(
            service_host,
            os.getenv('PATIENTS_AUTH') or PATIENTS_AUTH
        )

        response = r.get_service()

        return response


