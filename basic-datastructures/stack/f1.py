from pythonds.basic.stack import Stack

m = Stack()


# def revstring(mystr):
#     g = list()
#
#     v = list(mystr)
#
#     for i in v:
#         m.push(i)
#     while not m.isEmpty():
#         g.append(m.peek())
#         m.pop()
#     print(''.join(g))

def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)

    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr + myStack.pop()

    return revstr


revstring('george')
