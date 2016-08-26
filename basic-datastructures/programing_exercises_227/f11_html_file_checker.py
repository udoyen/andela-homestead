from pythonds.basic.deque import Deque
import re


def parChecker(tagname):
    s = Deque()
    succount = 0
    balance = False
    token = re.findall(r"(<[</[\w']+>)", tagname)
    for i in token:
        s.addFront(i)
    items = s.size()
    it = 0
    while not s.isEmpty() and not balance:
        if it < items // 2:
            f2 = list(s.removeFront())
            f1 = list(s.removeRear())
            for i in f1:
                for j in f2:
                    if j not in f1 and j == '/':
                        f2.remove(j)
                        if set(f2) & set(f1):
                            succount += 1
                            if succount == items // 2:
                                balance = True
                            else:
                                print("False")
                    else:
                        balance = False
            it += 1
    return False


parChecker("<html><head><title></title></head></html>")
