from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#pip install webdriver-manager
#pip install -U pytest
#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")



