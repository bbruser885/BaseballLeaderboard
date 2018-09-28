import json
import string
import sys

def gui_interface():
    pass

def get_user_input():
    while True:
        user_input = input("What would you like to search? ")
        exclude = set(string.punctuation)
        user_parsed_input = ''.join(ch for ch in user_input if ch not in exclude).lower()
        if user_parsed_input == 'quit':
            break
        else:
            return user_parsed_input
def check_respone(str):
    pass

def scrape_respone(str):
    pass
