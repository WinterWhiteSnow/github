import requests
from bs4 import BeautifulSoup

URL = requests.get("https://www.iban.com/currency-codes")
soup = BeautifulSoup(URL.text, "html.parser")

pages = soup.find("table",{"class":"table"})
page = pages.find_all("tbody")

temporarily = {}
number_country = {}

countries_lists = []
for country in page:

    a = country.find_all("td")
    a = list(a)

    country_list = 0
    code_list = 2

    while code_list >= 0:
        b = a[country_list].text
        c = a[code_list].text        
        temporarily[f"{b}"] = f"{c}"
        country_list +=4
        code_list +=4
        if code_list >= len(a):
            break
    results = {key: value for key, value in temporarily.items() if len(value) != 0}

countries_lists.append(list(results))
countries_lists = countries_lists[0]
countries_list = [i.strip() for i in countries_lists]


def start():
    country = results.keys()  
    max_numb = len(results.keys())      
    number = 0
    print("hello, my friend! Please choose select a country by number:")
    for i in country:        
        print(f" # {number} {i}")
        number += 1
        if number >= max_numb:
            break
    while[1]:
        try:
            select = int(input(" # : "))            
            if countries_list[select] in countries_list:
                print(F" You choose {countries_list[select]} \n The currency code is {results[countries_list[select]]}")
                break
            elif type(select) == int:
                print(" please, enter a number from the list.")
            else:
                print(" That's wasn't a number.")                                
        except:            
            print(" That's wasn't a number.")

start()