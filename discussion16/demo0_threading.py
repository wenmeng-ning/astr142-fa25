import threading
import math
import logging
import time

def cpu_bound_task(n=10000):
    count = 0
    for i in range(n):
        math.factorial(i)
        count += 1
    return count

def run_threads():

    threads = []
    for i in range(1):
        t = threading.Thread(target=cpu_bound_task, args=(10000,))
        threads.append(t)
        logging.info("Thread %s: starting", i)
        t.start() # start a thread

    for t in threads:
        t.join() #

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    start = time.time()
    cpu_bound_task(1)
    end = time.time()
    print("Single thread time:", end - start)
    thread_start = time.time()
    run_threads()
    thread_end = time.time()
    print("Threaded time:", thread_end - thread_start)
    # having more threads may reduce performance 
    # due to overhead from context switching, resource contention, etc
