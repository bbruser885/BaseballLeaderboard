import json
import string
import sys
import os
import scraper
import re

def gui_interface():
    pass

def get_user_input():

    ''' Gets user data from the command line '''

    while True:
        user_input = input("Search 2018 stats: ")
        if user_input == 'quit':
            break
        else:
            return user_input

def parse_user_input(user_input):

    ''' Parses the command line input of users.
    strips it of punctuation and checks if the string is empty or not '''

    exclude = set(string.punctuation)
    user_parsed_input = ''.join(char for char in user_input if char not in exclude).lower()
    if user_parsed_input == "":
        return None
    else:
        return user_parsed_input

def load_JSON():
    path = os.path.join("response", "stat.JSON")
    with open(path) as json_data:
         response_data = json.loads(json_data.read())
         return response_data

def check_respone(str):
    response_data = load_JSON()
    for key, values in response_data.items():
        for val in values:
            if val in str.lower():
                return key
    return None

def parse_year(str):
    year = re.search(".*([1-2][0-9]{3})", str)
    return year.group(1)

def scrape_respone(str):
    pass

if __name__ == '__main__':
    user_input = get_user_input()
    p_usr_inpt = parse_user_input(user_input)
    check_respone(p_usr_inpt)
    parse_year(p_usr_inpt)
    new_scraper = scraper.br_scraper(check_respone(p_usr_inpt))
