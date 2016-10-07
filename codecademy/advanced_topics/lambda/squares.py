squares = [x**2 for x in range(1, 11)]

print(list(filter(lambda x: 29 < x < 71, squares)))

