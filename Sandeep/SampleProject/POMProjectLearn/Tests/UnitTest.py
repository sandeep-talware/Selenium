from selenium import webdriver
import time
import unittest

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Test Start")
        cls.driver = webdriver.Chrome(executable_path="E:/study/Python_Program/Python_Selenium_Proj_1/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_Login(self):
        self.driver.get(url="https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(1)
        self.driver.find_element_by_id("welcome").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")