'''
Demo of how tasks are distributed among worker processes in a multiprocessing Pool.
Look at the process IDs in the logging output to see which process handles which task.
'''
import logging
import multiprocessing
from multiprocessing import Pool
import math
import numpy as np


logger = multiprocessing.get_logger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(process)d - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def factorial(x: int):
    pid = multiprocessing.current_process().pid
    logger.info(f"Calculating factorial of {x} in process {pid}") 
    return math.factorial(x)

if __name__ == "__main__":
    size = int(1e4)
    numbers = np.arange(size) + 1

    numberOfWorkers = 3  # number of worker processes
    pool = Pool(processes=numberOfWorkers) # create a pool of worker processes
    results = pool.map(factorial, numbers) # distribute the work among the workers

    print("Done")