from math import inf
from typing import List


class Solution:
    #     # top-down
    #     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #         def min_sum(r: int, c: int) -> int:
    #             if r == n - 1:
    #                 return matrix[r][c]

    #             if (r, c) in memo:
    #                 return memo[(r, c)]

    #             curr_min_sum = inf
    #             for dr, dc in [(1, -1), (1, 0), (1, 1)]:
    #                 new_r = r + dr
    #                 new_c = c + dc
    #                 if 0 <= new_r < n and 0 <= new_c < n:
    #                     curr_min_sum = min(curr_min_sum, min_sum(new_r, new_c))

    #             curr_min_sum += matrix[r][c]
    #             memo[(r, c)] = curr_min_sum
    #             return curr_min_sum

    #         n = len(matrix)
    #         memo = {}
    #         result_min_sum = inf
    #         for i in range(n):
    #             result_min_sum = min(result_min_sum, min_sum(0, i))
    #         return result_min_sum

    # bottom-up
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        row_below = matrix[-1]
        for r in range(n - 2, -1, -1):
            curr_row = [0] * n
            for c in range(n):
                curr_min_sum = inf
                for dc in [-1, 0, 1]:
                    new_c = c + dc
                    if 0 <= new_c < n:
                        curr_min_sum = min(curr_min_sum, row_below[new_c])

                curr_row[c] = curr_min_sum + matrix[r][c]
            row_below = curr_row

        return min(row_below)