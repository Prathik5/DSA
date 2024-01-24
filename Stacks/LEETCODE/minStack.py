
# todo: MIN STACK(NEETCODE 150, PROBLEM NUMBER - 155, MEDIUM)

# ? Here we have to design a stack that supports PUSH, POP, GETMIN, TOP function in O(1) time, i.e constant time

# * So, to solve this, we will have to use another stack where we will store the minimum values, so as to perform GETMIN function. Rest all functions already happen in O(1) time

# * Time Complexity - O(1)

# * Space Complexity - O(n)...as we will create another stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # ! Here we are taking the minimum of the existing minimum, and the new value from the input, and store the most minimum until that point
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def getMin(self) -> int:
        print(self.minStack[-1])
        return self.minStack[-1]

    def top(self) -> int:
        print(self.stack[-1])
        return self.stack[-1]


obj = MinStack()
obj.push(10)
obj.push(20)
obj.push(30)

obj.pop()

param3 = obj.top()
param4 = obj.getMin()
