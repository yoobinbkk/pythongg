'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

from selenium import webdriver

# [1] webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://google.com')
# driver.get('https://daum.net')
# driver.get('https://naver.com')

#----------------------------------------------
# [2]

search_bt = driver.find_element_by_name('q')        # google -> q, naver -> query, daum -> q
search_bt.send_keys('코로나극복')
search_bt.submit()