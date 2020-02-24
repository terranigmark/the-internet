###CLICK ON CHEBOXES AND KNOW THEIR STATUS
'''
This script goes to http://the-internet.herokuapp.com/checkboxes
Check if the first checkbox is selected or not and changes it's status
Does the same for the following checkbox
'''

import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website
    def test_clicking_checkboxes(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Checkboxes")
        excercise.click()
        sleep(1)

        #Find the checkbox to know it's current state, changes it and return it to screen
        for i in range (2):
            checkbox = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/form/input[{i + 1}]')
            if checkbox.is_selected():
                print(f'The checkbox number {i + 1} is selected')
            else:
                print(f'The checkbox number {i + 1} is NOT selected')
            checkbox.click()

    #Tearing down browser's instance
    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()