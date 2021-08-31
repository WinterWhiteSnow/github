import requests
from bs4 import BeautifulSoup



def scraping(wow):
	list_list=[]
	for i in wow:
		try:
			tag= i.find_all("a")[1]
			link = "https://weworkremotely.com"+tag["href"]
			title = tag.find("span",{"class":"title"}).string
			company = tag.find("span",{"class":"company"}).string
			dict_list = {
				"title":title,
				"company":company,
				"link":link
			}
			list_list.append(dict_list)		
		except:
			pass
	return list_list

def weworkremotely_scrap(word):
	url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	full_stack_tag = soup.find("section",{"id":"category-2"}).find_all("li")
	back_end_tag = soup.find("section",{"id":"category-18"}).find_all("li")
	all_tag = soup.find("section",{"id":"category-4"}).find_all("li")
	a = scraping(full_stack_tag)
	b = scraping(back_end_tag)
	c = scraping(all_tag)
	result = a+b+c
	return result

if __name__ == "__main__":
	print(len(weworkremotely_scrap("python")))
