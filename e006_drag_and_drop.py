import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_drag_and_drop(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Drag and Drop")
        excercise.click()

        source_element = driver.find_element_by_id("column-a")
        destination = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]")
        action = ActionChains(driver)
        drag = action.click_and_hold(source_element).move_to_element(destination).release(destination)

        drag.perform()
        print("Columns are switched")
        sleep(1)


    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()