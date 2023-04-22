import requests
from pytest_voluptuous import S
from requests import Response


def check_ok_response(url, schema):
    response: Response = requests.get(url)

    assert response.status_code == 200
    assert S(schema) == response.json()