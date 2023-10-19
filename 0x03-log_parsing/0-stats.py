#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print("File size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.strip().split()
        if len(parts) != 7:
            continue
        ip, _, _, status_code, file_size = parts[0], parts[5], parts[6]
        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        total_file_size += file_size
        status_code_count[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except (ValueError, IndexError):
        continue
