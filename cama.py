import json
import urllib.request as request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
src = request.Request(url="https://www.camacafe.com/store_location/getList", headers=headers)
with request.urlopen(src) as res:
    data = json.load(res)
with open('cama.json', mode="w", encoding="utf-8")as file:
    json.dump(data, file, ensure_ascii=False)