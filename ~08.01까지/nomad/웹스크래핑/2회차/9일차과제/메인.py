import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import math

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

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

new_list_list = []

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
            list.append(imfo)
                      
  new_list = []
  for v in list:
      if v not in new_list:
          new_list.append(v)
  content = sorted(new_list, key=lambda wow: wow["upvotes"],reverse=True)
  new_list_list.append(content)

a = new_list_list[0]
b = new_list_list[1]
result_list = a+b  
result_lists = sorted(result_list, key=lambda wow: wow["upvotes"],reverse=True)

app = Flask("DayEleven")

@app.route("/")
def main():
  return render_template("home.html", subreddits =subreddits)

@app.route("/read")
def read():
  language = list(request.args.to_dict())
  languages_list = []
  url_list = []
  for urls in language:
    languages_list.append("r/"+urls)
    url_list.append(f"https://www.reddit.com/r/{urls}/top/?t=month")  
  return render_template("read.html",language=languages_list,content=result_lists)
  

app.run(host="0.0.0.0")