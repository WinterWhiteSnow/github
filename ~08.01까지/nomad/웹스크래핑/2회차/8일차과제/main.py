import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

db = {}

def get_request(url, name):
  memory = requests.get(url)
  request_json = memory.json()
  hits = request_json["hits"]
  list = []
  for hit in hits:
      title = hit["title"]
      url = hit["url"]
      author = hit["author"]
      point = hit["points"]
      id = hit["objectID"]
      num_comment = hit["num_comments"]
      contents = {
          "title" : title,
          "url" : url,
          "author" : author,
          "point" : point,
          "num_comment" : num_comment,
          "id" : id
      }
      list.append(contents)
  db[name]=list    

def get_comment(id):
  get_url = requests.get(f"{base_url}/items/{id}")
  json_url = get_url.json()
  title = json_url["title"]
  url = json_url["url"]
  point = json_url["points"]
  author = json_url["author"]
  parent_tag = json_url["children"]
  a =  {
      "title":title,
      "url":url,
      "point":point,
      "author":author,
      "list" : []}
  for i in parent_tag:
      author = i["author"]
      text = i["text"]
      if i["author"] == None or i["text"]==None:
          text = "[deleted]"
          a["list"].append(text)
      else:
          text = {
              "author" : author,
              "text" : text
          } 
          a["list"].append(text)
  return a          

get_request(popular, "popular")
get_request(new, "new")
# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api



app = Flask("DayNine")

@app.route("/")
def main_popular():
  word = request.args.get("order_by")
  if word == None or word == "popular":
    key = "popular"
    script = db[key]            
  elif word == "new":
    key = "new"
    script = db[key]
  return render_template("index.html", wow=script, standard = key)

@app.route("/<id>")
def make_detail_url(id):
  script = get_comment(id)
  return render_template("detail.html", comments = script)

app.run(host="0.0.0.0")