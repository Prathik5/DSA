
# todo: VALID SUDOKU PROBLEM(NEETCODE 150, PROBLEM NUMBER - 36, MEDIUM)

from collections import defaultdict
from inputs import validSudokuInput


def ValidSudoku(board: list[list[int]]):
    cols = defaultdict(set)  # ! Here we are initializing a hashSET of columns
    rows = defaultdict(set)  # ! Initializing a hashSET of rows
    squares = defaultdict(set)  # ! HashSET for the 3 * 3 grid

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":  # ! This is for the condition where the block is empty
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):  # ! Here we are checking if the element is already in any row or column or grid
                print("False")
                return False

    #! If there is no element present, we will add that element in this respective position.

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    print("True")
    return True


ValidSudoku(validSudokuInput)
