import requests
from flask import Flask, render_template, request
from pprint import pprint

base_url = "http://hn.algolia.com/api/v1"
db = {}
# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

def news(url, name):
  url_list = requests.get(url).json()
  a = url_list['hits']
  for i in a:
    title = i['title']
    url = i['url']
    points = i['points']
    author = i['author']
    comments = i["num_comments"]
    id = i["objectID"]
    nomad_news = {
      'title':title,
      'url':url,
      'points':points,
      'author':author,
      'comments':comments,
      'id':id
    }
    db[name] = nomad_news

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