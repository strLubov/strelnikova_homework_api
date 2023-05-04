from requests import Response

from helpers.metods import check_ok_response
from helpers.urls import  APIRoutes
from schemas.list_resources import list_resources_schema


def test_check_ok_responce_get_resources(reqres_api_client):
    url = f'{APIRoutes.RESOURCES}2'
    response = reqres_api_client.send_request(method="get", url=url)
    check_ok_response(response=response, schema=list_resources_schema)


def test_get_resources_total(reqres_api_client):
    """Проверяем общее количество пользователей"""
    url = f'{APIRoutes.RESOURCES}2'
    response: Response = reqres_api_client.send_request(method='get', url=url)
    total = response.json()["total"]

    assert total == 12