import requests

formula = '1+1'    
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
get_url = 'https://www.symbolab.com/pub_api/steps?subscribed=false&origin=input&language=en&query=1%2B5&referer=https%3A%%2F%%2Fwww.symbolab.com%%2Fsolver%%2Fstep-by-step%%2F%255Cint%%2520x%%255E%257B-1%257D&plotRequest=PlotOptional&page=step-by-step'
response = requests.get(url=get_url, headers=headers)
json_data = response.json()['solutions']