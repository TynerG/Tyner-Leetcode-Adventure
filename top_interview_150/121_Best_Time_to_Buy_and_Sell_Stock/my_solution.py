from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_so_far = inf
        profit_highest = 0
        for i in prices:
            if i < min_so_far:
                min_so_far = i

            profit = i - min_so_far
            if profit > profit_highest:
                profit_highest = profit

        return profit_highest