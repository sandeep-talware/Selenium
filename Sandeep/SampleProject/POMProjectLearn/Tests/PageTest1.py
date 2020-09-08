import unittest

from selenium import webdriver
from SampleProject.POMProjectLearn.Pages.HomePage import HomePage
from SampleProject.POMProjectLearn.Pages.LoginPage import LoginPage
import HtmlTestRunner
import time


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Test Start")
        cls.driver = webdriver.Chrome(
            executable_path="E:/study/Python_Program/Python_Selenium_Proj_1/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_valid_login(self):
        driver = self.driver
        driver.get(url="https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username(username="Admin")
        login.enter_password(password="admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(1)

    def test_02_invalid_login(self):
        driver = self.driver
        driver.get(url="https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username(username="Admin123")
        login.enter_password(password="admin123")
        login.click_login()
        massage = login.get_invalid_massage()
        self.assertEqual(massage,"Invalid credentials")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/study/Python_Program/Python_Selenium_Proj_1/Report'))
