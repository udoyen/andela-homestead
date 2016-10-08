g = [1, 4, 4, 10, 12, 9, 0, 45]


def my_sort(melist):
    r1 = sorted(list(melist))
    r2 = []
    for i in range(len(r1) // 2):
        r2.append(r1.pop(0) + r1.pop(len(r1) - 1))
    print(r2)

my_sort(g)
