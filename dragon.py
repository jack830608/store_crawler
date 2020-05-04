import urllib.request as req
import json
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
src = req.Request(
    url="http://www.kq-tea.com/webc/html/location/", headers=headers)
with req.urlopen(src) as res:
    data = res.read()
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.findAll("ul", class_="list-unstyled")
with open('dragon.txt','w',  encoding="utf-8") as file:
    for title in titles:
        Ls = title.findAll('li')
        for l in Ls:
            if l.samp != None :
                print(l.samp.string)
                file.write(f"{l.samp.string}\n")
