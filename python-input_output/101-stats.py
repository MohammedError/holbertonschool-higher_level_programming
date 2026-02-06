#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
"""
import sys


def print_stats(total_size, status_codes):
    """Prints the accumulated statistics.

    Args:
        total_size (int): The total read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) >= 2:
                    total_size += int(parts[-1])
                    code = int(parts[-2])
                    if code in status_codes:
                        status_codes[code] += 1
            except (ValueError, IndexError):
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
