from os import access
import requests
import random

ACCESS_TOKEN = 'BQBYJDvdIJBgH0VBwXMFlM6m2QNPsrR0aFFxSIWTuVE-P-ueyPOZZSEP-pH51C_PjqO4uBhHiiXk78dFYkij5OUApw7KWq12wK9aHHuXtJGgwNdnn05gTHMZrgmE0KjTLgFMlfFiMbRZqdDsLxUQOoI_pqoiXmdg2lYG2wI'



def get_track():
    num = random.randint(0,99)
    headers = {"Authorization" : f"Bearer {ACCESS_TOKEN}"}
    get_url = "https://api.spotify.com/v1/playlists/0hkMbHNNTtbyHOibUudH3g"
    response = requests.get(url=get_url, headers=headers)
    data = response.json()['tracks']['items'][num]['track']['external_urls']['spotify']
    return data

