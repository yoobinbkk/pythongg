
from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html, 'html.parser')

# [1]
infos = soup.select('#yesSchList .info_name .gd_name')
for info in infos:
    print(info.text)

print()
print(len(infos), '권이 검색되었습니다')
print()

# [2]
imgUrls = soup.select('#yesSchList div.itemUnit img')
# print(imgUrls)
for imgUrls in imgUrls:
    # 이미지 링크를 출력 : src
    # 책제목을 출력 : alt
    imgPath = imgUrls.attrs['data-original']
    bookName = imgUrls.attrs['alt'].strip().replace('/', '_')
    print(bookName, imgPath)
    request.urlretrieve(imgPath, 'imgs/' + bookName + '.jpg')