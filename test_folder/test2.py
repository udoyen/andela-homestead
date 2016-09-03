import enchant
from distlib.compat import raw_input

d = enchant.Dict("en_US")

u_input = raw_input("Please enter an english word: ")

if d.check(u_input):
    print(u_input[1:] + u_input[0] + 'ay')
else:
    print("Word entered is not a valid english word")
