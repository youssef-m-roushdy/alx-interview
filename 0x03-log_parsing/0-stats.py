#!/usr/bin/python3
"""
Script to read lines from stdin,
track file size and status occurrences,
and print statistics after every 10 lines
or when interrupted with CTRL + C.
"""
import sys
import signal


status_occurrences = {}
total_size = 0
line_count = 0


def print_stats():
    """
    Print the total file size and the count of each HTTP status code.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_occurrences.keys()):
        if status_occurrences[status] > 0:
            print("{}: {}".format(status, status_occurrences[status]))


def handle_interrupt(signal, frame):
    """
    Handle SIGINT (CTRL + C) by printing the stats and exiting the program.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


for line in sys.stdin:
    try:
        status = line.split(' ')[-2]
        total_size += int(line.split(' ')[-1])
        if status in status_occurrences:
            status_occurrences[status] += 1
        else:
            status_occurrences[status] = 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

print_stats()
