#!/usr/bin/python3
import sys
import signal

# Initialize variables to keep track of metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print statistics
def print_msg(dict_sc, total_file_size):
    """
    Method to print the file size and status code counts.

    Args:
        dict_sc (dict): A dictionary with status codes as keys and their counts as values.
        total_file_size (int): The total file size.
    """
    print("File size:", total_file_size)
    for code in sorted(dict_sc.keys()):
        if dict_sc[code] > 0:
            print(f"{code}: {dict_sc[code]}")

# Function to handle Ctrl+C
def signal_handler(signal, frame):
    """
    Signal handler for Ctrl+C. It prints the statistics and exits.

    Args:
        signal: The signal being handled.
        frame: The current stack frame.
    """
    print_msg(status_code_count, total_file_size)
    sys.exit(0)

# Register the Ctrl+C signal handler
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
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
            print_msg(status_code_count, total_file_size)

    except (ValueError, IndexError):
        # Ignore lines that don't match the expected format
        continue
