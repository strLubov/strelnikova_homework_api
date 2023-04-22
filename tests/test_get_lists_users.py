import pytest
import requests
from requests import Response

from schemas.list_user import list_users_schema
from helpers.urls import get_list_users_url, get_list_users_2_page_url
from helpers.metods import check_ok_response


def test_check_get_list_users():
    """Проверяем схему и код страницы"""
    check_ok_response(get_list_users_2_page_url, list_users_schema)


@pytest.mark.parametrize('number_page', [1, 2])
def test_get_users_page_number(number_page):
    """Проверяем номер страницы"""

    response: Response = requests.get(f"{get_list_users_url}{number_page}")

    assert response.json().get("page") == number_page


def test_get_users_users_on_page():
    """Проверяем дефолтное количество пользователей на странице и что вернулось столько же пользователей."""

    response: Response = requests.get(get_list_users_2_page_url)

    per_page = response.json().get("per_page")
    data_len = len(response.json().get("data"))

    assert data_len == per_page == 6


def test_get_users_total():
    """Проверяем общее количество пользователей"""

    response: Response = requests.get(get_list_users_2_page_url)
    total = response.json()["total"]

    assert total == 12
