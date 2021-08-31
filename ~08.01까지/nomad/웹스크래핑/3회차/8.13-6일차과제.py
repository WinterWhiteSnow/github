import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("cls")
url = "https://www.iban.com/currency-codes"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
parent_tag = soup.find("table",{"class":"table"}).find("tbody").find_all("tr")
list_dict = []
for i in parent_tag:
	list_list = i.find_all("td")
	country = list_list[0].string.replace("   ","").capitalize()
	code = list_list[2].string	
	if country and code:
		dict_list = {
			"country":country,
			"code":code
		}
		list_dict.append(dict_list)
print("Welcome to CurrencyConvert PRO 2000")		
for i,a in enumerate(list_dict):
	print("#",i,a["country"])		
print("Q1. where are you from? choose a country number.")

def first():
	try:
		answer = int(input("#1 : "))
		if 0 <= answer <= 264:
			country = list_dict[answer]["country"]
			code = list_dict[answer]["code"]
			print(f"A1. You choose {country} \n\nQ2.now choose another country.\n" )
			second(code)
		else:
			print("choose a number from the list")
			first()
	except:
		print("That wasn't a number.")	
		first()

def second(code):
	first_code = code
	try:
		answer = int(input("#2 : "))
		if 0 <= answer <= 264:
			second_country = list_dict[answer]["country"]
			second_code = list_dict[answer]["code"]
			print(f"A2. You choose {second_country}\n\nQ3. How many {first_code} do you want to convert to {second_code}?")
			convert(first_code,second_code)
		else:
			print("choose a number from the list")
			second(first_code)
	except:
		print("That wasn't a number.")	
		second(first_code)			

def convert(first_code,second_code):
	first_code = first_code
	second_code = second_code
	try:
		amount = int(input("#3 : "))
		if amount >=0:
			url = f"https://wise.com/gb/currency-converter/{first_code}-to-{second_code}-rate"
			r = requests.get(url)
			soup = BeautifulSoup(r.text,"html.parser")
			parent_tag = soup.find("span",{"class":"text-success"}).string
			parent_tag = float(parent_tag)
			total = amount * parent_tag
			result = format_currency(total, second_code, locale="ko_KR")
			print(f"{first_code}{amount:,} is {result}")
		else:
			print("Please enter a positive number.")
			convert(first_code,second_code)
	except:
		print("That wasn't a number.")
		convert(first_code,second_code)		

first()		


