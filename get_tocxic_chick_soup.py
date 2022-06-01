import requests

def get_soup():
    try:
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        get_url = "https://www.iamwawa.cn/home/dujitang/ajax"
        response = requests.get(url=get_url, headers=headers)
        data = response.json()['data']
        return data

    except:
        return 'API has been restricted.'