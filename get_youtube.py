import requests
from lxml import etree
from urllib.parse import urlencode

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

url_youtube = "https://www.youtuberandom.com/"

def get_url():
    try:
        with requests.request('GET', url_youtube, headers = headers) as res:
            content = res.text
            html = etree.HTML(content)
            data = ''.join(html.xpath('//meta[@property="og:video:url" and @content]/@content'))
            dataList = list(data)
            dataList = dataList[-11:]

            url = 'https://www.youtube.com/watch?v=' + ''.join(dataList)

            return url

    except:
        return 'API has been restricted.'
