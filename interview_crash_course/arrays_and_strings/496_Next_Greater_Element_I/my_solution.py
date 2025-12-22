from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # go through nums2 to find NGE for all elements
        num_to_nge = defaultdict(lambda: -1)
        dec_stack = []
        for num in nums2:
            while dec_stack and dec_stack[-1] < num:
                ele = dec_stack.pop()
                num_to_nge[ele] = num

            dec_stack.append(num)

        # go through num1 to build the result list
        nges = []
        for num in nums1:
            nges.append(num_to_nge[num])

        return nges