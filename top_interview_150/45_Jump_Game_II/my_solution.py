from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        indexToJumps = dict()
        indexToJumps[len(nums) - 1] = 0

        i = len(nums) - 2
        while i >= 0:
            curr_min_jump = len(nums)
            for idx in indexToJumps:
                if nums[i] >= idx - i:
                    curr_min_jump = min(curr_min_jump, indexToJumps[idx] + 1)

            indexToJumps[i] = curr_min_jump
            i -= 1

        return indexToJumps[0]