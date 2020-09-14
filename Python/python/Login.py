
from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open("https://www.saucedemo.com/index.html")
        print("url opened successfully")
