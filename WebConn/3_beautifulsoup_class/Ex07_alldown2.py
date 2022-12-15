"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명 : download_file
    인자  : url ()
    리턴값 : savepath (저장 경로)
    역할  : 해당 페이지, index.html의 내용을 가져와서 저장
'''

def download_file(url):
    p = parse.urlparse(url)
    # print('1-', p)
    savepath = './' + p.netloc + p.path
    # print('2-', savepath)

    if re.search('/$', savepath):
        savepath += 'index.html'
        # print('3-', savepath)

    if os.path.exists((savepath)):
        return savepath

    savedir = os.path.dirname(savepath)
    if not os.path.exists((savedir)):
        os.makedirs(savedir)

    try:
        request.urlretrieve(url, savepath)
        time.sleep(2)
        print('download -', url)
        return savepath
    except:
        print('fail download :', url)
        return None


if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



