import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Sachin Joshi/PycharmProjects/Selenium/Jar Files & Driver/chromedriver_win32_84.0.4147.30/chromedriver.exe")

driver.get("https://www.saucedemo.com/index.html")
driver.maximize_window()

driver.find_element_by_css_selector("input#user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element_by_css_selector("input#password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element_by_css_selector("input#login-button").click()