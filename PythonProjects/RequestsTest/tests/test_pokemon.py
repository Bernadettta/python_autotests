import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eefd8e8089f64a55abdd32aa60b04d11'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': 'eefd8e8089f64a55abdd32aa60b04d11'}
TRAINER_ID = '31146'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["name"] == 'Bernadetta' 