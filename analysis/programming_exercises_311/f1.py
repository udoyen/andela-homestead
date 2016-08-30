def test1():
    l = []
    for i in range(1000):
        l = l + [i]
    for j in range(1, len(l) + 1, 100):
        return l.index(j)


def test2():
    l = []
    for i in range(1000):
        l.append(i)
    for j in range(1, len(l) + 1, 100):
        return l.index(j)


def test3():
    l = [i for i in range(1000)]
    for j in range(1, len(l) + 1, 100):
        return l.index(j)


def test4():
    l = list(range(1000))
    for j in range(1, len(l) + 1, 100):
        return l.index(j)
