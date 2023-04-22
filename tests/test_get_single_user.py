import pytest
import requests
from requests import Response

from schemas.list_user import single_user_schema
from helpers.urls import get_single_user_url, get_single_user_2_url
from helpers.metods import check_ok_response


def test_check_get_list_users():
    """Проверяем схему и код страницы"""
    check_ok_response(get_single_user_2_url, single_user_schema)


@pytest.mark.parametrize('user_id', [2, 3, 4, 5])
def test_get_single_user_id(user_id):
    """Проверяем существующих пользователй. id равно значению запроса из url"""

    response: Response = requests.get(f'{get_single_user_url}/{user_id}')

    assert response.json().get("data").get("id") == user_id


def test_get_single_user_id():
    """Проверяем id пользователя"""

    response: Response = requests.get(get_single_user_2_url)
    id = response.json().get("data").get("id")

    assert id == 2


def test_get_nonexistent_user_id():
    """Проверка несуществующего пользователя"""

    response: Response = requests.get(f'{get_single_user_url}/23')

    assert response.status_code == 404
