def manipulate_data(num):
    # check for positive integers
    poscount = 0
    negcount = 0
    if isinstance(num, list):
        for i in num:
            if i >= 0:
                poscount += 1
            else:
                negcount += i
        return [poscount, negcount]
    else:
        return "Only lists allowed"


print(manipulate_data([-1, 2, 3, 6, -23, -12, 6, -6, -9]))
