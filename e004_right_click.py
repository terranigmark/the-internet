###RIGHT CLICK ON A SPECIFIC ELEMENT
'''
This script goes to http://the-internet.herokuapp.com/context_menu
Clicks on the box with the dotted line in order to trigger an alert
Handles the alert and closes the driver
This is to demonstrate how to open context menu over items
'''

import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website
    def test_right_click(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Context Menu")
        excercise.click()

        #Create the action to right click over an item and calls on it
        right_click = ActionChains(driver)
        hot_spot = driver.find_element_by_id("hot-spot")
        right_click.context_click(hot_spot).perform()
        sleep(1)

        #Alert handling focusing on it and clicking in the accepting button
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

    #Tearing down browser's instance
    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()