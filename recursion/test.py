# def toStr(n, base):
#     convertString = "0123456789ABCDEF"
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n // base, base) + convertString[n % base]
#
#
# print(toStr(1453, 16))


# def rev(word):
#     l = list(word)
#     newls = []
#     if len(word) == 1:
#         return "".join(newls.append(word))
#     else:
#         r = l.pop()
#         newls.append(r)
#         return rev("".join(l))
#
# print(rev("abcd"))

def rev(word):
    l = list(word)
    for i in range(0, len(word)):
        for j in range(0, 1):
            l.insert(0, l.pop())
        l.append(l.pop())
        word = "".join(l)
    return rev(word)

print(rev("loop"))
