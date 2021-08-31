import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")


def get_csv(company):
    file = open(f"{company['name']}.csv", 'w', encoding='utf-8', newline='')
    csvfile = csv.writer(file)
    csvfile.writerow(["place", "title", "time", "pay", "date"])
    for job in company["jobs"]:
        csvfile.writerow(list(job.values()))


albamon_url = "http://www.alba.co.kr"


albamon_request = requests.get(albamon_url)
albamon_soup = BeautifulSoup(albamon_request.text, "html.parser")
brands = albamon_soup.find("div", {"id": "MainSuperBrand"})
super_brands = brands.find_all("li", {"class": "impact"})

for brand in super_brands:
    link = brand.find("a", {"class": "goodsBox-info"})
    name = brand.find("span", {"class": "company"})
    if link and name:
        link = link["href"]
        name = name.text
        if "/" in name:
            name = name.replace("/", " ")
        company = {'name': name, 'jobs': []}

        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")
        inner_data = jobs_soup.find("div", {"id": "NormalInfo"}).find("tbody")
        tbody_data = inner_data.find_all("tr", {"class": ""})

        for data in tbody_data:
            location = data.find("td", {"class": "local first"}).text

            title = data.find("td", {"class": "title"})
            if title:
                title = title.find("a").find("span", {"class": "company"}).text.strip()

            time = data.find("td", {"class": "data"}).text

            pay = data.find("td", {"class": "pay"}).text

            date = data.find("td", {"class": "regDate last"}).text

            job = {
                "place": location,
                "title": title,
                "time": time,
                "pay": pay,
                "date": date
            }
            company["jobs"].append(job)
        # get_csv(company)