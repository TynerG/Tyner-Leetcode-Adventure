from typing import List

# can be optimized for less space: build the answer array directly in the first two iterations
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_left_right = [1]
        prod_right_left = [1]
        for i in range(len(nums)):
            prod_left_right.append(nums[i] * prod_left_right[-1])
            prod_right_left.append(nums[len(nums) - 1 - i] * prod_right_left[-1])

        answers = []
        for i in range(len(nums)):
            answers.append(prod_left_right[i] * prod_right_left[len(prod_right_left) - 2 - i])

        return answers
