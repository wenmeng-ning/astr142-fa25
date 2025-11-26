'''
Demo of using multiprocessing Manager to create shared objects between processes.
'''
from multiprocessing import Process, Manager

def update_dict(d):
    d['count'] += 1

if __name__ == '__main__':
    with Manager() as manager:
        shared_dict = manager.dict(count=0)

        processes = [Process(target=update_dict, args=(shared_dict,)) for _ in range(5)]

        for p in processes:
            p.start()
        for p in processes:
            p.join()

        print(shared_dict)
