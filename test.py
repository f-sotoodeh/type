from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from functools import partial
from random import uniform
from time import sleep


browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
presence = partial(EC.presence_of_element_located, locator=By.XPATH)
wait = WebDriverWait(browser, 5)
click = lambda el: wait.until(EC.element_to_be_clickable((By.XPATH, el))).click()

def login():
    URL = 'https://typistapp.ca/#/home'
    USERNAME = 'mnaeimi2'
    PASSWORD = 'Kh213348'
    XP_USERNAME = '//input[@id="usernameInput"]'
    XP_PASSWORD = '//input[@id="passwordInput"]'
    XP_LOGIN = '//button[@class="submit"]'
    browser.get(URL)
    sleep(3)
    click(XP_USERNAME)
    browser.find_element(By.ID, 'usernameInput').send_keys(USERNAME)
    click(XP_PASSWORD)
    browser.find_element(By.ID, 'passwordInput').send_keys(PASSWORD)
    click(XP_LOGIN)


def start():
    sleep(2)
    XP = '//div[contains(@class,"word")]//div[not((@class="pressed-correct")or(@class="pressed-incorrect"))]/span'
    BODY = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
    while True:
        try:
            ch = wait.until(EC.element_to_be_clickable((By.XPATH, XP)))
            BODY.send_keys(ch.text)
            sleep(uniform(.05, .3))
        except:
            break


if __name__ == '__main__':
    login()
    print()
    print('Go to the exam page. Take a deep breath, and press Enter.')
    input()
    start()
