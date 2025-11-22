from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        idx_left = 0
        idx_right = 0
        num_zeros = 0

        max_len = 0
        while idx_right < len(nums):
            if nums[idx_right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[idx_left] == 0:
                    num_zeros -= 1

                idx_left += 1

            max_len = max(max_len, idx_right - idx_left + 1)

            idx_right += 1

        return max_len