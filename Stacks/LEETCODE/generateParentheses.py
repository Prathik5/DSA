
# todo: GENERATE PARENTHESES(NEETCODE 150, PROBLEM NUMBER - 22, MEDIUM)

# ? Here we are given an input and we have to generate parentheses of that input size. The parentheses must be in order, i.e if one is opened it must be closed. And the order must be maintained, closing number of parentheses must be equal to the opening ones. if n = 2, then ["(())" "()()"] are valid but [")("] this is not valid.

# * This problem is crazy as of now, as we have to solve this using backtracking and recursion, which I have not learnt yet. So, what we do is, we backtrack through the input and push the parentheses into a stack, and we perform it until the input is reached. I'll come back to this once I understand backtracking and recursion completely.

from inputs import parenthesesInput1, parenthesesInput2


def genParentheses(n: int) -> list[str]:
    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    print(res)
    return res


genParentheses(parenthesesInput1)
genParentheses(parenthesesInput2)
