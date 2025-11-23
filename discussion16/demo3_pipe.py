'''
Demo of using multiprocessing Pipe for inter-process communication.
'''
from multiprocessing import Process, Pipe

def child(conn):
    conn.send("Hello parent")
    print("Child sent message")
    conn.close()

def random_task():
    print('random task running')


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    p.join()
    p = Process(target=random_task, args=())
    p.start()
    p.join()
    print("Parent received:", parent_conn.recv())
