# from ast import Index
# import os
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.dhlottery.co.kr/gameResult.do?method=statByNumber"


# request = requests.get(url)
# soup = BeautifulSoup(request.text, "html.parser")
# a = soup.find("table",{"id":"printTarget"}).find_all("tr")[1:]
# b = []
# for i in a:
#     item = i.find_all("td")
#     number = item[0].text
#     count = item[2].text
#     print(item)

# date = sorted(b, key=lambda potato:(potato["count"]), reverse=True)
# for i in date:
#     print(i)

a = {"a":[{"title":1}]}
b = {"b":[{"title":7}]}
print(a["a"][0])