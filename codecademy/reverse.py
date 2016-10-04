def reverse(text):
    if len(text) == 1:
        return text
    else:
        last = ""
        for i in range(len(text) - 1, -1, -1):
            last += text[i]

        return last

print(reverse("abcd"))
