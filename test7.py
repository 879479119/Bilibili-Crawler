# coding=utf-8
import threading
from time import ctime, sleep

p = 0


def music():
    global p
    for k in range(10):
        print type(mutex)
        if mutex.acquire():
            p += 1
            # sleep(1)
            k += 1
            print p
            # 释放
            mutex.release()


mutex = threading.Lock()
threads = []
for i in range(0, 10):
    threads.append(threading.Thread(target=music, args=()))

if __name__ == '__main__':
    t = None
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
