from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        seen = {tuple(entrance)}
        queue = deque([(entrance[0], entrance[1], 0)])

        def valid(r: int, c: int):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and (r, c) not in seen and maze[r][c] == "."

        def is_exit(r: int, c: int):
            return r == 0 or r == len(maze) - 1 or c == 0 or c == len(maze[0]) - 1

        while queue:
            node = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                curr_coord = (node[0] + dx, node[1] + dy)

                if valid(curr_coord[0], curr_coord[1]):
                    if is_exit(curr_coord[0], curr_coord[1]):
                        return node[2] + 1
                    seen.add((curr_coord[0], curr_coord[1]))
                    queue.append((curr_coord[0], curr_coord[1], node[2] + 1))

        return -1
