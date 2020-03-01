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
        posts = []
        total_pictures = 5
        total_comments = 0
        shown_pictures = 3
        shown_comments = 3
        tries = 1

        while len(pictures) < total_pictures and len(posts) < 30:

            for i in range(shown_pictures):
                avatar = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div/div/div[{i + 1}]/div[1]/img")
                avatar_route = avatar.get_attribute("src")
                
                if avatar_route not in pictures:
                    pictures.append(avatar_route)
                    
                else:
                    pass
            
            for i in range(shown_comments):
                post = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div/div/div[{i + 1}]/div[2]")
                post_test = post.text
                print(post_test)
                total_comments += 1

                if post_test not in posts:
                    posts.append(post_test)                    
                else:
                    print("There are no new posts")
                
            tries += 1
            print(pictures)
            print(f"\n COMENT BATCH #{len(posts)}   ".join(posts))
            print(tries, total_pictures, total_comments)
            driver.refresh()            

            print(posts[::-1])

    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

""" 
Pictures XPath structure
/html/body/div[2]/div/div/div/div/div[1]/div[1]/img
/html/body/div[2]/div/div/div/div/div[2]/div[1]/img
/html/body/div[2]/div/div/div/div/div[3]/div[1]/img 

Text XPath structure
/html/body/div[2]/div/div/div/div/div[1]/div[2]
/html/body/div[2]/div/div/div/div/div[2]/div[2]
/html/body/div[2]/div/div/div/div/div[3]/div[2]/text()
"""