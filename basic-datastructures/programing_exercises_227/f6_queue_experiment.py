###############################################################
# Experiment to determine the differences between a list      #
# implemented queue and the 'queue' ADT (abstract data object)#
###############################################################
from pythonds import Queue


class MyQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            while self.items:
                self.items.pop()
        return

    def size(self):
        return len(self.items)


q = Queue()


# Steps:
# 1) Enter 10 to five items in both 'MyQueue' and 'Queue'
# 2) This should be done from instance of the various classes
# 3) Check the number of steps that it takes to remove items from
#    these object instances.

m = MyQueue()
for i in range(1, 51):
    m.enqueue(i)

m.dequeue()

for u in range(1, 51):
    q.enqueue(u)

if not q.isEmpty():
    while q.items:
        q.dequeue()


