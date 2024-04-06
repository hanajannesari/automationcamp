from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# Initialize the driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
random_number = random.uniform(19758.00, 19758.12345678)
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.chrome.options import Options

#ورود به سامانه
driver.set_window_size(1920, 1080)
driver.get('http://212.16.83.235:1669/')
sleep(10)
driver.find_element('id','nationalCode').send_keys('2930146532')
driver.find_element ( 'id' ,'password').send_keys('123456hH@')

driver.find_element('id' ,'securitycode').click()
sleep(7)

driver.find_element('xpath' , "//button[text()='ورود']").click()
sleep(5)
b=driver.find_element('id', 'confirmCode')
b.click()
b.send_keys('101010')
driver.find_element('xpath', "//button[@variant='primary']").click()
sleep(5)

#ورود به ثبت درخواست
driver.find_element('xpath' , "(//a[@title=' ثبت درخواست گواهي الکترونيکي '])[2]")
sleep(4)
driver.find_element('xpath' , " css-19bb58m").click()
driver.find_element('id' , "react-select-2-option-2").click()
sleep(3)
#برای بستن سشن
driver.close()
driver.quit()

