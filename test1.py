import requests

# Defina sua chave de API aqui
api_key = "J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n"

# Data específica da imagem desejada no formato YYYY-MM-DD
date = "2023-07-01"
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
    dados = response.json()

    data = dados.get('date')
    explicacao = dados.get('explanation')
    url = dados.get('url')
    titulo = dados.get('title')

    print(f"Data: {data}")
    print(f"Título: {titulo}")
    print(f"Explicação: {explicacao}")
    print(f"URL: {url}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as err:
    print(f"An error occurred: {err}")
