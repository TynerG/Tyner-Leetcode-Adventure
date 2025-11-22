from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(num + sums[-1])

        return max(1 - min(sums), 1)