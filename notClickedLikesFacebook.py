#! python3
# notClickedLikesFacebook.py - logges under Chrome to the facebook account and hit button 'Like'
# on account's feed page scrolling down the feed page to search for posts w/o account's likes.
# It is needed to download Chrome driver before for you version and put it to PATH folder, link = http://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open the facebook page on browser.
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://facebook.com')
time.sleep(2.5)

# Log to the facebook and simulate human actions with delay.
emailElem = browser.find_element_by_id('email')
emailElem.send_keys('enter_email') # Enter your email instead of 'enter_email'
time.sleep(1.5)
passElem = browser.find_element_by_id('pass')
passElem.send_keys('enter_password') # Enter your password instead of 'enter_password'
time.sleep(1.5)
browser.find_element_by_id('loginbutton').click()

# Wait for annoying notification option to escape it.
htmlElem = browser.find_element_by_tag_name('html')
time.sleep(5)
htmlElem.send_keys(Keys.ESCAPE)

# Get elements of "Like" button and loop the process.
while True:
    likes = browser.find_elements_by_xpath("//a[@class=' _6a-y _3l2t  _18vj']")   
    if len(likes) == 0:
        htmlElem.send_keys(Keys.END)
        time.sleep(2)
        continue
    if len(likes) != 0:
        while True:
            for like in likes:
                time.sleep(2)
                like.click()
                time.sleep(2)
            likes = browser.find_elements_by_xpath("//a[@class=' _6a-y _3l2t  _18vj']")
            if len(likes) == 0:
                htmlElem.send_keys(Keys.END)
                time.sleep(2)
                break

        
