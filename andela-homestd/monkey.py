import random
import string

# produces random string of type ascii
# s = string.ascii_lowercase
#
#
# def generate():
#     """Generates random letters"""
#     # word creation
#     w1 = ''.join(random.sample(s, 8))
#     w2 = ''.join(random.sample(s, 2))
#     w3 = ''.join(random.sample(s, 2))
#     w4 = ''.join(random.sample(s, 1))
#     w5 = ''.join(random.sample(s, 6))
#
#     # join the randomly created words
#     fw = ''.join(w1 + ' ' + w2 + ' ' + w3 + ' ' + w4 + ' ' + w5)
#
#     # print(fw)
#
#     return fw
#
#
# def score():
#     """scorer function"""
#     goal = "methink it is a weasel"
#     mon = generate()
#     if mon == goal:
#         return '100%'
#     else:
#         return 'almost there'
#
#
# def callfunc():
#     count = 1000
#     while count < 1000:
#         score()
#     return print(score())

# print(random.randint(0, 9))
# print(random.randrange(1, 26))


# print(''.join(random.sample(s, 8)))
# print(''.join(random.sample(s, 2)))
# print(''.join(random.sample(s, 2)))
# print(''.join(random.sample(s, 4)))
# print(''.join(random.sample(s, 1)))
# print(''.join(random.sample(s, 6)))
# print(''.join(random.choice(s) for _ in range(3)))
# callfunc()


def generateone(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res += alphabet[random.randrange(27)]

    return res

# print(generateone(20))


def score(goal, teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            # add a score when ever a character in a
            # goal matches one in teststring
            numsame += 1
    return (numsame / len(goal)) * 100  # multiplication by 100 gives a better representation of the score


def main():

    goalstring = "methinks it is like a weasel"
    newstring = generateone(28)
    best = 0
    # both strings are being compared
    newscore = score(goalstring, newstring)
    count = 0

    while newscore < 100:
        count += 1
        if newscore > best:
            if count % 1000000 == 0:
                print(newscore, newstring)
                best = newscore
        newstring = generateone(28)
        newscore = score(goalstring, newstring)

        # print(newstring)

main()
