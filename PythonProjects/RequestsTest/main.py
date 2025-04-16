import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eefd8e8089f64a55abdd32aa60b04d11'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': 'eefd8e8089f64a55abdd32aa60b04d11'}
body_pokemons = {
    "name": "Lilo",
    "photo_id": 741
}

body_change = {
    "pokemon_id": "291301",
    "name": "Fenya",
    "photo_id": 741
}

body_pokeball = {
    "pokemon_id": "291301"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text) 

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response.text) 

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.text) 
