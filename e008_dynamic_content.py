import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")
        
    def test_locating_pictures(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dynamic Content")
        excercise.click()

        

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

""" /html/body/div[2]/div/div/div/div/div[1]/div[1]/img
/html/body/div[2]/div/div/div/div/div[2]/div[1]/img
/html/body/div[2]/div/div/div/div/div[3]/div[1]/img """