#!/usr/bin/python3
"""
Displays X-request-Id header variable of request to specific URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
