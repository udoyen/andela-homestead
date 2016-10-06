from codecademy.grades.grades import *


def grades_average(grades):
    average = 0
    average = grades_sum(grades) / float(len(grades))
    return average

print(grades_average(grades))
