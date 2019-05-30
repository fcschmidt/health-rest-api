from health.app.blueprints.api.schemas import PrescriptionsSchemas
from health.app.blueprints.api.errors import (
    malformed_request,
    patient_not_found,
    patients_service_not_available,
    physician_not_found,
    physicians_service_not_available,
    metrics_service_not_available,
    invalid_syntax,
    clinic_not_found,
    timeout_request,
    unauthorized
    )


prescriptions_schema = PrescriptionsSchemas()


def serializer(content, state):
    serialized = prescriptions_schema.dump(content, many=state).data
    return serialized


def prescription_parser(content):
    for c in content:
        if not c:
            return malformed_request()


def patients_response_parser(resp):
    if resp == '404':
        return patient_not_found()

    if resp == '400':
        return invalid_syntax()

    if resp == '401':
        return unauthorized()

    if resp == '408':
        return timeout_request('Patients')

    if resp == '503':
        return patients_service_not_available()


def physicians_response_parser(resp):
    if resp == '404':
        return physician_not_found()

    if resp == '400':
        return invalid_syntax()

    if resp == '401':
        return unauthorized()

    if resp == '408':
        return timeout_request('Physicians')

    if resp == '503':
        return physicians_service_not_available()


def clinics_response_parser(resp):
    if resp == '404':
        return clinic_not_found()

    if resp == '400':
        return invalid_syntax()

    if resp == '401':
        return unauthorized()


def metrics_response_parser(resp, query):
    if resp == '400':
        query.delete()
        return malformed_request()

    if resp == '401':
        return unauthorized()

    if resp == '408':
        query.delete()
        return timeout_request('Metrics')

    if resp == '503':
        query.delete()
        return metrics_service_not_available()
