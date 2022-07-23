import webexteamssdk
from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token="ZmMxMzg5MWEtOTQ5NC00M2ZlLTlmMDUtZjI5ZGI0ZTczN2VhY2IzNTExMzUtZmU5_PE93_34717e43-8e43-4f55-b8e9-8cf21a9f430d")

room = api.rooms.create("test room")

#Add a user to a room

api.memberships.create(room.id, personEmail="test_user@email.com")
