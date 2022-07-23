import webexteamssdk
from webexteamssdk import WebexTeamsAPI



api = WebexTeamsAPI(access_token="ZmMxMzg5MWEtOTQ5NC00M2ZlLTlmMDUtZjI5ZGI0ZTczN2VhY2IzNTExMzUtZmU5_PE93_34717e43-8e43-4f55-b8e9-8cf21a9f430d")
print(api.people.me())


