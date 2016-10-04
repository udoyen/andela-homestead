def is_prime(x):
    return x > 1 and all(x % i for i in range(2, x))


is_prime(2)
