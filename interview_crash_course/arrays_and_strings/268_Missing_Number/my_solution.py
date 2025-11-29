from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict_1 = set(nums)

        for i in range(len(nums) + 1):
            if i not in dict_1:
                return i
