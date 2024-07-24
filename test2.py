import requests

# Defina sua chave de API aqui
api_key = "J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n"

# Data específica da imagem desejada no formato YYYY-MM-DD
start_date = '2015-09-08'
end_date = '2015-09-09'
api_url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={api_key}&start_date={start_date}&end_date={end_date}"

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx
    dados = response.json()

    # Extraindo dados específicos do JSON
    data_start = dados.get('element_count')
    near_earth_objects = dados.get('near_earth_objects', {})

    print(f"Data de início: {start_date}")
    print(f"Data de fim: {end_date}")
    print(f"Contagem de objetos próximos da Terra: {data_start}")

    for date, objects in near_earth_objects.items():
        print(f"\nObjetos próximos da Terra em {date}:")
        for obj in objects:
            nome = obj.get('name')
            estimativa_diametro = obj.get('estimated_diameter', {}).get('kilometers', {})
            diametro_min = estimativa_diametro.get('estimated_diameter_min')
            diametro_max = estimativa_diametro.get('estimated_diameter_max')
            print(f"Nome: {nome}")
            print(f"Diâmetro estimado: {diametro_min} km - {diametro_max} km")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as err:
    print(f"An error occurred: {err}")
