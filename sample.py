# [5, 9, 4, 2, 8, 1]

# [10, 10, 9]


def g(A):
    if len(A) % 2 == 0:
        A = sorted(A)
        print(A)
        B = []
        for i in range(0, len(A) // 2):
            r1 = A.pop(0) + A.pop(len(A) - 1)
            B.append(r1)
        print(B)
    else:
        print("Please enter more values to make list len even")


g([5, 9, 4, 2, 8, 2, 1, 8, 11, 4])
