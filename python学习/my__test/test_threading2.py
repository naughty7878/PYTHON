import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    # 构造方法
    def __init__(self, threadId, name, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay

    # 线程在此方法中定义要执行的代码
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print("结束线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            print("退出当前%s线程" % threadName)
            exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
