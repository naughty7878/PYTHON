import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    # 构造方法
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name

    # 线程在此方法中定义要执行的代码
    def run(self):
        print("开始线程：" + self.name)
        process_data(self.name)
        print("结束线程：" + self.name)


def process_data(threadName):
    while not exitFlag:
        # 获取锁
        queueLock.acquire()
        if not workQueue.empty():
            data = workQueue.get()
            print("%s processing %s" % (threadName, data))
        # 释放锁
        queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
# 共享锁
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadId, tName)
    thread.start()
    threads.append(thread)
    threadId += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

print("退出主线程")
