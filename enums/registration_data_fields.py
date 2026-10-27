from enum import Enum


class Registration(str, Enum):
    EMAIL = "email"
    PASSWORD = "password"
    NAME = "name"

