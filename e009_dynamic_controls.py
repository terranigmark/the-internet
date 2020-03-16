###HANDLING DYNAMIC CONTROLS
'''
This script goes to http://the-internet.herokuapp.com/dynamic_controls
Where there are two controsl which take some time to be active/inactive
In order to use them after being activate it can be used some kind of wait
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website
    def test_using_dynamic_controls(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dynamic Controls")
        excercise.click()

        #Identifies the checkbox, clicks on it and then in the 'remove' button
        checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')
        checkbox.click()
        remove_checkbox_btn = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        remove_checkbox_btn.click()

        #Identifies the 'enable' button, clicks on it, focus the textbox and inputs a text
        enable_btn = driver.find_element_by_xpath('//*[@id="input-example"]/button')
        enable_btn.click()
        sleep(5)
        textbox = driver.find_element_by_xpath('//*[@id="input-example"]/input')
        textbox.send_keys("ola ke ase")
        enable_btn.click()

    #Tearing down browser's instance
    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()