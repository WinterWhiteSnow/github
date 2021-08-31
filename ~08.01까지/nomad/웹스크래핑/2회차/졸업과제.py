import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request,send_file, redirect
from requests.api import head
from werkzeug.datastructures import Headers
import csv

db = {}
languages = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django",
    "python",
    "nest"
]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}    

def save_file(db):
  file = open("jobs.csv",mode="w",encoding="utf8")
  writer = csv.writer(file)
  writer.writerow(["[ title ]  " + "[ company ]  " + "[ link ]  "])
  for content in db['weworkremotely']:
    writer.writerow(list(content.values())) 
  for content in db['stackoverflow']:
    writer.writerow(list(content.values())) 
  for content in db['remoteok']:
    writer.writerow(list(content.values())) 

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}    
db = {}

def weworkremotely(language):
  url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={language}"
  r = requests.get(url)
  soup = BeautifulSoup(r.text,"html.parser")
  parent_tag = soup.find_all("article")
  list = []
  for a in parent_tag:
    child_tag = a.find("ul")
    standard_tag = child_tag.find_all("li")
    for i in standard_tag:
      a = i.find_all("a")
      for i in a:
        company = i.find("span",{"class":"company"})
        if company:
            company = company.text
        if "remote-jobs" in i["href"]:
            link = "https://weworkremotely.com/"+i["href"]
        title = i.find("span",{"class":"title"})
        if title:
            title=title.text
      result = {
          "title":title, 
          "company":company, 
          "link":link
      }
      list.append(result)
  db["weworkremotely"]=list


def stackoverflow(language):
    stack_url = f"https://stackoverflow.com/jobs?q={language}"
    page_r = requests.get(stack_url, headers=headers)
    page_soup = BeautifulSoup(page_r.text,"html.parser")
    parent_tag_page = page_soup.find("div",{"class":"previewable-results"})
    page = parent_tag_page.find("div",{"py32 px16"}).find("div",{"class":"flex--item"}).find("div",{"class":"s-pagination"}).find_all("a")[:-1]
    last_page = int(page[-1].text.strip())
    list=[]
    for pages in range(last_page):
        urls = f"https://stackoverflow.com/jobs?q={language}&pg={pages+1}"
        r = requests.get(urls,headers=headers)
        soup = BeautifulSoup(r.text,"html.parser")   
        one = soup.find("div",{"class":"listResults"}).find_all("div",{"class":"d-flex"})
        two = soup.find("div",{"class":"listResults"}).find_all("p")
        for i in one:
            a = i.find_all("div",{"class":"flex--item fl1"})
            if a:
                for i in a:
                    wow = i.find("h2",{"class":"mb4"})
                    wow2 = i.find_all("h3",{"class":"mb4"})
                    if wow:
                        title = wow.text.strip()
                        link = wow.find("a")["href"]
                    if wow2:
                        for i in wow2:
                            company = i.find("span").text.strip()
                            e = {
                                "title":title,
                                "company":company,
                                "link":f"https://stackoverflow.com/{link}/"
                            }
                            list.append(e)
    db["stackoverflow"]=list                        
                            

def remoteok(language):
    url = f"https://remoteok.io/remote-{language}-jobs"
    request = requests.get(url,headers=headers)
    soup = BeautifulSoup(request.text,"html.parser")
    parent_tag = soup.find("div",{"class":"page"}).find("table",{"id":"jobsboard"})
    tbody = parent_tag.find_all("td",{"class":"company"})
    list=[]
    for i in tbody:
        title_tag =i.find("a",{"itemprop":"url"})
        company_tag = i.find("a",{"class":"preventLink"})
        if title_tag:
            title = title_tag.text
            link =title_tag["href"]
        if company_tag:
            company = company_tag.text
            result = {
                "title":title,
                "company":company,
                "link":f"https://remoteok.io{link}"
            }
            list.append(result)
    db["remoteok"]=list





app = Flask("DayEleven")

@app.route("/")
def main():
  return render_template("main.html",languages=languages)

@app.route("/search")
def search(): 
  language = request.args.to_dict()["language"]
  fromdb = db.get(language)
  if fromdb:
    all_db = db
    number = len(db["weworkremotely"])+len(db["stackoverflow"])+len(db["remoteok"])
  elif not fromdb:
      raise Exception()
  else:
    weworkremotely(language)
    stackoverflow(language)
    remoteok(language)
    all_db = db
    number = len(db["weworkremotely"])+len(db["stackoverflow"])+len(db["remoteok"])
  return render_template("search.html",db=all_db,number=number,language=language)

@app.route("/export")
def export():
  try:
    language = request.args.to_dict()["language"]
    if not language:
      raise Exception()
    fromdb = db.get("remoteok")
    if not fromdb:
      raise Exception()
    save_file(db)
    return save_file("jobs.csv")
  except: 
    return redirect("/")   
    
app.run(host="0.0.0.0")
