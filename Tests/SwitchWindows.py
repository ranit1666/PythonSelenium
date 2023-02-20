from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

#time.sleep is added intentionally to observe browser functions
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.delete_all_cookies()
driver.maximize_window()
time.sleep(5)
click_btn_xpath=driver.find_element(By.XPATH,"//button[contains(text(),'click')]/parent::a")
current_handle=driver.current_window_handle
print(driver.title)
click_btn_xpath.click()
all_handles=driver.window_handles
for i in all_handles:
    if i!=current_handle:
        driver.switch_to.window(i)
        print(driver.title)
        driver.close()
time.sleep(5)
driver.switch_to.window(current_handle)
print(driver.title)

time.sleep(5)






