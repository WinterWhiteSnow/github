import requests
from bs4 import BeautifulSoup
def stackoverflow_scrap(word):
	url = f"https://stackoverflow.com/jobs?q={word}"
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
	r = requests.get(url,headers=headers)
	# r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	list_list = []
	pagination = soup.find("div",{"class":"py32 px16"}).find("div",{"class":"flex--item"}).find_all("span")[:-1]
	last_page = int(pagination[-1].string)
	for i in range(1,2+1):
		new_url = f"https://stackoverflow.com/jobs?q={word}&pg={i}"
		print(f"stackoverflow scraping...{i} page")
		r = requests.get(new_url)
		soup = BeautifulSoup(r.text,"html.parser")
		parent_tag = soup.find("div",{"class":"listResults"}).find_all("div")
		for i in parent_tag:
			try:
				link = "https://stackoverflow.com/jobs/"+i["data-result-id"]
				title =i.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).find("a").string
				company = i.find("h3",{"class":"fc-black-700 fs-body1 mb4"}).find("span").string.strip()
				if link and title and company:
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
	print(len(stackoverflow_scrap("python")))





