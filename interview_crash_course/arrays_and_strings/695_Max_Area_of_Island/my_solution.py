from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int) -> int:
            area = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                moved_i = i + dx
                moved_j = j + dy
                if (0 <= moved_i < len(grid) and
                        0 <= moved_j < len(grid[0]) and
                        grid[moved_i][moved_j] == 1 and
                        (moved_i, moved_j) not in seen):
                    seen.add((moved_i, moved_j))
                    area += dfs(moved_i, moved_j)

            return area

        seen = set()  # {(i,j)}
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    seen.add((i, j))
                    max_area = max(max_area, dfs(i, j))

        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))