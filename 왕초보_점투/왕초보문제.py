# height = 100
# while height > 1:
# 	ball_position = height*3/5
# 	height = ball_position
# 	print(round(height,4))

# number = 358

# rem = rev = 0
# while number >= 1:
# 	print("first rem",rem, rev)
# 	if number >= 1:
# 		rem = number % 10 
# 		print("rem", rem)
# 		rev = rev * 10 + rem 
# 		print("rev", rev)
# 		number = number // 10 #
# 		print("number", number) 

# print(rev)

# num_num = 0
# while True:
# 	num = int(input("enter a number : "))
# 	if num > 0:
# 		print(f"{num_num}에 {num}을 더했습니다")
# 		num_num = num_num+ num
# 		print(f"현재 값:{num_num}")
# 	if num < 0 :
# 		print("it's over",num)
# 		break

# year = int(input("년도를 입력하세요 : "))
# if year%4 == 0 and year%100 == 0 and year%400 == 0:
# 	print(f"{year}년은 윤년입니다.")
# elif year%4 == 0 and year%100 == 0:
# 	print(f"{year}년은 평년입니다.")
# else:
# 	print(f"{year}년도 윤년이긴합니다.")

# num = int(input())
# i = 1
# while i <= num:
# 	print(num)
# 	i +=1

# num = int(input())
# for i in range(num):
# 	print(num)

# num = int(input())
# for i in range(1,num+1):
# 	print(i, i*i)
  
# number = input("enter two numbers with space to split\n").split()
# num1 = int(number[0])
# num2 = int(number[1])
# if num1 > num2:
# 	max = num1
# 	min = num2
# else:
# 	max = num2
# 	min = num1	
# temp = int(input())
# while temp != -999:
# 	if min <= temp <= max:
# 		print('Nothing to report')
# 		temp = int(input())
# 	else:
# 		print('Alert!')
# 		break

wow = [i for i in range(2,9+1)]
for a in wow:
	for i in range(1,9+1):

		result = f"0{a*i:2d}" if result < 10 else a*i
		print(f"{a} * {i} = {result}")		
		
# def multi(m):
#     for n in range(1, 10):
#         print(f'{m} * {n} = {m*n:2d}')

# if __name__ == '__main__':
#     for i in range(2, 10):
#         multi(i)
#         print()