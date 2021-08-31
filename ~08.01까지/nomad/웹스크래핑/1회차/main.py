import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"
db = {}
# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"
def news(url, key):
  url_list = requests.get(url).json()
  key = requests.args.get('order_by')
  if key == None:
    key = "popular"
  else:
    key = requests.args.get('order_by')
  a = url_list['hits']
  for i in a:
    title = i['title']
    url = i['url']
    points = i['points']
    author = i['author']
    comments = i["num_comments"]
    objectID = i["objectID"]
    nomad_news = {
      'title':title,
      'url':url,
      'points':points,
      'author':author,
      'comments':comments,
      'objectid':objectID
    }
    db[key] = nomad_news

def comments(make_detail_url):
  c = requests.get(make_detail_url).json()
  d = c["children"]
  for i in d:
    author = i["author"] 
    text = i["text"]
    if author and text:
      children = {
        'author':author,
        'text':text
      }
    else:
      children = ["deleted"]

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return  f"{base_url}/items/{id}"


app = Flask("DayNine")

@app.route("/")
def home():
  wow = new(popular)
  return render_template(
    "index.html",
    nomad_news = wow
  )

@app.route("/order_by")
def oder_by():
  state = requests.args.get('order_by')
  if state == "popular":
    db[state] = news(popular)
    if True:
      fromDb = db.get(state)
    else:
      nomad_news = new(popular)
      db[state] = nomad_news
      print(db[state].keys())
    return render_template(
      "index.html",
      nomad_news = db[state]
    )
  
app.run(host="0.0.0.0")
