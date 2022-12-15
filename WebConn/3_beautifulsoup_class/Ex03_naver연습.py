"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req
import requests


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'

# res = req.urlopen(url)
res = requests.get(url)
# print(res)

# 파싱하기
soup = BeautifulSoup(res.text, 'html.parser')

# 추출하기
# usd = soup.select('#exchangeList span.value')
usd = soup.select_one('#exchangeList span.value')
print('달러 :', usd.text)

yen = soup.select_one('#exchangeList > li:nth-child(2) span.value')
print('옌 :', yen.text)

exchange = soup.select('#exchangeList span.value')
# print(exchange)
print('옌 :', exchange[1].text)

print()

exchangeLi = soup.select('#exchangeList li')
for i in exchangeLi:
    country = i.select_one('.blind').text
    money = i.select_one('span.value').text
    print(country, ":", money)
