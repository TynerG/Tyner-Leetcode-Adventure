from typing import List

# Possible improvement: could've started from the outside and moved in, just remember to
# initialize the result array to avoid using list.insert every time. Make it more readable.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find the first positive element 
        idx_pos = -1
        idx_neg = -1

        for i in range(len(nums)):
            if nums[i] >= 0:
                idx_pos = i
                break

        # all positive
        if idx_pos == 0:
            return [x ** 2 for x in nums]

        # all negative
        elif idx_pos == -1:
            return [x ** 2 for x in reversed(nums)]

        # in the middle
        else:
            idx_neg = idx_pos - 1
            squares = []
            while idx_neg >= 0 and idx_pos < len(nums):
                neg_squared = nums[idx_neg] ** 2
                pos_squared = nums[idx_pos] ** 2

                if neg_squared >= pos_squared:
                    squares.append(pos_squared)
                    idx_pos += 1
                else:
                    squares.append(neg_squared)
                    idx_neg -= 1

            if idx_pos == len(nums):
                squares = squares + [x ** 2 for x in reversed(nums[:idx_neg + 1])]

            else:
                squares = squares + [x ** 2 for x in nums[idx_pos:]]

            return squares

