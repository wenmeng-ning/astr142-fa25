"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""
import logging as log

log.basicConfig(
    filename='logger.txt',
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
if __name__ == '__main__':
	keep_going = True
	while keep_going:
		### FIXME what happens if you enter something that isn't an int?
		checker = False
		while checker == False:
			try:
				num1 = int(input('Enter numerator >> '))
				num2 = int(input('Enter denominator >> '))
				if num2 != 0:
					checker = True
				else:
					log.error("denominator = 0, try again")
					print("Please enter proper denominator")
					continue
			except:
				log.error("Input wasn't 2 numbers as required, try again")
				print("Please input 2 numbers")
				continue
	
		print(num1, '/', num2, '=', num1/num2)
		res= num1/num2
		log.info(f"Computed the fraction successfully, {num1} / {num2} = {res} ")
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file

		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
		chk = True
		options = ['Y','y','n','N']
		while chk == True:
			rerun = input('Keep going? [Y/n] >> ')
			if rerun in options:
				if rerun not in ['Y', 'y']:
					keep_going = False
					chk = False
				else:
					chk = False
			else:
				log.error("Invalid input, please type y/n ")
				print("Invalid input, please type y/n")
				continue

