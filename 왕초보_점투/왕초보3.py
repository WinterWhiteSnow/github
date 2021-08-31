# def triple(x):
# 	print(x*3)
# triple(2)
# triple('x')

# from datetime import datetime as date
# today = date.today()
# year = today.year
# def korean_age(old,year):
# 	print(year - old)

# korean_age(1996,year)
# def simple_interest(원금, 시간, 이율):
# 	return 원금*시간*이율


# def simple_interest_amount(p, r, t):
#     return p * (1 + r * t)
# print(simple_interest_amount(1100000, 0.05, 5/12))	

# def compound_interest_amount(p,r,t,n):
# 	return p*(1+r/n)**(n*t)

# print(compound_interest_amount(1500000, 0.043, 6, 4))

#################################################
# for i in range(10):
# 	if i % 2: #True = 1, False = 0
# 		return i
#################################################
# def palindrome(wow):
# 	wow = wow.lower().strip()
# 	if wow == wow[::-1]:
# 		print("회문회문!")
# 	else:
# 		print("회문아님")

# num = input("")

# wow = 0
# for i in num:
# 	i = int(i)
# 	if i:
# 		wow +=i
# 		print(wow)
		
# stem_leaf = [[], [], []]
# wow =[[0, 0, 2, 4, 7, 7, 9], [1, 1, 3, 8], [0]]
# for i in range(len(stem_leaf)):
# 	stem_leaf[i]=wow[i]
# for ii in range(len(stem_leaf)):
# 	print(f"{ii} : {stem_leaf[ii]}")

# def sumOfDigits(wow):
# 	yes = list(map(lambda x:int(x),list(wow)))
# 	return sum(yes)
# num = input("")
# print(sumOfDigits(num))

# wow = int(input(""))
# list_list = [i for i in range(1,wow+1)]


# print(list_list,list(filter(lambda x: x / 2 ==False, list_list)))
# def prime(n):
#     L = L2 = list(range(2, n + 1))

#     for p in L:
#         if p in L2:
#             for q in L:
#                 if (q in L2) and (q!=p and q%p==0):
#                     L2.remove(q)

#     print(L2)

# if __name__ == '__main__':
#     prime(int(input()))
################################################################
# def prime(n):
#     L = L2 = list(range(2, n + 1))

#     for p in L:
#         if p in L2:
#             for q in L:
#                 if q in L2 and q!=p and q%p==0:
#                     L2.remove(q)

#     print(L2)

# if __name__ == '__main__':
#     prime(int(input()))
#################################################################

# wow = int(input(""))
# list_list = [i for i in bin(wow).replace("0b", "")]

# month = int(input("enter a month number : "))
# if month:
# 	days = int(input("enter a days number : "))
# 	if days:
# 		years = int(input("enter a years number : "))
# 		if (month <=12 and days <= 31) or (month == 2 and days <=28):
# 			print("오늘",month,days,years)
# 			days +=1
# 			if days >=32:
# 				days = 1
# 				month +=1
# 				if  month >=13:
# 					days = 1
# 					month = 1
# 					years += 1
# 					print("내일",month,days,years)
# 				else:
# 					print("내일",month,days,years)
# 			else:
# 				print("내일",month,days,years)				

# def korean_number(wow):
# 	dict_list = {
# 		1 : "일",
# 		2 : "이",
# 		3 : "삼",
# 		4 : "사",
# 		5 : "오",
# 		6 :	"육"
# 	}
# 	return dict_list[wow]

# print(korean_number(int(input(""))))

txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''
# txt = txt.split("\n")
# for i in txt:
# 	list_split = i.split(" ")
# 	for i in list_split:
# 		while i.encode().isalpha():
# 			a = i
# 			print(a)

# txt.split("\n")
# disorders = dict()

# is_eng = lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122

# for l in txt.split('\n'):
#     i = 0
#     while not is_eng(l[i]):
#         i += 1
#     else:
#         ko, en = l[:i - 1], l[i:]
#         disorders[ko] = en

# print(disorders)

# dice1 = (1, 2, 3, 4, 5, 6)
# dice2 = (2, 3, 5, 7, 11, 13)
# """
# dice1[0] + dice2[0].....dice2[5]
# dice2[1] + dice2[0].....dice2[5]
# .
# .
# .
# dice1[5] + dice2[0].....dice2[5]
# """
# list_list = []
# for i in dice1:
#     for a in dice2:
#         total = i + a
#         list_list.append(total)
# list_list = set(list_list)
# print(list_list, len(list_list))

# import calendar
# calendar.prmonth(2020,12)

from tkinter import *
yes = Tk()
 
lbl = Label(yes, text="왱알왱알")
lbl.grid(row=0, column=0)
txt = Entry(yes)
txt.grid(row=0, column=1)
btn = Button(yes, text="신기하다", width=15)
btn.grid(row=1, column=1)
 
yes.mainloop()