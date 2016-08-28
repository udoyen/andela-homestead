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
        return self.head == None

    def addRear(self, item):
        self.lssize += 1
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def removeRear(self):
        valremove = None
        done = False
        current = self.head
        while current is not None and not done:
            if self.size() == 1:
                valremove = current.getData()
                current = None
                self.head = current
                done = True
            else:
                valremove = current.getData()
                current = current.getNext()
                self.head = current
                done = True
        return valremove

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def removeFront(self):
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

    def addFront(self, item):
        current = self.head
        popvalue = None
        done = False
        if self.isEmpty():
            self.addRear(item)
        else:
            while current is not None and not done:
                if self.size() == 1:
                    current.setNext(item)
                    done = True
                else:
                    temp = Node(item)
                    current = current.getNext()
                    if current.getNext() is None:
                        current.setNext(temp)
                        current = current.getNext()
                        current.setNext(None)
                        done = True


mylist = UnorderedList()
mylist.addRear(50)
mylist.addRear(23)
mylist.addRear(21)
mylist.addRear(20)
mylist.addFront(12)

# print(mylist.removeFront())




