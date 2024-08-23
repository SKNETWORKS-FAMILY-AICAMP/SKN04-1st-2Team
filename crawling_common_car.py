import pandas as pd
import psycopg2
import requests
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


driver.get('https://stat.molit.go.kr/portal/cate/statView.do?hRsId=58&hFormId=5498&hSelectId=5498&hPoint=00&hAppr=1&hDivEng=&oFileName=&rFileName=&midpath=&sFormId=5498&sStart=201101&sEnd=202407&sStyleNum=2&settingRadio=xlsx')

time.sleep(10)

driver.find_element(By.XPATH,'/html/body/form/div/main/div/div[3]/div[1]/div/div[1]/div[2]/div/button[2]').click()
time.sleep(4)



source_location = {'x':792,'y': 420}
target_location = {'x':1017  ,'y': 400}
pyautogui.moveTo(source_location['x'], source_location['y'])
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(target_location['x'], target_location['y'])
pyautogui.mouseUp()


source_location = {'x':792,'y': 400}
target_location = {'x':1017  ,'y': 550}
pyautogui.moveTo(source_location['x'], source_location['y'])
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(target_location['x'], target_location['y'])
pyautogui.mouseUp()


source_location = {'x':792,'y': 680}
target_location = {'x':1017  ,'y': 700}
pyautogui.moveTo(source_location['x'], source_location['y'])
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(target_location['x'], target_location['y'])
pyautogui.mouseUp()

source_location = {'x':970,'y': 890}
pyautogui.moveTo(source_location['x'], source_location['y'])
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.mouseUp()

driver.find_element(By.XPATH, '/html/body/form/div/main/div/div[3]/div[1]/div/div[1]/div[2]/div/button[1]').click()

driver.find_element(By.XPATH,'/html/body/form/div/div[2]/div[2]/div[2]/ul/li[3]/div/label').click()

driver.find_element(By.XPATH,'/html/body/form/div/div[2]/div[2]/div[3]/button').click()


