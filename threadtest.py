import _thread
import threading
import time
import queue
# 为线程定义一个函数,使用_thread创建线程
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print('%s: %s' % (threadName, time.ctime(time.time())))
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(print_time, ('thread1', 2,))
#     _thread.start_new_thread(print_time, ('thread2', 4,))
# except:
#     print('Error:无法启动线程')
#
# while 1:
#     pass

# 使用threading创建线程
# exitFlag = 0
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print('开始线程：' + self.name)
#         print_time(self.name, self.counter, 5)
#         print('退出线程：' + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print('%s: %s' % (threadName, time.ctime(time.time())))
#         counter -= 1
# # 创建新线程
# thread1 = myThread(1, 'thread1', 1)
# thread2 = myThread(2, 'thread2', 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print('退出主线程')

# 线程同步
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print('开启线程：' + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print('%s:%s' % (threadName, time.ctime(time.time())))
#         counter -= 1
# threadLock = threading.Lock()
# threads = []
# # 创建新线程
# thread1 = myThread(1, 'thread1', 1)
# thread2 = myThread(2, 'thread2', 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print('退出主线程')

# 线程优先级队列
# exitFlag = 0
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print('开启线程：', self.name)
#         process_data(self.name, self.q)
#         print('退出线程：', self.name)
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print('%s processing %s' % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ['thread1', 'thread2', 'thread3']
# nameList = ['one', 'two', 'three', 'four', 'five']
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
# # 等待队列清空
# while not workQueue.empty():
#     pass
# # 通知线程是时候退出
# exitFlag = 1
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print('退出主线程')









