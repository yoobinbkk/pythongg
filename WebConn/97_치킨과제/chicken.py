from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
import time
import cx_Oracle as oci
import csv

conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
print(conn.version)

driver = webdriver.Chrome('../webdrive/chromedriver.exe')
driver.implicitly_wait(1)

with open('./data/치정.csv','a',encoding='utf-8-sig') as f:

    for page_num in range(1,8):
        driver.get('http://xn--9n3b23etshra259e96ao8h.kr/?c=Cat06&p=%d' % page_num)

        html = driver.page_source
        time.sleep(1)

        soup = BeautifulSoup(html,'html.parser')

        name = soup.select('.sbj')
        addr = soup.select('#bbslist tr>td:nth-child(3)')
        tel = soup.select('#bbslist tr>td:nth-child(4)')

        for addr, tel, name in zip(addr,tel,name) :
            print(addr.text.strip(),tel.text.strip(),name.text.strip())

            sql = f"insert into store_info values('{name.text}','{addr.text}','{tel.text}','','')"
            cursor = conn.cursor()
            cursor.execute(sql)
            cursor.close()

            data =[addr.text.strip(),tel.text.strip(),name.text.strip()]

            cout = csv.writer(f)  # csv.writer 를 f 랑 연결한다 / 이거하나를 꼭 가지고있어주장
            cout.writerow(data)  # 하나씩 읽어준다

conn.commit()
conn.close()



