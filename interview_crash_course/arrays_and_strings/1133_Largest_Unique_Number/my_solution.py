from collections import defaultdict
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1

        curr_max = -1
        for num in num_counts:
            if num_counts[num] == 1 and num > curr_max:
                curr_max = num

        return curr_max