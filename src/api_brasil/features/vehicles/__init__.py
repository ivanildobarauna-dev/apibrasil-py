from api_brasil import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class VehiclesApi(APIBrasilFeature):
    def __init__(self, api_brasil_client: APIBrasilClient, device_token: str):
        self.api_brasil_client = api_brasil_client
        self.device_token = device_token

    def set_plate(self, plate: str):
        self.plate = plate
    
    def consulta_fipe(self):

        endpoint = "/vehicles/consultafipe"

        if not self.plate:
            raise ValueError("The plate is not set. Use the 'set_plate' method to set the plate.")
        
        response = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "placa": self.plate,
            }
        )

        return response