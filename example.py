from api_brasil import APIBrasilClient, WhatsAppApi

client = APIBrasilClient(
    bearer_token='FakeBearerToken',
    device_token='FakeDeviceToken'
)

whatsapp = WhatsAppApi(client)

whatsapp.execute("FakeMessage", "19283192312931")