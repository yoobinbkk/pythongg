

from bs4 import BeautifulSoup
import requests
from urllib import request

url = "http://www.pythonscraping.com/pages/warandpeace.html"

res = requests.get(url).text
# res = request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

g = soup.select('.green')

for i in g:
    print(i.text)

print("-"*50)
# =================================================================================

url2 = "http://www.pythonscraping.com/pages/page3.html"

res2 = request.urlopen(url2)
soup2 = BeautifulSoup(res2, "html.parser")

gifts = soup2.select(".gift")

for gift in gifts:
    name = gift.select_one("td:nth-child(1)").text.strip()
    price = gift.select_one("td:nth-child(3)").text.strip()
    print(name, ":", price)

print("-"*50)
# =================================================================================

from urllib import parse
from urllib.parse import quote_plus

url3 = "https://wikidocs.net"

res3 = requests.get(url3).text
soup3 = BeautifulSoup(res3, "html.parser")

media = soup3.select("#books .media")

for i in media:
    title = i.select_one('.book-subject').text
    author = i.select_one('.menu_link').text
    print(f"[제목 : {title}] [저자 : {author}]")

    img_url = i.select_one('img.book-image').attrs['src']
    uu = quote_plus(url3 + img_url, safe="://")
    request.urlretrieve(uu, f"img2/{title}.jpg")


