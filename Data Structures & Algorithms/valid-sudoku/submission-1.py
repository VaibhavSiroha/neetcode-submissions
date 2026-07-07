from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            seen = set()
            for x in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in seen:
                    return False
                seen.add(board[y][x])

        for x in range(9):
            seen = set()
            for y in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in seen:
                    return False
                seen.add(board[y][x])

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = box_row + i
                        col = box_col + j

                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

        return True