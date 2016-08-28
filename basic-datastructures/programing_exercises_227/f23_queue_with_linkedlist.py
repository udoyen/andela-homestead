class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None
        self.lssize = 0

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item):
        self.lssize += 1
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def dequeue(self):
        current = self.head
        popvalue = None
        curpos = 0
        done = False
        lssize = self.size()
        if self.isEmpty():
            print("The linked list is empty")
        else:
            while current is not None and not done:
                curpos += 1
                if curpos == lssize - 1:
                    # This method is slower than that
                    # below it...
                    # self.remove(current.getNext().getData())
                    popvalue = current.getNext().getData()
                    current.setNext(None)
                    self.lssize -= 1
                    done = True
                else:
                    current = current.getNext()

            return popvalue


mylist = UnorderedList()
mylist.enqueue(50)
mylist.enqueue(23)
mylist.enqueue(21)
mylist.enqueue(20)

print(mylist.dequeue())



