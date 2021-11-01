from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import option

class Google_crawler:
    def __init__(self):
        self.limit_img = 1000


    def init_chrome(self, keword):
        options = Options()
        options.add_argument('--kiosk')

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

        elem = self.driver.find_element_by_name("q")
        elem.send_keys(str(keword))
        elem.send_keys(Keys.RETURN)

    def scrollbar(self):
        SCROLL_PAUSE_TIME = 1.5
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                try:
                    self.driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break
            last_height = new_height

    def get_img(self, keword):
        count = 1
        images = self.driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        img_folder = './Img/' + str(keword)
        for image in images:
            try:
                if not os.path.isdir(img_folder):
                    os.mkdir(img_folder)

                image.click()
                time.sleep(1)
                imgUrl = self.driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
                urllib.request.urlretrieve(imgUrl, "./Img/" + str(keword) + "/" + str(count) + ".jpg")
                count = count + 1
            except:
                pass

            if count == self.limit_img+1:
                break
        
        self.driver.close()

def file_read(file):
    re_kewords = []
    with open(file, 'r', encoding='utf-8') as f:
        kewords = f.readlines()
    
    for keword in kewords:
        re_kewords.append(keword.replace('\n', ''))

    return re_kewords

if __name__ == '__main__':
    kewords = file_read('kewords.txt')
    print(kewords)
    # kewords = list(map(str, input('키워드 입력 : ').split(',')))
    for keword in kewords:
        Face_net = Google_crawler()
        Face_net.init_chrome(keword)
        Face_net.scrollbar()
        Face_net.get_img(keword)
    
    