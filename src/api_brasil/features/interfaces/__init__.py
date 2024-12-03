from api_brasil import APIBrasilClient

from abc import ABC


class APIBrasilFeature(ABC):
    """The interface for implement APIBrasil Features"""

    def __init__(self, api_brasil_client: APIBrasilClient, device_token: str):
        pass
