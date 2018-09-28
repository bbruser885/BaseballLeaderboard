import requests
import json
from os import listdir
from bs4 import BeautifulSoup


url_to_parse = 'https://www.baseball-reference.com/leagues/MLB/2018-pitching-leaders.shtml'
desired_category = 'leaderboard_pitching_WAR_pitch'

def load_JSON_from_url():
    with open('src\\response\\url.JSON') as json_data:
        d = json.loads(json_data.read())
        return d

def get_html_data(url_to_parse):
    data = requests.get(url_to_parse)
    return BeautifulSoup(data.text, 'html.parser')

def scrape_baseball_reference(soup_data, desired_category):
    leaderboard = soup_data.find_all('div', {'id': '{}'.format(desired_category)})

    for leader in leaderboard:
        for tr in leader.find_all("tr", "first_place"):
            player_name = tr.find('a',)['title']
            team = tr.find('span').text.strip()
            stat = tr.find("td", "value").text.strip()
            return [player_name, team, stat]


soup_data = get_html_data(url_to_parse)
stringy = str(type(soup_data))
# print(scrape_baseball_reference(soup_data, desired_category))
# load_JSON_from_url()
# print(listdir())
