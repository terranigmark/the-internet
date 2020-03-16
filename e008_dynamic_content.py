###HANDLING DYNAMIC CONTENT
'''
This script goes to http://the-internet.herokuapp.com/dynamic_content
Where it has two tasks:
1. Get the URL of each different profile picture;
2. Scrap each coment generated.
It is known that there are 7 different profile pictures.
Comments are randomly generated which make it almost impossible to have duplicates
'''

import unittest
from selenium import webdriver
from time import sleep

class UsingUnittest(unittest.TestCase):

    #Setup browser instance using Opera
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    #Create browser instance and go to the excercise website    
    def test_locating_pictures(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dynamic Content")
        excercise.click()

        #Data structures to store information
        pictures = []
        posts = []
        total_pictures = 7
        total_comments = 0
        shown_pictures = 3
        shown_comments = 3
        tries = 1

        while len(pictures) < total_pictures and len(posts) < 1000:

            #for loop to iterate through the different profile pictures
            #Firt we locate the picture knowing there are 3 on screen and then we extract it's URL
            for i in range(shown_pictures):
                avatar = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div/div/div[{i + 1}]/div[1]/img")
                avatar_route = avatar.get_attribute("src")
                
                #In case the url is not already stored we'll include it in it's list
                if avatar_route not in pictures:
                    pictures.append(avatar_route)
                    
                else:
                    pass
            
            #Then we aim for the comments locating them, extracting the test and sum the amount of comments
            for i in range(shown_comments):
                post = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div/div/div[{i + 1}]/div[2]")
                post_test = post.text
                print(post_test)
                total_comments += 1

                #If the comment isn't in it's list already then it'll be stored
                if post_test not in posts:
                    posts.append(post_test)                    
                else:
                    print("There are no new posts")
                
            #As we don't know how many different comments are we count the number of iterations
            tries += 1
            print(pictures)
            print(f"\n COMENT BATCH #{len(posts)}   ".join(posts))
            print(tries, total_pictures, total_comments)
            driver.refresh()            

            print(posts[-1])

    #Tearing down browser's instance
    def tearDown(self):
        print("Browser is about to close...")
        sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

#XPath structure for both pictures and comments
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