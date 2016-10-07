languages = ["HTML", "JavaScript", "Python", "Ruby"]

for i in languages:
    if i == "Python":
        print(i)

print(list(filter(lambda x: x == "Python", languages)))


def me(x):
    return [i for i in x if i == "Python"]

print(me(languages))
