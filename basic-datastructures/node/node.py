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

    def add(self, item):
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

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getNext() == None:
                newitem = Node(item)
                current.setNext(newitem)
                found = True
            else:
                current = current.getNext()
        return found

    def insert(self, pos, item):
        # check if the list is empty
        # if it is then just call the add
        # method
        newitem = Node(item)
        done = False
        if self.size() == 0:
            self.add(newitem)
        else:
            current = self.head
            curpos = 0
            while current != None and not done:
                if pos == 1:
                    self.add(item)
                    done = True
                curpos += 1
                if curpos == pos - 1:
                    n = current.getNext()
                    newitem.setNext(n)
                    current.setNext(newitem)
                    done = True
                else:
                    current = current.getNext()

            return done

    def pop(self):
        current = self.head
        curpos = 0
        done = False
        lssize = self.size()
        if lssize == 0:
            print("The linked list is empty")
        else:
            while current != None and not done:
                curpos += 1
                print(current.getData())
                if curpos == lssize - 1:
                    # This method is slower than that
                    # below it...
                    # self.remove(current.getNext().getData())
                    current.setNext(None)
                    done = True
                else:
                    current = current.getNext()

            return done

    def index(self, item):
        curpos = 0
        found = False
        current = self.head
        if self.size() == 0:
            print("Linked list is empty!")
        else:
            while current != None and not found:
                curpos += 1
                if current.getData() == item:
                    found = True
                else:
                    current = current.getNext()

            return curpos

            pass


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(80)
mylist.add(22)
print(mylist.index(31))
print(mylist.index(22))
# mylist.append(20)
# mylist.insert(1, 22)


