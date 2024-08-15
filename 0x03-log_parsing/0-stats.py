#!/usr/bin/python3
"""
log parsing
"""
import sys
import signal
import re


status_occurrences = {str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

file_size = 0
line_count = 0


def print_stats():
    """
    helper function to display stats
    """
    print("File size: {}".format(file_size))
    for status in sorted(status_occurrences.keys()):
        if status_occurrences[status] > 0:
            print("{}: {}".format(status, status_occurrences[status]))


if __name__ == "__main__":
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8


def handle_interrupt(signal, frame):
    """
    handle interruption
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        match = regex.fullmatch(line)
        if (match):
            line_count += 1
            status = match.group(1)
            file_size += int(match.group(2))
            if status.isdecimal():
                status_occurrences[status] += 1

            if line_count % 10 == 0:
                print_stats()
finally:
    print_stats()
