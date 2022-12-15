"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse, request
# from urllib import request

'''
    함수명 :   enum_links()
    인자  :   html(a 링크의 href (경로)), base(사이트 주소)
    리턴값 :   result (링크 주소의 리스트)
    역할  :   해당 페이지의 모든 링크 주소를 스크래핑해서 result 리스트에 넣는다
'''

def enum_links(html,base):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')

    result = []
    for a in links:
        href = a.attrs["href"]
        url = parse.urljoin(base, href)
        result.append(url)

    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)