def remove_duplicates(melist):
    re = list(melist)
    p = []
    for i in re:
        if i not in p:
            p.append(i)
    print(p)


remove_duplicates([1, 1, 2, 2, 9, 9, 10, 11, 11, 11, 12, 12])
