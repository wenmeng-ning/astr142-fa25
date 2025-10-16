"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""

if __name__ == '__main__':
	keep_going = True
	while keep_going:
		try:### FIXME what happens if you enter something that isn't an int?
			num1 = int(input('Enter numerator >> '))
			num2 = int(input('Enter denominator >> '))
		except ValueError:
			print("Invalide value input")
			break
		### FIXME what happens if denom is 0?
		try:
			print(num1, '/', num2, '=', num1/num2)
		except ZeroDivisionError:
			print("Division by 0 not allowed")
			break
			
		
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file

		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
		
		rerun = input('Keep going? [Y/n] >> ')
		while (rerun != 'Y' or rerun != 'y' or rerun != 'n' or rerun != 'N'):
			print("Enter accepted value:")
			rerun = input('Keep going? [Y/n] >> ')
			
		if rerun not in ['Y', 'y']:
			keep_going = False

