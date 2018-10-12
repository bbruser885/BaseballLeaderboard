import requests
import json
import os
from os import listdir, path
from bs4 import BeautifulSoup


# url_to_parse = 'https://www.baseball-reference.com/leagues/MLB/2018-pitching-leaders.shtml'
url_to_parse = "https://www.baseball-reference.com/leagues/MLB/"
desired_category = 'leaderboard_pitching_WAR_pitch'


class br_scraper:
    def __init__(self, search_terms):
        self.desired_category = search_terms

    def load_JSON_from_url():
        path = os.path.join("src", "response", "url.JSON")
        # with open('src\\response\\url.JSON') as json_data:
        with open(path) as json_data:
            d = json.loads(json_data.read())
            return d

    def get_html_data(url_to_parse):
        data = requests.get(url_to_parse)
        return BeautifulSoup(data.text, 'html.parser')

    def scrape_baseball_reference(soup_data):
        leaderboard = soup_data.find_all('div', {'id': '{}'.format(desired_category)})

        for leader in leaderboard:
            for tr in leader.find_all("tr", "first_place"):
                player_name = tr.find('a',)['title']
                team = tr.find('span').text.strip()
                stat = tr.find("td", "value").text.strip()
                return [player_name, team, stat]


# soup_data = get_html_data(url_to_parse)
# stringy = str(type(soup_data))
# print(scrape_baseball_reference(soup_data, desired_category))
# print(load_JSON_from_url())
# print(listdir())
