#! python3
# Program który automatycznie będzie grać w grę 2048 pod adresem : https://play2048.co/
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
html_elem = browser.find_element_by_tag_name('html')
ruchy = [Keys.ARROW_LEFT, Keys.ARROW_DOWN, Keys.ARROW_RIGHT, Keys.ARROW_UP]
while True:
    try:
        html_over = browser.find_element_by_class_name('game-over')
        html_pause = browser.find_element_by_class_name('retry-button')
        html_pause.click()
    except:
        html_elem.send_keys(random.choice(ruchy))


