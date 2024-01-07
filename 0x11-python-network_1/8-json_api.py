#!/usr/bin/python3
""" Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Displays the id and name if the response body is properly JSON formatted and not empty. """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        user_data = response.json()
        if user_data:
            print("[{}] {}".format(user_data['id'], user_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
