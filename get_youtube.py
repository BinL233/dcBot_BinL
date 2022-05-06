import requests
from lxml import etree
from urllib.parse import urlencode

headers = {
    "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

url_youtube = "https://www.youtuberandom.com/"

def get_url():
    with requests.request('GET', url_youtube, headers = headers) as res:
        content = res.text
        html = etree.HTML(content)
        data = ''.join(html.xpath('//meta[@property="og:video:url" and @content]/@content'))
        dataList = list(data)
        dataList = dataList[-11:]

        url = 'https://www.youtube.com/watch?v=' + ''.join(dataList)

        return url
