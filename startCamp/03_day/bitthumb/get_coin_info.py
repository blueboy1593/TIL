import requests
import bs4
import csv

# 1.Bithumb 페이지를 가지고 온다.
response = requests.get('https://www.bithumb.com/') # 요청을 보내 응답을 받는다.
html = response.text    # 응답받은 객체에서 html 문서를 string으로 가지고 옴

# 2. Beautiful Soup 모듈을 이용하여 string type 의 html 을 파싱한다!
# coin_list 안쪽에 있는 tablerow를 가지고 오세요.
#print(type(html)) # <= 타입은? 
soup = bs4.BeautifulSoup(html, 'html.parser')

# 3. 각 코인이 담겨있는 table row 데이터를 list의 형태로 가져온다.
# td p a strong' #tr은 태그니까 그냥 접근해도 됨.
coins = soup.select('.coin_list tr')

# 4. 각 코인을 순회하며 필요한 정보만 추출한다.
for coin in coins: # coin == tr
    coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '') # >나 띄어쓰기나 똑같다.
    #coin_name = coin_name.replace('NEW', '')
    coin_price = coin.select_one('td:nth-child(2) > strong').text
    #print(coin_name, coin_price)
    #tableAsset > tbody > tr:nth-child(1) > td:nth-child(1)
    #tableAsset > tbody > tr:nth-child(1) > td:nth-child(2) > .sort_real
    # id값 -----> 티바디 > 첫번째 자식으로 접근 -> 첫번쨰 자식 접근. 즉 첫번째의 첫번째 자식으로 접근한 것.
    # 각 코인의 이름과 시세 데이터를 추출

# 5. csv writer 를 이용해서 정보를 저장한다.
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f) 
    for coin in coins:
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)  #이거 굉장히 중요하다. list? Dictionary로 만드는 거네.
        print(data)
        csv_writer.writerow(data)
# ,가 있으면 구분을 해주기 위해서 ""를 붙여준다.