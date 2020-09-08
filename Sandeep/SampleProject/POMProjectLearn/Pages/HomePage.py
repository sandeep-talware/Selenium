class HomePage():

    def __init__(self,driver):
        print("In POM Home Page")
        self.driver = driver
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"


    def click_welcome(self):
        print("In POM Home Page welcome link")
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        print("In POM Home Page Logout link")
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()