import requests

# Создание покемона  
    
response = requests.post(url="https://api.pokemonbattle.me:9104/pokemons",
json = { "name": "Бульбазав",
         "photo": "https://dolnikov.ru/pokemons/albums/001.png"
        },
 headers= {'Content-Type': 'application/json',
           "trainer_token": "9b4d31e7551d3eeac0d3dba8b698a1f5"}, timeout =5)

json_response = response.json()

print(json_response)

# Смена имени покемона
 
response = requests.put(url="https://api.pokemonbattle.me:9104/pokemons",
json = {  "pokemon_id": "6590",
            "name": "Котик",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
        },
headers= {'Content-Type': 'application/json',
           "trainer_token": "9b4d31e7551d3eeac0d3dba8b698a1f5"}, timeout =5)

json_response = response.json()

print(json_response)


# Поймать покемона в покебол 

response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/add_pokeball",
json = {  "pokemon_id": "6590"
       },
headers= {'Content-Type': 'application/json',
          "trainer_token": "9b4d31e7551d3eeac0d3dba8b698a1f5"}, timeout =5)

json_response = response.json()

print(json_response)

