from enum import Enum


class APIRoutes(str, Enum):
    SINGLE_USER = '/users/'
    USERS = '/users?page='
    RESOURCES = '/unknown'


    def __str__(self) -> str:
        return self.value