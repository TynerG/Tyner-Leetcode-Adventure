from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        idx_start = 1
        idx_end = k

        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        while idx_end < len(nums):
            curr_sum = curr_sum + nums[idx_end] - nums[idx_start - 1]
            max_sum = max(max_sum, curr_sum)
            idx_end += 1
            idx_start += 1

        return max_sum / k