# wordlist = ['cat', 'dog', 'rabbit']
#
# letterlist = []
#
# for aword in wordlist:
#     for aletter in aword:
#         if aletter not in letterlist:
#             letterlist.append(aletter)
#
# print(letterlist)

wordlist = ['cat', 'dog', 'rabbit']
#
letterlist = []
#
print([letterlist.append(aletter) for aword in wordlist for aletter in aword if aletter not in letterlist])

print("".join(['cat', 'dog', 'rabbit']))
print([ch for ch in "".join(['cat', 'dog', 'rabbit'])])
print([word[i] for word in ['cat', 'dog', 'rabbit'] for i in range(len(word))])
print(list(set([word[i] for word in ['cat', 'dog', 'rabbit'] for i in range(len(word))])))

