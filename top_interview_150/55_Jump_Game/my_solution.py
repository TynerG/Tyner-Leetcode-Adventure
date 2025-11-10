from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_dist = 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= min_dist:
                min_dist = 0

            min_dist += 1
            i -= 1

        return min_dist == 1