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

#open chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/JqueryProgressBar.html")
driver.delete_all_cookies()
driver.maximize_window()
wait=WebDriverWait(driver,30)
action=ActionChains(driver)
startDownload_xpath=driver.find_element(By.XPATH,"//button[@id='downloadButton']")
wait.until(EC.element_to_be_clickable(startDownload_xpath))
action.move_to_element(startDownload_xpath).click().perform()
#time.sleep(15)
#wait.until(EC.presence_of_element_located("//div[text()='Complete!']"))
WebDriverWait(driver,100).until(EC.presence_of_element_located(
  (By.XPATH, "//div[text()='Complete!']")))
progressbar_xpath=driver.find_element(By.XPATH,"//div[@id='progressbar']")
#complete_xpath=driver.find_element(By.XPATH,"//div[text()='Complete!']")

status=progressbar_xpath.get_attribute('aria-valuenow')
if status=="100":
    print("pass")
else:
    print("fail")