"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""
log_file = "log.txt"
def log_event(message):
    with open(log.txt, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Integer required.")
            log_event("Error: Non-integer input entered.")
if __name__ == '__main__':
	keep_going = True
	print("=====Fire====")
	while keep_going:
		num1 = int(input('Enter numerator >> '))
		num2 = int(input('Enter denominator >> '))

		 try:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
            log_event(f"Result: {num1} / {num2} = {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            log_event(f"Error: Division by zero. Inputs were {num1}, {num2}")

	 while True:
            rerun = input("Keep going? [Y/n] >> ").strip().lower() #I believe this will remove trailing numbers and round to the lowest number.
            if rerun in ["y", "yes", ""]:
                keep_going = True
                break
            elif rerun in ["n", "no"]:
                keep_going = False
                print("Goodbye!")
                break
            else:
                print("Please enter 'Y' or 'N'.")
		rerun = input('Keep going? [Y/n] >> ')


