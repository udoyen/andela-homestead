from codecademy.grades.standard_devaition import *


def information():
    print_grades(grades)
    stdout.write("Grade Total " + grades_sum(grades))
    stdout.write("Grades Average " + grades_average(grades))
    stdout.write("Variance " + grades_variance(grades))
    stdout.write("Deviation " + grades_std_deviation(variance))


information()
