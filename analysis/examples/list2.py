##############################################################################
# Analysis of the logarithm below
# -------------------------------
# 1.) The three assignment statements = 3
# 2.) The nested iteration = n^2 and assignments = 3, so 3n^2
# 3.) The iteration = n, assignments 2, so 2n
# 4.) The last assignment 1
# Together T(n) => O(f(n)), will give T(n) = 3 + 3n^2 + 2n + 1
# => 3n^2 + 2n + 4
# with increase in 'n' we have n^2, hence O(n^2)



a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33

