import os
import requests

os.system("cls")

popular ="https://hn.algolia.com/api/v1/search"
new = f"{popular}_by_date?tags=story"

db = {}
def rain(apple):
	list_list=[]
	r = requests.get(apple).json()
	for i in r["hits"]:
		if i["title"]:
			wow = {
				"title" : i["title"],
				"url" : i["url"],
				"points" : i["points"],
				"author" : i["author"],
				"num_comments" : i["num_comments"],
				"objectID" : i["objectID"]
			}
			list_list.append(wow)
			if apple == new:
				db["new"]=list_list
			else:
				db["popular"]=list_list		

rain(popular)
rain(new)
print(db)

				

		
	


