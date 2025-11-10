from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_so_far = 0
        price_prev_day = prices[0]

        for i in range(1, len(prices)):
            if price_prev_day < prices[i]:
                profit_so_far += prices[i] - price_prev_day

            price_prev_day = prices[i]

        return profit_so_far
