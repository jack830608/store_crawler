import urllib.request as req
import json
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
src = req.Request(
    url="http://www.i-write.idv.tw/life/info/starbucks17.html", headers=headers)
with req.urlopen(src) as res:
    data = res.read()
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.findAll("tr", height=[22, 44 ,66])
with open('starbucks.txt', 'w',  encoding="utf-8") as file:
    for title in titles:
        Ls = title.findAll('td')
        for l in Ls:
            if '門市名稱' in l.string:
                print(l.string)
            elif '門市電話' in l.string:
                print(l.string)
            elif '門市地址' in l.string:
                print(l.string)
            elif '門市營業時間' in l.string:
                print(l.string)
            elif '號' in l.string:
                file.write("location:"+ "\"" + l.string + "\"" + "}" +"," + "\n" )
            elif '-' in l.string:
                file.write("phone:"+ "\"" + l.string + "\"" +',')
            elif '門市' in l.string:
                file.write("{name:" + "\"" + l.string + "\"" +',')
            else:
                print(l.string)
