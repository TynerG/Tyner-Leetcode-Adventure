from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node: int) -> None:
            for nb in graph[node]:
                if nb not in seen:
                    seen.add(nb)
                    dfs(nb)

        graph = defaultdict(list)
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        seen = set()
        num_comp = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                num_comp += 1

        return num_comp

if __name__ == '__main__':
    s = Solution()
    print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))