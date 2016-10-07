movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

for key in movies:
    print(key, movies[key])

print("===================================")

for key, value in movies.items():
    print([(key, value)], end=' ')

# print("===================================")
#
# print(list(filter(lambda x: (movies[x], x), movies)))
#
# print("===================================")
#
# print([(key, value) for key, value in movies.items()])
