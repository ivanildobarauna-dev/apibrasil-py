""" Application feature to send messages to WhatsApp using the API Brasil. """

import os
from api_brasil.api_client.client_builder import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class CorreiosAPI(APIBrasilFeature):
    """The class is responsible for send messages to WhatsApp using the API Brasil."""

    def __init__(self, api_brasil_client: APIBrasilClient, device_token: str):
        self.api_brasil_client = api_brasil_client
        self.device_token = device_token

    def set_track_code(self, track_code: str):
        """Set the track code to track an object."""
        self.track_code = track_code

    def track(self) -> tuple:
        """Track an object."""
        endpoint = "/correios/rastreio"

        if not self.track_code:
            raise ValueError(
                "The track code is not set. Use the 'set_track_code' method to set the track code."
            )

        response, status_code = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "code": self.track_code,
            },
        )

        return response, status_code
