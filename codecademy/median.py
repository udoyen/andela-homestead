def median(melist):
    # create new list and sort it
    re = sorted(list(melist))
    if len(re) == 1:
        print(re[0])
    else:
        if len(re) % 2 == 0:
            m1 = (len(re) // 2) - 1
            m2 = m1 + 1
            m = (re[m1] + re[m2]) / (2.0)
            print(m)
        else:
            m = (len(re) // 2)
            print(re[m])


median([4, 5, 4])
