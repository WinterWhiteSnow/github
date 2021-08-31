import requests
sort_sites=[]
temp = []
x = 'y'
while(x == 'y'):
  print("Welcome to economy scrapper.py!")
  urls = input("Please write a URL or URLS you want to check.(separated by comma)\n")
  test = "    www.youtubue.co.kr, www.google.com"
  test = test.split(',')
  for i in test:
    i.lower()
    sort_sites.append("https://www."+ i.strip('w.htp:/ '))
  for i in sort_sites:
    res = requests.get(i)
    if res.status_code == 200:
      print(i+ "is up!\n")
    else:
      print(i + " is down!\n")
  while(1):
    x=input("Do you want restart?(y/n)")
    if (x != 'y' and x != 'n'):
      print("invalid answer")
    elif x == 'y':
      break;
    elif x =='n':
      print("okay bye bye~")
      break;

# 예외처리만하면됨

# results = URL.split(',')
#     for result in results:  
#         try:
#           r = requests.get(result)
#           if r.status_code == requests.codes.ok:
#             print(f"{result} is up!")
#           else:
#             print(f"{result} is down!")
#           break
#         except ConnectionError:
#             print("That is not a valid URL")
#             break

# import requests
# sort_sites=[]
# temp = []
# x = 'y'
# while(x == 'y'):
#   print("Welcome to economy scrapper.py!")
#   urls = input("Please write a URL or URLS you want to check.(separated by comma)\n")
#   test = "    www.youtubue.co.kr, www.google.com"
#   test = test.split(',')
#   for i in test:
#     i.lower()
#     sort_sites.append("https://www."+ i.strip('w.htp:/ '))
#   for i in sort_sites:
#     res = requests.get(i)
#     if res.status_code == 200:
#       print(i+ "is up!\n")
#     else:
#       print(i + " is down!\n")
#   while(1):
#     x=input("Do you want restart?(y/n)")
#     if (x != 'y' and x != 'n'):
#       print("invalid answer")
#     elif x == 'y':
#       break;
#     elif x =='n':
#       print("okay bye bye~")
#       break;          