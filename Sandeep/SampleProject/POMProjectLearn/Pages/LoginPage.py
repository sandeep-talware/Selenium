from selenium import webdriver


class LoginPage():

    def __init__(self, driver):
        print("In POM Login Page")
        self.driver = driver
        self.username_TextBox_id = "txtUsername"
        self.password_TextBox_id = "txtPassword"
        self.loginButton_id = "btnLogin"
        self.invalid_login_massage_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        print("In POM Login Page Enter Username")
        self.driver.find_element_by_id(self.username_TextBox_id).clear()
        self.driver.find_element_by_id(self.username_TextBox_id).send_keys(username)

    def enter_password(self, password):
        print("In POM Login Page Enter password")
        self.driver.find_element_by_id(self.password_TextBox_id).clear()
        self.driver.find_element_by_id(self.password_TextBox_id).send_keys(password)

    def click_login(self):
        print("In POM Login Page Submit Button")
        self.driver.find_element_by_id(self.loginButton_id).click()

    def get_invalid_massage(self):
        print("In POM Login Page Verification Invalid Login")
        msg = self.driver.find_element_by_xpath(self.invalid_login_massage_xpath).text
        return msg
