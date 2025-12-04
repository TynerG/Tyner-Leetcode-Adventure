from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node: int) -> int:
            num_nodes = 1

            for nb in adj_list[node]:
                if nb not in seen and nb not in restricted_set:
                    seen.add(nb)
                    num_nodes += dfs(nb)

            return num_nodes

        restricted_set = set(restricted)
        adj_list = defaultdict(list) # adj_list[i] = [neighbours of i]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        seen = {0}
        return dfs(0)

if __name__ == "__main__":
    s = Solution()
    print(s.reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5]))