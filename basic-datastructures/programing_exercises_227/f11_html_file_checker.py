from pythonds.basic.stack import Stack
import re


def parChecker(tagname):
    right = Stack()
    balanced = True
    # get list of start tags
    lefttoken = re.findall(r"(<[\w']+>)", tagname)
    # get list of end tags
    rightoken = re.findall(r"(</[\w']+>)", tagname)

    for j in rightoken:
        right.push(j)

    while not right.isEmpty() and balanced:
        if len(lefttoken) == len(rightoken):
            s = list(right.pop())
            for m in s:
                if m == "/":
                    s.remove(m)
                    neword = "".join(s)
                    if neword in lefttoken:
                        balanced = True
                    else:
                        balanced = False
        else:
            balanced = False
    if balanced:
        return True
    else:
        return False


parChecker("<html><head><title>Tony's Blog</title></head><body><div>Help is here!</div>"
           "<h1>Hello, World</h1></body></html>")
