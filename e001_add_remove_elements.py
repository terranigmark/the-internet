import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
    
    def test_go_to_excercise(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a')
        excercise.click()

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        sleep(3)
        
        for i in range(elements_added):
            add_button.click()
        
        sleep(3)
        delete_button = driver.find_element_by_class_xpath("/html/body/div[2]/div/div/div/button[1]")
        print(delete_button)

        for i in range(elements_removed):
            if i == elements_removed - 1:
                delete_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/button")
            else:
                delete_button.click()
        
        sleep(3)
    
    def tearDown(self):
        print('Closing broswer...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()