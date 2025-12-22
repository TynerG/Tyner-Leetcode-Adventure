from typing import List

# improvement: use a min heap
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ordered_apples = sorted(weight, reverse=True)

        num_apples = 0
        weight_left = 5000
        while ordered_apples and weight_left > 0:
            apple = ordered_apples.pop()
            if apple > weight_left:
                break

            weight_left -= apple
            num_apples += 1

        return num_apples