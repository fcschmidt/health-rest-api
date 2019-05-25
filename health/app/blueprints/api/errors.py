"""
Custom Errors: status code and Message
"""
from flask import jsonify


def malformed_request():
    """Error Response 01

    Malformed Request 01
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "malformed request",
                "code": "01"
            }
        }
    )
    return response


def physician_not_found():
    """Errors Response

    Physician not found 02
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "physician not found",
                "code": "02"
            }
        }
    )
    return response


def patient_not_found():
    """Error Response

    Patient not found 03
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "patient not found",
                "code": "03"
            }
        }
    )
    return response


def metrics_service_not_available():
    """Error Response 04

    Metrics service not available
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "metrics service not available",
                "code": "04"
            }
        }
    )
    return response


def physicians_service_not_available():
    """Error Response 05

    Physicians service not available
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "physicians service not available",
                "code": "05"
            }
        }
    )
    return response


def patients_service_not_available():
    """Error Response 06

    Patients service not available
    :return:
    """
    response = jsonify(
        {
            "error": {
                "message": "patients service not available",
                "code": "06"
            }
        }
    )
    return response
