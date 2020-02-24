import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_clicking_checkboxes(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Checkboxes")
        excercise.click()
        sleep(1)

        for i in range (2):
            checkbox = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/form/input[{i + 1}]')
            if checkbox.is_selected():
                print(f'The checkbox number {i + 1} is selected')
            checkbox.click()

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()