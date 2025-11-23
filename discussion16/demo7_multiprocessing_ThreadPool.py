'''
Demo of using ThreadPool to create multiple threads to run CPU-bound tasks.
'''
from multiprocessing import pool
import time
import math

def job(n: int):
    return math.factorial(n)

tasks = [int(100 + x) for x in range(1000)]

for i in range(1,5):
    start_time=time.time()
    with pool.ThreadPool(i) as pooli:
        outs = pooli.map(job, tasks)
    print(f'Threads={i} finished in time {time.time() - start_time}')

# observe the time taken as we increase the number of threads
# for CPU-bound tasks, more threads may not lead to better performance
