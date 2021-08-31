import requests
from bs4 import BeautifulSoup
from buying_list import title_list


def checking_buy(before_list):
    result_result_list=[]
    buying_title = title_list()
    for i in before_list:
        if i["title"] in buying_title:
            pass
        else:
            print(i["title"]+"는 구매목록")
            result_result_list.append(i)
    return  result_result_list       



def extract_last_page():
    url = "https://www.aladin.co.kr/shop/wbrowse.aspx?ItemType=100&ViewRowsCount=24&ViewType=Simple&PublishMonth=0&SortOrder=6&page=2&UsedShop=0&PublishDay=84&CID=50932&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=5000&SearchOption=&IsDirectDelivery=&QualityType=0&OrgStockStatus=&ShopNoCols=&IsUsedStore=0"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"}
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,"html.parser")
    parent_tag=soup.find("form",{"id":"Myform"})
    pagenation = soup.find_all("table",{"align":"center"})
    last_page = []
    for i in pagenation:
        extract_page=i.find("div",{"class":"numbox_last"})
        if extract_page:
            extract_page = extract_page.find("a")["href"]
            extract_page=extract_page[extract_page.find("'")+1:].replace("')","")
            extract_page = int(extract_page)
            last_page.append(extract_page)
    last_page = last_page[0]
    return last_page

def scraping():
    last_page=extract_last_page()
    dict_result = []
    for i in range(1,last_page+1):
        print(f"알라딘 무협소설 scraping....{i}page")
        new_url = f"https://www.aladin.co.kr/shop/wbrowse.aspx?ItemType=100&ViewRowsCount=24&ViewType=Simple&PublishMonth=0&SortOrder=6&page={i}&UsedShop=0&PublishDay=84&CID=50932&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=5000&SearchOption=&IsDirectDelivery=&QualityType=0&OrgStockStatus=&ShopNoCols=&IsUsedStore=0"
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"}
        r = requests.get(new_url,headers=headers)
        soup = BeautifulSoup(r.text,"html.parser")
        parent_tag=soup.find("form",{"id":"Myform"})
        a = parent_tag.find_all("table",{"cellspacing":"5"})
        for i in a:
            title = i.find_all("a",{"class":"bo"})
            price = i.find_all("span",{"class":"p1_bold"})
            for a,b in zip(title,price):
                link = a["href"]
                title_string = a.string
                price_string = b.string
                if "완결" in title_string:
                    title_string = title_string
                    price_string = price_string
                    link = link
                    if "신무협" in title_string: #1."신무협"인경우, 2.신무협판타지일경우
                        if "판타지" in title_string or "환타지" in title_string:
                            pass
                        else:
                            dict_list = {
                                    "title":title_string[:title_string.find("1")],
                                    "price":price_string,
                                    "link":link
                                }
                            dict_result.append(dict_list)
                    else:#제목에 신무협이 없는 경우    
                        input_title = title_string[:title_string.find("1")]
                        filter_url = f"https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query={input_title}"
                        r = requests.get(filter_url,headers=headers)
                        soup = BeautifulSoup(r.text,"html.parser")
                        try:
                            ul = soup.find("ul",{"class":"basic"}).find("li").find("dl").find("span").string
                            if "신무협" in ul: #괄호에 신무협이 있는경우
                                if "판타지" in ul and "환타지" in ul:
                                    pass
                                else:
                                    title_string = title_string
                                    price_string = price_string
                                    dict_list = {
                                        "title":title_string[:title_string.find("1")],
                                        "price":price_string,
                                        "link":link
                                    }
                                    dict_result.append(dict_list)
                            else:# 없는 경우 1. 정말로 신무협이 아닐경우, 2. 신무협은 맞는데 소개글에 적힌경우
                                introduce_text = soup.find("ul",{"class":"basic"}).find("li").find("dl").find("dd",{"type":"책소개"}).text
                                if "신무협" in introduce_text:
                                    if "판타지" in introduce_text or "환타지" in introduce_text:
                                        pass
                                    else:
                                        title_string = title_string
                                        price_string = price_string
                                        dict_list = {
                                        "title":title_string[:title_string.find("1")],
                                        "price":price_string,
                                        "link":link
                                        }
                                        dict_result.append(dict_list)
                                else:   
                                    pass
                        except:
                            pass    

    wow = checking_buy(dict_result)
    return wow
                       