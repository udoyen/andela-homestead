def count(sequence, item):
    i = None
    itemcount = 0
    if isinstance(item, list):
        if len(item) == 1:
            for i in sequence:
                for u in item:
                    if u == i:
                        itemcount += 1
        else:
            for i in range(len(item)):
                for u in sequence:
                    if item[i] == u:
                        itemcount += 1
    else:
        for i in range(len(sequence)):
            if item == sequence[i]:
                itemcount += 1
    return itemcount

count([1, 2, 3, 4, 4, 4], [4])
