def purify(melist):
    # use this to avoid changing original copy of melist
    re = list(melist)
    chlist = melist
    for u in re:
        for t in range(1, u + 1, 2):
            if u == t:
                chlist.remove(u)

    print(chlist)

purify([1, 2, 7, 9])
