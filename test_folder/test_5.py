def factorial(number):
    num = 0
    if number == 0:
        return 1
    num += 1
    print(num)
    return number * factorial(number-1)


factorial(5)
