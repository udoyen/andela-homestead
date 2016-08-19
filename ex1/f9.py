def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    # initializing variables for class
    def __init__(self, top, bottom):

        # check if entered fraction is an integer
        if isinstance(top, int) and isinstance(bottom, int):
            # reduce the given fractions to lowest term
            common = gcd(top, bottom)

            self.num = abs(top) // common
            self.den = abs(bottom) // common
        else:
            raise "Please only integers are allowed"

    # def __str__(self):
    #     return str(self.num) + "/" + str(self.den)

    # same as '__str__' but is unambiguous, while '__str__'
    # is for readability making things more understandable to
    # the reader
    def __repr__(self):
        return repr(self.num) + "/" + repr(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __radd__(self, other):
        """Implementation of tht __radd__
           function when __add__ won't
           fly
        """
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other):
        """
        Implementation of the '+='
        augmented function
        :param other:
        :return:
        """
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        v = Fraction(newnum, newden)

        return v

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        # common = gcd(newnum, newden)

        return Fraction(newnum, newden)

    def __ge__(self, other):
        newnum1 = self.num * other.den
        newnum2 = other.num * self.den

        if newnum1 > newnum2 or newnum1 == newnum2:
            return True
        else:
            return False

    def __le__(self, other):
        newnum1 = self.num * other.den
        newnum2 = other.num * self.den

        if newnum1 < newnum2 or newnum1 == newnum2:
            return True
        else:
            return False

    def __ne__(self, other):
        newnum1 = self.num * other.den
        newnum2 = other.num * self.den

        if newnum1 != newnum2:
            return True
        else:
            return False

    def getnum(self):
        return str(self.num)

    def getden(self):
        return str(self.den)


f1 = Fraction(1, 2)
f2 = Fraction(8, 10)
# f4 = Fraction(2, 10)
f3 = f1 + f2
# print(f1 != f2)
f1 += f2
print(repr(f1))


# print(gcd(3, 7))

