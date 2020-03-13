###ADD AND REMOVE ELEMENTS WITH BUTTONS
'''
This script goes to http://the-internet.herokuapp.com/add_remove_elements/
Add elements clicking in the "Add Element" button and delete them using as parameters
the inputs from the user. The script is capable to identify if its intended to 
delete more elements than the amount on screen and returns the total on in.
'''

import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
    
    def test_go_to_excercise(self):
        #Create browser instance and go to the excercise website
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a')
        excercise.click()

        #Data input to add, remove and count total of buttons on screen
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        sleep(3)
        
        #Process to add buttons
        for i in range(elements_added):
            add_button.click()
        
        sleep(3)

        #Process to delete buttons using as reference the one in the list
        #It has to be explicitly using xpath since the other buttons are erased from the DOM
        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/button[1]")
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break
        
        #Data output of elements on screen
        if total_elements > 0:
            print(f"There are {total_elements} elemetns on screen")
        else:
            print("There are 0 elements on screen")
        
        sleep(3)
    
    #Tearing down browser's instance
    def tearDown(self):
        print('Closing broswer...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    