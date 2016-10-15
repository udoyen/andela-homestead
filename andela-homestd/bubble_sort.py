# def shortBubbleSort(alist, num):
#     """ function to check result of number
#         of passes when using bubble sort"""
#     exchanges = True
#     passnum = len(alist) - 1
#     while num > 0 and exchanges:
#         exchanges = False
#         for i in range(num):
#             if alist[i] > alist[i + 1]:
#                 exchanges = True
#                 temp = alist[i]
#                 alist[i] = alist[i + 1]
#                 alist[i + 1] = temp
#         num -= 1
#
#
# alist = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
# shortBubbleSort(alist, 3)
# print(alist)


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
