#!/usr/bin/python3
"""
The script takes in URL, sends request to URL and dislays value of
the X-Request-id-variable in the header of the response
"""


import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print('{}'.format(resp.info().get('X-Request-id')))
