import json
import requests

def conversione_diz():
    fileJson = '{"chiave":"valore","chiave2":"valore2"}'

    #print(type(fileJson))

    fileJsonConvertito = json.loads(fileJson)

    print(fileJsonConvertito)

dizionario = {"chiave":"valore","chiave2":"valore2"}

fileJson = json.dumps(dizionario)

print(fileJson)



risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m,precipitation_probability")

"""
print(risposta.json()['latitude'])
"""

risposta_text = risposta.text

risposta_json = json.loads(risposta_text)

print(risposta_json['latitude'])