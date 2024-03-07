import requests

url = "https://farmadati.es/api/medicamentos/porNombre?nombre=ibuprofeno"

headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
