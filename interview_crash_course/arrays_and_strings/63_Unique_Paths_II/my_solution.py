# grid[i][j] = grid[i-1][j] + grid[i][j-1]
# grid[0][0] = 1

class Solution:
    #     # top-down
    #     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #         def num_path(i: int, j: int) -> int:
    #             if obstacleGrid[i][j] == 1:
    #                 return 0

    #             if i == 0 and j == 0:
    #                 return 1

    #             if (i, j) in memo:
    #                 return memo[(i, j)]

    #             curr_num = 0
    #             if 0 <= i - 1 < n:
    #                 curr_num += num_path(i - 1, j)

    #             if 0 <= j - 1 < m:
    #                 curr_num += num_path(i, j - 1)

    #             memo[(i, j)] = curr_num
    #             return curr_num

    #         n = len(obstacleGrid)
    #         m = len(obstacleGrid[0])
    #         memo = {}
    #         return num_path(n - 1, m - 1)

    # bottom-up
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        above = [0] * m
        above[0] = 1
        for i in range(n):
            left = 0
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    above[j] = 0
                    left = 0
                else:
                    above[j] = above[j] + left
                    left = above[j]

        return left