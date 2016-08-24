from pythonds.basic.queue import Queue
import random


def hotPotato(namelist):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        # randomize the number of circles
        d = random.randrange(1, 4)
        for i in range(d):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


for i in range(1, 20):
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"]))

