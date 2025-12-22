from heapq import *
from typing import List

# better sol: use quick select or binary search
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heappush(max_heap, (-dist, point))

            while len(max_heap) > k:
                heappop(max_heap)

        return [states[1] for states in max_heap]