import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.python.org")

        about_button = driver.find_element_by_link_text("About")
        sleep(3)
        about_button.click()

        search_bar = driver.find_element_by_id("id-search-field")
        search_bar.click()
        search_bar.send_keys("documentation")
        search_bar.send_keys(Keys.ENTER)
    
    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()