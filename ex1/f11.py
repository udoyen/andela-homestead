
class Parent:
    # class variables
    pa = 0
    pb = 0

    def __init__(self, n):
        # object variables
        self.name = n

    def getpinb(self):
        return Parent.pb

    def getpina(self):
        return Parent.pa

    def setpin(self):
        Parent.pa = int(input("Please enter first pin: "))
        Parent.pb = int(input("Please enter second pin: "))


class XorGate(Parent):
    def __init__(self, n):
        Parent.__init__(self, n)

    def performlogic(self):
        a = self.getpina()
        b = self.getpinb()
        if a == 1 and b == 1:
            return 0
        elif a == 0 and b == 0:
            return 0
        else:
            return 1


class AndGate(Parent):
    def __init__(self, n):
        Parent.__init__(self, n)

    def performlogic(self):
        a = self.getpina()
        b = self.getpinb()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

x = XorGate("XOR")
a = AndGate("AND")
p = Parent("Parent")
p.setpin()
print("INPUTS                 OUTPUTS")
print("====================================")
print("A         B         SUM       CARRY")
print('{0:1} {1:9} {2:10} {3:10}'.format(p.getpina(), p.getpinb(), x.performlogic(), a.performlogic()))

