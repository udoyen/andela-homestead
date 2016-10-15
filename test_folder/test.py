import timeit

print(timeit.timeit('(list(reversed([2, 4, 6, 8, 10])))', number=1000000))

print(timeit.timeit('(sorted(list({4, 2, 6, 8, 10}), reverse=True))', number=1000000))

print(timeit.timeit('(list(range(10, 0, -2)))', number=1000000))

