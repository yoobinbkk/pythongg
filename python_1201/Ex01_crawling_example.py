import urllib.request
from bs4 import BeautifulSoup

# daum 야구

url = "https://www.segye.com/newsView/20221208517840"
res = urllib.request.urlopen(url)

soup=BeautifulSoup(res,'html.parser')
title=soup.find('title').string
body=soup.find('body').string

print(title)
print('-'*50)
print(body)

