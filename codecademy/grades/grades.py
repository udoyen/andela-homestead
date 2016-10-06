from sys import stdout

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    stdout.write("Grades ")
    for i in grades:
        stdout.write(str(i) + ' ')


def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total

print_grades(grades)

# print(grades_sum(grades))
