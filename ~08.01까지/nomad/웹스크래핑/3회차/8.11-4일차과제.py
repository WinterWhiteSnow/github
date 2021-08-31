import os
import requests
from bs4 import BeautifulSoup

os.system("cls")
url = "https://www.iban.com/currency-codes"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
parent_tag = soup.find("table",{"class":"table"}).find("tbody").find_all("tr")
list_dict = []
for i in parent_tag:
	list_list = i.find_all("td")
	country = list_list[0].string.replace("   ","")
	code = list_list[2].string	
	if country and code:
		dict_list = {
			"country":country,
			"code":code
		}
		list_dict.append(dict_list)
print("Hello! Please choose select a country by number :")		
for i,a in enumerate(list_dict):
	print("#",i,a["country"])		

def start():
	try:
		answer = int(input("# : "))
		if 0 <= answer <= 264:
			country = list_dict[answer]["country"]
			code = list_dict[answer]["code"]
			print(f"You choose {country} \nThe currency code is {code}" )
		else:
			print("choose a number from the list")
			start()
	except:
		print("That wasn't a number.")	
		start()	
start()				  	
