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
        self.nodels = []

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        self.lssize += 1
        temp = Node(item)
        self.nodels.insert(0, temp)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        return self.lssize

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
            elif current.getNext() == None:
                print("Item not in linked list")
                return
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            self.lssize -= 1
        else:
            previous.setNext(current.getNext())
            self.nodels.remove(current.getNext())
            self.lssize -= 1

    def append(self, item):
        """
        Searches till the end of the
        linked list so it can append
        the given value or item
        :param item:
        :return:
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.getNext() == None:
                newitem = Node(item)
                current.setNext(newitem)
                self.lssize += 1
                self.nodels.append(newitem)
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
                    self.nodels.insert(pos, newitem)
                    self.lssize += 1
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
                if curpos == lssize - 1:
                    # This method is slower than that
                    # below it...
                    # self.remove(current.getNext().getData())
                    current.setNext(None)
                    self.lssize -= 1
                    self.nodels.pop()
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


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(80)
mylist.add(22)
print(mylist.size())
mylist.remove(33)
# print(mylist.index(31))
# print(mylist.index(22))
# print(UnorderedList.lssize())
# mylist.append(20)
# mylist.insert(1, 22)


