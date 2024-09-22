from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg

op = webdriver.ChromeOptions()
op.add_argument('headless')

# Initialize the WebDriver
driver = webdriver.Chrome(options=op) 
#driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get("https://www.xbox.com/en-AU/games/browse?Multiplayer=SinglePlayer")

games = driver.find_elements(By.XPATH, '//*[@class="ProductCard-module__infoBox___M5x18"]')

keeplist = '0123456789.-'

priceRange = 50

layout = [[sg.Button('Click Me!',key='click',size=(15,1))],
          [sg.Text('',key='updateMe')]]

window = sg.Window("Lego Search!", layout,finalize=True,resizable=True) #Creates main application window

def updateWindow():
    gameList = []
    for game in games:
        price = game.text.splitlines()[1]
        keeplist='0123456789-.'
        price = ''.join(i for i in price if i in keeplist)
        if price.count('.') > 1:
            price = price[price.find('.')+3:]
        try:
            if float(price) < priceRange:
                gameList.append(f'{game.text.splitlines()[0]} for ${price}')
        except:
            pass
    window["updateMe"].update('\n'.join(map(str, gameList)))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'click':
       updateWindow()
window.close()#