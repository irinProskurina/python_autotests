
import requests
HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
     response = requests.get(url= f'{HOST}/trainers', params= {'trainer_id': 1230}, timeout =5)
     assert response.status_code == 200, 'Unexpected status code for /trainers'
     assert response.json() ['trainer_name'] == 'sdsd', ''

    