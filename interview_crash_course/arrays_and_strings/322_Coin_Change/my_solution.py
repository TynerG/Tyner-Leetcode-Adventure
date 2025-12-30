from math import inf
from typing import List


class Solution:
    #     # top-down
    #     def coinChange(self, coins: List[int], amount: int) -> int:
    #         coins_set = set(coins)

    #         if amount == 0:
    #             return 0

    #         def smallest_num_coin(amount: int) -> int:
    #             if amount in coins_set:
    #                 return 1

    #             if amount <= 0:
    #                 return inf

    #             if amount in memo:
    #                 return memo[amount]

    #             min_num = inf
    #             for coin in coins:
    #                 min_num = min(min_num, 1 + smallest_num_coin(amount - coin))

    #             memo[amount] = min_num
    #             return memo[amount]

    #         memo = {}
    #         smallest_num = smallest_num_coin(amount)
    #         if smallest_num == inf:
    #             return -1

    #         return smallest_num

    # bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [inf] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        if memo[-1] == inf:
            return -1

        return memo[-1]