import  requests
from  bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import datetime
import random
import string
import json

requests.packages.urllib3.disable_warnings()

#地点集合，需要手动生成
name_list = {
    '北京': 'beijing1',
}

htl_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }


def get_max_page(url):
    '''
    #请求当前地点的酒店页面个数
    :param url: 地点url
    :return:  最大页面数
    '''
    try:
        response = requests.get(url, headers=htl_headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            max_page = soup.select('div[class="c_page_list layoutfix"]')[0].find_all('a')[-1].string
            return int(max_page)
    except Exception as e:
        raise e
# def get_th(url):
#     '''
#     获取请求酒店房间需要的th参数
#     :param url:  酒店url
#     :return:  th 参数
#     '''
#     driver  = webdriver.PhantomJS()
#     driver.get(url)
#     th = re.search('id="th" value="(\d+)"',driver.page_source).group(1)
#     driver.close()
#     if th:
#         return int(th)

def get_hotel(name, cookie):
    '''
    获取点的所有 酒店房间信息
    :param name:  地点名
    :param cookie: 需要手动输入cookie至
    :return:
    '''
    htl_host = f'https://hotels.ctrip.com/hotel/{name}'
    max_page = 2
    for i  in range(1, max_page+1):
        url = htl_host + f'/p{i}'
        response = requests.get(url, headers =htl_headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.select('#hotel_list [class="hotel_new_list J_HotelListBaseCell"]')
            host = 'https://hotels.ctrip.com'
            for item  in  items:
                hotle_name = item.h2.a['title']
                socre = item.select('.hotel_value')[0].string
                hotel_site = (re.search('</a>】(.*?)<a',str(item.select('.hotel_item_htladdress')[0]),re.S).group(1).strip())
                url = host + item.select('h2.hotel_name')[0].a.get('href')
                hotel_id = int(re.search('hotel/(.*)\.html',url).group(1))
                # th = get_th(url)
                print('酒店名称:',hotle_name,'评分:',socre,'酒店位置:', hotel_site)
                get_htl_room(hotel_id, url,cookie)

        time.sleep(2)

def get_eleven_th(b,d, url):
    '''
    获取eleven至
    :param b: js提取到的参数b
    :param d: js提取到的参数d
    :param url: hotel_url
    :return:  eleven值
    '''
    driver = webdriver.PhantomJS()
    try:
        # url = 'http://www.baidu.com'
        driver.get(url)
        th = re.search('id="th" value="(\d+)"', driver.page_source).group(1)
        with open('evlen.js', encoding='utf-8') as f:
            js = f"{f.read()}"
        driver.execute_script(js)
        eleven = driver.execute_script(f'return target("{b}",{d})')
        if len(eleven) == 64  and th:
            return  eleven, th
    except Exception as e:
        print(e)
        print('发生错误，请检查eleven参数...')
    finally:
        driver.close()

def get_d_b(hotel_id,callback, cookie):
    '''
    获取b,d 参数值
    :param hotel_id: 酒店id
    :param callback: callback
    :param cookie:  cookie
    :return:  b, d 参数
    '''
    s_time = round(datetime.datetime.now().timestamp() * 1e3)
    url = f'https://hotels.ctrip.com/domestic/cas/oceanball?callback={callback}&_={s_time}'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'cookie': f'{cookie}',
        'referer': f"https://hotels.ctrip.com/hotel/{hotel_id}.html?isFull=F",
               }
    response = requests.get(url, headers=headers, verify=False)
    try:
        b = re.search('"b":"(.*?)","d"', response.text).group(1)
        d = json.loads(re.search('"d":(\[.*?\])', response.text).group(1))
        return b, d
    except Exception as e:
        print('出现神秘错误，_eleven.js文件请求失败，请稍后再试...')
        raise e


def get_htl_room(hotel_id, base_url,cookie):
    '''
    获取酒店房间信息
    :param hotel_id:  酒店id
    :param th:  th值
    :param cookie:  cookie
    :return:
    '''
    url = 'https://hotels.ctrip.com/Domestic/tool/AjaxHote1RoomListForDetai1.aspx?'

    headers = {
        'content-type': "application/x-www-form-urlencoded; charset=utf-8",
        'Cookie': f'{cookie}',
        'Referer': f"https://hotels.ctrip.com/hotel/{hotel_id}.html",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    }
    callback = 'CAS' + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=15))
    b, d = get_d_b(hotel_id, callback, cookie)
    eleven,th = get_eleven_th(b,d, base_url)

    params = {
        "hotel": f"{hotel_id}",
        "RoomGuestCount": "1,1,0",
        'th':f'{th}',
        "eleven": f"{eleven}",
        "callback": f"{callback}"
    }
    try:
        response= requests.get(url, params=params, headers=headers, verify=False)
        if response.status_code == 200:
            html = response.json().get('html')
            soup = BeautifulSoup(html, 'lxml')
            items = soup.find_all(class_="base_txtdiv")
            prices = []
            ## 这里因为提取的时候会提取到重复的优惠信息，所以直接去掉
            for i, item in enumerate(items):
                if i < 2:
                    continue
                prices.append(item.get_text())
            print(len(items) - 2)
            print(prices)
    except Exception as e:
        raise e



if __name__ == '__main__':
    cookie = 'magicid=mDQ61jeCnU2lcZPvFoBh9Aa9jqoXqpkenozF/26ugITBaLSQv4yIN4/TI76Mhhde; clientid=51482107310538457157; hoteluuid=mcqFuNgoU9Q1CAT0; _HGUID=%05PT%04%04%01%01UMW%05Y%01MT%05%01%04M%02SWUMY%05VTWPV%01%03VPQ; HotelDomesticVisitedHotels1=608516=0,0,4.6,353,/200t160000010oeje3CF7.jpg,&425222=0,0,4.8,14014,/2009050000000s26546BC.jpg,; cticket=F5DA837CCCE8A6A90B11ACB93C8A6508E882325F26705D29DC1CAF6DFF3ADAE4; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojEopJGkSi016ceujUXpY19EasqrgM0dDxqGYJ70r2R6AZFX9XeBmPzd7Q25WdlFkY7e25rd4y92VIYkL8J4bF4oGI5vfY02KR8a8gAzZ6DqmnJUCBFFmQ/+kKxvCTu3tnmmPz4ZJHZAnNb9uv5Bya7tr1Q+hqSPQQfapAnHpMDBNYlS11N56lAXj3YEpeZbCp4hFmo/fY4O1JNCXKRcjieKpYZZjKkq8xDuB1k40MOTymSrA64ypuJeIXhvWhDbRyOWqeUU5gNRA=; _abtest_userid=92524e7b-2d94-4762-8611-26b18619cd1e; AHeadUserInfo=VipGrade=10&VipGradeName=%bb%c6%bd%f0%b9%f3%b1%f6&UserName=%d1%d5%c7%ef&NoReadMessageCount=1&U=400810DBAEE3C19890C2A9B1D8CD3F2A; _ga=GA1.2.815634878.1568942600; _gid=GA1.2.715637298.1568942600; Union=SID=155952&AllianceID=4897&OUID=index; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; MKT_Pagesource=PC; _RF1=183.17.236.96; _RSG=jwac.LgsD1E1OiQmHcdrDB; _RDG=288f0d6f708a5f248823097ed3698d0826; _RGUID=e04ddaa5-7e9a-4ead-b375-9e64706ac601; HotelCityID=1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2019-9-20split2019-09-21split0; ASP.NET_SessionId=hbbkzxntgridij45zutuguxl; OID_ForOnlineHotel=15689425996072j7c91568942614076102002; fcerror=1767659013; _zQdjfing=1336fa3165bb275ad03165bb275ad0d5c08665b02e4ea0841336fa5fa4cc; _jzqco=%7C%7C%7C%7C1568942616389%7C1.1830231036.1568942600130.1568942622741.1568942636244.1568942622741.1568942636244.undefined.0.0.4.4; __zpspc=9.1.1568942600.1568942636.4%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfi=p1%3D102003%26p2%3D102003%26v1%3D4%26v2%3D3; hoteluuidkeys=QctJSQY1beplEfMW3Y5YNOY6qENYqY8UeUnEZHj4HWZYhY5pIQBe8QvSOj4Y1YHpinkwN4KUMjlY5YcBjg0wUfIG4j6YBY90yn7YL0y3Mv61wPbeb5Y0ljLgysYSY7sI84K1lxgowApI0DiHGi3diZYHYFYXYhqv4he5sYOoisdYlYDYcYoYdLEaUKkNwPci4QRP0jmrhzYdNJ57y6rGOYgOW6OvN7xoFeBUYmOxDPxU7YfXiqQw4zj5SES8JgFWNSjArdcJsdiFLwbmv38RU0jgfYd6jbrQOytFiUswaHRf9Enbjpdx3UxUME03EXDEAaWN8eh4wbcEdZjOteDniSaYcgrF4eZ7efdx14iz3iOmxH4WzQj46ezXw0XKsqwpziSXRDLjP3emfEcky61vUci35EHkynpva8K01Em0KHUwq7i3sRONjQraFYoFJb0yNrX7jaNePBjdMKMGj4QwZpx9bxdmxogxabEOlEcoEGoWPoe4GwGTETojZ3e0biU7YGprT1E1MyfNvbsiB5EZ9yFavFmK87WkpE3AjSGe0cx9MjorUoE7UWtpeP1j75Y1oj9sx09xzhxS3xt5E0PEPoEQ3WPHe5nwMTEaSj0Se3tiGsYUkrPle6Be9FYhlEcawNzW1GillKUmEcqE1GEqUW1Be7swFpENkjc6eATiqnYLArGBesDel7EUtY3SEhkwUtWdmiZY1YXnYs6i8XitLiT5jkYSYzsYB8wmbEhLjL8ydZjkPYkFELYDYMkR4BJ69whqjN8vpLEz4i3qyMhy0OJNSEb7vZQjkY8YGNRF3w4QJzky8dv7OWOTxsZisby1bv7aiknRTXElbYqMw6TWQYGYhdRmaJDkwdmj0Uv6qEGpY9MJd7vAfvaXwUmWcb; _bfa=1.1568942599607.2j7c9.1.1568942599607.1568942599607.1.5; _bfs=1.5; hotelhst=50349362'
    name = input('请输入地点：').strip()
    if name_list.get(name) is not None:
        get_hotel(name_list.get(name),cookie)

