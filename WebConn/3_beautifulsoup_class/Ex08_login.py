"""
    일단 http://www.hanbit.co.kr 회원가입

    [예] 한빛출판네트워크 ( 단순 페이지 ) : 이 예문은 위키북스 출판사 교재 예문임
                                    <파이썬을 이용한 머신러닝, 딥러닝 실전개발 예문>
    로그인페이지 : http://www.hanbit.co.kr/member/login.html
    마이페이지 : http://www.hanbit.co.kr/myhanbit/myhanbit.html

    1. 로그인 페이지에서 개발자모드에서 로그인 form 태그를 분석
        입력태그의 name='m_id' / name='m_passwd' 확인

    2. 로그인 후에 마이페이지에서 마일리지와 한빛이코인 부분
        마일리지 (.mileage_section1 > dd > span ) / 한빛이코인 (.mileage_section2 > dd > span )

    3. 로그인과정에 어떤 통신이 오가는지 분석
        Network > Preserve log 체크 > Doc 탭을 선택하고 다시 처음부터 로그인을 하면 서버와 통신을 오고간다
        이 때 Name 중 login_proc.php를 선택하고 Headers 부분을 확인한다
        
        Gereral : Request Mathod : POST
        Form Data : m_id와 m_passwd 값 확인
"""

import requests
from bs4 import BeautifulSoup

req = requests.session()  # 서버의 세션과 다르다. 사용자의 접속을 의미한다. (접속할 때 세션을 주니까)

login_info = {
    "m_id" : "yoobinbkk",
    "m_passwd" : "ybbinbkk34"
}

url_login = "https://www.hanbit.co.kr/member/login_proc.php"
res = req.post(url_login, data=login_info)
print(res)

url_mypage = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = req.get(url_mypage)
print(res)

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one('.mileage_section1 span')
print('마일리지 :', mileage.get_text())