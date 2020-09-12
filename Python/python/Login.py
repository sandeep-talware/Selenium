import os
import time

from selenium import webdriver

from Python.python import _readproperties
from selenium.webdriver.support import expected_conditions as EC

# this is the normal way to get the absolute path till the current folder
# abs_path = os.path.abspath('.')

# we need to go 2 level up to reach the parent folder so that we can navigate to the chromedriver folder
abs_path = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),".."))

# apps variable will have the dictionary of all properties data in key:value pair
apps = _readproperties(abs_path+'/Python/config/app-config.properties')
driver = webdriver.Chrome(abs_path+"/Jar Files & Driver/chromedriver_win32_84.0.4147.30/chromedriver.exe")
driver.get(apps["APP_URL"])
driver.maximize_window()

driver.find_element_by_css_selector("input#user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element_by_css_selector("input#password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element_by_css_selector("input#login-button").click()
