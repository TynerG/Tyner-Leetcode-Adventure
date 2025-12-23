from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(divisor: int) -> bool:
            return sum([ceil(x / divisor) for x in nums]) <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left