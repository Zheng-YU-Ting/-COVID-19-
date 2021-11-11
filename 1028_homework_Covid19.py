import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

ans = open('C:\\Users\\MSI\\Desktop\\作業\\三上\\物聯網大數據分析\python程式\\ans.csv', "w", encoding="utf-8")

URL = 'https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85'

req = requests.get(URL,headers = headers)

soup = BeautifulSoup(req.content, "html.parser")

tag_id = soup.find("div",id="covid19-container")
tag_tbody = tag_id.find("tbody")
tag_tr = tag_tbody.find_all("tr")
tag_td_a = tag_tbody.find_all("a")

n=1
ans.write("國家/地區,確診,死亡,治癒\n")
for i in range(0,len(tag_tr)):

    tag_td = tag_tr[i].find_all("td")

    if (str(tag_td_a[i+1].string)[0] == "[" or str(tag_td_a[i+1].string)[0] == "詳" or str(tag_td_a[i+1].string)[0] == "N"):
        continue
    else:
        ans.write(str(tag_td_a[i+1].string)+",")
    
        
        tag_td_body = tag_tr[n].find_all("td")

        for j in range(1,len(tag_td_body)-1):
            for k in str(tag_td_body[j].string).split():
                ans.write("\"" + k + "\"")
            ans.write(",")
        ans.write("\n")
        n+=1

ans.close