import urllib.request as req
import json
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
src = req.Request(
    url="http://50lan.com/web/pointsout.asp", headers=headers)
with req.urlopen(src) as res:
    data = res.read()
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.findAll("td", class_="tdinr")
with open('50blue.txt', 'w',  encoding="utf-8") as file:
    for title in titles:
        if title.string != None:
            if '服務地址' in title.string:
                file.write("location:"+ "\"" + title.string.replace('服務地址：','')+ "\"" + ',')
            elif '服務電話' in title.string:
                file.write("phone:"+ "\"" + title.string.replace('服務電話：','') + "\"" + "}" +"," + "\n" )
            elif '店' in title.string:
                file.write("{name:" + "\"" + title.string + "\"" +',')
            else:
                print(title.string)
# for 官網