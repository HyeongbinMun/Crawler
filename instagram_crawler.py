from option import instagram_option
from bs4 import BeautifulSoup
import os
import time
import requests
import shutil

class Instagram_Crawler:
    def __init__(self):
        self.limit_img = 100


    def options(self, search):
        self.driver = instagram_option(search)
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html)

    def get_img(self, keword):
        imglist = []
        for i in range(0, 5):
            insta = self.soup.select('.v1Nh3.kIKUG._bz0w')
            for i in insta:
                imgUrl = i.select_one('.KL4Bh').img['src']
                imglist.append(imgUrl)
                imglist = list(set(imglist))
                html = self.driver.page_source
                soup = BeautifulSoup(html)
                insta = self.soup.select('.v1Nh3.kIKUG._bz0w')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        n = 0
        for i in range(0, self.limit_img):
            image_url = imglist[n]
            resp = requests.get(image_url, stream=True)
            img_folder = './img/' + str(keword)
            if not os.path.isdir(img_folder):
                os.mkdir(img_folder)
            local_file = open(img_folder + '/' + str(n) + '.jpg', 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            n += 1
            del resp

        self.driver.close()





