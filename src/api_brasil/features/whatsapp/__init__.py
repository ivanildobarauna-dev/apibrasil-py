""" Application feature to send messages to WhatsApp using the API Brasil. """

import os
from api_brasil.api_client.client_builder import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class WhatsAppApi(APIBrasilFeature):
    """The class is responsible for send messages to WhatsApp using the API Brasil."""

    def __init__(
        self,
        api_brasil_client: APIBrasilClient,
        device_token: str,
        time_typing: int = 1,
    ):
        self.api_brasil_client = api_brasil_client
        self.device_token = device_token
        self.time_typing = time_typing
        self.phone_number = None

    def to_number(self, phone_number: str):
        """Set the phone number to send the message."""
        self.phone_number = phone_number

    def send_message(self, message: str) -> tuple:
        """Send a message to the phone number set."""
        endpoint = "/whatsapp/sendText"

        if not self.phone_number:
            raise ValueError(
                "The phone number is not set. Use the 'to_number' method to set the phone number."
            )

        if not message:
            raise ValueError("The message is empty.")

        response, status_code = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "text": message,
                "number": self.phone_number,
                "time_typing": self.time_typing,
            },
        )

        return response, status_code

    def send_file(
        self, file_path: str, file_description: str = None, create_chat: bool = True
    ) -> tuple:
        """Send a file to the phone number set."""
        endpoint = "/whatsapp/sendFile"

        if not self.phone_number:
            raise ValueError(
                "The phone number is not set. Use the 'to_number' method to set the phone number."
            )

        if not file_path:
            raise ValueError("The file path is empty.")

        response, status_code = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "number": self.phone_number,
                "path": file_path,
                "time_typing": self.time_typing,
                "options": {
                    "caption": file_description if file_description else "",
                    "createChat": create_chat,
                    "filename": os.path.basename(file_path),
                },
            },
        )

        return response, status_code
