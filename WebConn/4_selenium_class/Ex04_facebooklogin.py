
from selenium import webdriver

# facebook, instagram
usr = 'yoobinbkk@naver.com'
pwd = 'youbkk34'

# [1] webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

#-------------------- facebook --------------------------
# driver.get('https://www.facebook.com')
#
# email = driver.find_element_by_id('email')
# passwd = driver.find_element_by_id('pass')
#
# email.send_keys(usr)
# passwd.send_keys(pwd)
#
# btn = driver.find_element_by_name('login')
# btn.click()
# driver.implicitly_wait(2)

#-------------------- instagram --------------------------
driver.get('https://www.instagram.com/')

username = driver.find_element_by_name('username')
passwd = driver.find_element_by_name('password')

username.send_keys(usr)
passwd.send_keys(pwd)

btn = driver.find_element_by_tag_name('form')
btn.submit()
driver.implicitly_wait(2)