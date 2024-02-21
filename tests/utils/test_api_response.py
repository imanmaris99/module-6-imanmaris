from flask import Flask
from app.utils.api_response import api_response

app = Flask(__name__)

def test_api_response():
    with app.test_request_context():
       response, status_code = api_response(200,{"test": "check"},"message")

    expected_response = {"test": "check"}
    assert response.json['data'] == expected_response
    assert status_code == 200


def test_api_response_return_400():
    with app.test_request_context():
       response, status_code = api_response(400,{},"not available")

    expected_response = {}
    assert response.json['data'] == expected_response
    assert status_code == 400