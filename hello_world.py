from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Opera(executable_path = "./operadriver")
driver.get("https://www.python.org")

about_link = driver.find_element_by_link_text("About")
about_link.click()

search_bar = driver.find_elements_by_id("id-search-field")
search_bar.send_keys

sleep(3)

driver.close()