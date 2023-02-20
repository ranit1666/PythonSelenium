from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import os

#open chrome browser
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "./downloads/"}
chrome_options.add_experimental_option("prefs", prefs)
#driver = webdriver.Chrome()
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",chrome_options=chrome_options)
#driver=webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.delete_all_cookies()
driver.maximize_window()
#file should be downloaded inside project downloads folder
generateFile=driver.find_element(By.XPATH,"(//button[text()='Generate File'])[1]")
enter_data=driver.find_element(By.XPATH,"(//label[text()='Enter Data:'])[1]/parent::div/child::textarea")
enter_data.send_keys("my name is ranit")
WebDriverWait(driver,30).until(EC.element_to_be_clickable(generateFile))
generateFile.click()
WebDriverWait(driver,30).until(EC.presence_of_element_located(
  (By.XPATH, "(//button[text()='Generate File'])[1]/preceding-sibling::div/following-sibling::a")))
download=driver.find_element(By.XPATH,"(//button[text()='Generate File'])[1]/preceding-sibling::div/following-sibling::a")
download.click()
time.sleep(5)