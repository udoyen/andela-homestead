# noinspection PyGlobalUndefined
# def g(num):
#     global r
#     dlen = len(str(num))
#     counter = 0
#     d = 10
#     data = int(num)
#     while counter < dlen:
#         r = data % d
#         data //= d
#         # data = (data - r) % d
#         counter += 1
#     return r
#
#
# print(g(93240))


def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i // placement
            print("i is ", i)
            print("placement is ", placement)
            print("tmp is ", tmp)
            print("tmp % RADIX is ", tmp % RADIX)
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    return aList


a = radixsort([18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2])
print(a)
