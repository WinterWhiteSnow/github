import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

url = "https://wikidocs.net/42526"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
parent_tag = soup.find("div",{"class":"page-content"})

def q1_answer():
	q1 = parent_tag.find("tbody").find_all("tr")
	q1_list = []
	q1_score= []	
	for i in q1:
		q1_tag = i.find_all("td")
		subject = q1_tag[0].string
		score = int(q1_tag[1].string)
		wow = {
			"subject":subject,
			"score":score
		}
		q1_list.append(wow)

	for i in range(0,len(q1_list)):
		a = q1_list[i]["score"]
		q1_score.append(a)

	result = int(sum(q1_score)/len(q1_score))
	return f"홍길동 씨의 평균점수는 {result}점 입니다."

def q2_answer():
	answer = int(input("plase enter a number "))
	division = answer % 2
	if division == 0:
		return f"{answer}(은)는 짝수입니다."
	else:
		return(f"{answer}(은)는 홀수입니다.")

def q3q4_answer():
	q3 = parent_tag.find_all("p")
	q3 = q3[3].text
	q3_question = q3
	resident_registration_number = q3[q3.find("8"):q3.find("4")+1]
	number = resident_registration_number.split("-")
	q3 = number[0]
	q4 = number[1]
	year = q3[:2]
	month = q3[2:4]
	days = q3[4:6]
	if int(q4[:1]) == 1 :
		sex = "남성"
	else :
		sex = "여성"
	return f"홍길동씨의 생년월일은 {year}년 {month}월 {days}일이며 성별은 {sex}입니다."

def q5_answer():
	q5_question = parent_tag.find_all("code", {"class":"python"})
	q5_question = q5_question[1].string
	return q5_question.replace(":","#")

def q6_answer():
	q6 = parent_tag.find_all("p")
	q6 = q6[8].string
	q6_list = q6[1:q6.find("]")].split(",")
	q6_num_list = []
	for i in q6_list:
		q6_num_list.append(int(i.strip()))

	q6_num_list = sorted(q6_num_list, reverse=True)
	return q6_num_list

def q7_answer():
	q7 = parent_tag.find_all("p")
	q7 = q7[10].string
	q7 = q7[1:q7.find("]")]
	q7 = q7.replace("'","").split(",")
	result1 = "".join(q7)
	result2 = "".join(result1)
	return result2

def q8_answer():
	q8 = parent_tag.find_all("p")
	q8 = q8[12].string
	q8 = q8[1:q8.find(")")]
	q8 = q8.split(",")
	q8_list = []
	for i in q8:
		wow = int(i)
		q8_list.append(wow)
	q8_tuple = tuple(q8_list)

	route1 = list(q8_tuple)
	route1.append(4)
	route1 = tuple(route1)

	q8_tuple +=(4,)
	print(q8_tuple)

	return route1,q8_tuple

def q9_answer():
	return "2번(리스트, 변경가능)만 불가능하고 나머지는 다가능함, immutable하면 뭐든 가능하다"

def q10_answer():
	q10 = parent_tag.find_all("code",{"class":"python"})
	q10 = q10[3].string
	q10 = q10[q10.find("{")+1:q10.find("}")].replace("'","").split(",")
	q10_dict = {}
	for i in q10:
		result = i.strip().split(":")
		key = result[0]
		value = int(result[1])
		q10_dict[f"{key}"]=value

	return q10_dict.pop("B")

def q11_answer():
	q11 = parent_tag.find_all("code",{"class":"python"})
	q11 = q11[4].string
	a = q11[q11.find("[")+1:q11.find("]")].split(",")
	a_list = []
	for i in a:
		a_list.append(int(i.strip()))

	new_list = []
	for i in a_list:
		if i not in new_list:
			new_list.append(i)
		else:
			pass

	a_set = set(a_list)
	a_list = list(a_set)

	return new_list, a_list
	
# q12 = parent_tag.find_all("code",{"class":"python"})
# q12 = q12[5].string
# q12_list = q12.split(">>>")[1:]
# list_list = []
# for i in q12_list:
# 	list_list.append(i.strip())
# print(list_list)
a = b = [1, 2, 3]
a[1] = 4
print(b)