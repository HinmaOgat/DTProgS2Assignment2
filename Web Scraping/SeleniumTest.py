from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime

now = datetime.datetime.now()
print(now.time())

op = webdriver.ChromeOptions()
op.add_argument('headless')

# Initialize the WebDriver
driver = webdriver.Chrome(options=op) 
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get("https://www.xbox.com/en-AU/games/browse?Multiplayer=SinglePlayer")

games = driver.find_elements(By.XPATH, '//*[@class="ProductCard-module__infoBox___M5x18"]')

keeplist = '0123456789.-'

priceRange = 50

for game in games:
    price = game.text.splitlines()[1]
    keeplist='0123456789-.'
    price = ''.join(i for i in price if i in keeplist)
    if price.count('.') > 1:
        price = price[price.find('.')+3:]
    try:
        if float(price) < priceRange:
            print(f'{game.text.splitlines()[0]} for ${price}')
    except:
        pass