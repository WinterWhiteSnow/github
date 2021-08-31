import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("cls")

def save_to_file(dict_list):
	name = dict_list["company_name"]
	file = open(f"{name}.csv",mode ="w",encoding="utf8")
	writer = csv.writer(file)
	info = dict_list["company_info"]
	writer.writerow(["local | title | time | pay | reg date"])
	for i in info:
		writer.writerow(list(i.values()))
	return

url = "http://www.alba.co.kr/"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
parent_tag = soup.find("div",{"id":"MainSuperBrand"}).find("ul",{"class":"goodsBox"}).find_all("li",{"class":"impact"})

url_name ="https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC_%EC%9D%B4%EB%A6%84#%EC%82%AC%EC%9A%A9%ED%95%A0_%EC%88%98_%EC%97%86%EB%8A%94_%EA%B8%B0%ED%98%B8%EC%99%80_%EB%AC%B8%EC%9E%90"
r_name = requests.get(url_name)
soup_name = BeautifulSoup(r_name.text,"html.parser")
not_name_list_tag = soup_name.find("table",{"class":"wikitable"}).find_all("tr")[1:]
not_name = []
for i in not_name_list_tag:
   wow = i.find("td",{"align":"center"}).text.strip()
   not_name.append(wow)

for i in parent_tag:
	main_link = i.find("a")["href"]
	main_company_name=i.find("span",{"class":"company"}).string
	if main_link and main_company_name:
		for i in not_name:
			if i in main_company_name:
				main_company_name = main_company_name.replace(i," ")
		dict_list = {
			"company_name":main_company_name,
			"company_info":[]
		}
		r = requests.get(main_link)
		soup = BeautifulSoup(r.text, "html.parser")
		brand_tag = soup.find_all("tr",{"class":""})
		for i in brand_tag:
			local_tag = i.find("td",{"class":"local"})
			title_tag = i.find("span",{"class":"company"})
			time_tag = i.find("td",{"class":"data"})
			pay_tag = i.find("td",{"class":"pay"})
			regDate_tag = i.find("td",{"class":"regDate last"})
			if local_tag and title_tag and time_tag and pay_tag and regDate_tag:
				local = local_tag.text.replace("\xa0"," ")
				title = title_tag.string
				time = time_tag.text
				pay = pay_tag.text
				reg_date = regDate_tag.text
				dict_list_list = {
					"local":local,
					"title":title,
					"time":time,
					"pay":pay,
					"reg_date":reg_date
				}
				dict_list["company_info"].append(dict_list_list)
		save_to_file(dict_list)

