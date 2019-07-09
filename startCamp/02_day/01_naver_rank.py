import requests
import bs4

url = 'https://www.naver.com'

response = requests.get(url)
html = response.text
selector = '.ah_l .ah_item .ah_a .ah_k'

soup = bs4.BeautifulSoup(html, 'html.parser')
silgum = soup.select(selector)

for rank in silgum:
    print(rank.text)

#ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)
#.ah_l .ah_item .ah_a .ah_k