from selenium import webdriver
from time import sleep
import os
from bs4 import BeautifulSoup
import lxml
import shutil
import requests

class App:
    def __init__(self, username='Kazitipu007',password='tipu016411', driver=webdriver.Chrome(),main_url='https://www.instagram.com'):
        self.username= username
        self.password= password
        self.driver=driver
        self.main_url= main_url
        self.driver.get(self.main_url,)
        sleep(7)
        self.log_in()
        self.clicking_dl_box()
        self.getting_target_profile()
        self.no_of_posts_scrolls()
        self.downloading_images()


    def log_in(self):
        log_in_button= self.driver.find_element_by_xpath('//article[@class="_4_yKc"]//p[@class="izU2O"]/a')
        log_in_button.click()
        sleep(3)
        email_field= self.driver.find_element_by_xpath('//input[@name="username"]')
        email_field.send_keys('Kazitipu007')
        pass_field= self.driver.find_element_by_xpath('//input[@name="password"]')
        pass_field.send_keys('tipu016411')
        pass_field.submit()
        sleep(5)

    def clicking_dl_box(self):
        dl_box=self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
        dl_box.click()
        sleep(2)

    def getting_target_profile(self):
        search_bar=self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_bar.send_keys('masum')
        sleep(2)       
        target_profile='https://www.instagram.com/masum2329/'
        self.driver.get(target_profile)
        sleep(2)

    def no_of_posts_scrolls(self):        
        no_of_posts=self.driver.find_element_by_xpath('//span[@class="g47SY "]')
        no_of_posts=str(no_of_posts.text).replace(',', '')
        no_of_posts=int(no_of_posts)
        print(no_of_posts)

        if no_of_posts > 12:
            no_of_scrolls= int(no_of_posts / 12) + 3
            for value in range(no_of_scrolls):
                print(value)
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(8)

    def downloading_images(self):
        path=('C:\\Users\\Tipu\\Desktop\\instaphotos')
        if not os.path.exists(path):
            os.mkdir(path)

        soup=BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        print('length of images', len(all_images))

        for index, image in enumerate(all_images):
            filename='image_'+str(index)+'.jpg'
            image_path=os.path.join(path, filename)
            link=image['src']
            response=requests.get(link, stream=True)
            print('downloading image', index)

            if not os.path.exists(image_path):
                try:
                    with open(image_path, "wb") as file:
                        shutil.copyfileobj(response.raw, file)
                except Exception as e:
                    print(e)
                    print('could not download image no',index)
            else:
                pass




        
if __name__ == "__main__":
    app=App()

