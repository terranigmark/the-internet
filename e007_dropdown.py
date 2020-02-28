import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_handling_dropdown(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dropdown")
        excercise.click()

        dropdown_menu = Select(driver.find_elements_by_id("dropdown"))
        dropdown_menu.select_by_index(0)
        sleep(1)
        dropdown_menu.select_by_index(1)

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()