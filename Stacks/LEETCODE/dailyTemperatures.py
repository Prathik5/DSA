
# todo: DAILY TEMPERATURES (NEETDCODE 150, PROBLEM NUMBER - 739, MEDIUM)

# ? Here we are given an array of daily temperatures, we have to return an array, which has elements in such a way that we get to know that where has the next greater temperature occurred. Like if the given array is [73, 74, 75, 71, 69, 72, 76, 73] we have to return [1, 1, 4, 2, 1, 1, 0, 0]  i.e the next greater temp of 73 has occurred in next position, for 73 it's again next, for 75 it is after 4 positions etc. etc. If there is no greater element, then store 0.

# * So, to solve this problem we have to return an array after subtracting the index. To solve this we will have to use enumerate method. That's the first intuition. We can use monotonic stack to traverse through the array. The monotonic stack stores the array in descending order and pops out the unwanted ones. We just store the difference in the resultant stack

# * Time complexity - O(1)

# * Space complexity - O(n)

from inputs import dailyTempInput1, dailyTempInput2


def dailyTemp(temperatures: list[int]) -> list[int]:
    # ! We initialize it with 0 initially, because if we don't find any greater value we don't append anything to it
    res = [0] * len(temperatures)
    stack = []  # ! Values here are stored in pairs: temperature and index

    for i, t in enumerate(temperatures):
        # ! Here we are checking if the stack has any values AND if the current temperature is actually greater than the temperature in the stack already (stack[-1][0] means the the top position check for temperature, as the values are in pairs)
        while stack and t > stack[-1][0]:
            # ! If the current temperature is greater, then we pop the element in the monotonic stack
            stackT, stackInd = stack.pop()
            # ! This gives us the number of days to find the greater temperature, and we add it into the same index in the result, if there is nothing to add, then it is already a 0
            res[stackInd] = (i - stackInd)

# ? PS. If the temperature is not greater, we just leave the index with 0 as it is

        stack.append([t, i])
    print(res)
    return res


dailyTemp(dailyTempInput1)
dailyTemp(dailyTempInput2)
