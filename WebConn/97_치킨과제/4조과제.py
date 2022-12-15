from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, quote

import time, csv, json, folium
import cx_Oracle as oci



# DB 접속
conn = oci.connect('scott/tiger@192.168.0.57:1521/xe')

# 크롬 드라이버 구동 (selenium용)
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(1)

# folium 세팅 (지도 파일용)
map_osm = folium.Map(location=[37.572807, 126.975918])

# csv에 입력하기 위해 파일을 열기
with open('./data/치정.csv', 'a', encoding='utf-8-sig') as f:

    # 페이지마다 크롤링하기 위해 for문 돌렸다
    for page_num in range(1, 8):
        # 드라이버로 페이지의 정로를 가져오기
        driver.get('http://xn--9n3b23etshra259e96ao8h.kr/?c=Cat06&p=%d' % page_num)
        html = driver.page_source
        time.sleep(1)

        # 그 페이지를 BeautifulSoup로 스캔하기
        soup = BeautifulSoup(html, 'html.parser')

        name = soup.select('.sbj')
        addr = soup.select('#bbslist tr>td:nth-child(3)')
        tel = soup.select('#bbslist tr>td:nth-child(4)')

        for addr, tel, name, in zip(addr, tel, name):
            print(addr.text.strip(), tel.text.strip(), name.text.strip())

            vworld_apikey = 'BB68F9B0-D068-3F5A-956A-52342E38F074'
            url = "http://api.vworld.kr/req/address?service=address&request=getCoord&type=ROAD&refine=false&key=%s&" % (
                vworld_apikey) + urlencode({quote_plus('address'): addr.text.strip()}, encoding='UTF-8')
            print(url)

            request = Request(url)
            response = urlopen(request)
            rescode = response.getcode()
            print(response)
            if rescode == 200:
                response_body = response.read().decode('utf-8')
            else:
                print('error code:', rescode)

            try:
                jsonData = json.loads(response_body)
                lat = float(jsonData['response']['result']['point']['y'])
                lng = float(jsonData['response']['result']['point']['x'])
                # print('lat:{}, lng:{}'.format(lat, lng))
            except:
                print('error :', Exception)
                lat = ""
                lng = ""

            sql = f"insert into store_info values('{name.text}','{addr.text}','{tel.text}','{lat}','{lng}')"

            cursor = conn.cursor()

            cursor.execute(sql)

            cursor.close()

            data =[name.text.strip(),addr.text.strip(),tel.text.strip(),lat,lng]

            cout = csv.writer(f)  # csv.writer 를 f 랑 연결한다 / 이거하나를 꼭 가지고있어주장
            cout.writerow(data)  # 하나씩 읽어준다

            if lat != "":

                folium.Marker(location=[lat, lng],
                              popup=f"'{name.text}'",
                              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)


map_osm.save('./map/1.html')


conn.commit()
conn.close()

driver.close()





