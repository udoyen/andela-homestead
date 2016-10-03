def digit_sum(n):
    n2 = 0
    while n != 0:
        n2 += n % 10
        n //= 10
    print(n2)

digit_sum(1000)
