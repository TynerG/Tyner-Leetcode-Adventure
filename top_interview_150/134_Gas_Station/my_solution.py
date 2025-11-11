from typing import List

# Problem: O(n^2), correct but atoo slow.
# Key takeaway: no need to do the whole trip for every starting location - if we start
# from 1 and failed at 6, there is no way we can start from 2 and not fail at 6.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            if self._startJourney(gas, cost, start):
                return start

        return -1

    def _startJourney(self, gas: List[int], cost: List[int], start: int) -> bool:
        tank = 0
        for i in range(len(gas)):
            departure = (i + start) % len(gas)
            tank += gas[departure]
            if tank >= cost[departure]:
                tank -= cost[departure]
            else:
                return False

        return True