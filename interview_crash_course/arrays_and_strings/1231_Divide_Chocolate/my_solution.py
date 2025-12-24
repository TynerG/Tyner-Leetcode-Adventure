from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def is_valid(min_val: int) -> bool:
            num_pieces = 0
            curr_chunk = 0
            for sweet in sweetness:
                curr_chunk += sweet

                if curr_chunk >= min_val:
                    num_pieces += 1
                    curr_chunk = 0

                    if num_pieces == k + 1:
                        return True

            return False

        left = min(sweetness)  # 7
        right = sum(sweetness) // (k + 1)  # 7
        while left <= right:
            mid = (left + right) // 2  # 6

            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right