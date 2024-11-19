# SDK Python - APIGratis by APIBrasil

Conjunto de API, para desenvolvedores.

_Transforme seus projetos em solucoes inteligentes com nossa API. Com recursos como API do WhatsApp, geolocalizacao, rastreamento de encomendas, verificacao de CPF/CNPJ e mais, voce pode criar solucoes eficientes e funcionais._

## Como instalar

```pip install apigratis-sdk-python```
## Canais de suporte (Comunidade)
[![WhatsApp Group](https://img.shields.io/badge/WhatsApp-Group-25D366?logo=whatsapp)](https://chat.whatsapp.com/EeAWALQb6Ga5oeTbG7DD2k)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-32AFED?logo=telegram)](https://t.me/apigratisoficial)

## Obtenha suas credenciais
https://apibrasil.com.br

## Mais informacoes

https://pypi.org/project/api-brasil

## Servicos de API disponiveis

| Up  | Services available            | Description       | Free    | Beta        | Stable   |
------|-------------------------------|-------------------|---------| ------------------------- | ------------------------- |
| Yes | WhatsAppService                | API do WhatsApp                         |   Yes   | Yes                   | Yes                   |
| Yes | SMS                            | API de SMS              .               |   Yes   | Yes                   | Yes                   |
| Yes | Receita Data CNPJ              | API Dados CNPJ Receita.                 |   Yes   | Yes                   | Yes                   |
| Yes | Receita Data CPF               | API Dados de CPF Serasa.                |   Yes   | Yes                   | Yes                   |
| Yes | CorreiosService                | API Busca encomendas Correios Brazil.   |   Yes   | Yes                   | Yes                   |
| Yes | CEPLocation                    | API CEP Geolocation + IBGE Brazil.      |   Yes   | Yes                   | Yes                   |
| Yes | VehiclesService                | API Placa Dados.                        |   Yes   | Yes                   | Yes                   |
| Yes | FipeService                    | API Placa FIPE.                         |   Yes   | Yes                   | Yes                   |

## Como Instalar

* Usando pip

``` bash
pip install api-brasil 
```

* Usando poetry

``` bash
poetry add api-brasil 
```

## Documentacoes
https://apibrasil.com.br/documentacoes

```python
from api_brasil import APIBrasilClient, WhatsAppApi, VehiclesApi, CNPJApi
from api_brasil.features.vehicles import Endpoints


# Usando o cliente da API Brasil
api_brasil_client = APIBrasilClient(bearer_token="your_bearer_token_here")  # Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais

# # Usando a API de WhatsApp
whatsapp_api = WhatsAppApi(api_brasil_client=api_brasil_client, device_token="your_device_token_here") # Você pode encontrar o seu device token em https://apibrasil.com.br na área de Dispositivos

# # Enviando uma mensagem
whatsapp_api.to_number(phone_number="5511999999999")   # Número de telefone para enviar a mensagem
response, status_code = whatsapp_api.send_message(message="Hello, estou integrado com sucesso com Api Brasil!")

print(response, status_code)

# # Enviando um arquivo para o número definido no método to_number
response, status_code = whatsapp_api.send_file(file_path="https://apibrasil.io/img/capa.png", file_description="Bem vindo a API Brasil")

print(response, status_code)

# # Usando a API de Veículos
vehicles_api = VehiclesApi(api_brasil_client=api_brasil_client, device_token="your_device_token_here")
vehicles_api.set_plate(plate="ABC-1234")  # Placa do veículo
response, status_code = vehicles_api.consulta(vechiles_api_endpoint=Endpoints.dados) # Consulta os dados do veículo

print(response, status_code)

# # Usando a API de CNPJ
cnpj_api = CNPJApi(api_brasil_client=api_brasil_client, device_token="your_device_token_here")
cnpj_api.set_cnpj(cnpj="44.959.669/0001-80")  # CNPJ
response, status_code = cnpj_api.consulta() # Consulta os dados do CNPJ

print(response, status_code)
```