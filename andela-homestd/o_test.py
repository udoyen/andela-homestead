ele = [1, 1, 2, 3, 5, 5, 7, 8, 19, 10, 4, ]


# O(1) always execute in the same time
def isfirstelement(el):
    return el[0] is None


# O(N) performance will grow linearly and in
# direct proportion to the size of the input data set
def containsvalue(el, value):
    for i in el:
        if i == value:
            return True
    return False


# O(N^2)
# performance is directly proportinal
# to the square of the size of the input data
# set
def containsduplicates(el):
    outer = 0
    inner = 0
    while outer < el.count:
        while inner < el.count:
            # don't compare with self
            if outer == inner:
                continue
            if el[outer] == el[inner]:
                return True
            ++inner
        ++outer
    return False


# O(2^N)
# denotes an algorithm whose growth doubles with each
# addition to the input data set.
# The growth curve of an O(2^N) is exponential
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number + 2) + fibonacci(number - 1)


print(isfirstelement(ele[0]))
