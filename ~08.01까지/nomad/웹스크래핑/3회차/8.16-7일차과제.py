import os
import requests
from bs4 import BeautifulSoup
import csv

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
for i in parent_tag:
	main_link = i.find("a")["href"]
	main_company_name=i.find("span",{"class":"company"}).string
	if main_link and main_company_name:
		if "/" in main_company_name:
			main_company_name = main_company_name.replace("/"," ")
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





