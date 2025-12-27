from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def comboBuilder(curr: List[int], curr_sum: int, curr_idx: int) -> None:
            if len(curr) == k:
                if curr_sum == n:
                    answers.append(curr[:])

                return

            for i in range(curr_idx, 10):
                potential_sum = curr_sum + i
                if potential_sum <= n:
                    curr.append(i)
                    comboBuilder(curr, potential_sum, i + 1)
                    curr.pop()

        answers = []
        comboBuilder([], 0, 1)
        return answers