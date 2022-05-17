import requests
from lxml import etree

def get_course(name, code):
    try:
        datalist = []
        data = ''
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        get_url = "https://bulletins.psu.edu/ribbit/index.cgi?page=getcourse.rjs&code=" + name + "%20" + code
        response = requests.get(url=get_url, headers=headers)
        content = response.text
        html = etree.HTML(content)
        datalist.append(html.xpath('/html/body/courseinfo/course/div[1]/div[1]/div[2]'))
        datalist.append(html.xpath('/html/body/courseinfo/course/div[2]/div[2]/div[2]/div[2]'))
        x=1
        while x <= 10:
            if html.xpath('/html/body/courseinfo/course/div[3]/div[2]/p[' + str(x) + ']') != []:
                datalist.append(html.xpath('/html/body/courseinfo/course/div[3]/div[2]/p[' + str(x) + ']'))
                x+=1
            else:
                break
        
        i = 0
        while i < len(datalist):
            data += datalist[i][0].text.strip() + "\n"
            i+=1
        
        return data
        

    except:
        return 'API has been restricted.'