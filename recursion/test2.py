def digitalSum(n):
    if n < 10:
        return n
    else:
        addme = digitalSum(n % 10)
        return addme + digitalSum(n // 10)


print(digitalSum(12345))


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

factorial(5)
