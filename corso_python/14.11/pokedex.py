import json, requests, random


num = random.randint(1,1025)

url = f"https://pokeapi.co/api/v2/pokemon/{num}"

response = requests.get(url)
data = response.json()

print(data)