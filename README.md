# SDK Python - APIBrasil: Feito por desenvolvedores, para desenvolvedores.

Desbloqueie todo o potencial dos seus projetos com a APIBrasil! Integre funcionalidades como API do WhatsApp, geolocalização, rastreamento de encomendas, consulta de CPF/CNPJ e muito mais. Crie soluções inteligentes, eficientes e funcionais com rapidez e simplicidade.

## Documentações das APIs
https://apibrasil.com.br/documentacoes


## Features Disponíveis

| Up  | Services available            | Description       | Free    | Stable   |
------|-------------------------------|-------------------|---------| -------------------------| 
| ✅ | WhatsAppApi                   | API do WhatsApp                         |   ✅                      | ✅                   
| ✅ | SMSApi                        | API de SMS              .               |   ✅                      | ✅                   
| ✅ | CNPJApi                       | API Dados CNPJ Receita.                 |   ✅                      | ✅                   
| ✅ | CPFApi.                       | API Dados de CPF Serasa.                |   ✅                      | ✅                   
| ✅ | CorreiosAPI.                  | API Busca encomendas Correios Brazil.   |   🚧                      | ✅                   
| ✅ | CEPGeoLocationAPI             | API CEP Geolocation + IBGE Brazil.      |   ✅                      | ✅                   
| ✅ | VehiclesApi                   | API Placa Dados.                        |   ✅                      | ✅                   
| ✅ | VehiclesApi                   | API Placa FIPE.                         |   ✅                      | ✅                   


## Como usar esta SDK? 

1. Faça seu cadastro na plataforma -> https://apibrasil.com.br

2. Obtenha suas credenciais -> https://plataforma.apibrasil.com.br/myaccount/credentials
    - Importante: Você pode colocar suas credenciais diretamente em código o que chamamos de hard-coded, porém nós recomendamos que você coloque suas credenciais em variáveis de ambiente ou serviços gerenciados específicos para secrets.

2. Como Instalar

    * Usando pip

    ``` bash
    pip install api-brasil 
    ```

    * Usando poetry

    ``` bash
    poetry add api-brasil 
    ```


## Usando as APIs na prática, lets do this!

### _WhatsAppApi_
```python
from api_brasil import APIBrasilClient, WhatsAppApi

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


## Usando a API de WhatsApp
whatsapp_api = WhatsAppApi(api_brasil_client=api_brasil_client device_token="your_device_token_here") 
### Você pode encontrar o seu device token em https://apibrasil.com.br na área de Dispositivos


# # Enviando uma mensagem
whatsapp_api.to_number(phone_number="5511999999999")   # Número de telefone para enviar a mensagem
response, status_code = whatsapp_api.send_message(message="Hello, estou integrado com sucesso com Api Brasil!")

print(response, status_code)


# # Enviando um arquivo para o número definido no método to_number
response, status_code = whatsapp_api.send_file(file_path="https://apibrasil.io/img/capa.png", file_description="Bem vindo a API Brasil")

print(response, status_code)

```
### _VehiclesAPI_

```python

from api_brasil import APIBrasilClient, VehiclesAPI
from api_brasil.features.vehicles import Endpoints

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


# # Usando a API de Veículos
vehicles_api = VehiclesApi(api_brasil_client=api_brasil_client, device_token="your_device_token_here")
vehicles_api.set_plate(plate="ABC-1234")  # Placa do veículo
response, status_code = vehicles_api.consulta(vechiles_api_endpoint=Endpoints.dados) # Consulta os dados do veículo

print(response, status_code)
```

### _CNPJApi_
```python
from api_brasil import APIBrasilClient, CNPJApi

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


# # Usando a API de CNPJ
cnpj_api = CNPJApi(api_brasil_client=api_brasil_client, device_token="your_device_token_here")
cnpj_api.set_cnpj(cnpj="44.959.669/0001-80")  # CNPJ
response, status_code = cnpj_api.consulta() # Consulta os dados do CNPJ

print(response, status_code)
```

### _CorreiosApi_
```python
# # Usando a API de Correios
from api_brasil import APIBrasilClient, CorreiosAPI

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


correios_api = CorreiosAPI(api_brasil_client=api_brasil_client,
                           device_token="your_device_token")
correios_api.set_track_code(track_code="PN123456789BR")  # Código de rastreamento
response, status_code = correios_api.track() # Rastreia o objeto

print(response, status_code)

```

### _GeoLocalizationAPI_
```python
# # Usando a API de Geolocalização de CEP
from api_brasil import APIBrasilClient, CEPGeoLocationAPI

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


cep_geolocation_api = CEPGeoLocationAPI(api_brasil_client=api_brasil_client,
                           device_token="your_device_token")
                           

cep_geolocation_api.set_cep(cep="00000-000")  # CEP
response, status_code = cep_geolocation_api.consulta() # Consulta a geolocalização do CEP

print(response, status_code)
```

### CPFApi
```python
# Usando a API de CPF
from api_brasil import APIBrasilClient, CPFApi

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


cpf_api = CPFApi(api_brasil_client=api_brasil_client,
                           device_token="your_device_token")
cpf_api.set_cpf(cpf="00000000000")  # CPF
response, status_code = cpf_api.consulta() # Consulta os dados do CPF
print(response, status_code)

```

### _SMSApi_
```python
# Usando a API de SMS
from api_brasil import APIBrasilClient, SMSApi

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClien(bearer_token="your_bearer_token_here")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais

sms = SMSApi(api_brasil_client=api_brasil_client,
             device_token="your_device_token")

sms.set_phone_number(number="5511900000000")  # Número de telefone 
response, status_code = sms.send(message="Hello, estou integrado com sucesso com Api Brasil!") # Envia a mensagem
print(response, status_code)
```

# Canais de suporte e comunidade
[![WhatsApp Group](https://img.shields.io/badge/WhatsApp-Group-25D366?logo=whatsapp)](https://chat.whatsapp.com/EeAWALQb6Ga5oeTbG7DD2k)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-32AFED?logo=telegram)](https://t.me/apigratisoficial)
