import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

def q1_answer():
	a = "Life is too short, you need python"

	if "wife" in a: 
		print("wife")
	elif "python" in a and "you" not in a: 
		print("python")
	elif "shirt" not in a: 
		print("shirt")
	elif "need" in a: 
		print("need")
	else: 
		print("none")

def q2_answer():
	standard_number={
		"plus" : 0,
		"count" : 0
	}
	while standard_number["count"] <= 1000:
		plus_num = standard_number["plus"]
		count_num = standard_number["count"]
		for number in range(1,1001):
			if number%3 == 0:
				count_num += 1
				print(f"{plus_num}에 {number}를 더했습니다. {count_num}회")
				plus_num += number
			elif number == 1000:
				return f"3의 배수의 총합은 {plus_num}입니다."



def d3_answer(n):
	count = 0					
	while count <n:
		if count <n:
			for i in range(0,n+1):
				print("*"*i)
				count +=1
			if i == n:
				return "end!"
# number = int(input("enter a counting number : "))
# wow = d3_answer(number)
# print(wow)

def d4_answer():
	for i in range(0,101):
		print(i)

def d5_answer():
	url = "https://wikidocs.net/42527"
	r= requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	parent_tag = soup.find("div",{"page-content tex2jax_process"})
	tag = parent_tag.find_all("p")
	list_str = tag[6].string.replace("[","").replace("]","").split(",")
	list_int = []
	for i in list_str:
		list_int.append(int(i))
	num = 0
	for i in list_int:
		num += i
	total = num/len(list_int)
	return int(total)

# url = "https://wikidocs.net/42527"
# r= requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# parent_tag = soup.find("div",{"page-content tex2jax_process"})
# tag = parent_tag.find_all("code",{"class":"python"})
# print(tag[-1].string.strip())
numbers = [1, 2, 3, 4, 5]
result = [i*2 for i in numbers if i%2 ==1]
print(result)		

