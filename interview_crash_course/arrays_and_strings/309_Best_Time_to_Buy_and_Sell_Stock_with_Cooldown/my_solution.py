from typing import List


class Solution:
    #     # top-down
    #     def maxProfit(self, prices: List[int]) -> int:
    #         def profit_dp(idx: int, holding: bool) -> int:
    #             if idx >= len(prices):
    #                 return 0

    #             if (idx, holding) in memo:
    #                 return memo[(idx, holding)]

    #             # skipping
    #             profit = profit_dp(idx + 1, holding)

    #             # buying / selling
    #             if not holding:
    #                 profit = max(profit, -prices[idx] + profit_dp(idx + 1, True))
    #             else:
    #                 profit = max(profit, prices[idx] + profit_dp(idx + 2, False))

    #             memo[(idx, holding)] = profit
    #             return profit

    #         memo = {}
    #         return profit_dp(0, False)

    # bottom-up
    def maxProfit(self, prices: List[int]) -> int:
        next_holding = 0
        next_not_holding = [0, 0]
        for i in range(len(prices) - 1, -1, -1):
            profit_holding = max(next_holding, prices[i] + next_not_holding[1])
            profit_not_holding = [max(next_not_holding[0], -prices[i] + next_holding), next_not_holding[0]]
            next_holding, next_not_holding = profit_holding, profit_not_holding

        return next_not_holding[0]