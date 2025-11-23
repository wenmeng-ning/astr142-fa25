'''
Demo of using Pool to run multiple processes in parallel.
'''
from multiprocessing import Pool
import math
import time

def factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    start = time.time()
    # nums = list(range(100))
    nums = list(range(10000))
    result = [factorial(n) for n in nums]
    print("Done in:", time.time() - start)
    with Pool(4) as pool:
        start = time.time()
        result = pool.map(factorial, nums)
        print("Done in:", time.time() - start)
