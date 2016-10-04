def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    l = list(text)
    for v in vowels:
        for i in l:
            if v in l:
                l.remove(v)
    return "".join(l)

anti_vowel('Hey look Words!')
