###DISSAPEARING ELEMENTS
'''
This script goes to http://the-internet.herokuapp.com/disappearing_elements
Knowing there are 4 or 5 elements at random every time the site refreshes
The script will take the name of each element and refresh if there are only 4
Once there are 5, the script will create a list with the names
'''

import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website
    def test_name_elements(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Disappearing Elements")
        excercise.click()

        #Declaration of variables to use
        options = [] #List to store options names
        menu = 5 #Number of total known options
        tries = 1 #Tries counter

        #While loop which iterate until the options list gets 5 elements
        while len(options) < 5:
            options.clear() #Clears the list since each iteration adds at least 4 elements

            for i in range(menu): #Tries to get 5 elements even if there are only 4
                try:
                    option_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i + 1}]/a")
                    options.append(option_name.text)
                    print(options)
                except: #Exception raises if there are only 4 elements and refreshes the browser trying to get 5
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries += 1
                    driver.refresh()
        
        print(f"Finished in {tries} tries")

    #Tearing down browser's instance
    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()