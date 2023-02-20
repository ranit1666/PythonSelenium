from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time

#open chrome browser
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.delete_all_cookies()
driver.maximize_window()
#verify double click operation
field2_xpath= driver.find_element(By.XPATH,"//input[@id='field2']")
copyText_xpath = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
time.sleep(5)
blank_text=field2_xpath.get_attribute('value')
if blank_text=="":
    print("textbox contains no value")
else:
    print("textbox contains value. Test fails")
action=ActionChains(driver)
action.move_to_element(copyText_xpath).double_click(copyText_xpath).perform()
time.sleep(5)
blank_text_new=field2_xpath.get_attribute('value')
if blank_text_new=="Hello World!":
    print("textbox contains Hello World!")
else:
    print("textbox does not contains Hello World!. Test fails")

#drag and drop
drag_xpath= driver.find_element(By.XPATH,"//p[text()='Drag me to my target']/parent::div")
drop_xpath= driver.find_element(By.XPATH,"//p[text()='Drop here']/parent::div")
driver.execute_script("arguments[0].scrollIntoView;",drag_xpath)
action.click_and_hold(drag_xpath).move_to_element(drop_xpath).release().perform()
time.sleep(5)



