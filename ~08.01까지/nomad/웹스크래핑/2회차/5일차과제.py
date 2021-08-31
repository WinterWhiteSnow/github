import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

url = "https://www.iban.com/currency-codes"

print(" Hello! please choose select a country by number :")
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
parent_tag = soup.find("table",{"class":"tablesorter"}).find("tbody").find_all("tr")

list = []

for i in parent_tag:
    wow = i.find_all("td")
    country = wow[0].text
    code = wow[2].text
    if country and code:
        object = {
            "country":country,
            "code":code
        }
        list.append(object)

for number in range(0,len(list)):
    countries = list[number]["country"].strip()
    print(f" # {number} {countries}")

def question():
    while True:
        try:
            answer = int(input(" #: "))
            if answer < 265:
                country = list[answer]["country"]
                code = list[answer]["code"]
                print(f" you choose {country} \n The currency code is {code}")
                return        
            else:
                print(" Please enter a number from the list")
                question()
        except:
            print(" That wasn't a number")
            question()        
        return

question()