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

https://pypi.org/project/apigratis-sdk-python

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

## Como utilizar

_Voce pode utilizar todos os endpoints da API do WhatsApp, basta mudar o action e o body_

## Documentacoes
https://apibrasil.com.br/documentacoes

## WhatsApp Service

```python
from apigratis.Service import Service
import json

def whatsapp():

    #sendText
    sendText = Service().whatsapp(json.dumps({
        "action": "sendText",
        "credentials": {
            "DeviceToken": "SEU_DEVICE_TOKEN",
            "BearerToken": "SEU_BEARER_TOKEN",
        },
        "body": {
            "text": "Hello World for Python",
            "number": "5531994359434",
            "time_typing": 1
        }
    }))

    #sendFile
    sendFile = Service().whatsapp(json.dumps({
        "action": "sendFile",
        "credentials": {
            "DeviceToken": "SEU_DEVICE_TOKEN",
            "BearerToken": "SEU_BEARER_TOKEN",
        },
        "body":  {
            "number" : "5531994359434",
            "path" : "https://assets.nagios.com/downloads/nagiosxi/docs/Installing_The_XI_Linux_Agent.pdf",
            "options" : {
                "caption": "texto do caption para arquivo",
                "createChat": True,
                "filename": "arquivo X"
            }
        }
    }))

    print(sendFile)

if __name__ == "__main__":
    whatsapp()
```

## Vehicles Data Service

```python
from apigratis.Service import Service
import json

def vehicles():

    dados = Service().vehicles(json.dumps({
        "action": "dados",
        "credentials": {
            "DeviceToken": "SEU_DEVICE_TOKEN",
            "BearerToken": "SEU_BEARER_TOKEN",
        },
        "body":  {
            "placa": "OQH3A65"
        }
    }))

    print(dados)

if __name__ == "__main__":
    vehicles()
```

## Vehicles FIPE Service

```python
from apigratis.Service import Service
import json

def fipe():

    vehicle = Service().vehicles(json.dumps({
        "action": "fipe",
        "credentials": {
            "DeviceToken": "SEU_DEVICE_TOKEN",
            "BearerToken": "SEU_BEARER_TOKEN",
        },
        "body": {
            "placa": "OQH3065",
        }
    }))

    print(vehicle)

if __name__ == "__main__":
    fipe()
```

## Dados CNPJ Service

```python
from apigratis.Service import Service
import json

def cnpj():

    dados = Service().cnpj(json.dumps({
        "action": "cnpj",
        "credentials": {
            "DeviceToken": "SEU_DEVICE_TOKEN",
            "BearerToken": "SEU_BEARER_TOKEN",
        },
        "body": {
            "cnpj": "44.959.669/0001-80",
        }
    }))

    print(dados)

if __name__ == "__main__":
    cnpj()
```
