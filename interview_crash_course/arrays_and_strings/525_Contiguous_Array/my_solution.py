from typing import List

# note: it was hard to find the pattern that if the counter becomes a same value as before,
# it contains the same number of 1s and 0s.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_to_idx = dict()
        count_to_idx[0] = -1
        counter = 0

        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                counter -= 1

            if counter in count_to_idx:
                max_len = max(max_len, i - count_to_idx[counter])
            else:
                count_to_idx[counter] = i

        return max_len
