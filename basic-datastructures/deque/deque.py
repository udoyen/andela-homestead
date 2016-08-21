from pythonds.basic.deque import Deque


d = Deque()
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront('True')
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
d.removeRear()
d.removeFront()
