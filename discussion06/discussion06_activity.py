"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""

if __name__ == '__main__':
	keep_going = True
	while keep_going:
		### FIXME what happens if you enter something that isn't an int?
		num1 = int(input('Enter numerator >> '))
		num2 = int(input('Enter denominator >> '))
		### FIXME what happens if denom is 0?
		while num2 = 0:
			num2 = int(input('Demoninator cannot be 0, choose another number >>'))
		print(num1, '/', num2, '=', num1/num2)
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file
except ValueError:
print("Invalid number entered")
		
		
		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
		rerun = input('Keep going? [Y/n] >> ')
		if rerun not in ['Y', 'y']:
			return break


