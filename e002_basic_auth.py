import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
    
    def test_basic_auth(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")

        user = "admin"
        password = "admin"

        excercise = driver.find_element_by_link_text("Basic Auth")
        excercise.click()
        sleep(1)

        login_modal = driver.switch_to.active_element
        login_modal.send_keys(user)        

    def tearDown(self):
        print("The browser is about to close...")
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()