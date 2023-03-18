from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, random

url = 'https://monkeytype.com/'
wpm = 200
delay = random.randint(35, 85) / wpm / 5

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, executable_path='path/to/executable')
driver.get(url)

time.sleep(15)
word_divs = driver.find_elements(By.CSS_SELECTOR, '.word')

for word_div in word_divs:
    word = word_div.text
    for letter in word:
        driver.switch_to.active_element.send_keys(letter)
        time.sleep(delay)
    driver.switch_to.active_element.send_keys(Keys.SPACE)