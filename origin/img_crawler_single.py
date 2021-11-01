from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import option

search = input ('검색어를 입력하세요: ')
num = int(input ('다운로드 받고 싶은 이미지의 갯수를 입력하세요: '))

options = Options()
options.add_argument('--kiosk')

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

elem = driver.find_element_by_name("q") 
elem.send_keys(str(search))
elem.send_keys(Keys.RETURN) 

if num>=50:

    SCROLL_PAUSE_TIME = 1.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height


count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
links = []
img_folder = './Img/' + str(search)
for image in images:
    try:
        if not os.path.isdir(img_folder):
            os.mkdir(img_folder)

        image.click()
        time.sleep(1)
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
        urllib.request.urlretrieve(imgUrl, "./Img/" + str(search) + "/" + str(count) + ".jpg")
        count = count + 1
    except:
        pass

    if count == int(num)+1:
        break

driver.close()