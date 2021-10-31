

from datetime import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
import unittest

'''
browser = webdriver.Chrome()
# Sharhan has heard about a new online to-do app. He goes
# to check it out on its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention to-lists
assert 'todo-list' in browser.title, "Browser title is " + browser.title

# He is invited to enter a to-do item straight-away
# He types "Pray Asr" into the text box (his hobby is prayers)

# When he hits enter, the page updates and say "1: Pray Asr" as 
# an item in the to-do list

# There's still a text box inviting her to write another item. He 
# writes "Hang out with wife".

# The page updates again, and now shows both items on the list

# Sharhan wonders if the site will remember his list. Then he sees that the 
# site generated a unique URL for him

# He visits the URL -- and his to-do list is found there

# He took a break and left the site

browser.quit()
'''

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # self.opts = FirefoxOptions().add_argument("--headless")
        # self.browser = webdriver.Firefox(firefox_options=self.opts)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.browser = webdriver.Chrome(options=self.chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sharhan heard about a todo-list app and goes to check it out
        self.browser.get('http://localhost:8000')

        # He notices the title of the app say 'todo-list'
        self.assertIn('To-Do list', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Pray Asr" intot he text box
        inputbox.send_keys('Pray Asr')

        # Whe he hits enter the page updates, and show the to-do item lists
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Pray Asr' for row in rows)
        )
        # He is invited to enter an item in todo-list

        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')