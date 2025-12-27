from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def intBuilder(curr: int) -> None:
            if curr >= 10 ** (n - 1):
                answers.append(curr)
                return

            last_digit = curr % 10
            potential_new_digits = {last_digit + k, last_digit - k}
            for new_digit in potential_new_digits:
                if 0 <= new_digit < 10:
                    curr = curr * 10 + new_digit
                    intBuilder(curr)
                    curr = curr // 10

        answers = []
        for i in range(1, 10):
            intBuilder(i)
        return answers