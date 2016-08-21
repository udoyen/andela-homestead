from pythonds.basic.queue import Queue

q = Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
q.dequeue()
q.dequeue()
print(q.size())
