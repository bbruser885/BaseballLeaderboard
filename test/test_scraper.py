import unittest
import context
import requests
import re
from bs4 import BeautifulSoup
from src import scraper

class testScraper(unittest.TestCase):

    def setUp(self):
        pass

    def test_load_JSON_from_url(self):
        dict = {}
        result = scraper.load_JSON_from_url()
        self.assertEqual(type(result), type(dict) )
        self.assertTrue(result)


    def test_get_html_data(self):
        ## test <class 'bs4.BeautifulSoup'> ##
        result = scraper.get_html_data('https://www.baseball-reference.com/leagues/MLB/2018-pitching-leaders.shtml')
        self.assertEqual(str(type(result)), "<class 'bs4.BeautifulSoup'>")

    def test_scrape_baseball_reference(self):
        data = requests.get('https://www.baseball-reference.com/leagues/MLB/2018-pitching-leaders.shtml')
        soup_data = BeautifulSoup(data.text, 'html.parser')
        result = scraper.scrape_baseball_reference(soup_data,'leaderboard_pitching_WAR_pitch')
        ##test recieve all three elements of the list
        self.assertEqual(len(result), 3)

        ##test that the elements are not empty
        for string in result:
            self.assertNotEqual(string, "")
        ## Test return with regex
        # regex = re.compile("([A-Z][a-zA-Z]*")
        # self.assertTrue(regex.match(result[0]))
        ## player should be [0 or more letters] a space [zero or more letter]

        ## Team should be of length 3 and contain only letters

        ##stats
        ## [1 or more digits] . [zero or more digits]
if __name__ == '__main__':
    unittest.main()
