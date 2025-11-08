from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elementsToAppearance = dict()
        for i in nums:
            if i in elementsToAppearance:
                elementsToAppearance[i] += 1
            else:
                elementsToAppearance[i] = 1

        for j in elementsToAppearance:
            if elementsToAppearance[j] > len(nums) / 2:
                return j
