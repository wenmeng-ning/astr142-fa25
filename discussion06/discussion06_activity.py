"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""
import logging as log

log.basicConfig(filename="newfile.log", level=log.DEBUG,
                    format='%(asctime)s %(message)s',
                    filemode='w')

if __name__ == '__main__':
  keep_going = True
  while keep_going:
      try:
            log.info("Starting new cycle")
		### FIXME what happens if you enter something that isn't an int?
            num1 = int(input('Enter numerator >> '))
            num2 = int(input('Enter denominator >> '))
      except ValueError:
            log.error("Error: input was not an integer")
            print('Non-integer value input - shutting down')
        
		### FIXME what happens if denom is 0?
      if num2==0:
            log.error("Error: division by zero")
            exit("No division by zero allowed")
      else:
            print(num1, '/', num2, '=', num1/num2)
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file

		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
      rerun = input('Keep going? [Y/n] >> ')
      if rerun not in ['N', 'n', 'Y','y']:
            log.error("Invalid input")
            print("Error, input not 'y' or 'n', stopping process")
            keep_going = False
      elif rerun in ['N', 'n']:
            log.info("'No' option selected, stopping")
            keep_going = False
      elif rerun in ['Y', 'y']:
            log.info("'Yes' option selected, continuing")
            keep_going = True
