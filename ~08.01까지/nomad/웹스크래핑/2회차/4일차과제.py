import requests
import os


# google.co.kr,     a,   naver.com, gg. gg, https://redddit.com 

def start():
    os.system("cls")
    print("""Welcome to IsItDown.py! Please write a URL or URLs you want to check. (separated by comma)""")
    URL = input("").lower().split(",")
    for i in URL:
        URLs = []
        strip = i.strip()
        if "." in strip:
            if "https://" not in strip:
                URLs.append("https://"+strip)
            else:
                URLs.append(strip)       
        else:
            print(strip+" is not vaild url")
        for i in URLs:
            try:  
                r = requests.get(i)
                if r.status_code == 200:
                    print(f"{i} is up!")
                else:
                    print(f"{i} is down!")
            except:        
                print(f"{i} is down!")
    overstart()        

def overstart():
    while True:
        answer = input("do you want to start over? ").lower()
        if answer == "y" or answer == "yes":
            start()
        elif answer == "n" or answer == "no":
            print("ok, bye!")
            break    
        else:
            print("please enter y or n")
            overstart()    
        break
start()

