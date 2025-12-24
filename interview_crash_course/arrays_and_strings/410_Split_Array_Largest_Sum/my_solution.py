from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(max_val: int) -> bool:
            curr_chunk_sum = 0
            num_chunks = 0
            i = 0
            while i < len(nums):
                curr_chunk_sum += nums[i]
                if curr_chunk_sum > max_val:
                    num_chunks += 1
                    curr_chunk_sum = 0

                    if num_chunks == k:
                        return False

                    continue

                i += 1

            return True

        left = min(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left