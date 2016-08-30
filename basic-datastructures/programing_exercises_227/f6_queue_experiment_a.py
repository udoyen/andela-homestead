##########################################################################################################
# Experiment to determine the differences between a list                                                 #
# implemented queue and the 'queue' ADT (abstract data type)                                             #
# Using Python's timer function                                                                          #
# Reading sources: http://pages.cs.wisc.edu/~vernon/cs367/notes/3.COMPLEXITY.html#youtry1                #
#                  https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt                  #
#                  http://www.greenteapress.com/thinkpython/html/thinkpython022.html                     #
##########################################################################################################

from pythonds import Queue
import time
import timeit


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

print(timeit.timeit('(m.enqueue(i) for i in range(1, 100001))', number=10000))

print(timeit.timeit('(q.enqueue(u) for u in range(1, 100001))', number=10000))


def py():
    if not q.isEmpty():
        while q.items:
            q.dequeue()


def me():
    if not m.items:
        while m.items:
            m.dequeue()

def k():
    pass


t1 = timeit.Timer("py()", "from __main__ import py")
print("Python Queue dequeue ", t1.timeit(number=1000), "milliseconds")

t1 = timeit.Timer("me()", "from __main__ import me")
print("MyQueue dequeue      ", t1.timeit(number=1000), "milliseconds")

t1 = timeit.Timer("k()", "from __main__ import k")
print("My k function call      ", t1.timeit(number=1000), "milliseconds")


# print(timeit.timeit('m.dequeue()', '(m.enqueue(i) for i in range(1, 100001))', number=10000))



#
# me()
#
# py()

#
# print("")
# print("----------------------")
# print("Enqueue Operations")
# print("----------------------")
# print("MyQueue Result 1: ",     exec_time)
# print("Python Queue Result 2: ", exec_time2)
# print("----------------------")
# print("Dequeue Operations")
# print("----------------------")
# print("MyQueue Result 1: ",      exec_time3)
# print("Python Queue Result 2: ", exec_time4)
