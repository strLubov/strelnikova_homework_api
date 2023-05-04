from pytest_voluptuous import S
from requests import Response


def check_ok_response(response: Response, schema) -> dict:
    assert response.status_code == 200
    assert S(schema) == response.json()
    return response.json()
