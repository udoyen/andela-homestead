from codecademy.grades.grades_average import *


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

# print(grades_variance(grades))
