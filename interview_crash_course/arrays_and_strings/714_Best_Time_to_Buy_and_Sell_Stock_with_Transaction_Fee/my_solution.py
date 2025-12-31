from typing import List


class Solution:
    #     # top-down
    #     def maxProfit(self, prices: List[int], fee: int) -> int:
    #         def profitDp(idx: int, holding: bool) -> int:
    #             if idx >= len(prices):
    #                 return 0

    #             if (idx, holding) in memo:
    #                 return memo[(idx, holding)]

    #             # skiping
    #             profit = profitDp(idx + 1, holding)

    #             # buying / selling
    #             if holding:
    #                 profit = max(profit, prices[idx] - fee + profitDp(idx, False))
    #             else:
    #                 profit = max(profit, -prices[idx] + profitDp(idx + 1, True))

    #             memo[(idx, holding)] = profit
    #             return profit

    #         memo = {}
    #         return profitDp(0, False)

    # bottom-up
    def maxProfit(self, prices: List[int], fee: int) -> int:
        next_holding = 0
        next_not_holding = 0
        for i in range(len(prices) - 1, -1, -1):
            profit_holding = max(next_holding, prices[i] - fee + next_not_holding)
            profit_not_holding = max(next_not_holding, -prices[i] + next_holding)

            next_holding, next_not_holding = profit_holding, profit_not_holding

        return next_not_holding