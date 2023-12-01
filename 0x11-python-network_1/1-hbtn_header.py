#!/usr/bin/python3
"""
The script takes in URL, sends request to URL and dislays value of
the X-Request-id-variable in the header of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
