import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PokeScraping(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../python-dojo/chromedriver')
        driver = self.driver
        driver.get('https://pokemondb.net/pokedex/all')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text('Bulbasaur').click()

    def test_scaping_pokemons(self):
        driver = self.driver

        pokedex = {}
        pokemon = {}
        total_pokemons = 890
        number = 1

        while number < 890:
            print(number)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > main > h2:nth-child(9)')))

            pokemon_number = driver.find_element_by_xpath(f'//*[@id="tab-basic-{number}"]/div[1]/div[2]/table/tbody/tr[1]/td/strong').text
            pokemon_name = driver.find_element_by_css_selector('body > main > h1').text
            pokemon_species = driver.find_element_by_xpath(f'//*[@id="tab-basic-{number}"]/div[1]/div[2]/table/tbody/tr[3]/td').text
            pokemon_type1 = driver.find_element_by_xpath(f'//*[@id="tab-basic-{number}"]/div[1]/div[2]/table/tbody/tr[2]/td/a[1]').text
            try:
                pokemon_type2 = driver.find_element_by_xpath(f'//*[@id="tab-basic-{number}"]/div[1]/div[2]/table/tbody/tr[2]/td/a[2]').text
            except:
                print('This pokemon has only 1 type')
                pass

            # update pokemon dictionary
            pokemon.update([ ('number', pokemon_number), ('name', pokemon_name), ('species', pokemon_species), ('type1', pokemon_type1), ('type2', pokemon_type2) ])

            #update podekex appending pokemon dictionary
            pokedex[pokemon_number] = pokemon
            number += 1

            print(f'Single pokemon updated {pokemon}')
            print(f'Pokedex updated: {pokedex}')

            next_pokemon = driver.find_element_by_class_name('entity-nav-next')
            next_pokemon.click()

    def tearDown(self):
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()