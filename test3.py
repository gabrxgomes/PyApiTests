import requests

api_key = "J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n"
#api_key = "J3QlMqNxK84jeDNWX0UJJhEjJJCBJlU5bSobtp5n"
def hihihi(api_key):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={api_key}" # - PADRÃO
    response = requests.get(url) # - PADRÃO
    data = response.json() # - PADRÃO
    return data # - PADRÃO



data = hihihi(api_key) # - PADRÃO

print(data) # - PADRÃO
