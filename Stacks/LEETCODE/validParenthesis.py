
# todo: VALID PARENTHESIS (NEETCODE 150, PROBLEM NUMBER - 20, EASY)

# ? Here we are given a list of brackets opening and closing ones. We have to check if they are in the same order and return true if they are, else we have to return false. Say for example, [(]) -> This is false, but this is true -> ((([])))

# * So to solve this we use Stacks, and also the help of a hashmap(just to store the brackets). We first push the elements into the stack, and then later on we push the closing ones on the top, if the opening of that bracket exist in the previous node, we return true, else we return false.

# * Time Complexity - O(n)

# * Space Compelxity - O(n)

def validParenthesis(s: str) -> bool:
    stack = []
    # ! Here we are initializing a hashmap which contains the pair of brackets, the keys must be closing ones and the values must be opening ones
    closeBracket = {")": "(", "]": "[", "}": "{"}

    for c in s:
        # ! In this if statement, we are checking if the particular iterable is a closing bracket.
        if c in closeBracket:
            # ! Here we check if the stack has some value. AND, if the top most element is a key of the map, i.e a closing bracket
            if stack and stack[-1] == closeBracket[c]:
                # ! If yes, we just pop it
                stack.pop()
            else:
                print(False)
                return False
        else:
            # ! This is to add if it is an opening bracket
            stack.append(c)

    if not stack:
        print(True)
        return True
    else:
        print(False)
        return False


validParenthesis("(]")
