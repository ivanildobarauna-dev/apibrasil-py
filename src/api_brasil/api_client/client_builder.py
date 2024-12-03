from typing import Tuple
import json
import requests


class APIBrasilClient:
    BASE_URL: str = "https://gateway.apibrasil.io/api/v2"
    """ The client class is responsible for provide credentials to feature's ApiBrasil """

    def __init__(
        self, bearer_token: str, user_agent: str = "APIBrasil/Python-SDK"
    ) -> None:

        self.bearer_token = bearer_token
        self.user_agent = user_agent

    def _headers(self, device_token: str) -> dict:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.bearer_token,
            "DeviceToken": device_token,
            "User-Agent": self.user_agent,
        }

        return headers

    def post_request(
        self, endpoint: str, device_token: str, body: str
    ) -> Tuple[dict, int]:
        url = self.BASE_URL + endpoint
        response = requests.post(
            url=url,
            headers=self._headers(device_token=device_token),
            data=json.dumps(body),
            allow_redirects=True,
            stream=True,
        )

        if not (200 <= response.status_code < 300):
            raw_response = {
                "is_error": response.json()["error"],
                "response_status_code": response.status_code,
                "response_reason": response.reason,
                "response_body": response.json(),
            }

            return json.dumps(raw_response, indent=4), response.status_code

        return json.dumps(response.json(), indent=4), response.status_code
