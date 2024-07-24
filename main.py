import requests

# Defina sua chave de API aqui
api_key = "J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n" # - PADRÃO
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}" # - DEPENDE DO ENDPOINT

try:
    response = requests.get(api_url)# - PADRÃO
    response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx# - PADRÃO
    dados = response.json()# - PADRÃO

    data = dados.get('date') # - TÁ NA API https://api.nasa.gov/ - APOD CLICANDO NO LINK - "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    #CADA INFO ESTÁ NO JSON
    explicacao = dados.get('explanation')
    url = dados.get('url')
    titulo = dados.get('title')

    print(f"Data: {data}") # - PRINTANDO DADOS A CIMA
    print(f"Título: {titulo}") # - PRINTANDO DADOS A CIMA
    print(f"Explicação: {explicacao}") # - PRINTANDO DADOS A CIMA
    print(f"URL: {url}") # - PRINTANDO DADOS A CIMA

except requests.exceptions.HTTPError as http_err: # -  TRATAMENTO DE EXCESSÃO - PADRÃO
    print(f"HTTP error occurred: {http_err}") # -  TRATAMENTO DE EXCESSÃO - PADRÃO
except requests.exceptions.RequestException as req_err: # -  TRATAMENTO DE EXCESSÃO - PADRÃO
    print(f"Request error occurred: {req_err}") # -  TRATAMENTO DE EXCESSÃO - PADRÃO
except Exception as err: # -  TRATAMENTO DE EXCESSÃO - PADRÃO
    print(f"An error occurred: {err}") # -  TRATAMENTO DE EXCESSÃO - PADRÃO
