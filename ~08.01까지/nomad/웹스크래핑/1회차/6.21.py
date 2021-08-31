import os
import csv
import requests
from bs4 import BeautifulSoup


alba_url = "http://www.alba.co.kr/"


def open_csv(company):
    file = open(f"{company['name']}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["location","title","time","pay","befor"])
    for a in company["jobs"]:
        writer.writerow(list(a.values()))

request = requests.get(alba_url)
soup = BeautifulSoup(request.text, "html.parser")
a = soup.find("div",{"id":"MainSuperBrand"}).find("ul",{"class":"goodsBox"})
b = a.find_all("li",{"class":"impact"})


for i in b:
    name = i.find("strong").text  
    site = i.find("a")["href"]      
    if "/" in name:
        name = name.replace("/","").replace("?","").replace("%","").replace("*","").replace(":","").replace("|","").replace("'","").replace('"',"").replace(">","").replace("<","").replace(".","")
    
    company = {"name":name,'jobs':[]}

    request = requests.get(site)
    soup = BeautifulSoup(request.text, "html.parser")
    total = soup.find("div", {"id": "NormalInfo"}).find("tbody")
    result = total.find_all("tr",{"class":""})
    for a in result:
        tag_location = a.find("td", {"class": "local first"}).text
        tag_title = a.find("td", {"class":"title"}).find("span",{"class":"company"}).text
        tag_time = a.find("td", {"class":"data"}).text
        tag_pay = a.find("td",{"class":"pay"}).text
        tag_last = a.find("td", {"class": "regDate last"}).text
        jobs = {
            "location" : tag_location,
            "title" : tag_title,
            "time" : tag_time,
            "pay" : tag_pay,
            "befor" : tag_last
        }
        company['jobs'].append(jobs)


open_csv(company)




        



