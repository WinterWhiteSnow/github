import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import math

url = "https://www.reddit.com/r/{subreddit}/top/?t=month"
temporarily_url = "https://www.reddit.com/r/reactjs/top/?t=month"
subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]
www = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
def wow(url, languages):
    url_request =  requests.get(url, headers=headers)
    soup = BeautifulSoup(url_request.text, "html.parser")
    parent_tag = soup.find("div",{"class":"_1OVBBWLtHoSPfGCRaPzpTf _3nSp9cdBpqL13CqjdMr2L_ _2OVNlZuUd8L9v0yVECZ2iA"}).find("div", {"class":"rpBJOHq2PR60pnwJlUyP0"})
    child_tag = parent_tag.find_all("div")[1:]
    list = []
    for i in child_tag:
      standard = i.find("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
      if standard:
          title = standard.find("a",{"data-click-id":"body"})
          link = standard.find("a",{"data-click-id":"body"})
          upvotes = standard.find("div",{"class":"_1E9mcoVn4MYnuBQSVDt1gC"}).find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"})
          if title and upvotes and link:            
            titlt_text = title.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).text
            upvotes_text = upvotes.text
            if "k" in upvotes_text:
                upvotes_text_number = float(upvotes_text.split("k")[0])*1000
                upvotes_text = math.floor(upvotes_text_number)
            else:
                upvotes_text = int(upvotes_text)        
            link_text = link["href"]
            imfo = {
                "language": languages,
                "title":titlt_text,
                "link":link_text,
                "upvotes":upvotes_text
            }
            print(link_text)
            list.append(imfo)
                      
    new_list = []
    for v in list:
        if v not in new_list:
            new_list.append(v)
    content = sorted(new_list, key=lambda wow: wow["upvotes"],reverse=True)
    www.append(content)

# request =  requests.get(temporarily_url, headers=headers)
# soup = BeautifulSoup(request.text, "html.parser")
# parent_tag = soup.find("div",{"class":"_1OVBBWLtHoSPfGCRaPzpTf _3nSp9cdBpqL13CqjdMr2L_ _2OVNlZuUd8L9v0yVECZ2iA"}).find("div", {"class":"rpBJOHq2PR60pnwJlUyP0"})
# child_tag = parent_tag.find_all("div")[1:]
# list = []
# for i in child_tag:
#     standard = i.find("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
#     if standard:
#         title = standard.find("a",{"data-click-id":"body"})
#         link = standard.find("a",{"data-click-id":"body"})
#         upvotes = standard.find("div",{"class":"_1E9mcoVn4MYnuBQSVDt1gC"}).find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"})
#         if title and upvotes and link:            
#             titlt_text = title.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).text
#             upvotes_text = upvotes.text
#             if "k" in upvotes_text:
#                 upvotes_text_number = float(upvotes_text.split("k")[0])*1000
#                 upvotes_text = math.floor(upvotes_text_number)
#             else:
#                 upvotes_text = int(upvotes_text)        
#             link_text = link["href"]
#             imfo = {
#                 "language": "reactjs",
#                 "title":titlt_text,
#                 "link":link_text,
#                 "upvotes":upvotes_text
#             }
#             list.append(imfo)
                     

url_list = ["https://www.reddit.com/r/javascript/top/?t=month","https://www.reddit.com/r/reactjs/top/?t=month"]
languages_list = ["javascript","reactjs"]
for i,b in zip(url_list,languages_list):
    url = i
    languages = b
    wow(url=url, languages=languages)


a = www[0]
b = www[1]
c = a+b
content = sorted(c, key=lambda wow: wow["upvotes"],reverse=True)


    
          
   
/r/javascript/comments/odbrfy/i_studied_for_physics_exams_by_programming/