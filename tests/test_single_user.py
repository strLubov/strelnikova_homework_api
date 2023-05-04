import pytest
from requests import Response

from helpers.metods import check_ok_response
from helpers.urls import APIRoutes
from schemas.list_user import single_user_schema


def test_check_get_single_user(reqres_api_client):
    """Проверяем схему и код страницы"""
    url = f'{APIRoutes.SINGLE_USER}2'
    response = reqres_api_client.send_request(method="get", url=url)
    check_ok_response(response=response, schema=single_user_schema)


@pytest.mark.parametrize('id_for_user', [1, 2])
def test_get_single_user(reqres_api_client, id_for_user):
    """Проверяем существующих пользователй. id равно значению запроса из url"""
    url = f'{APIRoutes.SINGLE_USER}{id_for_user}'
    response: Response = reqres_api_client.send_request(method='get', url=url)
    assert response.json().get("data").get("id") == id_for_user


def test_get_nonexistent_user_id(reqres_api_client):
    """Проверка несуществующего пользователя"""

    url = f'{APIRoutes.SINGLE_USER}23'

    response: Response = reqres_api_client.send_request(method='get', url=url)

    assert response.status_code == 404

def test_create_user(reqres_api_client):
    """Создание нового пользователя"""

    url = f'{APIRoutes.SINGLE_USER}'
    payload = {'name': 'morpheus', 'job': 'leader'}

    response: Response = reqres_api_client.send_request(method='post', url=url, json=payload)
    name = response.json()["name"]
    job = response.json()["job"]

    assert response.status_code == 201
    assert name == 'morpheus'
    assert job == 'leader'


def test_update_user(reqres_api_client, create_user):

    id_user = create_user

    url = f'{APIRoutes.SINGLE_USER}{id_user}'
    payload = {'name': 'morpheus', 'job': 'new job'}

    response: Response = reqres_api_client.send_request(method='put', url=url, json=payload)

    name = response.json()["name"]
    job = response.json()["job"]

    assert response.status_code == 200
    assert name == 'morpheus'
    assert job == 'new job'

