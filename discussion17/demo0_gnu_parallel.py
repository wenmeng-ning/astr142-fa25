import sys
import os

print(f'Executing script {sys.argv[1]} at PID {os.getpid()}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python demo0_gnu_parallel.py <number>")
        sys.exit(1)

