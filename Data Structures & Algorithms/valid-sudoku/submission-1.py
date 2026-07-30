from collections import defaultdict
from typing import Dict, List
class Solution:  # 1 error: check if a tuple is inside a list of list is not valid (need to be a list instead of tuple) # 42 minutes
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check if valid with three things (rules)
          1. Loop through the first row and check all columns are valid.
          2. Loop through the first column and check all rows are valid.
          3. Check every 3x3 sub-box if it is valid.
        Valid conditions:
         1. No duplicate integer for the row/column
         2. Ignore dots.

        """
        def is_valid_series(series: List[int]) -> bool:
            """Check if a certain column/row is valid"""
            d_freq: Dict[int, int] = defaultdict(int)
            for index in range(len(series)):
                number = series[index]
                if number == ".":
                    continue
                else:
                    d_freq[number] += 1
                if d_freq[number] > 1:
                    return False
            return True

        def get_neighbours(row_ind: int, col_ind: int) -> List[int]:
            delta_positions: List[List[int]] = [ # row_delta, col_delta
                [-1, -1], [0, -1], [1, -1], # first column of 3x3
                [-1, 0], [0, 0], [1, 0], # second column
                [-1, 1], [0, 1], [1, 1]
            ]
            numbers: List[int] = []
            for delta_row, delta_col in delta_positions:
                number = board[row_ind + delta_row][col_ind + delta_col]
                if number == ".":
                    continue
                numbers.append(number)
            return numbers

        center_subboxes: List[List[int]] = [[r, c] for c in [1, 4, 7] for r in [1, 4, 7]]
        row_checked = set()
        col_checked = set()
        for row_ind in range(len(board)):
            for col_ind in range(len(board[row_ind])):
                if [row_ind, col_ind] in center_subboxes: # check subboxes
                    numbers = get_neighbours(row_ind, col_ind)
                    if len(numbers) != len(set(numbers)):
                        return False
                # retrieve all values in row
                if row_ind not in row_checked:
                    row_checked.add(row_ind)
                    if not is_valid_series(board[row_ind]):
                        return False
                # retrieve all values in column
                if col_ind not in col_checked:
                    col_checked.add(col_ind)
                    if not is_valid_series([r[col_ind] for r in board]):
                        return False
        return True

