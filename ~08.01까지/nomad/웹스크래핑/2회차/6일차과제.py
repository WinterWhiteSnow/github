import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("cls")

url = "https://www.iban.com/currency-codes"

print(" Hello! please choose select a country by number :")
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
parent_tag = soup.find("table",{"class":"tablesorter"}).find("tbody").find_all("tr")

list = []
link_element = []

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
print("Q1. where are you from? choose a country by number from the country list")

def question():
    try:
        answer = int(input(" # first country : "))
        if 0 <= answer < len(list):
            country = list[answer]["country"]
            code = list[answer]["code"]
            print(f"\n you choose first country : {country}")
            print("\nQ2. now choose another country.")
            selet1 = {
                "country":country,
                "code":code
                }
            link_element.append(selet1) 
            selected()       
        else:
            print(" Please enter a number from the list")
            question()
    except:
        print(" That wasn't a number")
        question()          


def selected():
    try:
        answer= int(input(" # second country : "))
        if 0 <= answer < len(list):
            country = list[answer]["country"]
            code = list[answer]["code"]
            print(f" \nyou choose second country : {country}")
            selet2 = {
                "country":country,
                "code":code
                }
            link_element.append(selet2)
            code1 = link_element[0]["code"]
            print(f"Q3. how many {code1} do you want to convert to {code}?")
            currency()        
        else:
            print(" Please enter a number from the list")
            selected()
    except:
        print(" That wasn't a number")
        selected()        

def currency():
    select1 = link_element[0]
    select2 = link_element[1]
    code = "code"
    try:    
        answer = int(input(" # amount : "))
        url = f"https://wise.com/gb/currency-converter/{select1[code]}-to-{select2[code]}-rate?amount={answer}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        parent_tag = soup.find("h3", {"class":"cc__source-to-target"})
        child_tag = parent_tag.find("span", {"class":"text-success"}).text
        result = float(child_tag)*answer
        money = format_currency(result, select2[code], locale="ko_KR")
        print(f"{select1[code]}{answer:,} is {money}{select2[code]}")
    except:
        print("that isn't number, enter a amount")
        currency()        

question()