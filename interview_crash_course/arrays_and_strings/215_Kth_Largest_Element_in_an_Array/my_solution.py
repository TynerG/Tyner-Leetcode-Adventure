from heapq import *
from typing import List

# better solution: use quick select
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)

        cost = 0
        while len(sticks) > 1:
            shortest = heappop(sticks)
            sec_shortest = heappop(sticks)
            connected = shortest + sec_shortest
            cost += connected
            heappush(sticks, connected)

        return cost