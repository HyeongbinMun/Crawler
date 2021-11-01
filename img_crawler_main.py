from google_crawler import Google_crawler
from instagram_crawler import Instagram_Crawler
from option import file_read

if __name__=="__main__":

    print('Crawler Start\n')
    print('Select Option(1. Google, 2. instagram) : ')
    select_num = input()
    kewords = file_read('kewords.txt')

    if select_num == "1":
        Face_net = Google_crawler()
    elif select_num == "2":
        Face_net = Instagram_Crawler()
    else:
        print("Error Select option")
        exit()

    for keword in kewords:
            Face_net.options(keword)
            Face_net.get_img(keword)

    print('Crawler End')