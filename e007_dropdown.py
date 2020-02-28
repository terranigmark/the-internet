###HANDLING DROPDOWN MENUS
'''
This script goes to http://the-internet.herokuapp.com/dropdown
Focuses on the dropdown menu and select each option available
This is done by different methods and can be done with control flows too
'''

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website
    def test_handling_dropdown(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dropdown")
        excercise.click()

        #Creates and instance that focus on the dropdown menu
        dropdown_menu = Select(driver.find_element_by_id("dropdown"))
        sleep(1)
        
        #Select dropdown's options through different methods
        dropdown_menu.select_by_value("1")
        sleep(1)
        dropdown_menu.select_by_value("2")
        sleep(1)
        dropdown_menu.select_by_index(1)
        sleep(1)
        dropdown_menu.select_by_index(2)
        sleep(1)
        dropdown_menu.select_by_visible_text("Option 1")
        sleep(1)
        dropdown_menu.select_by_visible_text("Option 2")

    #Tearing down browser's instance
    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()