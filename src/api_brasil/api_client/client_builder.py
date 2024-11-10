class APIBrasilClient:
    """ The client class is responsible for provide credentials to feature's ApiBrasil """
    def __init__(self,
                bearer_token: str,
                device_token: str) -> None:
        
        self.bearer_token = bearer_token
        self.device_token = device_token

    def get_credentials(self) -> dict:
        return {
            'bearer_token': self.bearer_token,
            'device_token': self.device_token
        }        