from os import access
import requests
import random

ACCESS_TOKEN = 'BQBa4es87Sw1PyUW83DYblvz6j-yrKpWfNOT2C46pr6QFbIabvhv3hBsS8pcD629ZLCj80vOlEpeKtNOBi02JdccDrpD334lesYp7WURFfZoFiCn7k8FobiTH9gIX11XWNi-h732hQPQq6K7Svuso6fJVVcwo2V47eK8vJY'



def get_track():
    try:
        num = random.randint(0,52)
        headers = {"Authorization" : f"Bearer {ACCESS_TOKEN}"}
        get_url = "https://api.spotify.com/v1/playlists/0hkMbHNNTtbyHOibUudH3g"
        response = requests.get(url=get_url, headers=headers)
        data = response.json()['tracks']['items'][num]['track']['external_urls']['spotify']
        return data

    except:
        return 'API has been restricted.'