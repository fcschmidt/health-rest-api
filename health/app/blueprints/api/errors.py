"""
Custom Errors: status code and Message
"""


class ErrorResponse(object):

    def __init__(self, code: str, message: str):
        self.message = message
        self.code = code

    def get_error_response(self):
        error = {
            "error": {
                "message": self.message,
                "code": self.code
            }
        }
        return error


def malformed_request():
    error_response = ErrorResponse(
        "malformed request",
        "01"
    )
    return error_response.get_error_response()


def physician_not_found():
    error_response = ErrorResponse(
        "physician not found",
        "02"
    )
    return error_response.get_error_response()


def patient_not_found():
    error_response = ErrorResponse(
        "patient not found",
        "03"
    )
    return error_response.get_error_response()


def metrics_service_not_available():
    error_response = ErrorResponse(
        "metrics service not available",
        "04"
    )
    return error_response.get_error_response()


def physicians_service_not_available():
    error_response = ErrorResponse(
        "physicians service not available",
        "05"
    )
    return error_response.get_error_response()


def patients_service_not_available():
    error_response = ErrorResponse(
        "patients service not available",
        "06"
    )
    return error_response.get_error_response()
