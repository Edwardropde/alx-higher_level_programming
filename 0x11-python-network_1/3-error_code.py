#!/usr/bin/python3
"""
Script that takes in URL, sends request to URL displays the body of response
(decoddin utf-8)
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
