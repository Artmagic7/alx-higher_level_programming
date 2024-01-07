#!/usr/bin/python3
""" This takes in a URL, sends a request to the URL, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code """

from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
