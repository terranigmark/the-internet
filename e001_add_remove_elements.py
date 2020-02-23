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
        total_elements = elements_added - elements_removed
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        sleep(3)
        
        for i in range(elements_added):
            add_button.click()
        
        sleep(3)

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/button[1]")
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elemetns on screen")
        else:
            print("There are 0 elements on screen")
        
        sleep(3)
    
    def tearDown(self):
        print('Closing broswer...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()