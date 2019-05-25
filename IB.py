from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

UN = str(input("Type Username: "))
PW = str(input("Type Password: "))
option = str.lower(str(input("Like or Add? ")))
print("Input 5 hashtags")
hashtags = [str(input("#")), str(input("#")), str(input("#")), str(input("#")), str(input("#"))]
print("Initiating...")


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
        #gather data
        driver = self.driver
        print("Gathering posts for #" + hashtag + ".")
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(3)
        for i in range(1, 9):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        #filter profiles
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print("Number of posts: " + str(len(pic_hrefs)) + ". Likes iniciated.")
        count = len(pic_hrefs)

        #like pictures
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("dCJp8").click()
                count = count - 1
                print(str(count) + "/" + str(len(pic_hrefs)) + " remaining.")
                time.sleep(20)
            except Exception as e:
                time.sleep(2)

    def add_users(self, hashtag):
        #gather data
        driver = self.driver
        print("Gathering posts for #" + hashtag + ".")
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(3)
        for i in range(1, 9):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        #filter profiles
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print("Number of posts: " + str(len(pic_hrefs)) + ". Adding iniciated.")
        count = len(pic_hrefs)

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("FPmhX").click()
                time.sleep(2)
                driver.find_element_by_class_name("vBF20").click()
                count = count - 1
                print(str(count) + "/" + str(len(pic_hrefs)) + " remaining.")
                time.sleep(20)
            except Exception as e:
                time.sleep(2)



targetIG = InstagramBot(UN, PW)
targetIG.login()
if option == "like":
    targetIG.like_photos(hashtags[0])
    targetIG.like_photos(hashtags[1])
    targetIG.like_photos(hashtags[2])
    targetIG.like_photos(hashtags[3])
    targetIG.like_photos(hashtags[4])
elif option == "add":
    targetIG.add_users(hashtags[0])
    targetIG.add_users(hashtags[1])
    targetIG.add_users(hashtags[2])
    targetIG.add_users(hashtags[3])
    targetIG.add_users(hashtags[4])
else: 
    print("Invalid input.")

targetIG.closeBrowser()