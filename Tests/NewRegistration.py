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
print("testing")
driver.get("https://demo.automationtesting.in/Register.html")
driver.delete_all_cookies()
driver.maximize_window()
#provide first and last name
fname_xpath= driver.find_element(By.XPATH,"//label[text()='Full Name* ']/parent::div/child::div/input[@ng-model='FirstName']")
lname_xpath = driver.find_element(By.XPATH,"//label[text()='Full Name* ']/parent::div/child::div/input[@ng-model='LastName']")
time.sleep(5)
fname_xpath.send_keys("Ranit")
lname_xpath.send_keys("ray")
#provide address
address_xpath= driver.find_element(By.XPATH,"//label[text()='Address']/parent::div/child::div/textarea")
address_xpath.send_keys("1b/17 kustia road, picnic garden")
#provide email
email_xpath= driver.find_element(By.XPATH,"//label[text()='Email address*']/parent::div/child::div/input")
#check the tooltip for email
email_tooltip_xpath= driver.find_element(By.XPATH,"//label[text()='Email address*']/parent::div/child::div/following-sibling::div/span")
tooltip_text=email_tooltip_xpath.text
#verify tooltip value
action=ActionChains(driver)
action.move_to_element(email_xpath).perform()
tooltip_text=email_tooltip_xpath.text
#assertEqual (tooltip_text,"Provide a valid email id for further updates")
email_xpath.send_keys("ray@gmail.com")
#select Male/Female from gender radio button
gender_xpath= driver.find_elements(By.XPATH,"//input[@name='radiooptions']")
option="Male"

for i in gender_xpath:
    value=i.get_attribute("value")
    print(value)
    if value==option:
        i.click()
        break
#select hobby checkboxes
hobbies_xpath= driver.find_elements(By.XPATH,"//label[text()='Hobbies']/parent::div/child::div/descendant::input")
hobbylist=["Cricket","Hockey"]
for i in hobbies_xpath:
    value=i.get_attribute("value")
    print(value)
    if value in hobbylist:
        i.click()

language_xpath= driver.find_element(By.XPATH,"//div[@id='msdd']")
language__options_xpath= driver.find_elements(By.XPATH,"//div[@id='msdd']/parent::multi-select/descendant::li/a")

#select skill from dropdown
skills__options_xpath= driver.find_element(By.XPATH,"//label[text()='Skills']/parent::div/descendant::select")
driver.execute_script("arguments[0].scrollIntoView;",skills__options_xpath)
select=Select(skills__options_xpath)
select.select_by_visible_text("Adobe InDesign")
time.sleep(2)
#select country from dropdown
countryName="India"
country_xpath= driver.find_element(By.XPATH,"//span[@class='selection']/span")
country_options_xpath= driver.find_element(By.XPATH,"//select[@id='country']")
driver.execute_script("arguments[0].scrollIntoView;",country_xpath)
time.sleep(2)
slct=Select(country_options_xpath)
slct.select_by_visible_text(countryName)
time.sleep(5)
#select multiple languages from dropdown
hobbylist=["Catalan","Danish","English"]
language_xpath.click()
for i in language__options_xpath:
    value=i.text
    print(value)
    if value in hobbylist:
        i.click()
time.sleep(10)

