import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

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



def scrap(a):
    url = f"https://www.reddit.com/r/{a}/top/?t=month"
    list_list=[]
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,"html.parser")
    prent_tag = soup.find("div",{"class":"rpBJOHq2PR60pnwJlUyP0"})
    prent_tag = prent_tag.find_all("div",{"class":"Post"})
    for i in prent_tag:
        title = i.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).text
        vote_point = i.find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"}).string
        link = i.find("a",{"data-click-id":"body"})
        if "k" in vote_point:
            vote_point = float(vote_point.replace("k",""))*1000
        if link:
            link = link["href"]
            vote_point= int(vote_point)
            dict_list = {
                "title":title,
                "vote_point":vote_point,
                "link":link,
                "word":a

            }
            list_list.append(dict_list)
    return list_list


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html",wow=subreddits)

@app.route("/read")
def read():
    sort_list=[]
    db_list = []
    word = request.args
    word = list(word.keys())
    for a in word:
        wow = scrap(a)
        db_list.append(wow)
    for i in db_list:
        for a in i:
            sort_list.append(a)
    result = sorted(sort_list, key=lambda potato: potato['vote_point'], reverse=True)              
    return render_template("read.html",wow=result,word=word)

if __name__ == "__main__":
    app.run()



# result = sorted(db_list, key=lambda potato: potato['vote_point'], reverse=True)