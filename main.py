from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random


# URL of the webpage containing the words
url = 'https://monkeytype.com/'

# Words per minute
wpm = 200

# Calculate delay between keystrokes in seconds
delay = random.randint(35, 85) / wpm / 5

# Set up Chrome driver
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path="path/to/executable")


# Navigate to website
driver.get(url)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

time.sleep(30)

# Find all div elements containing words
word_divs = driver.find_elements(By.CSS_SELECTOR, '.word')

# Loop through each word
for word_div in word_divs:
    # Get the text content of the word div
    word = word_div.text

    # Loop through each letter in the word
    for letter in word:
        # Simulate typing the letter
        driver.switch_to.active_element.send_keys(letter)
        
        # Wait for the appropriate delay between keystrokes
        time.sleep(delay)

    # Add a space after the word
    driver.switch_to.active_element.send_keys(Keys.SPACE)


