"""
Fixed version of buggy code.
Handles invalid inputs, division by zero, and logs all operations to a file.
"""

import datetime

LOG_FILE = "discussion06_log.txt"

def log_message(message):
    """Write a message with a timestamp to the log file."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

if __name__ == '__main__':
    keep_going = True
    while keep_going:
        try:
            num1 = int(input('Enter numerator >> '))
            num2 = int(input('Enter denominator >> '))
            if num2 == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")

            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            log_message(f"Success: {num1} / {num2} = {result}")

        except ValueError:
            print("❌ Please enter valid integers only.")
            log_message("Error: Invalid input (non-integer).")

        except ZeroDivisionError as e:
            print("❌ Cannot divide by zero.")
            log_message(f"Error: {e}")

        rerun = input('Keep going? [Y/n] >> ').strip().lower()
        while rerun not in ['y', 'n', '']:
            print("Please enter 'Y' or 'n'.")
            rerun = input('Keep going? [Y/n] >> ').strip().lower()

        if rerun == 'n':
            keep_going = False
            print("Goodbye!")
