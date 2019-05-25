from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

UN = str(input("Type Username: "))
PW = str(input("Type Password: "))

class InstagramBot:
    def  __init__(self, username, password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox()


    def closeBrowser(self):
        self.driver.close()


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def like_photos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(3)
        for i in range(1, 10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print("Working on " + hashtag + ". Number of photos: " + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("dCJp8").click()
                time.sleep(20)
            except Exception as e:
                time.sleep(2)


targetIG = InstagramBot(UN, PW)
targetIG.login()
targetIG.like_photos("puppylovers")
targetIG.like_photos("puppyoftheday")
targetIG.like_photos("puppystagram")
targetIG.like_photos("puppy")
targetIG.like_photos("puppygram")