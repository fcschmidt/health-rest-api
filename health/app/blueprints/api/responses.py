from flask import jsonify


def resp_content_successfully(content):
    """Response 201 Created Successfully"""
    response = jsonify({"data": content})
    response.status_code = 201
    return response
