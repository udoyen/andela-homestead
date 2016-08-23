from distlib.compat import raw_input
from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 5
    prec["^"] = 4
    prec["*"] = 3
    prec["//"] = 3
    prec["%"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(int(opStack.pop()))
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "**":
        return op1 ** op2
    elif op == "%":
        return op1 % op2
    elif op == "//":
        return op1 // op2
    else:
        return op1 - op2


def simple_calculator():
    """
    Function to calculate simple
    mathematical problems
    :return:
    """
    try:
        math = raw_input("Please enter a math problem > : ")

        print(postfixEval(infixToPostfix(math)))
    except IOError:
        print("Error, can't read data")
    except StopIteration:
        print("Error, sequence iteration problem")
    except ZeroDivisionError:
        print("Error, zero division error")
    except ArithmeticError:
        print("Error, calculation error")
    except KeyboardInterrupt:
        print("Error, user keyboard interruption")
    except Exception:
        print("Error, unknown error")


simple_calculator()
