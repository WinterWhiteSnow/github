import requests
import os

# naver.com,   http://google.com,   daum.net,  yahoooooo.com, dfefdsf
print("""
Welcome to IsItDown.py!
Please write a URL or URLs you want to check. (separated by comma)
""")

URL = input("").split(",")
URLs = [i.strip() for i in URL]

while[1]:      
  result = []
  for i in URLs:
    result.append(i.lower())

  wow = []
  for a in result:        
    if "http" in a and "." in a:
      wow.append(a) 
    elif "http" not in a and "." in a:
      wow.append("http://"+a)
    else:
      wow.append(a)   
          
  for check in wow:
    try:
      updown = requests.get(check)
      if updown.status_code == requests.codes.ok:
        print(f"{check} is up!")                
      else:
        print(f"{check} is down!")        
    except:
      print(f"{check} is not URL!")
       
  while[1]:
    answer = input("Do you want to start over? y/n ")
    try:
      if answer == "y":
        os.system('cls')
        break
      elif answer == "n":
        print("ok, everything is stopped")
        break
      else:
        print("please, write y or n") 
    except:
      print("please, write y or n")
  break    