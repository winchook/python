#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by winchoo
# 2018/9/18

#对event对象的解释：
# An event is a simple synchronization object;the event represents an internal flag,
#
# and threads can wait for the flag to be set, or set or clear the flag themselves.
#
#
# event = threading.Event()
#
# # a client thread can wait for the flag to be set
# event.wait()
#
# # a server thread can set or reset it
# event.set()
# event.clear()
#
#
# If the flag is set, the wait method doesn’t do anything.
# If the flag is cleared, wait will block until it becomes set again.
# Any number of threads may wait for the same event.

#for example
import threading,time
class Boss(threading.Thread):

    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        print(event.isSet())# 打印False
        event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        print(event.isSet())
        event.set()

class Worker(threading.Thread):
    def run(self):

        event.wait()#    一旦event被设定，等同于pass

        print("Worker：哎……命苦啊！")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker：OhYeah!")


if __name__=="__main__":
    event=threading.Event()


    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("ending.....")
