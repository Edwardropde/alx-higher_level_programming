#!/usr/bin/python3
import sys


def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d}".format(code, status_codes[code]))


try:
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403:
                    0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            try:
                code = int(parts[-2])
                size = int(parts[-1])
                if code in status_codes:
                    status_codes[code] += 1
                total_size += size
                line_count += 1
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
