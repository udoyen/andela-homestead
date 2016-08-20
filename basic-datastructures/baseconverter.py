from pythonds.basic.stack import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        # or newString = newString + digits[remstack.pop()]
        newString = "{0}{1}".format(newString, digits[remstack.pop()])

    return newString


print(baseConverter(25, 2))
print(baseConverter(25, 16))
