class Parent:
    # class variables
    pa = 0
    pb = 0
    pc = 0

    def __init__(self, n):
        # object variables
        self.name = n

    def getpinb(self):
        return Parent.pb

    def getpina(self):
        return Parent.pa

    def getpinc(self):
        return Parent.pc

    def setpin(self):
        Parent.pa = int(input("Please enter first pin: "))
        Parent.pb = int(input("Please enter second pin: "))
        Parent.pc = int(input("Please enter third pin: "))


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


class OutXorGate(XorGate):
    def __init__(self, n):
        XorGate.__init__(self, n)

    def performlogic(self):
        if super(OutXorGate, self).performlogic() == 0 and self.getpinc() == 0:
            return 0
        elif super(OutXorGate, self).performlogic() == 1 and self.getpinc() == 1:
            return 0
        else:
            return 1


class SecAndGate(XorGate):
    def __init__(self, n):
        XorGate.__init__(self, n)

    def performlogic(self):
        if super(SecAndGate, self).performlogic() == 1 and super(SecAndGate, self).getpinc() == 1:
            return 1
        else:
            return 0


class OutOrGate(AndGate, SecAndGate):
    def __init__(self, n):
        AndGate.__init__(self, n)
        SecAndGate.__init__(self, n)

    def performlogic(self):
        if super(OutOrGate, self).performlogic() == 0 and SecAndGate.performlogic(self) == 0:
            return 0
        else:
            return 1


x = OutXorGate("XOR")
a = OutOrGate("AND")
p = Parent("Parent")
p.setpin()
print("INPUTS                 OUTPUTS")
print("============================================")
print("A         B         CIN       COUT    S")
print('{0:1} {1:9} {2:10} {3:10} {4:5}'.format(p.getpina(), p.getpinb(),
                                               p.getpinc(), a.performlogic(), x.performlogic()))
