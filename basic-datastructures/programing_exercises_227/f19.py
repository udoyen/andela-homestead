class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

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

    def __str__(self):
        return str(self.nodels)

    def add(self, item):
        self.lssize += 1
        temp = Node(item)
        self.nodels.insert(0, temp)
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
            self.nodels.remove(current.getNext())

    def append(self, item):
        """
        Searches till the end of the
        linked list so it can append
        the given value or item
        :param item:
        :return:
        """
        current = self.nodels[len(self.nodels) - 1]
        newitem = Node(item)
        current.setNext(newitem)
        self.lssize += 1
        self.nodels.append(newitem)

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
        elif current.getData() == item:
            curpos += 1
            return curpos
        else:
            while current != None and not found:
                curpos += 1
                if current.getData() == item:
                    found = True
                else:
                    current = current.getNext()

            return curpos

    def slice(self, start, stop):
        current = self.head
        revalue = True
        res = []
        currpos = 1
        if self.size() < stop < start or start < 1:
            print("Out of index error!")
            revalue = False
            return res
        else:
            if start == currpos and start == stop:
                current = current.getData()
                res.append(current)
                revalue = True
            else:
                revalue = True
                p = start - currpos
                newpos = 1
                for i in range(p):
                    newpos += 1
                    current = current.getNext()
                if stop - newpos == 1:
                    res.append(current.getData())
                else:
                    res.append(current.getData())
                    k = (stop - start) - 1
                    for e in range(0, k):
                        res.append(current.getNext())
                        if k > 1:
                            current = current.getNext()
        if revalue:
            return res


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(80)
mylist.add(22)
mylist.add(67)
# print(mylist.index(31))
# print(mylist.index(22))
# print(UnorderedList.lssize())
print(mylist.slice(5, 5))
# mylist.insert(1, 22)


