from urllib import request as req
import requests

url = 'https://finance.naver.com/marketindex/'

res = req.urlopen(url)
print(res)
res = requests.get(url)
print(res)





url='https://wikidocs.net/'
html = request.urlopen(url)

soup = BeautifulSoup(html,'html.parser')
titles = soup.select('#books .book-subject')
author = soup.select('#books .book-detail .menu_link')
imgs = soup.select('#books .book-image')

for i in imgs:
    print(i.attrs['src'])

for t, a in zip(titles, author):
    print("책제목 : ",t.text, " - 책 저자 : ",a.text)

for i, t in zip(imgs, titles):
    try:
        request.urlretrieve(parse.urljoin(url,i.attrs['src']),'./wikiImage/{}.png'.format(t.text))
    except UnicodeEncodeError:
        i = quote_plus(parse.urljoin(url,i.attrs['src']),safe="://")
        request.urlretrieve(i,'./wikiImage/{}.png'.format(t.text))
print(len(titles))


from bs4 import BeautifulSoup
from urllib import request as req
from urllib.parse import quote_plus



html3 = req.urlopen("https://wikidocs.net/")
soup3 = BeautifulSoup(html3,'html.parser')

item3 = soup3.select("#books .media")
print(item3)

for it3 in item3:
    bt = it3.select('.book-subject')[0].text    # 제목
    # print(bt)
    bn = it3.select('.menu_link')[0].text   # 저자
    # print(bn)
    print(bt, ': ',bn)
    bl = it3.select('.book-image')[0].attrs['src']  # 책 링크
    parse = "https://wikidocs.net"
    i = quote_plus(parse+bl, safe="://")

    req.urlretrieve(i,'imgs4/'+bt+'.jpg')
