import pytest
from requests import Response

from helpers.metods import check_ok_response
from helpers.urls import APIRoutes
from schemas.list_user import list_users_schema


def test_check_get_list_users(reqres_api_client):
    """Проверяем схему и код страницы"""
    url = f'{APIRoutes.USERS}2'
    response = reqres_api_client.send_request(method="get", url=url)
    check_ok_response(response=response, schema=list_users_schema)


@pytest.mark.parametrize('number_page', [1, 2])
def test_get_users_page_number(reqres_api_client, number_page):
    """Проверяем номер страницы"""

    url = f'{APIRoutes.USERS}{number_page}'

    response: Response = reqres_api_client.send_request(method='get', url=url)

    assert response.json().get("page") == number_page


def test_get_users_users_on_page(reqres_api_client):
    """Проверяем дефолтное количество пользователей на странице и что вернулось столько же пользователей."""

    url = f'{APIRoutes.USERS}2'

    response: Response = reqres_api_client.send_request(method='get', url=url)

    per_page = response.json().get("per_page")
    data_len = len(response.json().get("data"))

    assert data_len == per_page == 6


def test_get_users_total(reqres_api_client):
    """Проверяем общее количество пользователей"""

    url = f'{APIRoutes.USERS}2'

    response: Response = reqres_api_client.send_request(method='get', url=url)
    total = response.json()["total"]

    assert total == 12
