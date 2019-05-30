"""
Custom Errors: status code and Message
"""
from flask import jsonify


class ErrorResponse(object):

    def __init__(self, code_error: str, message: str, status_code: int):
        self.code_error = code_error
        self.message = message
        self.status_code = status_code

    def get_error_response(self):
        error_response = jsonify(
            {
                "error": {
                    "code": self.code_error,
                    "message": self.message
                }
            }
        )
        error_response.status_code = self.status_code
        return error_response


def malformed_request():
    error_response = ErrorResponse(
        "01",
        "malformed request",
        400
    )
    return error_response.get_error_response()


def physician_not_found():
    error_response = ErrorResponse(
        "02",
        "physician not found",
        404
    )
    return error_response.get_error_response()


def patient_not_found():
    error_response = ErrorResponse(
        "03",
        "patient not found",
        404
    )
    return error_response.get_error_response()


def metrics_service_not_available():
    error_response = ErrorResponse(
        "04",
        "metrics service not available",
        503
    )
    return error_response.get_error_response()


def physicians_service_not_available():
    error_response = ErrorResponse(
        "05",
        "physicians service not available",
        503
    )
    return error_response.get_error_response()


def patients_service_not_available():
    error_response = ErrorResponse(
        "06",
        "patients service not available",
        503
    )
    return error_response.get_error_response()


def invalid_syntax():
    error_response = ErrorResponse(
        "07",
        "parameter must be integer",
        400
    )
    return error_response.get_error_response()


def clinic_not_found():
    error_response = ErrorResponse(
        "08",
        "clinic not found",
        404
    )
    return error_response.get_error_response()


def timeout_request(service):
    error_response = ErrorResponse(
        "09",
        f"Timeout {service}",
        408
    )
    return error_response.get_error_response()


def unauthorized():
    error_response = ErrorResponse(
        "10",
        "Unauthorized",
        401
    )
    return error_response.get_error_response()
