from typing import List


class Solution:
    #     # top-down
    #     def minCostClimbingStairs(self, cost: List[int]) -> int:
    #         def dp(idx: int) -> int:
    #             if idx >= len(cost) - 2:
    #                 return cost[idx]

    #             if idx in memo:
    #                 return memo[idx]

    #             memo[idx] = cost[idx] + min(dp(idx + 1), dp(idx + 2))
    #             return memo[idx]

    #         memo = {}
    #         return min(dp(0), dp(1))

    # bottom-up
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        prev_one = cost[-2]
        prev_two = cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            prev_one, prev_two = cost[i] + min(prev_one, prev_two), prev_one

        return min(prev_one, prev_two)

    # # bottom-up (other direction)
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     if len(cost) <= 2:
    #         return min(cost)

    #     prev_one = cost[1]
    #     prev_two = cost[0]

    #     for i in range(2, len(cost)):
    #         prev_one, prev_two = cost[i] + min(prev_one, prev_two), prev_one

    #     return min(prev_one, prev_two)