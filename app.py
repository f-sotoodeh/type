from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from yaml import safe_load as load
from playsound import playsound
from functools import partial
from random import uniform
from time import sleep




def wait():
    try:
        playsound('87478.mp3')
    except:
        pass
    input('Press ENTER')
    # modal = browser.find_element(By.CLASS_NAME, 'modal')
    # print()
    # print('WAIT')
    # print(modal.value_of_css_property('display'))
    # print()
    # if modal.value_of_css_property('display') != 'none':
    # while True:
    #     sleep(1)
    #     modal = browser.find_element(By.CLASS_NAME, 'modal')
    #     if modal.value_of_css_property('display') == 'none':
    #         break
    # sleep(1)

def select_lesson():
    with open('data.yaml') as f:
        data = load(f)
    for i, course in enumerate(data.keys(), start=1):
        print(i, course, sep=' >> ')
    ci = int(input('Which one? ')) - 1
    course = list(data.keys())[ci]
    for i, lesson in enumerate(data[course], start=1):
        print(i, lesson, sep=' >> ')
    li = int(input('Which one? ')) - 1
    lesson = list(data[course].keys())[li]
    part = data[course][lesson]
    if type(part) == list:
        if len(part) == 1:
            part = part[0]
        else:
            for i, p in enumerate(part, start=1):
                print(i, p, sep=' >> ')
            pi = int(input('Which one? ')) - 1
            part = part[pi]
    return course, lesson, part

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

def go_to_course(course, lesson, part):
    CLASS = 'form-select'
    XP_COURSE = f'''//a[@class="ng-binding" and contains(text(), "{course}")]'''
    XP_LESSON = f'''//h3[@class="ng-binding" and contains(text(), '{lesson}')]'''
    XP_PART = f'''//a[@class="ng-binding" and contains(text(), '{part}')]'''
    _wait.until(EC.visibility_of_element_located((By.CLASS_NAME, CLASS)))
    select = Select(browser.find_element(By.CLASS_NAME, CLASS))
    select.select_by_visible_text('KEYS103')
    sleep(3)
    click(XP_COURSE)
    sleep(3)
    click(XP_LESSON)
    click(XP_PART)

def start():
    # browser.find_element(By.CLASS_NAME, 'modal-content').send_keys(Keys.SPACE)
    sleep(3)
    _wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.word>.digit-container')))
    _wait.until(EC.element_to_be_clickable((By.ID, 'react-keyboard')))
    while True:
        for ch in browser.find_elements(By.CSS_SELECTOR, '.word>.digit-container'):
            _wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body'))).send_keys(ch.text)
            sleep(uniform(.1, .3))
        wait()



if __name__ == '__main__':
    print()
    course_lesson = select_lesson()
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    presence = partial(EC.presence_of_element_located, locator=By.XPATH)
    _wait = WebDriverWait(browser, 60)
    click = lambda el: _wait.until(EC.element_to_be_clickable((By.XPATH, el))).click()

    login()
    go_to_course(*course_lesson)
    wait()
    start()
