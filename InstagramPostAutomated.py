from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config
from pynput.keyboard import Key, Controller


user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"


class InstagramPostAutomated:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.bot = webdriver.Firefox(profile)
    #
    def login(self):
        keyboard = Controller()
        bot = self.bot
        bot.get('http://www.instagram.com/')
        time.sleep(2)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        loginButton = bot.find_element_by_xpath('//button[text()="Log In"]')
        loginButton.click()
        time.sleep(2)
        emailInput = bot.find_elements_by_css_selector('form input')[0]
        passwordInput = bot.find_elements_by_css_selector('form input')[1]
        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        notNowBtn = bot.find_element_by_xpath('//button[text()="Not Now"]')
        notNowBtn.click()
        time.sleep(3)


    def postImage(self):
        keyboard = Controller()
        bot = self.bot
        postBtn = bot.find_element_by_xpath('//div[@data-testid="new-post-button"]')
        postBtn.click()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(4)
        nextBtn = bot.find_element_by_xpath('//button[text()="Next"]')
        nextBtn.click()
        time.sleep(5)
        captionBox = bot.find_element_by_xpath('//textarea[@aria-label="Write a caption…"]')
        captionBox.send_keys("Step away from the fridge - testing greed cam #RaspberryPI ")
        shareBtn = bot.find_element_by_xpath('//button[text()="Share"]')
        shareBtn.click()