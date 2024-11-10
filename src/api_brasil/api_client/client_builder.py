from typing import Optional, Tuple
import requests

class APIBrasilClient:
    BASE_URL: str = "https://gateway.apibrasil.io/api/v2/"
    """ The client class is responsible for provide credentials to feature's ApiBrasil """
    def __init__(self,
                bearer_token: str,
                device_token: str,
                user_agent: str = "APIBrasil/Python-SDK") -> None:
        
        self.bearer_token = bearer_token
        self.device_token = device_token
        self.user_agent = user_agent 
        
    def _headers(self) -> dict:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.bearer_token,
            'DeviceToken': self.device_token,
            'User-Agent': self.user_agent
            }
        
        return headers

    def post_request(self, endpoint: str, body: str) -> Tuple[int, Optional[str]]:
            url = self.BASE_URL + endpoint
            response = requests.post(url=url, headers=self._headers(), data=body, allow_redirects=True, stream=True )

            if response.status_code != 200:
                 return response.status_code, response.reason

            return response.json()