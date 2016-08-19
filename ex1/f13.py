class LogicGate:
    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performgatelogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pina = None
        self.pinb = None

    def getpina(self):
        return self.pina

    def getpinb(self):
        return self.pinb

    def setpina(self, source):
        if self.pina == None:
            self.pina = int(input("Please enter value for pin 1: "))
            return source
        else:
            return self.pina

    def setpinb(self, source):
        if self.pinb == None:
            self.pinb = int(input("Please enter value for pin 2: "))
            return source
        else:
            return self.pinb


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performgatelogic(self):
        a = self.getpina()
        b = self.getpinb()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performgatelogic(self):

        a = self.getpina()
        b = self.getpinb()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def performgatelogic(self):
        if super(NandGate, self).performgatelogic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def performgatelogic(self):
        if super(NorGate, self).performgatelogic() == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    def performgatelogic(self):

        a = self.getpina()
        b = self.getpinb()
        if a == 1 and b == 1:
            return 0
        elif a == 0 and b == 0:
            return 0
        else:
            return 1


class XnorGate(XorGate):
    def performgatelogic(self):
        if super(XnorGate, self).performgatelogic() == 1:
            return 0
        else:
            return 1


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pina = None

    def getpina(self):
        return self.pina

    def setpin(self, source):
        if self.pina == None:
            self.pina = int(input("Please enter value for pin 1: "))
            return source
        else:
            return self.pina


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performgatelogic(self):
        # if the getPin is True i.e. '1'
        # return False i.e. '0'
        # or True otherwise
        if self.getpina():
            return 0
        else:
            return 1


class Connector:
    result = 0

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        if isinstance(fgate, BinaryGate):
            fgate.setpina(self)
            fgate.setpinb(self)
            fg = fgate.getOutput()
            # set the value of pin a in other
            # logic gate
            if isinstance(tgate, UnaryGate):
                # since the second gate is a not
                # change the fgate value
                if fg == 1:
                    result = 0
                else:
                    result = 1
            else:
                # set the state of the first
                # pin for second gate
                tgate.pina = fg
                tgate.setpinb(self)
                tgate.getOutput()

        else:
            fgate.setpin(self)
            # get output from fgate
            fg = fgate.getOutput()

            # set the value of pin a in other
            # logic gate
            if isinstance(tgate, UnaryGate):
                # since the second gate is a not
                # change the fgate value
                if fg == 1:
                    result = 1
                else:
                    result = 0
            else:
                # set the state of the first
                # pin for second gate
                tgate.pina = fg
                tgate.setpinb(self)
                tgate.getOutput()


def main():
    g1 = AndGate("G1")
    g2 = OrGate("G2")

    c1 = Connector(g1, g2)
    print(g2.getOutput())


main()
