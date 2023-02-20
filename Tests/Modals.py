from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

#open chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Modals.html")
driver.delete_all_cookies()
driver.maximize_window()
time.sleep(5)
#multiple modal test
multiple_modal_LaunchModal_xpath=driver.find_element(By.XPATH,"//div[text()='Multiple Modals']/parent::div/descendant::a[text()='Launch modal'][1]")
multiple_modal_LaunchModal_xpath.click()
firstModal_xpath=driver.find_element(By.XPATH,"//h4[text()='First Modal']")
time.sleep(2)
firstModal_text=firstModal_xpath.text
assert firstModal_text,"First Modal"
fModal_LaunchModal_xpath=driver.find_element(By.XPATH,"//h4[text()='First Modal']/parent::div/following-sibling::div[2]/a")
fModal_LaunchModal_xpath.click()
time.sleep(2)
modal2_xpath=driver.find_element(By.XPATH,"//h4[text()='Modal 2']")
Modal2_text=modal2_xpath.text
assert Modal2_text,"Modal 2"



