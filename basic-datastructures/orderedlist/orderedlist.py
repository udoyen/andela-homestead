from xdg.Menu import sort


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


class OderedList:
    def __init__(self):
        self.head = None
        self.nodels = []
        self.lssize = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
            self.lssize += 1
            sort(self.nodels.insert(0, temp))
        else:
            temp.setNext(current)
            previous.setNext(temp)
            self.lssize += 1
            sort(self.nodels.insert(0, temp))

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

