import requests
import json


apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'ZmMxMzg5MWEtOTQ5NC00M2ZlLTlmMDUtZjI5ZGI0ZTczN2VhY2IzNTExMzUtZmU5_PE93_34717e43-8e43-4f55-b8e9-8cf21a9f430d'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = {'sortBy': 'lastactivity', 'max': '2'}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

json_object = json.loads(response.text)
json_formatted = json.dumps(json_object, indent=4)

print( response.status_code )
print(json_formatted)
