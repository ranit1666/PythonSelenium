from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

#driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#open chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.delete_all_cookies()
driver.maximize_window()
Alert_btn_xpath=driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display an  alert box:')]")
Alert_With_ConfirmBox_xpath=driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display a confirm box')]")
Alert_With_PromptBox_xpath=driver.find_element(By.XPATH,"//button[contains(text(),'click the button to demonstrate the prompt box')]")
#time.sleep is added intentionally to observe browser functions
Alert_with_OK_Cancel_xpath=driver.find_element(By.XPATH,"//a[contains(text(),'Alert with OK & Cancel')]")
Alert_with_textbox_xpath=driver.find_element(By.XPATH,"//a[contains(text(),'Alert with Textbox')]")
time.sleep(5)
Alert_btn_xpath.click()
time.sleep(2)
driver.switch_to.alert.accept()
Alert_with_OK_Cancel_xpath.click()
time.sleep(2)
Alert_With_ConfirmBox_xpath.click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
Alert_with_textbox_xpath.click()
time.sleep(2)
Alert_With_PromptBox_xpath.click()
time.sleep(2)
driver.switch_to.alert
driver.switch_to.alert.send_keys("i am ranit")
time.sleep(2)