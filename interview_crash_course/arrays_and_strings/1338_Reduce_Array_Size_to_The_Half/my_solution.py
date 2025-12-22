from collections import Counter
from heapq import *
from math import ceil
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target_num = ceil(len(arr) / 2)

        counted = [-x for x in Counter(arr).values()]
        heapify(counted)
        num_removed = 0
        while target_num > 0:
            target_num += heappop(counted)
            num_removed += 1

        return num_removed