from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def google_option(search):
    options = Options()
    options.add_argument('--kiosk')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

    elem = driver.find_element_by_name("q")
    elem.send_keys(str(search))
    elem.send_keys(Keys.RETURN)

    return driver

def instagram_option(search):
    user_id = "bin96525"
    user_passwd = "rydbrqud1!"
    instagram_id_name = "username"
    instagram_pw_name = "password"
    instagram_login_btn = ".sqdOP.L3NKy.y3zKF     "
    login_url = "https://www.instagram.com/accounts/login/"

    options = Options()
    options.add_argument('--kiosk')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(login_url)
    time.sleep(5)
    try:
        instagram_id_form = driver.find_element_by_name(instagram_id_name)
        instagram_id_form.send_keys(user_id)
        time.sleep(5)

        instagram_pw_form = driver.find_element_by_name(instagram_pw_name)
        instagram_pw_form.send_keys(user_passwd)
        time.sleep(7)

        login_ok_button = driver.find_element_by_css_selector(instagram_login_btn)
        login_ok_button.click()
    except:
        print("instagram login fail")


    time.sleep(10)
    baseUrl = 'http://www.instagram.com/explore/tags/'
    plusUrl = search
    url = baseUrl + quote_plus(plusUrl)

    driver.get(url)
    time.sleep(10)

    return driver

def file_read(file):
    re_kewords = []
    with open(file, 'r', encoding='utf-8') as f:
        kewords = f.readlines()

    for keword in kewords:
        re_kewords.append(keword.replace('\n', ''))

    return re_kewords
