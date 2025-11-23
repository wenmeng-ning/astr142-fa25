'''
Demo of creating and managing multiple processes using the multiprocessing module.
'''
from multiprocessing import Process
import time
import os

def task(name, delay):
    print(f"[{os.getpid()}] Starting {name}")
    time.sleep(delay)
    print(f"[{os.getpid()}] Finished {name}")

if __name__ == "__main__":
    p1 = Process(target=task, args=("A", 2))
    p2 = Process(target=task, args=("B", 1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
