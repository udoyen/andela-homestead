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

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def pop(self):
        current = self.head
        done = False
        valcurr = None
        if self.isEmpty():
            print("The linked list is empty")
        else:
            while current != None and not done:
                valcurr = current.getData()
                current = current.getNext()
                self.head = current
                done = True
            return valcurr

    def peek(self):
        current = self.head
        peekvalue = current.getData()
        return peekvalue


mylist = UnorderedList()
mylist.push(11)
mylist.push(10)
mylist.push(20)
mylist.push(30)

print(mylist.pop())
print(mylist.size())
