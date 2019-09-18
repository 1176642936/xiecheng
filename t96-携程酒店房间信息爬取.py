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
def get_th(url):
    '''
    获取请求酒店房间需要的th参数
    :param url:  酒店url
    :return:  th 参数
    '''
    driver  = webdriver.PhantomJS()
    driver.get(url)
    th = re.search('id="th" value="(\d+)"',driver.page_source).group(1)
    driver.close()
    if th:
        return int(th)

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
                th = get_th(url)
                print('酒店名称:',hotle_name,'评分:',socre,'酒店位置:', hotel_site)
                get_htl_room(hotel_id, th,cookie)

        time.sleep(2)

def get_eleven(b,d):
    '''
    获取eleven至
    :param b: js提取到的参数b
    :param d: js提取到的参数d
    :return:  eleven值
    '''
    driver = webdriver.PhantomJS()
    try:
        url = 'http://www.baidu.com'
        driver.get(url)
        with open('evlen.js', encoding='utf-8') as f:
            js = f"{f.read()}"
        driver.execute_script(js)
        eleven = driver.execute_script(f'return target("{b}",{d})')
        if len(eleven) == 64:
            return  eleven
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


def get_htl_room(hotel_id, th,cookie):
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
    eleven = get_eleven(b,d)

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
    cookie = 'magicid=mDQ61jeCnU2lcZPvFoBh9Aa9jqoXqpkenozF/26ugITBaLSQv4yIN4/TI76Mhhde; clientid=51482107310538457157; hoteluuid=mcqFuNgoU9Q1CAT0; _HGUID=%05PT%04%04%01%01UMW%05Y%01MT%05%01%04M%02SWUMY%05VTWPV%01%03VPQ; HotelDomesticVisitedHotels1=608516=0,0,4.6,353,/200t160000010oeje3CF7.jpg,&425222=0,0,4.8,14014,/2009050000000s26546BC.jpg,; cticket=F5DA837CCCE8A6A90B11ACB93C8A6508E882325F26705D29DC1CAF6DFF3ADAE4; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojEopJGkSi016ceujUXpY19EasqrgM0dDxqGYJ70r2R6AZFX9XeBmPzd7Q25WdlFkY7e25rd4y92VIYkL8J4bF4oGI5vfY02KR8a8gAzZ6DqmnJUCBFFmQ/+kKxvCTu3tnmmPz4ZJHZAnNb9uv5Bya7tr1Q+hqSPQQfapAnHpMDBNYlS11N56lAXj3YEpeZbCp4hFmo/fY4O1JNCXKRcjieKpYZZjKkq8xDuB1k40MOTymSrA64ypuJeIXhvWhDbRyOWqeUU5gNRA=; _abtest_userid=8ac600a7-fe21-48b3-a2e5-043d0bbdaf3a; AHeadUserInfo=VipGrade=10&VipGradeName=%bb%c6%bd%f0%b9%f3%b1%f6&UserName=%d1%d5%c7%ef&NoReadMessageCount=1&U=400810DBAEE3C1987AF727C4C0B7BAF7; _ga=GA1.2.1619054620.1568767127; _gid=GA1.2.316888540.1568767127; Union=OUID=&AllianceID=1026871&SID=1636637&SourceID=&Expires=1569371927166; _RF1=113.110.221.136; _RSG=jwac.LgsD1E1OiQmHcdrDB; _RDG=288f0d6f708a5f248823097ed3698d0826; _RGUID=e04ddaa5-7e9a-4ead-b375-9e64706ac601; HotelCityID=1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2019-9-18split2019-09-19split0; ASP.NET_SessionId=urhjwtqg2anm20dln4tu0p12; OID_ForOnlineHotel=15687671221142ak1br1568767134528102002; MKT_Pagesource=PC; MjAxNS8wNi8yOSAgSE9URUwgIERFQlVH=OceanBall; fcerror=2062417365; _zQdjfing=3365ac4ea084275ad03365ac186ad91336fa3165bb5fa4cc275ad0d5c086; _jzqco=%7C%7C%7C%7C1568767127603%7C1.1844025595.1568767127385.1568788394522.1568788871404.1568788394522.1568788871404.undefined.0.0.52.52; __zpspc=9.5.1568786244.1568788871.16%234%7C%7C%7C%7C%7C%23; _bfi=p1%3D102003%26p2%3D102003%26v1%3D56%26v2%3D55; hoteluuidkeys=6c4JL6vAZeaTE0mj5YfYHqYZ0E5YUYA5e01EBsjo0WaYUYboI5AxoLvcPjqYkYlojNbvScwOmjGYfYUcrOHYfGvbZj8YLYcqvldY05e1PKdDv75yMbYZtjk7y6YXY5zWSMvpnYgmwXljfled3iH8YfY6YgYLYlnvFaeAdY3fimqYFYsY8YDY4zEs3K1SwsXim3RTDjdrPMYsnJGhyMrdlYUDW4zv5NxQNeXZYDAxnfx0UY9AikbwaXjhHELXJ7UWnPj7rzXJ48ihOwaSvN3RBqjQqYhXjOrLqyoOicQwXhROtETzj0Nx9QxmZEFbEqdEs9Wlze7FwXtEapj0ceToiP7YPTrUOe8ce0HxoHiZ0iLfxmnWSdjbdegDwS9K90wp7iO9RMkj3neP3E7aym9vPgiopE7hyzLvl9KzHEqaKS6w4Dik7RtQj8rTDYZ5JQ4yprnljFcegmj18Kkfj3NwXLxg8xSoxApxp7EhpESQEBQW6ke70woTE4ajogeXAiHbY6ZrfoE6ByhQvnmiB0EdPy0Lvb3KOsWQaEZ1jnHeThx1sjmrtXEQ8W46eSgj4kYgqjbtxoMxTAx5Txq9EbfEPhEp6WZHehmwtZEShj5gebgi7ZYQ1rqdeb3el5YfqEzGwoTWtGinnKO1ElXE1lEt9Wclez6wZNEOUjfbe6diapYLQrb4efpe5AEZ3YdaE6UwQLWoUi7YbYGBY3Mit3iFHi5UjaYLYXMY6swGNEFkjkQynbjs3YkOEOYTY9URZDJ8twM7jk4ymgjSgvQ4jkAj0LJbQyhoi5kWzYqYc0RZLwfzJk8yQMvZLW0OxMQi4gyXNvk1i5bRa7EsDYPmwd9WtY5YO5RZdJcdw0MjbmyUnwM5yn1RM8YG6YNgRL7R9z; _bfa=1.1568767122114.2ak1br.1.1568784063533.1568786240839.4.57; _bfs=1.17; hotelhst=50349362'
    name = input('请输入地点：').strip()
    if name_list.get(name) is not None:
        get_hotel(name_list.get(name),cookie)

