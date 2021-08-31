import os
import requests

os.system("cls")
         
def commnet():
	list_list = []
	url = "https://hn.algolia.com/api/v1/items/16582136"
	r = requests.get(url).json()
	title = r["title"]
	points = r["points"]
	first_author = r["author"]
	url_url =r["url"]
	for i in r["children"]:
		second_author =i["author"]
		commnet = i["text"]
		dict_list = {
			"title":title,
			"points":points,
			"first_author":first_author,
			"url_url":url_url,
			"second_author":second_author,
			"commnet":commnet      
		}
		list_list.append(dict_list)
	return list_list

for i in commnet():
	print(i)
   