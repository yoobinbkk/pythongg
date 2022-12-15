"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

# import urllib
from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))         # http://www.example.com/html/b.html
print(parse.urljoin(baseUrl, 'sub/c.html'))     # http://www.example.com/html/sub/c.html
print(parse.urljoin(baseUrl, '/sub/d.html'))    # http://www.example.com/sub/d.html
print(parse.urljoin(baseUrl, '../temp/e.html')) # http://www.example.com/temp/e.html
print(parse.urljoin(baseUrl, 'http://www.daum.net')) # http://www.daum.net
