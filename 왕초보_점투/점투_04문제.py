import os
import requests
from bs4 import BeautifulSoup

os.system("cls")

def q1_answer():
	num = int(input("enter a number : "))
	if type(num) == int:
		if num%2 == 0:
			print(f"{num}는 짝수입니다.")
		else:
			print(f"{num}는 홀수입니다.")

def q2_answer():
	# 1, 22 , 1      1,4
	num = input("Enter as many numbers as you want, use the comma: ")
	num = num.split(",")
	score = 0
	for i in num:
		num_list = i.strip().replace(" ", "")
		num_lists = int(num_list)
		if type(num_lists) == int:
			score += num_lists
	total = score / int(len(num))
	return total

def q3_answer():
	input1 = input("첫번째 숫자를 입력하세요:")
	input2 = input("두번째 숫자를 입력하세요:")
	total = int(input1) + int(input2)
	print("두 수의 합은 %s 입니다" % total)
def q5_answer():
	f1 = open("test.txt", 'w')
	f1.write("Life is too short")
	f1.close()

	f2 = open("test.txt", 'r', encoding="utf8")
	print(f2.readline())
	f2.close()

def q6_answer():
	f = open("wow.txt", 'a', encoding="utf8")
	answer = input("write that you want anything! :")
	f.write(answer +"\n")
	f.close()

def q7_answer():
	f = open("text.txt","r",encoding="utf8")
	original = f.readlines()
	originals = [i.replace("java", "python").strip() for i in original]
	f.close()
	f1 = open("test.txt","w",encoding="utf8")
	for i in originals:
		f1.write(i+"\n")
	f1.close()

