from typing import List

# improvements: no need to compute the average until return statement, the sum will suffice
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        idx_start = 1
        idx_end = k

        curr_avg = sum(nums[:k]) / k
        max_avg = curr_avg
        while idx_end < len(nums):
            curr_avg = (curr_avg * k + nums[idx_end] - nums[idx_start - 1]) / k
            max_avg = max(max_avg, curr_avg)
            idx_end += 1
            idx_start += 1

        return max_avg