class Solution:
    #     # top-down
    #     def climbStairs(self, n: int) -> int:

    #         def distinct_ways(stair_idx: int) -> int:
    #             if stair_idx == 1:
    #                 return 1

    #             if stair_idx == 2:
    #                 return 2

    #             if stair_idx in memo:
    #                 return memo[stair_idx]

    #             memo[stair_idx] = distinct_ways(stair_idx - 1) + distinct_ways(stair_idx - 2)
    #             return memo[stair_idx]

    #         memo = dict()
    #         return distinct_ways(n)

    # bottom-up
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev_one = 2
        prev_two = 1

        for i in range(2, n):
            prev_one, prev_two = prev_one + prev_two, prev_one

        return prev_one