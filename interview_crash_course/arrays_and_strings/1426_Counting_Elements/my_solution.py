from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        set_arr = set(arr)

        counter = 0
        for i in arr:
            if i + 1 in set_arr:
                counter += 1

        return counter
