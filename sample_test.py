g = [1, 4, 4, 10, 12, 9, 0, 45]


def my_sort1(melist):
    """using sorted() method, which returns
    sorted list"""
    r1 = sorted(list(melist))
    r2 = []
    for i in range(len(r1) // 2):
        r2.append(r1.pop(0) + r1.pop(len(r1) - 1))
    print(r2)


def my_sort2(melist):
    """sort using sort() method"""
    melist.sort()
    r2 = []
    for i in range(len(melist) // 2):
        r2.append(melist.pop(0) + melist.pop(len(melist) - 1))
    print(r2)


my_sort2(g)
