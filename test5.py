# coding=utf-8
from test4 import Crawler
from test6 import MySQLConnect
import threading
from time import ctime, sleep
conn_ = MySQLConnect()
# 设置开始进行爬取的id
now_aid = 1666500
now_aid -= 500


def func(i):
    global now_aid
    # per_crawl = 30000
    # store_count = 100
    # count = 0
    global conn_
    # 创建线程锁，避免IO操作报错
    mutex = threading.Lock()
    # for it in range(0, per_crawl / store_count):
    #     st = 209400+it*store_count+i*per_crawl
    #     ed = 209400+(it+1)*store_count+i*per_crawl
    #     worker[i].run(st, ed)
    #     p = worker[i].output('video')
    #     for pp in p:
    #         print pp
    #
    #     # 锁定
    #     if mutex.acquire(1):
    #         conn_.insert_video(p)
    #         # 释放
    #         it += 1
    #         count += len(p)
    #         mutex.release()
    while True:
        if mutex.acquire(1):
            try:
                now_aid += 500

                print '*'*50 + str(now_aid)

                worker[i].run(now_aid, now_aid + 499)
                p = worker[i].output('video')
                print '-'*20 + str(ctime()) + '-'*20

                conn_.insert_video(p)
                mutex.release()
            except Exception, e:
                print "ERROR -------->  " + e.message
        else:
            print 'X_X      Thread Died'
            break

worker = []
result = []
threads = []
for k in range(0, 8):
    worker.append(Crawler())
    threads.append(threading.Thread(target=func, args=(k,)))

if __name__ == '__main__':
    t = None
    for t in threads:
        # t.setDaemon(True)
        t.start()
        # 低频率IO，休眠一段时间减少冲突
        sleep(20)

    t.join()

exit(0)
