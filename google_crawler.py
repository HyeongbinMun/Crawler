import time
import urllib.request
import os
from option import google_option


class Google_crawler:
    def __init__(self):
        self.limit_img = 100

    def options(self, search):
        self.driver = google_option(search)

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
        if self.limit_img > 50:
            self.scrollbar()
        count = 1
        images = self.driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        img_folder = './img/' + str(keword)
        for image in images:
            try:
                if not os.path.isdir(img_folder):
                    os.mkdir(img_folder)

                image.click()
                time.sleep(1)
                imgUrl = self.driver.find_element_by_xpath(
                    '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute(
                    'src')
                urllib.request.urlretrieve(imgUrl, "./Img/" + str(keword) + "/" + str(count) + ".jpg")
                count = count + 1
            except:
                pass

            if count == self.limit_img + 1:
                break

        self.driver.close()




