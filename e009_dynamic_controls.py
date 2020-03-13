import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_using_dynamic_controls(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dynamic Controls")
        excercise.click()

        checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')
        checkbox.click()
        remove_checkbox_btn = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        remove_checkbox_btn.click()

        try:
            add_btn = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((
                    By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')))
            add_btn.click()
        finally:
            sleep(5)

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()