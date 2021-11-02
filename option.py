import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

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
    baseUrl = 'http://www.instagram.com/explore/tags/'
    plusUrl = search
    url = baseUrl + quote_plus(plusUrl)

    options = Options()
    options.add_argument('--kiosk')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)

    return driver

def file_read(file):
    re_kewords = []
    with open(file, 'r', encoding='utf-8') as f:
        kewords = f.readlines()

    for keword in kewords:
        re_kewords.append(keword.replace('\n', ''))

    return re_kewords
