f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def minval(val):
    overallmin = val[0]
    for i in val:
        issmallest = True
        for j in val:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


def minval(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(minval(f))
