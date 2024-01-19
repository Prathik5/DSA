
# todo:  PASCALS TRIANGLE(STRIVER SDE SHEET, PROBLEM NUMBER - 118, EASY)

# ? We have to create a set of lists which is actually in a pascals triangle order

# * So, to solve this, we use arrays and two pointers(?). What we do is, we add 0's to both ends of the list that is being generated and then add the consecutive elements in order to create another list. Then we append this list to the original list.

# * Time Complexity - O(n^2)
# * Space complexity - O(n^2)

from inputs import PascalsTriangleInput


def PascalsTriangle(numRows: int) -> list[list[int]]:
    # ! Here we have our result list, we initialize it with 1, because we know that's the first element
    res = [[1]]

    for i in range(numRows - 1):  # ! Minus 1 because we already have the first element
        temp = [0] + res[-1] + [0]  # ! Here we are appending 0's on both sides
        row = []
        # ! creating list that is to be inserted. Plus one because the size of the list is gonna be one more than the previous list
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])

        res.append(row)  # ! Here we are appending the list

    print(res)
    return res


PascalsTriangle(PascalsTriangleInput)
