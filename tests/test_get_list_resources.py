from schemas.list_resources import list_resources_schema
from helpers.metods import check_ok_response
from helpers.urls import get_list_resources

import requests
from requests import Response


def test_check_ok_responce_get_resources():
    check_ok_response(get_list_resources, list_resources_schema)


def test_get_resources_total():
    """Проверяем общее количество пользователей"""

    response: Response = requests.get(get_list_resources)
    total = response.json()["total"]

    assert total == 12