# [start:stop(exclusive):stride]

even_squares = [i**2 for i in range(1, 11) if (i**2) % 2 == 0]

print(even_squares)

cubes_by_four = [c**3 for c in range(1, 11) if (c**3) % 4 == 0]

print(cubes_by_four)

l = [i ** 2 for i in range(1, 11)]

print(l[2:9:2])
