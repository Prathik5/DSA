
# todo: CONTAINER WITH MOST WATER(NEETCODE 150, PROBLEM NUMBER - 11, MEDIUM)

# ? Here we are given a list of numbers, we have to calculate the max area between the two digits of the list item.

# * So here we use Two pointers to solve this problem. First we go through the array, and then we calculate the area between those two elements in the array. Later we store the sum in the resultant array, and keep checking with all the possible solutions and only update if the area is greater than already stored result.

# * Time complexity - O(n)

from inputs import mostwaterInput


def mostWater(mostwaterInput: list[int]) -> int:
    res = 0  # ! Initializing the result
    L, R = 0, len(mostwaterInput) - 1  # ! Assigning the pointers

    while L < R:
        # ! This is the formula to calculate the area of the water container
        area = (R - L) * min(mostwaterInput[L], mostwaterInput[R])
        res = max(res, area)  # ! Here we are updating the result

        if mostwaterInput[L] < mostwaterInput[R]:
            L += 1
        elif mostwaterInput[L] > mostwaterInput[R]:
            R -= 1
        else:  # ! This condition is if both the left pointer and the right pointer has the same number
            R -= 1
    print(res)
    return res


mostWater(mostwaterInput)
