import pytest
from requests import Response

from helpers.api_client import BaseSession
from helpers.urls import APIRoutes


@pytest.fixture()
def reqres_api_client():
    client = BaseSession(base_url="https://reqres.in/api")
    return client


@pytest.fixture()
def create_user(reqres_api_client):
    url = f'{APIRoutes.SINGLE_USER}'
    payload = {'name': 'morpheus', 'job': 'leader'}

    response: Response = reqres_api_client.send_request(method='post', url=url, json=payload)
    id = response.json()["id"]
    return id