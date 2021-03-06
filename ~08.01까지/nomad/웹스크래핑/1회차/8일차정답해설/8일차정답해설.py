import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"
new = f"{base_url}/search_by_date?tags=story"
popular = f"{base_url}/search?tags=story"

def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get('order_by', 'popular')
  if order_by not in db:
    print("Requesting")
    if order_by == 'popular':
      news = requests.get(popular)
    elif order_by == 'new':
      news = requests.get(new)
    results = news.json()['hits']
    db[order_by] = results
  results = db[order_by]
  return render_template("index.html", order_by=order_by, results=results)


@app.route("/<id>")
def detail(id):
  detail_request = requests.get(make_detail_url(id))
  result = detail_request.json()
  return render_template("detail.html",result=result)

app.run(host="0.0.0.0")








# 이번 챌린지는 requests 라이브러리를 이용하여 api에 요청을 보내 정보를 가져온 뒤, 웹 프레임워크인 flask 를 이용하여 웹사이트를 만듭니다.

# API URL 설정 & fake DB (Line 4 ~ 12)
# flask로 만든 홈페이지에 뿌려줘야 될 정보는 인기순과 최신순으로 정렬된 데이터들 입니다.
# Line 4 ~ 6 : base_url 을 기본으로 하여 최신순 데이터들의 api는 new에 인기순 데이터들의 api는 popular에 저장합니다.
# make_detail_url(id) 함수 : 이 함수는 각 기사에 해당하는 코멘트들을 얻기 위한 api를 id값을 이용해 호출합니다.
# Line 11 ~ 12 : 로딩속도를 줄여주기 위한 빈 fakeDB를 만들어주고 플라스크 애플리케이션을 생성해주는 코드인 app = Flask("DayNine") 를 입력해줍니다.
# 루트패스 "/" 구현 (Line 14 ~ 26, index.html)
# 한 페이지 내에서 popular, new로 왔다갔다 하려면 URL 파라미터로 값을 넘겨 받아야 됩니다.
# 참고문서 : request.args.get()
# Line 17 ~ Line 22 : 만약 fakeDB에 해당 파라미터에 대한 정보가 저장되어 있지 않다면 requests 라이브러리를 이용하여 해당하는 api에 요청을 보내서 그 결과를 해당 변수에 저장해야 됩니다.
# Line 23 : 요청해서 받아 온 api를 읽어오기 위해 requests 라이브러리의 .json() 을 사용합니다.
# 참고문서 : .json()
# Line 25 : 받아 온 데이터를 fakeDB에 저장합니다.
# Line 26 : index.html 로 order_by 값과 results 값을 보내줍니다.
# index.html의 Line 19 ~ Line 32 : 조건문을 활용하여 사용자가 new 를 클릭하면 popular에 popular로 이동할 수 있는 링크를 생성해 주고 사용자가 popular를 클릭하면 new에 new로 이동할 수 있는 링크를 생성해 줍니다.
# index.html의 Line 35 ~ Line 48 : 사용자가 선택한 order_by 값을 토대로 해당하는 정보들을 뿌려줍니다.
# "/＜id＞" 패스 구현 (Line 29 ~ 33, detail.html)
# index.html에서 타이틀을 클릭하면 해당 페이지로 이동하여 코멘트들을 보여줍니다.
# index.html 파일에서 title 부분에 해당하는 코드를 보면 <a href="/{{result.objectID}} 를 사용하여 링크가 걸려있는 것을 확인할 수 있습니다.
# 저 링크를 클릭하면 주소가 nomadNews/123456 와 같은 페이지로 이동하게됩니다.
# Line 31 : 위의 페이지에 코멘트를 뿌려주기 위해 make_detail_url(id) 함수를 호출하여 해당하는 api 주소를 얻고 그 주소를 requests 라이브러리를 사용하여 HTTP요청을 합니다.
# Line 32 : 그리고나서 .json() 을 사용하여 api를 읽어옵니다.
# Line 33 : detail.html 로 result 값을 보내줍니다.
# detail.html : 조건문과 반복문을 이용하여 result에 저장된 정보를 필요한 것만 꺼내어 뿌려줍니다.
# 결론
# 이번 챌린지는 웹 스크래핑이 아닌 api를 호출하여 데이터를 가져와 flask를 이용하여 간단한 웹사이트를 만들 수 있는 연습 할 수 있었습니다.