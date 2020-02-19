import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def input_data(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
    
    def tearDown(self):
        print('Closing browser...')
        self.driver.close()

if __name__ == "__main__":
    unittest.main()