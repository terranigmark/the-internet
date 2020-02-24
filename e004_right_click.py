import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_right_click(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Context Menu")
        excercise.click()

        right_click = ActionChains(driver)
        hot_spot = driver.find_element_by_id("hot-spot")
        right_click.context_click(hot_spot).perform()
        


    def test_handling_alert(self):
        pass

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()