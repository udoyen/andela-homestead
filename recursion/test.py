def rev(word):
    if len(word) == 1:
        return word
    else:
        clip = rev(word[:-1])
        return rev(word[-1:]) + clip

print(rev("apple"))
