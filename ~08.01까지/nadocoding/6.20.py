import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

url = "https://www.iban.com/currency-codes"


countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask():
  try:
    choice = int(input("#: "))
    if choice >= len(countries) or choice <0:
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"{country['name']} \nnow choose another country. \n")
      currency_exchange(choice)
  except ValueError:
    print("That wasn't a number.")
    ask()

def currency_exchange(choice):
    try:
        choice2 = int(input("#: "))
        if choice2 >= len(countries) or choice2 <0:
            print("Choose a number from the list.")
            currency_exchange(choice)
        else:
            country1 = countries[choice]
            country2 = countries[choice2]
            print(f"{country2['name']} \nhow many {country1['code']} do you want to convert to {country2['code']}?")
            try:
                amount = int(input(""))
                if amount == str:
                    print("please enter a integer")
                else:
                    URL = f"https://wise.com/gb/currency-converter/{country1['code']}-to-{country2['code']}-rate?amount={amount}"
                    request = requests.get(URL)
                    soup = BeautifulSoup(request.text, "html.parser")
                    rate = soup.find("h3", {"class":"cc__source-to-target"})
                    rate1 = rate.find_all("span")
                    result_rate = float(rate1[2].text)
                    print(type(result_rate))
                    result = amount*int(result_rate)
                    print(result)
                    print(f"{country1['code']} {amount} is", end=" ")
                    print(format_currency(result, country2['name'], locale="ko_KR"))                   
            except:
               print("please enter a integer")         

    except ValueError:
        print("That wasn't a number.")
        currency_exchange() 


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")
print("\nwhere are you from? choose a country by number.\n")

ask()