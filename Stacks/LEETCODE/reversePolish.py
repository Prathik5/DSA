
# todo: EVALUATE EVALUATE POLISH NOTATION(NEETCODE 150, PROBLEM NUMBER - 150, MEDIUM)

# ? We are given an array in postfix notation, we have to operate on that and return the final answer

# * We can do this using Stacks. Here we create a stack, and keep on appending the value until we find an operator, once we find the operator, we pop the previously appended values and perform operations on them and put them back until we have gone through the array completely.

# *Time complexity - O(n)

# * Space Complexity - O(n)

from inputs import evalRPNInput


def evalRPN(tokens: list[str]) -> int:
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            # ! To round it down to 0, we do this
            stack.append(int(float(b / a)))
        else:
            stack.append(int(c))  # ! Don't forget to convert it into int
    print(stack[0])
    return stack[0]


evalRPN(evalRPNInput)
