###############################################################
# Experiment to determine the differences between a list      #
# implemented queue and the 'queue' ADT (abstract data type)  #
# Using Python's timer function                               #
###############################################################
from pythonds import Queue
import time


class MyQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()


# Steps:
# 1) Enter 10 to five items in both 'MyQueue' and 'Queue'
# 2) This should be done from instance of the various classes
# 3) Check the number of steps that it takes to remove items from
#    these object instances.

m = MyQueue()
t1 = time.time()
for i in range(1, 50001):
    m.enqueue(i)
t2 = time.time()

exec_time = t2 - t1
print("Result 1: ", exec_time)
# m.dequeue()

t3 = time.time()
for u in range(1, 50001):
    q.enqueue(u)
t4 = time.time()

exec_time2 = t4 - t3
print("Result 2: ", exec_time2)

t5 = time.time()
if not q.isEmpty():
    while q.items:
        q.dequeue()
t6 = time.time()
exec_time3 = t6 - t5

t7 = time.time()
if not m.items:
    while m.items:
        m.dequeue()
t8 = time.time()

exec_time4 = t8 - t7
print("Dequeue Operations")

print("Result 1: ", exec_time3)
print("Result 1: ", exec_time4)
