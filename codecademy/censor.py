def censor(text, word):
    text = list(text.split(' '))
    pos = 0
    for t in text:
        star = ""
        if word == t:
            for i in range(len(word)):
                star += '*'
            text[pos] = star
        pos += 1
    return " ".join(text)

censor("this hack is wack hack", "hack")
