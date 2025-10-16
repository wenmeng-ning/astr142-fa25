import logging

# Configure logging
logging.basicConfig(
    filename='calc.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_int(prompt):
    """Safely get an integer from user input."""
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            logging.error(f"Invalid integer input: {val}")
            print("Invalid input. Please enter an integer.")

def get_nonzero_denominator(prompt):
    """Get a non-zero integer for denominator."""
    while True:
        denom = get_int(prompt)
        if denom == 0:
            logging.error("Attempted division by zero.")
            print("Denominator cannot be zero.")
        else:
            return denom

def ask_rerun():
    """Ask the user if they want to keep going."""
    while True:
        ans = input('Keep going? [Y/n] >> ').strip().lower()
        if ans in ['', 'y']:
            return True
        elif ans == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == '__main__':
    keep_going = True
    while keep_going:
        num1 = get_int('Enter numerator >> ')
        num2 = get_nonzero_denominator('Enter denominator >> ')

        try:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            logging.info(f"Computed: {num1} / {num2} = {result}")
        except Exception as e:
            logging.exception(f"Unexpected error during computation: {e}")
            print("An unexpected error occurred.")

        keep_going = ask_rerun()
