import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_drag_and_drop(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/drag_and_drop")
        excercise = driver.find_element_by_link_text("Drag and Drop")
        excercise.click()

        source_element = driver.find_element_by_id("column-a")
        destination_element = driver.find_element_by_id("column-b")
        drag = 


    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()