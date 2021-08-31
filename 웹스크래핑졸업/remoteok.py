import requests
from bs4 import BeautifulSoup

def remoteok_scrap(word):
	url =f"https://remoteok.io/remote-{word}-jobs"
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
	r = requests.get(url,headers=headers)
	soup = BeautifulSoup(r.text,"html.parser")
	parent_tag = soup.find("table",{"id":"jobsboard"})
	list_list = []
	for i in parent_tag:
		try:
			title = i.find("h2",{"itemprop":"title"})
			company = i.find("h3",{"itemprop":"name"})
			link = i["data-id"]
			if title and company and link:
				title = title.string
				company = company.string
				link = "https://remoteok.io/l/"+link
				dict_list = {
					"title":title,
					"company":company,
					"link":link
				}
				list_list.append(dict_list)
		except:
			pass
	return list_list
	
if __name__ == "__main__":
	print(len(remoteok_scrap("python")))