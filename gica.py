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
def open_session():
    user_dir = "C:/Users/MM/Documents/AutomationCamp/temp/user_dir"
    options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    options.add_argument("--remote-debugging-port=8484")
    options.add_argument(f"--user-data-dir={user_dir}")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    return driver
def continue_session():
    service2 = Service(executable_path=ChromeDriverManager().install())
    options2 = webdriver.ChromeOptions()
    options2.add_experimental_option("debuggerAddress", "localhost:8484")
    driver2 = webdriver.Chrome(service=service2, options=options2)
    return driver2
options = webdriver.ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver.set_window_size(1400, 1040)
driver.implicitly_wait(25)
driver.get("https://www.ntsw.ir/index.aspx")
driver.find_element('id', 'txtUserName').send_keys('test')
driver.find_element('id', 'txtPassword').send_keys('NSW@tesT#13950505')
driver.find_element('id', 'txtCapcha').send_keys(1)
driver.implicitly_wait(25)
driver.find_element('id', 'btnStepOneLogin').click()
driver.implicitly_wait(25)
driver.find_element('id', "roleSelector").click()
dropdown = driver.find_element('id', "roleSelector")
dropdown.find_element(By.XPATH, "//option[. = 'بازرگان حقیقی - فعال']").click()
sleep(10)
driver.get('https://www.ntsw.ir/Users/AC/Currency/OriginOfBankCurrency')
driver.implicitly_wait(25)
driver.find_element('id', 'prfVCodeInt').send_keys(66813170)
driver.implicitly_wait(25)
driver.find_element('xpath', "//div[contains(@class, 'ant-select-item ant-select-item-option')]").click()
driver.implicitly_wait(25)
driver.find_element('xpath', "//button[@class='btn undefined']").click()
sleep(10)
driver.find_element('xpath', "//button[text()='ایجاد منشاء ارز']").click()
sleep(8)
driver.find_element('id', 'sanadHaml').click()
driver.implicitly_wait(25)
driver.find_element('id', "sanadHaml-0-565027").click()
driver.implicitly_wait(25)
driver.find_element('xpath', "(//input[@class='ant-checkbox-input'])[2]").click()
driver.implicitly_wait(25)
w2 = driver.find_element('xpath', "//input[@value='39,000']")
w2.click()
for i in range(9):  # Adjust the range as needed
    w2.send_keys(Keys.BACKSPACE)
driver.switch_to_parent_frame()
w2.send_keys(random_number)
w3=driver.find_element(By.XPATH,"(//div[@class='ant-table-content']//table)[2]")
w3.click()

driver.close()
driver.quit()

