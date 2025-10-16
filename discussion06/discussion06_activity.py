"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""

if __name__ == '__main__':
	keep_going = True
	while keep_going:
		### FIXME what happens if you enter something that isn't an int?
        input1 = input('Enter numerator >> ')
        input2 = input('Enter denominator >> ')
        while input1 is not int:
            input1 = int(input('Please enter an integer for the numerator: >> '))
        while input2 is not int:
            input2 = int(input('Please enter an integer for the denominator: >> '))
        
        num1 = int(input1)
        num2 = int(input2)
        
		### FIXME what happens if denom is 0?
        if num2 == 0:
            print('undefined')
		else:
            print(num1, '/', num2, '=', num1/num2)
            
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file

		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
		rerun = input('Keep going? [Y/n] >> ')
		if rerun not in ['Y', 'y']:
			keep_going = False
