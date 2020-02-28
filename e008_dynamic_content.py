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

        pictures = []
        total_pictures = 5
        shown_pictures = 3
        tries = 1

        while len(pictures) < total_pictures:

            for i in range(shown_pictures):
                avatar = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div/div/div[{i + 1}]/div[1]/img")
                avatar_route = avatar.get_attribute("src")
                
                if avatar_route not in pictures:
                    pictures.append(avatar_route)
                    print(pictures)                
                
            tries += 1
            print(tries)
            driver.refresh()            

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

""" 
/html/body/div[2]/div/div/div/div/div[1]/div[1]/img
/html/body/div[2]/div/div/div/div/div[2]/div[1]/img
/html/body/div[2]/div/div/div/div/div[3]/div[1]/img 
"""