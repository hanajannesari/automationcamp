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
driver.get('https://www.ntsw.ir/Index.aspx')
sleep(5)
driver.find_element('xpath', "//input[@placeholder='نام کاربری']").send_keys('test')
driver.find_element('xpath', "//input[@placeholder='کلمه عبور']").send_keys('NSW@tesT#13950505')
driver.find_element('id', 'txtCapcha').click()
sleep(7)
driver.find_element('xpath', "//button[text()='ورود']").click()
sleep(6)
driver.find_element('id', "roleSelector").click()
dropdown = driver.find_element('id', "roleSelector")
dropdown.find_element(By.XPATH, "//option[. = 'بازرگان حقیقی - فعال']").click()
sleep(7)






