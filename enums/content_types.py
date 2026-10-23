from enum import Enum


class ContentTypes(str, Enum):
    JSON_LD = "application/ld+json"
    JSON = "application/json"
