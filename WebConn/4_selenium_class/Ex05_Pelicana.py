
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# [1] webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

for page_no in range(1, 11):

    # [연습]
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' % (page_no))
    html = driver.page_source
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select(".table > tbody > tr > td:nth-child(1)")
    tel = soup.select(".table > tbody > tr > td:nth-child(3)")

    for name, tel in zip(name, tel):
        print(name.text.strip(), tel.text.strip())

driver.close()
