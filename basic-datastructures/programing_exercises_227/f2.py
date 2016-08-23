from pythonds.basic.stack import Stack


def postfixEval(postfixExpr):
    try:
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
    except IOError:
        print("Error, can't read data")
    except StopIteration:
        print("Error, sequence iteration problem")
    except:
        print("Error, unknown error")


def doMath(op, op1, op2):
    try:
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

    except IOError:
        print("Error, can't read data")
    except:
        print("Error, unknown error")


print(postfixEval('3 8 6 2 - - 4 5 + / +'))
