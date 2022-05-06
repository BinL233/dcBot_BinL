from os import access
import requests
import random

ACCESS_TOKEN = 'BQBBQzr1SNX-5m3OmXpQ-Sz96ej_N0PPB4FNp6wTBkLLiUCEArB0ZtmwVdcDFlJgnfdsrxRGUe49sse2Xu2VjxYx-fwHZsQvrZhKVTVgXLi9JdCLz_S-6giUYEdPoIiMl5lbfk5XOdtnTNVYmN8zXlOkaA4EKZscwPn21b8'



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