from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time


class Registration(unittest.TestCase):

    # @classmethod
    def abc(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        #self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("testing")
        self.driver.get("https://demo.automationtesting.in/Register.html")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()


    # def fillUpForm(self):
    #     self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #     print("testing")
    #     self.driver.get("https://demo.automationtesting.in/Register.html")
    #     self.driver.delete_all_cookies()
    #     self.driver.maximize_window()
    #     # fname_xpath= self.driver.find_element(By.XPATH,"//label[text()='Full Name* ']/parent::div/child::div/input[@ng-model='FirstName']")
    #     # lname_xpath = self.driver.find_element(By.XPATH,"//label[text()='Full Name* ']/parent::div/child::div/input[@ng-model='LastName']")
    #     # time.sleep(5)
    #     # fname_xpath.send_keys("Ranit")
    #     # lname_xpath.send_keys("ray")
if __name__ == "__main__":
    unittest.main()



