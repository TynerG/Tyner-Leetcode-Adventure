from heapq import *
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.min_heap = []
        for num in nums:
            heappush(self.min_heap, num)
            while len(self.min_heap) > self.k:
                heappop(self.min_heap)

    def add(self, val: int) -> int:
        self.nums.append(val)
        heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)