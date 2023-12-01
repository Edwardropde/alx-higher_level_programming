#!/usr/bin/python3
"""
Displays X-request-Id header variable of request to specific URL
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers['X-Request-Id']))
