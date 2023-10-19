#!/usr/bin/python3
import sys
import signal

# Initialize variables to keep track of metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print statistics
def print_statistics():
    print("File size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

# Function to handle Ctrl+C
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 8:
            continue

        ip, _, _, _, status_code, file_size = parts[0], parts[3], parts[6], parts[5], parts[7]
        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except (ValueError, IndexError):
        # Ignore lines that don't match the expected format
        continue

# Print the final statistics
print_statistics()
