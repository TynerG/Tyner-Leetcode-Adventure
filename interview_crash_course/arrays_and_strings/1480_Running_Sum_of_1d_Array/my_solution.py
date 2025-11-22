from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_sum = [nums[0]]
        for num in nums[1:]:
            nums_sum.append(nums_sum[-1] + num)

        return nums_sum
