from os import access
import requests
import random

ACCESS_TOKEN = 'BQBEyYaFcQetSplzP6W_GIKoVqfrXAl1YqXk9TZ_PJwrTdYDPoEXh9m792Ffctw2YntWWA3xr-L5Q_N0j3WiYxQx81Qg3dEjVxw7x6BSRElgYo5Duws_OXwAfbv5yqfWYQ3uKbyEWz0YcKCaPCbtVnZLy2Ncp4yQTcqKaAU'



def get_track():
    num = random.randint(0,52)
    headers = {"Authorization" : f"Bearer {ACCESS_TOKEN}"}
    get_url = "https://api.spotify.com/v1/playlists/0hkMbHNNTtbyHOibUudH3g"
    response = requests.get(url=get_url, headers=headers)
    data = response.json()['tracks']['items'][num]['track']['external_urls']['spotify']
    return data