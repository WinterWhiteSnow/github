from bs4 import BeautifulSoup
import os
import requests
import csv

os.system("cls")

url = "http://www.alba.co.kr/"

def write_file(index):
    file = open(f"{index['name']}.csv",mode="w",encoding="utf8")
    writer = csv.writer(file)
    writer.writerow(["[ local ]  " + "[ title ]  " + "[ time ]  " + "[ pay ]  " + "[ date ]  "])
    for content in index['content']:
        writer.writerow(list(content.values())) 

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
parent_tag = soup.find("div", {"id":"MainSuperBrand"}).find("ul",{"class":"goodsBox"})
child_tag = parent_tag.find_all("li",{"class":"impact"})
for superbrand in child_tag:
    links = superbrand.find("a")["href"]
    element = superbrand.find_all("a",{"class":"goodsBox-info"})
    for company in element:
        name = company.find("span",{"class":"company"}).text
        if "/" in name:
            name = name.replace("/",".")
    a = {
        "name":name,
        "content":[]
    }                   
    if links:                                                 
        request = requests.get(links)
        impo_soup = BeautifulSoup(request.text,"html.parser")
        parent_tag = impo_soup.find("div",{"id":"NormalInfo"}).find("tbody")
        child_tag = parent_tag.find_all("tr", {"class":""})
        for i in child_tag:
            local = i.find("td",{"class":"local"})
            if local:
                local = local.text     
            title = i.find("span",{"class":"company"})
            if title:
                title = title.text 
            time = i.find("td", {"class":"data"})
            if time:
                time = time.text 
            pay = i.find("td",{"class":"pay"})
            if pay:
                pay = pay.text 
            date = i.find("td",{"class":"last"})
            if date:
                date = date.text
            answer = {
                "local":local,
                "title" : title,
                "time" : time,
                "pay" : pay,
                "date" : date
            }    
            a["content"].append(answer)
    write_file(a)



         
            




